from django.contrib import admin
from .models import Language, Course, Lesson, Game, UserProfile, UserProgress, Badge, Feedback


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("order", "name", "slug", "short_code", "category", "is_active")
    list_display_links = ("name",)
    list_editable = ("order", "is_active")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


class LessonInline(admin.TabularInline):
    model = Lesson
    fields = ("order", "title", "slug", "execution_type", "est_minutes", "xp")
    extra = 1
    show_change_link = True


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("order", "title", "language", "level", "lesson_count", "xp_reward")
    list_display_links = ("title",)
    list_editable = ("order",)
    list_filter = ("language", "level")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [LessonInline]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("order", "title", "course", "execution_type", "est_minutes", "xp")
    list_display_links = ("title",)
    list_editable = ("order", "est_minutes", "xp")
    list_filter = ("course__language", "course", "execution_type")
    search_fields = ("title", "body_md", "starter_code")
    fieldsets = (
        ("Structure", {"fields": ("course", "title", "slug", "order", "est_minutes", "xp", "execution_type")}),
        ("Bite-Sized Explanation", {"fields": ("body_md", "diagram_svg")}),
        ("Interactive Task", {"fields": ("task_prompt", "starter_code", "solution")}),
        ("Validation & Hints (JSON)", {"fields": ("tests_json", "hints_json")}),
    )


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("order", "title", "slug", "category", "difficulty", "xp_per_win")
    list_display_links = ("title",)
    list_editable = ("order", "xp_per_win")
    search_fields = ("title", "description")


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "xp", "streak", "last_active", "theme_pref")
    search_fields = ("user__username", "user__email")
    list_filter = ("theme_pref", "last_active")


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "lesson", "status", "attempts", "completed_at")
    list_filter = ("status", "completed_at")
    search_fields = ("user__username", "lesson__title")


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "xp_required")
    search_fields = ("name", "description")


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("category", "user", "lesson", "created_at")
    list_filter = ("category", "created_at")
    search_fields = ("message", "email")
    readonly_fields = ("created_at",)
