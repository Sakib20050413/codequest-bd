from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.db.models import Count, Sum
from django.contrib.auth.models import User
import json

from .models import LanguageTrack, ChallengeLevel, QuizQuestion, StudentSubmission, LabAnnouncement
from accounts.models import StudentProfile
from .piston_service import execute_code, evaluate_level_submission


def home_view(request):
    tracks = LanguageTrack.objects.filter(is_active=True).prefetch_related('levels')
    announcements = LabAnnouncement.objects.filter(is_active=True)[:2]
    total_challenges = ChallengeLevel.objects.count()
    total_quizzes = QuizQuestion.objects.count()
    total_students = StudentProfile.objects.count()
    total_xp_awarded = StudentProfile.objects.aggregate(Sum('xp'))['xp__sum'] or 0

    # Top 3 leaderboard preview
    top_students = StudentProfile.objects.select_related('user').order_by('-xp')[:3]

    context = {
        'tracks': tracks,
        'announcements': announcements,
        'total_challenges': total_challenges,
        'total_quizzes': total_quizzes,
        'total_students': total_students,
        'total_xp_awarded': total_xp_awarded,
        'top_students': top_students,
    }
    return render(request, 'arena/index.html', context)


def tracks_view(request):
    tracks = LanguageTrack.objects.filter(is_active=True).prefetch_related('levels')
    user_solved = request.user.profile.solved_levels if request.user.is_authenticated else []
    return render(request, 'arena/tracks.html', {'tracks': tracks, 'user_solved': user_solved})


def track_detail_view(request, slug):
    track = get_object_or_404(LanguageTrack, slug=slug, is_active=True)
    levels = track.levels.all().order_by('level_number')
    user_solved = request.user.profile.solved_levels if request.user.is_authenticated else []
    return render(request, 'arena/track_detail.html', {'track': track, 'levels': levels, 'user_solved': user_solved})


def level_play_view(request, slug):
    level = get_object_or_404(ChallengeLevel.objects.select_related('track'), slug=slug)
    track_levels = level.track.levels.all().order_by('level_number')
    user_solved = request.user.profile.solved_levels if request.user.is_authenticated else []
    is_solved = level.slug in user_solved

    # Find previous and next levels
    prev_level = None
    next_level = None
    level_list = list(track_levels)
    for idx, l in enumerate(level_list):
        if l.id == level.id:
            if idx > 0:
                prev_level = level_list[idx - 1]
            if idx < len(level_list) - 1:
                next_level = level_list[idx + 1]
            break

    context = {
        'level': level,
        'track': level.track,
        'track_levels': track_levels,
        'is_solved': is_solved,
        'prev_level': prev_level,
        'next_level': next_level,
        'maze_config_json': json.dumps(level.maze_grid_config),
        'dom_config_json': json.dumps(level.dom_builder_config),
        'test_cases_json': json.dumps(level.test_cases),
    }
    return render(request, 'arena/level_play.html', context)


def blitz_view(request):
    """
    Mode 4: Bug-Hunter & Output Blitz (60-second rapid quiz trainer)
    """
    questions = list(QuizQuestion.objects.all().order_by('?')[:15])
    # Serialize questions for client-side blitz engine
    quiz_bank = []
    for q in questions:
        quiz_bank.append({
            'id': q.id,
            'category': q.get_category_display(),
            'question': q.question_text,
            'code': q.code_snippet,
            'options': {
                'A': q.option_a,
                'B': q.option_b,
                'C': q.option_c,
                'D': q.option_d,
            },
            'correct': q.correct_option,
            'explanation': q.explanation,
            'points': q.points,
        })

    return render(request, 'arena/blitz.html', {
        'quiz_bank_json': json.dumps(quiz_bank),
        'total_questions': len(quiz_bank),
    })


def leaderboard_view(request):
    section_filter = request.GET.get('section', 'all')
    profiles = StudentProfile.objects.select_related('user').order_by('-xp', '-updated_at')

    if section_filter != 'all':
        profiles = profiles.filter(batch_section__icontains=section_filter)

    return render(request, 'arena/leaderboard.html', {
        'profiles': profiles,
        'current_filter': section_filter,
    })


def proposal_view(request):
    """
    Printable Formal CSE 324 Project Proposal Document
    Formatted for BAIUST CSE Lab Evaluation
    """
    return render(request, 'arena/proposal.html')


# ==============================================================================
# AJAX & REST API ENDPOINTS
# ==============================================================================

def run_code_api(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'POST required'}, status=405)

    try:
        data = json.loads(request.body)
        language = data.get('language', 'c')
        code = data.get('code', '')
        stdin = data.get('stdin', '')

        result = execute_code(language, code, stdin)
        return JsonResponse({
            'status': 'ok',
            'execution': result
        })
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


def submit_level_api(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'POST required'}, status=405)

    try:
        data = json.loads(request.body)
        level_id = data.get('level_id')
        language = data.get('language', 'c')
        code = data.get('code', '')

        level = get_object_or_404(ChallengeLevel, id=level_id)
        eval_result = evaluate_level_submission(level, language, code)

        earned_xp = 0
        is_first_solve = False

        if eval_result['all_passed']:
            if request.user.is_authenticated:
                profile = request.user.profile
                if level.slug not in profile.solved_levels:
                    earned_xp = level.xp_reward
                    profile.add_xp(earned_xp, level.slug)
                    is_first_solve = True
                
                # Log student submission
                StudentSubmission.objects.create(
                    user=request.user,
                    level=level,
                    language=language,
                    submitted_code=code,
                    status='ACCEPTED',
                    stdout=eval_result.get('stdout', ''),
                    stderr=eval_result.get('stderr', ''),
                    execution_time_ms=eval_result.get('execution_time_ms', 0),
                    xp_earned=earned_xp
                )
        else:
            if request.user.is_authenticated:
                StudentSubmission.objects.create(
                    user=request.user,
                    level=level,
                    language=language,
                    submitted_code=code,
                    status=eval_result['status'],
                    stdout=eval_result.get('stdout', ''),
                    stderr=eval_result.get('stderr', ''),
                    execution_time_ms=eval_result.get('execution_time_ms', 0),
                    xp_earned=0
                )

        return JsonResponse({
            'status': 'ok',
            'evaluation': eval_result,
            'earned_xp': earned_xp,
            'is_first_solve': is_first_solve,
            'user_total_xp': request.user.profile.xp if request.user.is_authenticated else 0,
            'user_rank': request.user.profile.rank_name if request.user.is_authenticated else 'Guest',
        })
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


def blitz_submit_api(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'POST required'}, status=405)

    try:
        data = json.loads(request.body)
        score = int(data.get('score', 0))
        correct_count = int(data.get('correct_count', 0))

        if request.user.is_authenticated and score > 0:
            profile = request.user.profile
            # Scale blitz XP to a fair award
            awarded_xp = min(score, 300)
            profile.add_xp(awarded_xp)
            if "Blitz Champion" not in profile.badges and correct_count >= 10:
                badges = list(profile.badges)
                badges.append("Blitz Champion")
                profile.badges = badges
                profile.save()

            return JsonResponse({
                'status': 'ok',
                'awarded_xp': awarded_xp,
                'total_xp': profile.xp,
                'rank_name': profile.rank_name,
            })

        return JsonResponse({'status': 'ok', 'awarded_xp': 0})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
