import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.management import call_command
from django.db.utils import OperationalError, ProgrammingError
from .models import (
    Language,
    Course,
    Lesson,
    CodingGame,
    PracticeTask,
    UserProfile,
    Submission,
)


def ensure_seeded():
    try:
        if Language.objects.count() == 0 or Course.objects.count() == 0:
            from seed_codequest import seed_all
            seed_all()
    except (OperationalError, ProgrammingError):
        try:
            call_command("migrate", interactive=False, verbosity=0)
            from seed_codequest import seed_all
            seed_all()
        except Exception:
            pass


def get_active_profile(request):
    ensure_seeded()
    if request.user.is_authenticated:
        prof, _ = UserProfile.objects.get_or_create(user=request.user)
        return prof
    first_prof = UserProfile.objects.first()
    return first_prof


def home_view(request):
    ensure_seeded()
    profile = get_active_profile(request)
    languages = Language.objects.all()
    courses = Course.objects.select_related("language").all()
    games = CodingGame.objects.all()
    tasks = PracticeTask.objects.all()[:4]
    return render(
        request,
        "learn/home.html",
        {
            "profile": profile,
            "languages": languages,
            "courses": courses,
            "games": games,
            "tasks": tasks,
        },
    )


def courses_view(request):
    ensure_seeded()
    profile = get_active_profile(request)
    pillar_filter = request.GET.get("pillar", "ALL")
    courses = Course.objects.select_related("language").prefetch_related("lessons").all()
    if pillar_filter != "ALL":
        courses = [c for c in courses if c.language.pillar == pillar_filter]
    return render(
        request,
        "learn/courses.html",
        {
            "profile": profile,
            "courses": courses,
            "pillar_filter": pillar_filter,
        },
    )


def lesson_player_view(request, course_slug):
    ensure_seeded()
    profile = get_active_profile(request)
    course = get_object_or_404(Course.objects.select_related("language"), slug=course_slug)
    lesson = course.lessons.first()
    all_courses = Course.objects.select_related("language").all()
    return render(
        request,
        "learn/lesson_player.html",
        {
            "profile": profile,
            "course": course,
            "lesson": lesson,
            "all_courses": all_courses,
        },
    )


def games_arcade_view(request):
    ensure_seeded()
    profile = get_active_profile(request)
    games = CodingGame.objects.all()
    games_json = json.dumps([
        {
            "id": g.id,
            "slug": g.slug,
            "title": g.title,
            "engineKey": g.engine_key,
            "languageTag": g.language_tag,
            "difficulty": g.difficulty,
            "brief": g.scenario_brief,
            "requirement": g.real_code_requirement,
            "starter": g.starter_code,
            "solution": g.solution_code,
            "xp": g.xp_reward,
        }
        for g in games
    ])
    return render(
        request,
        "learn/games_arcade.html",
        {
            "profile": profile,
            "games": games,
            "games_json": games_json,
        },
    )


def tasks_contests_view(request):
    ensure_seeded()
    profile = get_active_profile(request)
    tasks = PracticeTask.objects.all()
    tasks_json = json.dumps([
        {
            "id": t.id,
            "codeId": t.code_id,
            "slug": t.slug,
            "title": t.title,
            "languageTag": t.language_tag,
            "topic": t.topic_tag,
            "difficulty": t.difficulty,
            "inspiredBy": t.inspired_by,
            "statement": t.problem_statement,
            "sampleInput": t.sample_input,
            "sampleOutput": t.sample_output,
            "starter": t.starter_code,
            "solution": t.solution_code,
            "xp": t.xp_reward,
        }
        for t in tasks
    ])
    submissions = Submission.objects.all()[:10]
    return render(
        request,
        "learn/tasks_contests.html",
        {
            "profile": profile,
            "tasks": tasks,
            "tasks_json": tasks_json,
            "submissions": submissions,
        },
    )


def sandbox_ide_view(request):
    ensure_seeded()
    profile = get_active_profile(request)
    languages = Language.objects.all()
    return render(
        request,
        "learn/sandbox_ide.html",
        {
            "profile": profile,
            "languages": languages,
        },
    )


def student_dashboard_view(request):
    ensure_seeded()
    profile = get_active_profile(request)
    courses = Course.objects.select_related("language").all()
    submissions = Submission.objects.all()[:12]
    return render(
        request,
        "learn/student_dashboard.html",
        {
            "profile": profile,
            "courses": courses,
            "submissions": submissions,
        },
    )


def certificate_view(request):
    ensure_seeded()
    profile = get_active_profile(request)
    return render(request, "learn/certificate.html", {"profile": profile})


def about_view(request):
    ensure_seeded()
    profile = get_active_profile(request)
    return render(request, "learn/about.html", {"profile": profile})


def login_view(request):
    ensure_seeded()
    err = None
    if request.method == "POST":
        u = request.POST.get("username", "").strip()
        p = request.POST.get("password", "").strip()
        user = authenticate(request, username=u, password=p)
        if user:
            login(request, user)
            if user.is_staff:
                return redirect("instructor_crud")
            return redirect("student_dashboard")
        err = "Invalid credentials. Use sakib_admin / baiust1119003 (Instructor) or student_demo / cse324pass (Student)."
    return render(request, "learn/login.html", {"error": err, "profile": get_active_profile(request)})


def logout_view(request):
    logout(request)
    return redirect("home")


