import csv
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.management import call_command
from django.db.utils import OperationalError, ProgrammingError
from .models import (
    LanguageTrack,
    MicroLesson,
    CodingGameChallenge,
    StudentProfile,
    TelemetryAndSecurityLog,
)


def ensure_v10_seeded():
    """Auto-migrates and seeds 16 languages + 108 games on cold start if needed."""
    try:
        if LanguageTrack.objects.count() < 16 or CodingGameChallenge.objects.count() < 100:
            from seed_codequest import seed_all
            seed_all()
    except (OperationalError, ProgrammingError):
        try:
            call_command("migrate", interactive=False, verbosity=0)
            from seed_codequest import seed_all
            seed_all()
        except Exception:
            pass


def build_common_payload():
    ensure_v10_seeded()
    tracks = LanguageTrack.objects.prefetch_related("lessons").all()
    games = CodingGameChallenge.objects.all()

    lessons_list = []
    for tr in tracks:
        for les in tr.lessons.all():
            lessons_list.append({
                "id": les.id,
                "trackSlug": tr.slug,
                "trackName": tr.name,
                "trackCode": tr.short_code,
                "category": tr.category,
                "runtime": tr.compiler_runtime,
                "engineMode": tr.engine_mode,
                "accentHex": tr.accent_hex,
                "summary": tr.summary,
                "lessonSlug": les.slug,
                "title": les.title,
                "durationBadge": les.duration_badge,
                "mentalModel": les.cs50_mental_model,
                "videoScript": les.ai_video_narration,
                "cheatRows": les.parsed_cheats(),
                "task1": les.task_1_prompt,
                "task2": les.task_2_prompt,
                "task3": les.task_3_prompt,
                "starterCode": les.starter_code,
                "solutionCode": les.solution_code,
                "hint": les.hint_text,
                "xp": les.xp_reward,
            })

    games_list = [
        {
            "num": g.game_number,
            "slug": g.slug,
            "title": g.title,
            "category": g.category_name,
            "engine": g.engine_mode,
            "lang": g.language_tag,
            "diff": g.difficulty,
            "dur": g.duration_Label,
            "xp": g.xp_reward,
            "brief": g.mission_brief,
            "starter": g.starter_code,
            "solution": g.solution_code,
        }
        for g in games
    ]
    return tracks, games, lessons_list, games_list


def landing(request):
    tracks, games, lessons_list, games_list = build_common_payload()
    telemetry_logs = TelemetryAndSecurityLog.objects.all()[:12]
    return render(
        request,
        "learn/landing.html",
        {
            "tracks": tracks,
            "games_featured": games[:12],
            "total_games_count": games.count(),
            "lessons_json": json.dumps(lessons_list),
            "games_json": json.dumps(games_list),
            "telemetry_logs": telemetry_logs,
            "active_page": "home",
        },
    )


def catalogue(request):
    tracks, games, lessons_list, games_list = build_common_payload()
    return render(
        request,
        "learn/catalogue.html",
        {
            "tracks": tracks,
            "lessons_json": json.dumps(lessons_list),
            "active_page": "courses",
        },
    )


def course_detail(request, course_slug):
    ensure_v10_seeded()
    track = get_object_or_404(LanguageTrack, slug=course_slug)
    lesson = track.lessons.first()
    if lesson:
        return redirect("lesson_detail", course_slug=track.slug, lesson_slug=lesson.slug)
    return redirect("catalogue")


def lesson_detail(request, course_slug, lesson_slug):
    tracks, games, lessons_list, games_list = build_common_payload()
    track = get_object_or_404(LanguageTrack, slug=course_slug)
    lesson = track.lessons.filter(slug=lesson_slug).first() or track.lessons.first()
    return render(
        request,
        "learn/lesson_detail.html",
        {
            "track": track,
            "lesson": lesson,
            "tracks": tracks,
            "lessons_json": json.dumps(lessons_list),
            "active_page": "courses",
        },
    )


def playground(request):
    tracks, games, lessons_list, games_list = build_common_payload()
    return render(
        request,
        "learn/playground.html",
        {
            "tracks": tracks,
            "lessons_json": json.dumps(lessons_list),
            "active_page": "playground",
        },
    )


def games_hub(request):
    tracks, games, lessons_list, games_list = build_common_payload()
    return render(
        request,
        "games/hub.html",
        {
            "games": games,
            "total_games_count": games.count(),
            "games_json": json.dumps(games_list),
            "active_page": "games",
        },
    )


def game_play(request, game_slug):
    tracks, games, lessons_list, games_list = build_common_payload()
    game = CodingGameChallenge.objects.filter(slug=game_slug).first() or games.first()
    return render(
        request,
        "games/rover_3d.html",
        {
            "game": game,
            "games_json": json.dumps(games_list),
            "active_page": "games",
        },
    )


def about_view(request):
    ensure_v10_seeded()
    return render(request, "learn/about.html", {"active_page": "about"})


