from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from learn.models import (
    LanguageTrack,
    MicroLesson,
    CodingGameChallenge,
    StudentProfile,
    TelemetryAndSecurityLog,
)
from learn.views import ensure_v10_seeded


def admin_dashboard(request):
    """Separate Admin Power Control Center (Req #22, #24)."""
    ensure_v10_seeded()
    msg = None
    if request.method == "POST":
        act = request.POST.get("admin_action", "")
        if act == "create_game":
            num = CodingGameChallenge.objects.count() + 1
            title = request.POST.get("title", f"Custom 3D Game #{num}")
            CodingGameChallenge.objects.create(
                game_number=num,
                slug=f"game-{num:03d}-custom",
                title=f"#{num:03d} — {title}",
                category_name=request.POST.get("category_name", "CyberPunk 3D Rover"),
                engine_mode=request.POST.get("engine_mode", "ROVER_3D"),
                language_tag=request.POST.get("language_tag", "Python / JS"),
                difficulty=request.POST.get("difficulty", "Intermediate"),
                xp_reward=int(request.POST.get("xp_reward", 100) or 100),
                mission_brief=request.POST.get("mission_brief", "Custom admin-created 3D coding challenge."),
                starter_code=request.POST.get("starter_code", "for d in range(6):\n    grow_branch(26)"),
                solution_code=request.POST.get("starter_code", "for d in range(6):\n    grow_branch(26)"),
            )
            msg = f"Created new 3D Game Challenge #{num:03d}: {title}!"
        elif act == "delete_game":
            CodingGameChallenge.objects.filter(pk=request.POST.get("game_id")).delete()
            msg = "Deleted coding game challenge."
        elif act == "create_language":
            LanguageTrack.objects.create(
                slug=request.POST.get("slug", "new-lang").strip(),
                name=request.POST.get("name", "New Language").strip(),
                short_code=request.POST.get("short_code", "NL").strip(),
                category=request.POST.get("category", "Systems & AI").strip(),
                engine_mode=request.POST.get("engine_mode", "TREE_3D"),
                summary=request.POST.get("summary", "Custom language track."),
                order=LanguageTrack.objects.count() + 1,
            )
            msg = "Added new programming language track!"
        elif act == "boost_student_xp":
            sp = StudentProfile.objects.filter(pk=request.POST.get("profile_id")).first()
            if sp:
                sp.xp += 500
                sp.streak_freeze_shields += 1
                sp.save()
                msg = f"Granted +500 Bonus XP & +1 Streak Shield to {sp.user.username}!"

    return render(
        request,
        "instructor_panel/dashboard.html",
        {
            "tracks": LanguageTrack.objects.all(),
            "games": CodingGameChallenge.objects.all()[:30],
            "total_games": CodingGameChallenge.objects.count(),
            "students": StudentProfile.objects.select_related("user").all(),
            "logs": TelemetryAndSecurityLog.objects.all()[:15],
            "status_msg": msg,
            "active_page": "admin_panel",
        },
    )
