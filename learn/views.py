from .tasks_data import CODING_TASKS
import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils import timezone
from .models import Language, Course, Lesson, Game, UserProfile, UserProgress, Badge, Feedback


def custom_admin_404(request):
    """Strictly return 404 on default /admin/ to deceive scanners and prevent brute force."""
    raise Http404("Admin endpoint not found.")


def landing(request):
    featured_courses = Course.objects.select_related("language").prefetch_related("lessons").all()[:6]
    games = Game.objects.all()[:6]
    total_lessons = Lesson.objects.count()
    languages = Language.objects.filter(is_active=True)

    recent_lesson = None
    if request.user.is_authenticated:
        recent_prog = request.user.progress.select_related("lesson__course__language").first()
        if recent_prog:
            recent_lesson = recent_prog.lesson

    return render(
        request,
        "learn/landing.html",
        {
            "featured_courses": featured_courses,
            "games": games,
            "total_lessons": total_lessons,
            "languages": languages,
            "recent_lesson": recent_lesson,
        },
    )


def catalogue(request):
    languages = list(Language.objects.filter(is_active=True).prefetch_related("courses__lessons"))
    
    learner_context = {
        "is_authenticated": False,
    }
    completed_lesson_ids = set()
    
    if request.user.is_authenticated:
        # User profile
        profile, _ = UserProfile.objects.get_or_create(user=request.user)
        
        # All user progress items
        user_progs = list(
            request.user.progress.select_related("lesson__course__language").all()
        )
        completed_progs = [p for p in user_progs if p.status == "COMPLETED"]
        completed_lesson_ids = set(p.lesson_id for p in completed_progs)
        
        total_lessons_count = Lesson.objects.count()
        completed_count = len(completed_lesson_ids)
        overall_pct = int(round((completed_count / total_lessons_count * 100))) if total_lessons_count > 0 else 0
        
        # Resume Lesson logic
        continue_lesson = None
        active_course = None
        
        # 1. Look for in-progress lesson
        in_progress = [p for p in user_progs if p.status == "IN_PROGRESS" and p.lesson_id not in completed_lesson_ids]
        if in_progress:
            continue_lesson = in_progress[0].lesson
            active_course = continue_lesson.course
        elif completed_progs:
            # Look for next lesson after the most recently completed one
            last_completed = completed_progs[0].lesson
            course_lessons = list(last_completed.course.lessons.order_by("order", "id"))
            curr_idx = -1
            for idx, l in enumerate(course_lessons):
                if l.id == last_completed.id:
                    curr_idx = idx
                    break
            if curr_idx != -1 and curr_idx + 1 < len(course_lessons):
                continue_lesson = course_lessons[curr_idx + 1]
                active_course = last_completed.course
            else:
                # Course is finished; find first uncompleted lesson in any active course
                for lang in languages:
                    for c in lang.courses.all():
                        for l in c.lessons.all():
                            if l.id not in completed_lesson_ids:
                                continue_lesson = l
                                active_course = c
                                break
                        if continue_lesson:
                            break
                    if continue_lesson:
                        break
        
        if not continue_lesson:
            first_course = Course.objects.first()
            if first_course:
                continue_lesson = first_course.lessons.first()
                active_course = first_course

        # Active course progress
        active_course_progress = {"completed": 0, "total": 0, "pct": 0}
        if active_course:
            total_c = active_course.lessons.count()
            comp_c = len([l for l in active_course.lessons.all() if l.id in completed_lesson_ids])
            pct_c = int(round((comp_c / total_c * 100))) if total_c > 0 else 0
            active_course_progress = {
                "completed": comp_c,
                "total": total_c,
                "pct": pct_c,
            }

        # Per-course progress map
        for lang in languages:
            for course in lang.courses.all():
                c_lessons = list(course.lessons.all())
                c_total = len(c_lessons)
                c_completed = len([l for l in c_lessons if l.id in completed_lesson_ids])
                c_pct = int(round((c_completed / c_total * 100))) if c_total > 0 else 0
                course.user_progress = {
                    "completed": c_completed,
                    "total": c_total,
                    "pct": c_pct,
                    "is_started": c_completed > 0 or any(p.lesson.course_id == course.id for p in user_progs),
                    "is_completed": c_completed == c_total and c_total > 0,
                }

        # 7-day activity tracking dots
        today = timezone.now().date()
        days = []
        for i in range(6, -1, -1):
            d = today - timezone.timedelta(days=i)
            is_active_day = False
            if profile.last_active == d:
                is_active_day = True
            elif profile.last_active > d and (profile.last_active - d).days < profile.streak:
                is_active_day = True

            days.append({
                "name": d.strftime("%a")[:3],
                "date_num": d.strftime("%d"),
                "is_today": (d == today),
                "is_active": is_active_day,
            })

        # Rank tiering
        xp = profile.xp
        if xp >= 1500:
            rank_title = "Architect Tier"
            rank_icon = "👑"
            next_tier_xp = 3000
        elif xp >= 800:
            rank_title = "Senior Engineer"
            rank_icon = "🚀"
            next_tier_xp = 1500
        elif xp >= 300:
            rank_title = "Fullstack Journeyman"
            rank_icon = "⚡"
            next_tier_xp = 800
        elif xp >= 100:
            rank_title = "Junior Explorer"
            rank_icon = "🌱"
            next_tier_xp = 300
        else:
            rank_title = "Novice Apprentice"
            rank_icon = "⭐"
            next_tier_xp = 100

        # Tier progress percentage
        prev_tier_xp = 0
        if rank_title == "Junior Explorer":
            prev_tier_xp = 100
        elif rank_title == "Fullstack Journeyman":
            prev_tier_xp = 300
        elif rank_title == "Senior Engineer":
            prev_tier_xp = 800
        elif rank_title == "Architect Tier":
            prev_tier_xp = 1500

        tier_span = max(1, next_tier_xp - prev_tier_xp)
        tier_xp_gained = max(0, xp - prev_tier_xp)
        tier_pct = min(100, int(round((tier_xp_gained / tier_span) * 100)))

        learner_stats = {
            "xp": profile.xp,
            "streak": profile.streak,
            "completed_lessons": completed_count,
            "total_lessons": total_lessons_count,
            "overall_pct": overall_pct,
            "rank_title": rank_title,
            "rank_icon": rank_icon,
            "next_tier_xp": next_tier_xp,
            "tier_pct": tier_pct,
            "days": days,
        }

        learner_context = {
            "is_authenticated": True,
            "profile": profile,
            "learner_stats": learner_stats,
            "continue_lesson": continue_lesson,
            "active_course": active_course,
            "active_course_progress": active_course_progress,
        }
    else:
        for lang in languages:
            for course in lang.courses.all():
                course.user_progress = {
                    "completed": 0,
                    "total": course.lessons.count(),
                    "pct": 0,
                    "is_started": False,
                    "is_completed": False,
                }

    return render(
        request,
        "learn/catalogue.html",
        {
            "languages": languages,
            "learner": learner_context,
            "completed_lesson_ids": completed_lesson_ids,
        },
    )