def login_view(request):
    ensure_v10_seeded()
    err = None
    if request.method == "POST":
        u = request.POST.get("username", "").strip()
        p = request.POST.get("password", "").strip()
        user = authenticate(request, username=u, password=p)
        if user:
            login(request, user)
            prof, _ = StudentProfile.objects.get_or_create(user=user)
            if prof.role == "ADMIN" or user.is_superuser:
                return redirect("/instructor-panel/")
            return redirect("profile_view")
        err = "Invalid credentials. Try Student (`pro_learner` / `codequest2026`) or Admin (`sakib_admin` / `baiust1119003`)."
    return render(request, "learn/login.html", {"error": err, "active_page": "login"})


def signup_view(request):
    ensure_v10_seeded()
    err = None
    if request.method == "POST":
        u = request.POST.get("username", "").strip()
        e = request.POST.get("email", "").strip()
        p = request.POST.get("password", "").strip()
        if not u or not p:
            err = "Username and password are required."
        elif User.objects.filter(username=u).exists():
            err = "Username already exists. Please choose another."
        else:
            user = User.objects.create_user(username=u, email=e, password=p)
            StudentProfile.objects.create(user=user, role="STUDENT", xp=500, streak_days=1)
            login(request, user)
            return redirect("profile_view")
    return render(request, "learn/signup.html", {"error": err, "active_page": "signup"})


def logout_view(request):
    logout(request)
    return redirect("landing")


def profile_view(request):
    """Programming-Hero-Style Student Learning Dashboard (Req #19, #21, #22, #23)."""
    tracks, games, lessons_list, games_list = build_common_payload()
    if request.user.is_authenticated:
        prof, _ = StudentProfile.objects.get_or_create(user=request.user)
    else:
        demo_u = User.objects.filter(username="pro_learner").first()
        prof = StudentProfile.objects.filter(user=demo_u).first()

    msg = None
    if request.method == "POST" and prof:
        act = request.POST.get("student_action", "")
        if act == "save_scratchpad":
            prof.personal_scratchpad = request.POST.get("scratchpad", "")
            prof.save()
            msg = "Saved your personal developer notes & scratchpad!"
        elif act == "claim_daily_chest":
            prof.xp += 150
            prof.streak_days += 1
            prof.save()
            msg = "🔥 Claimed Daily Streak Chest (+150 Bonus XP & +1 Day Streak)!"

    return render(
        request,
        "learn/profile.html",
        {
            "profile": prof,
            "tracks": tracks,
            "games_sample": games[:8],
            "status_msg": msg,
            "active_page": "student_dashboard",
        },
    )


@require_POST
def api_log_telemetry(request):
    ensure_v10_seeded()
    try:
        data = json.loads(request.body.decode("utf-8"))
        raw_code = str(data.get("code", ""))
        # Security / Anti-Hack Sandbox Check (Req #27)
        blocked_patterns = ["<script>alert(", "DROP TABLE", "rm -rf /", "__import__('os').system"]
        sec_status = "SANDBOX_CLEAN_PASS"
        for pat in blocked_patterns:
            if pat.lower() in raw_code.lower():
                sec_status = "BLOCKED_MALICIOUS_PAYLOAD"
                break

        log = TelemetryAndSecurityLog.objects.create(
            session_hash=data.get("session_hash", "live-learner"),
            event_type=data.get("event_type", "CODE_EXECUTION"),
            language_slug=data.get("language_slug", "python"),
            module_title=data.get("lesson_title", "Interactive Sandbox"),
            engine_mode=data.get("engine_mode", "TREE_3D"),
            ttc_seconds=float(data.get("ttc_sec", 38.5)),
            latency_ms=float(data.get("latency_ms", 4.1)),
            security_status=sec_status,
        )
        return JsonResponse({"ok": True, "id": log.id, "security_status": sec_status})
    except Exception as exc:
        return JsonResponse({"ok": False, "error": str(exc)}, status=400)


def api_export_telemetry_csv(request):
    ensure_v10_seeded()
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="codequest_v10_ieee_telemetry.csv"'
    writer = csv.writer(response)
    writer.writerow(["Session", "EventType", "Language", "Module", "3DEngine", "TTC_Sec", "Latency_Ms", "SecurityStatus", "Timestamp"])
    for r in TelemetryAndSecurityLog.objects.all():
        writer.writerow([r.session_hash, r.event_type, r.language_slug, r.module_title, r.engine_mode, r.ttc_seconds, r.latency_ms, r.security_status, r.created_at.isoformat()])
    return response


def api_export_telemetry_json(request):
    ensure_v10_seeded()
    records = [
        {
            "session": r.session_hash,
            "event": r.event_type,
            "language": r.language_slug,
            "module": r.module_title,
            "engine": r.engine_mode,
            "ttc_sec": r.ttc_seconds,
            "latency_ms": r.latency_ms,
            "security": r.security_status,
            "timestamp": r.created_at.isoformat(),
        }
        for r in TelemetryAndSecurityLog.objects.all()
    ]
    return JsonResponse({"dataset": "CodeQuest BD V10.0 Telemetry & Security Audit", "count": len(records), "records": records})
