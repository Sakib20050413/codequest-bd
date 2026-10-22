from .models import LabAnnouncement


def global_announcements(request):
    try:
        active_announcements = LabAnnouncement.objects.filter(is_active=True)[:3]
    except Exception:
        active_announcements = []
    return {
        'global_announcements': active_announcements,
        'app_student_name': 'Md Najmus Sakib Rahatul',
        'app_student_id': '1119003',
        'app_batch_section': 'CSE 3-2 Section A',
        'app_university': 'BAIUST, Cumilla',
        'app_course': 'CSE 324 Web Technologies Sessional',
    }