def course_detail(request, course_slug):
    course = get_object_or_404(Course.objects.select_related("language").prefetch_related("lessons"), slug=course_slug)
    lessons = list(course.lessons.all())
    
    completed_ids = set()
    if request.user.is_authenticated:
        completed_ids = set(
            request.user.progress.filter(lesson__course=course, status="COMPLETED").values_list("lesson_id", flat=True)
        )

    return render(
        request,
        "learn/course_detail.html",
        {
            "course": course,
            "lessons": lessons,
            "completed_ids": completed_ids,
        },
    )


def lesson_detail(request, course_slug, lesson_slug):
    course = get_object_or_404(Course.objects.select_related("language"), slug=course_slug)
    lesson = get_object_or_404(Lesson.objects.select_related("course"), course=course, slug=lesson_slug)
    all_lessons = list(course.lessons.all())
    
    curr_idx = -1
    for idx, l in enumerate(all_lessons):
        if l.id == lesson.id:
            curr_idx = idx
            break

    prev_lesson = all_lessons[curr_idx - 1] if curr_idx > 0 else None
    next_lesson = all_lessons[curr_idx + 1] if curr_idx < len(all_lessons) - 1 else None

    # Track start & fetch completed lessons for syllabus drawer
    completed_ids = set()
    if request.user.is_authenticated:
        UserProgress.objects.get_or_create(
            user=request.user,
            lesson=lesson,
            defaults={"status": "IN_PROGRESS", "attempts": 1}
        )
        completed_ids = set(
            UserProgress.objects.filter(
                user=request.user,
                lesson__course=course,
                status="COMPLETED"
            ).values_list("lesson_id", flat=True)
        )

    return render(
        request,
        "learn/lesson_detail.html",
        {
            "course": course,
            "lesson": lesson,
            "prev_lesson": prev_lesson,
            "next_lesson": next_lesson,
            "all_lessons": all_lessons,
            "completed_ids": completed_ids,
            "tests_json_str": json.dumps(lesson.tests_json or []),
            "hints_json_str": json.dumps(lesson.hints_json or []),
        },
    )


