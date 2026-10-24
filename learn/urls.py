from django.urls import path
from . import views
from instructor_panel.views import admin_dashboard

urlpatterns = [
    path("", views.landing, name="landing"),
    path("courses/", views.catalogue, name="catalogue"),
    path("courses/<slug:course_slug>/", views.course_detail, name="course_detail"),
    path("learn/<slug:course_slug>/<slug:lesson_slug>/", views.lesson_detail, name="lesson_detail"),
    path("playground/", views.playground, name="playground"),
    path("games/", views.games_hub, name="games_hub"),
    path("practice/", views.games_hub, name="practice_hub"),
    path("games/<slug:game_slug>/", views.game_play, name="game_play"),
    path("about/", views.about_view, name="about_view"),
    path("login/", views.login_view, name="login_view"),
    path("signup/", views.signup_view, name="signup_view"),
    path("logout/", views.logout_view, name="logout_view"),
    path("profile/", views.profile_view, name="profile_view"),
    path("student-dashboard/", views.profile_view, name="student_dashboard"),
    path("dashboard/", admin_dashboard, name="dashboard_cms"),
    path("api/telemetry/log/", views.api_log_telemetry, name="api_log_telemetry"),
    path("api/telemetry/export.csv", views.api_export_telemetry_csv, name="api_export_telemetry_csv"),
    path("api/telemetry/export.json", views.api_export_telemetry_json, name="api_export_telemetry_json"),
    path("api/games/<slug:game_slug>/score/", views.api_log_telemetry, name="api_record_game_score"),
    path("api/lesson/<int:lesson_id>/check/", views.api_log_telemetry, name="api_check_lesson"),
]
