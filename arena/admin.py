from django.contrib import admin
from .models import LanguageTrack, ChallengeLevel, QuizQuestion, StudentSubmission, LabAnnouncement


@admin.register(LanguageTrack)
class LanguageTrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'difficulty', 'order', 'is_active', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('difficulty', 'is_active')


@admin.register(ChallengeLevel)
class ChallengeLevelAdmin(admin.ModelAdmin):
    list_display = ('title', 'track', 'level_number', 'engine', 'xp_reward', 'order')
    list_filter = ('track', 'engine')
    search_fields = ('title', 'story_brief')


@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'category', 'difficulty', 'correct_option', 'points')
    list_filter = ('category', 'difficulty')
    search_fields = ('question_text', 'explanation')


@admin.register(StudentSubmission)
class StudentSubmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'language', 'status', 'xp_earned', 'submitted_at')
    list_filter = ('status', 'language')
    search_fields = ('user__username', 'level__title')


@admin.register(LabAnnouncement)
class LabAnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'badge', 'is_active', 'created_at')
    list_filter = ('badge', 'is_active')