@require_POST
def api_check_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    passed = False
    xp_awarded = 0
    new_badge = None

    try:
        data = json.loads(request.body.decode("utf-8"))
        passed = bool(data.get("passed", False))
    except Exception:
        pass

    if passed and request.user.is_authenticated:
        prog, created = UserProgress.objects.get_or_create(
            user=request.user,
            lesson=lesson,
            defaults={"status": "COMPLETED", "completed_at": timezone.now()}
        )
        if not created and prog.status != "COMPLETED":
            prog.status = "COMPLETED"
            prog.completed_at = timezone.now()
            prog.save(update_fields=["status", "completed_at"])

        profile = getattr(request.user, "profile", None)
        if profile:
            profile.xp += lesson.xp
            profile.record_activity()
            profile.save(update_fields=["xp", "streak", "last_active"])
            xp_awarded = lesson.xp

            # Badge unlock check
            if profile.xp >= 100:
                badge = Badge.objects.filter(slug="first-code").first()
                if badge and not badge.earned_by.filter(id=request.user.id).exists():
                    badge.earned_by.add(request.user)
                    new_badge = badge.name

    return JsonResponse({
        "ok": True,
        "passed": passed,
        "xp_awarded": xp_awarded,
        "new_badge": new_badge,
    })


@require_POST
def api_sync_guest_progress(request):
    """Sync guest localStorage lesson IDs & XP to the logged-in user profile."""
    if not request.user.is_authenticated:
        return JsonResponse({"ok": False, "error": "Not authenticated"}, status=401)

    try:
        data = json.loads(request.body.decode("utf-8"))
        completed_ids = data.get("completed_ids", [])
        profile = request.user.profile
        
        synced_count = 0
        for lid in completed_ids:
            try:
                lesson = Lesson.objects.get(pk=lid)
                prog, created = UserProgress.objects.get_or_create(
                    user=request.user,
                    lesson=lesson,
                    defaults={"status": "COMPLETED", "completed_at": timezone.now()}
                )
                if created:
                    profile.xp += lesson.xp
                    synced_count += 1
            except Lesson.DoesNotExist:
                pass

        if synced_count > 0:
            profile.record_activity()
            profile.save(update_fields=["xp", "streak", "last_active"])

        return JsonResponse({"ok": True, "synced_count": synced_count, "total_xp": profile.xp})
    except Exception as exc:
        return JsonResponse({"ok": False, "error": str(exc)}, status=400)


def playground(request):
    """Universal multi-language browser IDE and terminal studio."""
    task_id = request.GET.get("task")
    lang_param = request.GET.get("lang", "").lower().strip()
    selected_task = None
    initial_lang = "web"

    if task_id:
        for t in CODING_TASKS:
            if t["id"] == task_id:
                selected_task = t
                if t.get("cat") == "algorithms":
                    initial_lang = "python"
                elif t.get("cat") == "sql":
                    initial_lang = "sql"
                elif t.get("cat") == "systems":
                    initial_lang = "c"
                elif t.get("cat") == "frontend":
                    initial_lang = "web"
                break
    elif lang_param in ["python", "sql", "c", "go", "rust", "java", "bash", "web"]:
        initial_lang = lang_param

    return render(
        request,
        "learn/playground.html",
        {
            "selected_task": selected_task,
            "initial_lang": initial_lang,
            "task_id": task_id or "",
        },
    )


def games_hub(request):
    games = Game.objects.all()
    active_mode = request.GET.get("mode", "tasks")
    return render(request, "games/hub.html", {
        "games": games,
        "tasks": CODING_TASKS,
        "active_mode": active_mode,
        "total_tasks_xp": sum(t["xp"] for t in CODING_TASKS),
    })


def game_play(request, game_slug):
    game = get_object_or_404(Game, slug=game_slug)
    template_name = f"games/{game_slug.replace('-', '_')}.html"
    return render(request, template_name, {"game": game})


@require_POST
def api_record_game_score(request, game_slug):
    game = get_object_or_404(Game, slug=game_slug)
    xp_earned = 0
    if request.user.is_authenticated:
        profile = request.user.profile
        profile.xp += game.xp_per_win
        profile.record_activity()
        profile.save(update_fields=["xp", "streak", "last_active"])
        xp_earned = game.xp_per_win
    return JsonResponse({"ok": True, "xp_earned": xp_earned})


