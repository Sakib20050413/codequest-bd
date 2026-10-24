from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages
from django.http import JsonResponse
from django.utils.text import slugify
from django.db.models import Count, Sum
from django.contrib.auth.models import User
import json

from arena.models import LanguageTrack, ChallengeLevel, QuizQuestion, StudentSubmission, LabAnnouncement
from accounts.models import StudentProfile


def is_instructor(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser or user.username == 'sakib_admin')


# ==============================================================================
# DASHBOARD
# ==============================================================================

@user_passes_test(is_instructor, login_url='/accounts/login/')
def dashboard_view(request):
    total_tracks = LanguageTrack.objects.count()
    total_levels = ChallengeLevel.objects.count()
    total_quizzes = QuizQuestion.objects.count()
    total_students = StudentProfile.objects.count()
    total_submissions = StudentSubmission.objects.count()
    accepted_submissions = StudentSubmission.objects.filter(status='ACCEPTED').count()

    recent_submissions = StudentSubmission.objects.select_related('user', 'level').order_by('-submitted_at')[:8]
    recent_students = StudentProfile.objects.select_related('user').order_by('-xp')[:6]
    tracks = LanguageTrack.objects.annotate(level_cnt=Count('levels'))

    context = {
        'total_tracks': total_tracks,
        'total_levels': total_levels,
        'total_quizzes': total_quizzes,
        'total_students': total_students,
        'total_submissions': total_submissions,
        'accepted_submissions': accepted_submissions,
        'recent_submissions': recent_submissions,
        'recent_students': recent_students,
        'tracks': tracks,
    }
    return render(request, 'instructor_panel/dashboard.html', context)


# ==============================================================================
# 1. LANGUAGE TRACK CRUD
# ==============================================================================

@user_passes_test(is_instructor, login_url='/accounts/login/')
def tracks_crud_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'create':
            title = request.POST.get('title', '').strip()
            slug = request.POST.get('slug', '').strip() or slugify(title)
            description = request.POST.get('description', '').strip()
            icon = request.POST.get('icon', '💻').strip()
            badge_color = request.POST.get('badge_color', 'from-blue-600 to-indigo-600').strip()
            difficulty = request.POST.get('difficulty', 'Intermediate')
            order = int(request.POST.get('order', 1))

            LanguageTrack.objects.create(
                title=title,
                slug=slug,
                description=description,
                icon=icon,
                badge_color=badge_color,
                difficulty=difficulty,
                order=order,
                is_active=True
            )
            messages.success(request, f"Track '{title}' created successfully!")
            return redirect('instructor_panel:tracks')

        elif action == 'edit':
            track_id = request.POST.get('track_id')
            track = get_object_or_404(LanguageTrack, id=track_id)
            track.title = request.POST.get('title', track.title).strip()
            track.description = request.POST.get('description', track.description).strip()
            track.icon = request.POST.get('icon', track.icon).strip()
            track.badge_color = request.POST.get('badge_color', track.badge_color).strip()
            track.difficulty = request.POST.get('difficulty', track.difficulty)
            track.order = int(request.POST.get('order', track.order))
            track.is_active = request.POST.get('is_active') == 'on'
            track.save()
            messages.success(request, f"Track '{track.title}' updated successfully!")
            return redirect('instructor_panel:tracks')

        elif action == 'delete':
            track_id = request.POST.get('track_id')
            track = get_object_or_404(LanguageTrack, id=track_id)
            track_title = track.title
            track.delete()
            messages.success(request, f"Track '{track_title}' and its levels deleted!")
            return redirect('instructor_panel:tracks')

    tracks = LanguageTrack.objects.all().order_by('order', 'id')
    return render(request, 'instructor_panel/tracks_crud.html', {'tracks': tracks})


# ==============================================================================
# 2. CHALLENGE LEVEL CRUD
# ==============================================================================