@login_required
def instructor_crud_view(request):
    ensure_seeded()
    profile = get_active_profile(request)
    msg = None

    if request.method == "POST":
        act = request.POST.get("crud_action", "")
        if act == "create_course":
            lang = get_object_or_404(Language, pk=request.POST.get("language_id"))
            title = request.POST.get("title", "").strip()
            slug = request.POST.get("slug", "").strip() or f"course-{Course.objects.count()+1}"
            overview = request.POST.get("overview", "").strip()
            c = Course.objects.create(language=lang, slug=slug, title=title, overview=overview)
            Lesson.objects.create(
                course=c,
                module_number=1,
                module_title="Module 1: Core Concepts",
                step_number=1,
                slug=f"{slug}-lesson-1",
                title=f"1.1 Introduction to {title}",
                part1_concept=overview,
                syntax_anatomy_rows="Line 1 | // Starter syntax | Core statement",
                tips_and_tricks="Practice writing the full code in Part 3.",
                part2_trace_explanation=" Step 1 -> Allocates variables -> Step 2 -> Verifies output.",
                game_engine_key="FLEX_BRIDGE",
                part3_game_prompt=f"Write complete code for {title}.",
                starter_code=request.POST.get("starter_code", "// Write code here"),
                solution_code=request.POST.get("starter_code", "// Write code here"),
                part4_judge_prompt="Verify all 3 test cases pass.",
                xp_reward=100,
            )
            msg = f"Created new course '{title}' with initial 4-part module."

        elif act == "create_game":
            CodingGame.objects.create(
                slug=request.POST.get("slug", "").strip() or f"game-{CodingGame.objects.count()+1}",
                title=request.POST.get("title", "").strip(),
                engine_key=request.POST.get("engine_key", "FLEX_BRIDGE"),
                language_tag=request.POST.get("language_tag", "Python / JS"),
                difficulty=request.POST.get("difficulty", "Medium"),
                scenario_brief=request.POST.get("scenario_brief", ""),
                real_code_requirement=request.POST.get("real_code_requirement", "Write complete solution code."),
                starter_code=request.POST.get("starter_code", ""),
                solution_code=request.POST.get("solution_code", ""),
                xp_reward=int(request.POST.get("xp_reward", 120) or 120),
            )
            msg = "Created new playable coding game level."

        elif act == "create_task":
            PracticeTask.objects.create(
                code_id=request.POST.get("code_id", f"CQ-{101+PracticeTask.objects.count()}"),
                slug=request.POST.get("slug", "").strip() or f"task-{PracticeTask.objects.count()+1}",
                title=request.POST.get("title", "").strip(),
                language_tag=request.POST.get("language_tag", "Python / C++"),
                topic_tag=request.POST.get("topic_tag", "Algorithms"),
                difficulty=request.POST.get("difficulty", "Easy"),
                problem_statement=request.POST.get("problem_statement", ""),
                starter_code=request.POST.get("starter_code", ""),
                solution_code=request.POST.get("solution_code", ""),
                xp_reward=int(request.POST.get("xp_reward", 100) or 100),
            )
            msg = "Created new practice task in Problem Set."

        elif act == "delete_game":
            CodingGame.objects.filter(pk=request.POST.get("game_id")).delete()
            msg = "Deleted game level."

        elif act == "delete_task":
            PracticeTask.objects.filter(pk=request.POST.get("task_id")).delete()
            msg = "Deleted practice task."

        elif act == "award_bonus_xp":
            prof = UserProfile.objects.first()
            if prof:
                prof.xp += 150
                prof.save()
                msg = f"Awarded +150 Bonus XP to {prof.user.username} (Total: {prof.xp} XP)."

    return render(
        request,
        "learn/instructor_crud.html",
        {
            "profile": profile,
            "languages": Language.objects.all(),
            "courses": Course.objects.select_related("language").all(),
            "games": CodingGame.objects.all(),
            "tasks": PracticeTask.objects.all(),
            "submissions": Submission.objects.all()[:15],
            "status_msg": msg,
        },
    )


@require_POST
def api_submit_code(request):
    ensure_seeded()
    try:
        data = json.loads(request.body.decode("utf-8"))
        item_type = data.get("item_type", "Course Module")
        item_title = data.get("item_title", "Lesson Task")
        lang_used = data.get("language", "Python 3")
        code = data.get("code", "")
        xp_earned = int(data.get("xp", 100) or 100)

        prof = get_active_profile(request)
        student_label = "Md Najmus Sakib Rahatul (1119003)"
        if prof:
            prof.xp += xp_earned
            prof.save()
            student_label = f"{prof.user.username} ({prof.student_id})"

        Submission.objects.create(
            student_name=student_label,
            item_type=item_type,
            item_title=item_title,
            language_used=lang_used,
            submitted_code=code[:1200],
            passed=True,
            xp_earned=xp_earned,
        )
        return JsonResponse({"ok": True, "new_xp": prof.xp if prof else 750, "xp_added": xp_earned})
    except Exception as exc:
        return JsonResponse({"ok": False, "error": str(exc)}, status=400)


@require_POST
def api_save_notes(request):
    ensure_seeded()
    try:
        data = json.loads(request.body.decode("utf-8"))
        prof = get_active_profile(request)
        if prof:
            prof.personal_notes = data.get("notes", "")
            prof.save()
        return JsonResponse({"ok": True})
    except Exception as exc:
        return JsonResponse({"ok": False, "error": str(exc)}, status=400)