@login_required
def profile_view(request):
    profile = request.user.profile
    progress_list = request.user.progress.select_related("lesson__course__language").filter(status="COMPLETED")
    badges = request.user.badges.all()
    available_badges = Badge.objects.exclude(earned_by=request.user)

    return render(
        request,
        "learn/profile.html",
        {
            "profile": profile,
            "progress_list": progress_list,
            "badges": badges,
            "available_badges": available_badges,
        },
    )


def about_view(request):
    return render(request, "learn/about.html")


def login_view(request):
    if request.user.is_authenticated:
        return redirect("profile_view")
    err = None
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "demo_login":
            demo_user, _ = User.objects.get_or_create(
                username="demo_learner",
                defaults={"email": "demo@codequest-bd.com"}
            )
            login(request, demo_user)
            next_url = request.GET.get("next", "catalogue")
            return redirect(next_url)

        u = request.POST.get("username", "").strip()
        p = request.POST.get("password", "").strip()
        user = authenticate(request, username=u, password=p)
        if user:
            login(request, user)
            next_url = request.GET.get("next", "catalogue")
            return redirect(next_url)
        err = "Invalid username or password. Please try again."
    return render(request, "learn/login.html", {"error": err})


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("profile_view")
    err = None
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "demo_login":
            demo_user, _ = User.objects.get_or_create(
                username="demo_learner",
                defaults={"email": "demo@codequest-bd.com"}
            )
            login(request, demo_user)
            return redirect("catalogue")

        u = request.POST.get("username", "").strip()
        e = request.POST.get("email", "").strip()
        p = request.POST.get("password", "").strip()
        if not u or not p:
            err = "Username and password are required."
        elif User.objects.filter(username=u).exists():
            err = "That username is already registered."
        elif len(p) < 6:
            err = "Password must be at least 6 characters."
        else:
            user = User.objects.create_user(username=u, email=e, password=p)
            login(request, user)
            return redirect("catalogue")
    return render(request, "learn/signup.html", {"error": err})


def logout_view(request):
    logout(request)
    return redirect("landing")


@require_POST
def submit_feedback(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        lesson_id = data.get("lesson_id")
        lesson = Lesson.objects.filter(id=lesson_id).first() if lesson_id else None
        
        Feedback.objects.create(
            user=request.user if request.user.is_authenticated else None,
            lesson=lesson,
            category=data.get("category", "CONTENT"),
            message=data.get("message", "").strip(),
            email=data.get("email", "").strip(),
        )
        return JsonResponse({"ok": True})
    except Exception as exc:
        return JsonResponse({"ok": False, "error": str(exc)}, status=400)


def api_cloud_db_status(request):
    """
    Diagnostic and health check endpoint for database persistence and integrity.
    Provides immediate verification of whether Vercel is running on persistent Neon Postgres or ephemeral SQLite.
    """
    from django.db import connection
    from django.conf import settings
    from django.core.management import call_command
    import os

    db_settings = connection.settings_dict
    engine = db_settings.get("ENGINE", "")
    is_postgres = "postgresql" in engine
    is_vercel = "VERCEL" in os.environ
    db_host = db_settings.get("HOST", "")

    action = request.GET.get("action", "")
    key = request.GET.get("key", "")
    migration_output = None

    if action in ("migrate", "seed") and key and key == getattr(settings, "SECRET_KEY", ""):
        try:
            call_command("migrate", interactive=False)
            call_command("seed_lessons")
            migration_output = "Migration and seed executed successfully."
        except Exception as e:
            migration_output = f"Error during execution: {str(e)}"

    tables = connection.introspection.table_names()
    user_count = User.objects.count() if "auth_user" in tables else 0
    lesson_count = Lesson.objects.count() if "learn_lesson" in tables else 0
    course_count = Course.objects.count() if "learn_course" in tables else 0

    if is_postgres:
        status_msg = "HEALTHY: Connected to persistent cloud PostgreSQL database (Neon/Supabase)."
        persistence = "Persistent Cloud Storage"
    elif is_vercel:
        status_msg = "WARNING: Running on ephemeral Vercel /tmp SQLite. User accounts reset on cold start. Add DATABASE_URL to Vercel Environment Variables."
        persistence = "Ephemeral (Reset on cold start)"
    else:
        status_msg = "LOCAL: Running on local SQLite database."
        persistence = "Local File Storage"

    return JsonResponse({
        "status": status_msg,
        "engine": engine,
        "persistence_mode": persistence,
        "is_postgres": is_postgres,
        "is_vercel": is_vercel,
        "database_host": db_host if is_postgres else "Local /tmp",
        "tables_count": len(tables),
        "users_count": user_count,
        "courses_count": course_count,
        "lessons_count": lesson_count,
        "action_result": migration_output,
    })