@user_passes_test(is_instructor, login_url='/accounts/login/')
def levels_crud_view(request):
    tracks = LanguageTrack.objects.all().order_by('order')

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'create':
            track_id = request.POST.get('track_id')
            track = get_object_or_404(LanguageTrack, id=track_id)
            title = request.POST.get('title', '').strip()
            level_num = int(request.POST.get('level_number', 1))
            engine = request.POST.get('engine', 'CODE_JUDGE')
            story_brief = request.POST.get('story_brief', '').strip()
            instructions = request.POST.get('instructions_markdown', '').strip()
            xp_reward = int(request.POST.get('xp_reward', 100))

            # Parse JSON configs safely
            test_cases_raw = request.POST.get('test_cases', '[]')
            maze_config_raw = request.POST.get('maze_grid_config', '{}')
            dom_config_raw = request.POST.get('dom_builder_config', '{}')
            hints_raw = request.POST.get('hints', '')

            try:
                test_cases = json.loads(test_cases_raw) if test_cases_raw else []
            except Exception:
                test_cases = []

            try:
                maze_config = json.loads(maze_config_raw) if maze_config_raw else {}
            except Exception:
                maze_config = {}

            try:
                dom_config = json.loads(dom_config_raw) if dom_config_raw else {}
            except Exception:
                dom_config = {}

            hints = [h.strip() for h in hints_raw.split('\n') if h.strip()]

            level = ChallengeLevel.objects.create(
                track=track,
                title=title,
                level_number=level_num,
                engine=engine,
                story_brief=story_brief,
                instructions_markdown=instructions,
                starter_code_c=request.POST.get('starter_code_c', ''),
                starter_code_cpp=request.POST.get('starter_code_cpp', ''),
                starter_code_python=request.POST.get('starter_code_python', ''),
                starter_code_javascript=request.POST.get('starter_code_javascript', ''),
                starter_code_php=request.POST.get('starter_code_php', ''),
                solution_template=request.POST.get('solution_template', ''),
                maze_grid_config=maze_config,
                dom_builder_config=dom_config,
                test_cases=test_cases,
                hints=hints,
                xp_reward=xp_reward,
                order=level_num
            )
            messages.success(request, f"Level '{level.title}' created in {track.title}!")
            return redirect('instructor_panel:levels')

        elif action == 'edit':
            level_id = request.POST.get('level_id')
            level = get_object_or_404(ChallengeLevel, id=level_id)

            level.title = request.POST.get('title', level.title).strip()
            level.level_number = int(request.POST.get('level_number', level.level_number))
            level.engine = request.POST.get('engine', level.engine)
            level.story_brief = request.POST.get('story_brief', level.story_brief).strip()
            level.instructions_markdown = request.POST.get('instructions_markdown', level.instructions_markdown).strip()
            level.xp_reward = int(request.POST.get('xp_reward', level.xp_reward))
            level.starter_code_c = request.POST.get('starter_code_c', level.starter_code_c)
            level.starter_code_cpp = request.POST.get('starter_code_cpp', level.starter_code_cpp)
            level.starter_code_python = request.POST.get('starter_code_python', level.starter_code_python)
            level.starter_code_javascript = request.POST.get('starter_code_javascript', level.starter_code_javascript)
            level.starter_code_php = request.POST.get('starter_code_php', level.starter_code_php)
            level.solution_template = request.POST.get('solution_template', level.solution_template)

            test_cases_raw = request.POST.get('test_cases')
            if test_cases_raw:
                try:
                    level.test_cases = json.loads(test_cases_raw)
                except Exception:
                    pass

            maze_raw = request.POST.get('maze_grid_config')
            if maze_raw:
                try:
                    level.maze_grid_config = json.loads(maze_raw)
                except Exception:
                    pass

            dom_raw = request.POST.get('dom_builder_config')
            if dom_raw:
                try:
                    level.dom_builder_config = json.loads(dom_raw)
                except Exception:
                    pass

            hints_raw = request.POST.get('hints')
            if hints_raw is not None:
                level.hints = [h.strip() for h in hints_raw.split('\n') if h.strip()]

            level.save()
            messages.success(request, f"Level '{level.title}' updated successfully!")
            return redirect('instructor_panel:levels')

        elif action == 'delete':
            level_id = request.POST.get('level_id')
            level = get_object_or_404(ChallengeLevel, id=level_id)
            title = level.title
            level.delete()
            messages.success(request, f"Level '{title}' deleted!")
            return redirect('instructor_panel:levels')

    levels = ChallengeLevel.objects.select_related('track').all().order_by('track__order', 'level_number')
    return render(request, 'instructor_panel/levels_crud.html', {'levels': levels, 'tracks': tracks})


# ==============================================================================
# 3. QUIZ QUESTION CRUD (BUG-HUNTER BANK)
# ==============================================================================

@user_passes_test(is_instructor, login_url='/accounts/login/')
def quizzes_crud_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'create':
            QuizQuestion.objects.create(
                category=request.POST.get('category', 'HTML5'),
                question_text=request.POST.get('question_text', '').strip(),
                code_snippet=request.POST.get('code_snippet', '').strip(),
                option_a=request.POST.get('option_a', '').strip(),
                option_b=request.POST.get('option_b', '').strip(),
                option_c=request.POST.get('option_c', '').strip(),
                option_d=request.POST.get('option_d', '').strip(),
                correct_option=request.POST.get('correct_option', 'A'),
                explanation=request.POST.get('explanation', '').strip(),
                difficulty=request.POST.get('difficulty', 'Medium'),
                points=int(request.POST.get('points', 20))
            )
            messages.success(request, "Quiz Question added to Bug-Hunter Bank!")
            return redirect('instructor_panel:quizzes')

        elif action == 'edit':
            quiz_id = request.POST.get('quiz_id')
            quiz = get_object_or_404(QuizQuestion, id=quiz_id)
            quiz.category = request.POST.get('category', quiz.category)
            quiz.question_text = request.POST.get('question_text', quiz.question_text).strip()
            quiz.code_snippet = request.POST.get('code_snippet', quiz.code_snippet).strip()
            quiz.option_a = request.POST.get('option_a', quiz.option_a).strip()
            quiz.option_b = request.POST.get('option_b', quiz.option_b).strip()
            quiz.option_c = request.POST.get('option_c', quiz.option_c).strip()
            quiz.option_d = request.POST.get('option_d', quiz.option_d).strip()
            quiz.correct_option = request.POST.get('correct_option', quiz.correct_option)
            quiz.explanation = request.POST.get('explanation', quiz.explanation).strip()
            quiz.difficulty = request.POST.get('difficulty', quiz.difficulty)
            quiz.points = int(request.POST.get('points', quiz.points))
            quiz.save()
            messages.success(request, "Quiz Question updated successfully!")
            return redirect('instructor_panel:quizzes')

        elif action == 'delete':
            quiz_id = request.POST.get('quiz_id')
            quiz = get_object_or_404(QuizQuestion, id=quiz_id)
            quiz.delete()
            messages.success(request, "Quiz Question removed!")
            return redirect('instructor_panel:quizzes')

    quizzes = QuizQuestion.objects.all().order_by('-id')
    return render(request, 'instructor_panel/quizzes_crud.html', {'quizzes': quizzes})


