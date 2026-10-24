from django.contrib import admin
from .models import (
    LanguageTrack,
    MicroLesson,
    CodingGameChallenge,
    StudentProfile,
    TelemetryAndSecurityLog,
)


@admin.register(LanguageTrack)
class LanguageTrackAdmin(admin.ModelAdmin):
    list_display = ("order", "name", "slug", "short_code", "category", "engine_mode")
    list_display_links = ("name",)
    list_editable = ("order",)
    search_fields = ("name", "slug", "short_code")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(MicroLesson)
class MicroLessonAdmin(admin.ModelAdmin):
    list_display = ("step_number", "title", "track", "duration_badge", "xp_reward")
    list_display_links = ("title",)
    list_editable = ("step_number", "xp_reward")
    list_filter = ("track",)
    search_fields = ("title", "cs50_mental_model", "starter_code")


@admin.register(CodingGameChallenge)
class CodingGameChallengeAdmin(admin.ModelAdmin):
    list_display = ("game_number", "title", "category_name", "engine_mode", "difficulty", "xp_reward")
    list_display_links = ("title",)
    list_editable = ("difficulty", "xp_reward")
    list_filter = ("engine_mode", "difficulty")
    search_fields = ("title", "mission_brief")


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "xp", "streak_days", "league_tier")
    list_filter = ("role", "league_tier")
    search_fields = ("user__username", "user__email")


@admin.register(TelemetryAndSecurityLog)
class TelemetryAndSecurityLogAdmin(admin.ModelAdmin):
    list_display = ("created_at", "session_hash", "event_type", "language_slug", "security_status", "latency_ms")
    list_filter = ("event_type", "security_status")
    search_fields = ("session_hash", "module_title")
