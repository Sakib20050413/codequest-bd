from django.contrib import admin
from .models import StudentProfile


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'student_id', 'batch_section', 'xp', 'level', 'avatar', 'created_at')
    search_fields = ('user__username', 'student_id', 'batch_section', 'user__first_name')
    list_filter = ('level', 'batch_section')