# ==============================================================================
# 4. SUBMISSIONS & STUDENTS CRUD
# ==============================================================================

@user_passes_test(is_instructor, login_url='/accounts/login/')
def submissions_crud_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'delete':
            sub_id = request.POST.get('sub_id')
            sub = get_object_or_404(StudentSubmission, id=sub_id)
            sub.delete()
            messages.success(request, "Submission record deleted.")
            return redirect('instructor_panel:submissions')

    submissions = StudentSubmission.objects.select_related('user', 'level', 'user__profile').all().order_by('-submitted_at')[:100]
    return render(request, 'instructor_panel/submissions_crud.html', {'submissions': submissions})


@user_passes_test(is_instructor, login_url='/accounts/login/')
def students_crud_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        profile_id = request.POST.get('profile_id')
        profile = get_object_or_404(StudentProfile, id=profile_id)

        if action == 'award_xp':
            bonus_xp = int(request.POST.get('bonus_xp', 50))
            profile.add_xp(bonus_xp)
            messages.success(request, f"Awarded {bonus_xp} XP to {profile.user.username} ({profile.student_id})!")
            return redirect('instructor_panel:students')

        elif action == 'edit_rank':
            profile.level = int(request.POST.get('level', profile.level))
            profile.student_id = request.POST.get('student_id', profile.student_id)
            profile.batch_section = request.POST.get('batch_section', profile.batch_section)
            profile.save()
            messages.success(request, f"Updated profile for {profile.user.username}!")
            return redirect('instructor_panel:students')

        elif action == 'reset_progress':
            profile.xp = 0
            profile.level = 1
            profile.solved_levels = []
            profile.badges = ["First Blood (1st Solve)"]
            profile.save()
            messages.info(request, f"Reset progress for {profile.user.username}.")
            return redirect('instructor_panel:students')

    profiles = StudentProfile.objects.select_related('user').all().order_by('-xp')
    return render(request, 'instructor_panel/students_crud.html', {'profiles': profiles})


# ==============================================================================
# 5. LAB ANNOUNCEMENTS CRUD
# ==============================================================================

@user_passes_test(is_instructor, login_url='/accounts/login/')
def announcements_crud_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'create':
            LabAnnouncement.objects.create(
                title=request.POST.get('title', '').strip(),
                message=request.POST.get('message', '').strip(),
                badge=request.POST.get('badge', 'CSE 324 Final'),
                is_active=request.POST.get('is_active') == 'on'
            )
            messages.success(request, "Lab announcement broadcasted!")
            return redirect('instructor_panel:announcements')

        elif action == 'edit':
            ann_id = request.POST.get('ann_id')
            ann = get_object_or_404(LabAnnouncement, id=ann_id)
            ann.title = request.POST.get('title', ann.title).strip()
            ann.message = request.POST.get('message', ann.message).strip()
            ann.badge = request.POST.get('badge', ann.badge)
            ann.is_active = request.POST.get('is_active') == 'on'
            ann.save()
            messages.success(request, "Announcement updated!")
            return redirect('instructor_panel:announcements')

        elif action == 'toggle':
            ann_id = request.POST.get('ann_id')
            ann = get_object_or_404(LabAnnouncement, id=ann_id)
            ann.is_active = not ann.is_active
            ann.save()
            messages.info(request, f"Announcement status set to {'Active' if ann.is_active else 'Inactive'}.")
            return redirect('instructor_panel:announcements')

        elif action == 'delete':
            ann_id = request.POST.get('ann_id')
            ann = get_object_or_404(LabAnnouncement, id=ann_id)
            ann.delete()
            messages.success(request, "Announcement deleted.")
            return redirect('instructor_panel:announcements')

    announcements = LabAnnouncement.objects.all().order_by('-created_at')
    return render(request, 'instructor_panel/announcements_crud.html', {'announcements': announcements})
