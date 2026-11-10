from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("courses/", views.courses_view, name="courses"),
    path("learn/<slug:course_slug>/", views.lesson_player_view, name="lesson_player"),
    path("games/", views.games_arcade_view, name="games_arcade"),
    path("tasks/", views.tasks_contests_view, name="tasks_contests"),
    path("sandbox/", views.sandbox_ide_view, name="sandbox_ide"),
    path("student-dashboard/", views.student_dashboard_view, name="student_dashboard"),
    path("certificate/", views.certificate_view, name="certificate"),
    path("instructor-panel/", views.instructor_crud_view, name="instructor_crud"),
    path("about/", views.about_view, name="about"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("api/submit-code/", views.api_submit_code, name="api_submit_code"),
    path("api/save-notes/", views.api_save_notes, name="api_save_notes"),
]
