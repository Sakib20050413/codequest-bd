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
    languages = Language.objects.filter(is_active=True).prefetch_related("courses__lessons")
    return render(request, "learn/catalogue.html", {"languages": languages})


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

    # Track start
    if request.user.is_authenticated:
        UserProgress.objects.get_or_create(
            user=request.user,
            lesson=lesson,
            defaults={"status": "IN_PROGRESS", "attempts": 1}
        )

    return render(
        request,
        "learn/lesson_detail.html",
        {
            "course": course,
            "lesson": lesson,
            "prev_lesson": prev_lesson,
            "next_lesson": next_lesson,
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
    """Free-form interactive playground with iframe live preview."""
    return render(request, "learn/playground.html")


def games_hub(request):
    games = Game.objects.all()
    return render(request, "games/hub.html", {"games": games})


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
