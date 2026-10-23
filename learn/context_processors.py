from django.conf import settings
from .models import Course, Language


def global_stats(request):
    xp = 0
    streak = 1
    completed_ids = []
    if request.user.is_authenticated:
        if hasattr(request.user, "profile"):
            xp = request.user.profile.xp
            streak = request.user.profile.streak
        completed_ids = list(
            request.user.progress.filter(status="COMPLETED").values_list("lesson_id", flat=True)
        )

    return {
        "ADMIN_URL": getattr(settings, "ADMIN_URL", "hidden-core-cms"),
        "user_xp": xp,
        "user_streak": streak,
        "completed_lesson_ids": completed_ids,
        "nav_languages": Language.objects.filter(is_active=True).prefetch_related("courses")[:6],
    }
