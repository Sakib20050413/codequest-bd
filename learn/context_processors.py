from django.conf import settings
from .models import Course, Language
from .automation_engine import ensure_autonomous_platform_state, get_daily_auto_tasks


def global_stats(request):
    ensure_autonomous_platform_state()
    xp = 640
    course_streak = 7
    game_streak = 5
    completed_ids = []
    if request.user.is_authenticated:
        if hasattr(request.user, "profile"):
            xp = request.user.profile.xp
            course_streak = max(1, request.user.profile.streak)
            game_streak = max(1, (request.user.profile.xp // 120) or 3)
        completed_ids = list(
            request.user.progress.filter(status="COMPLETED").values_list("lesson_id", flat=True)
        )

    return {
        "ADMIN_URL": getattr(settings, "ADMIN_URL", "hidden-core-cms"),
        "user_xp": xp,
        "user_streak": course_streak,
        "course_streak": course_streak,
        "game_streak": game_streak,
        "completed_lesson_ids": completed_ids,
        "nav_languages": Language.objects.filter(is_active=True).prefetch_related("courses")[:16],
        "daily_auto_tasks": get_daily_auto_tasks(),
    }
