from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("courses/", views.catalogue, name="catalogue"),
    path("catalogue/", views.catalogue, name="catalogue_alias"),
    path("courses/<slug:course_slug>/", views.course_detail, name="course_detail"),
    path("learn/<slug:course_slug>/<slug:lesson_slug>/", views.lesson_detail, name="lesson_detail"),
    path("playground/", views.playground, name="playground"),
    
    # Interactive Games & Practice Hub (11 Full-Syntax + 108 Drills)
    path("games/", views.games_hub, name="games_hub"),
    path("practice/", views.games_hub, name="practice"),
    path("games/<slug:game_slug>/", views.game_play, name="game_play"),
    path("api/games/<slug:game_slug>/score/", views.api_record_game_score, name="api_record_game_score"),

    # Weekly Coding Competitions & Leaderboards
    path("contests/", views.contests_view, name="contests_hub"),
    path("contests/all/", views.contests_view, name="contests_view"),
    path("contests/<slug:contest_slug>/", views.contest_detail_view, name="contest_detail"),
    path("contests/<slug:contest_slug>/detail/", views.contest_detail_view, name="contest_detail_view"),
    path("api/contests/<slug:contest_slug>/submit/", views.api_submit_contest, name="api_submit_contest"),

    # Verifiable Certificate Engine
    path("certificates/", views.certificates_hub_view, name="certificates_hub"),
    path("certificates/all/", views.certificates_hub_view, name="certificates_hub_view"),
    path("verify/<str:credential_id>/", views.verify_certificate_view, name="verify_certificate_view"),
    path("verify/<str:credential_id>/cert/", views.verify_certificate_view, name="verify_cert"),
    path("api/certificates/claim/", views.api_claim_certificate, name="api_claim_certificate"),

    # Instructor & Admin CRUD Panel
    path("admin-panel/", views.admin_panel_view, name="admin_panel"),
    path("admin-panel/dashboard/", views.admin_panel_view, name="admin_panel_view"),
    path("api/admin-panel/stats/", views.api_admin_stats, name="api_admin_stats"),

    # Micro-Tasks & Daily Goals APIs
    path("api/micro-task/check/", views.api_check_micro_task, name="api_check_micro_task"),
    path("api/profile/daily-goal/", views.api_update_daily_goal, name="api_update_daily_goal"),

    # Auto-Checking & Guest Progress Sync
    path("api/lesson/<int:lesson_id>/check/", views.api_check_lesson, name="api_check_lesson"),
    path("api/progress/sync/", views.api_sync_guest_progress, name="api_sync_guest_progress"),
    path("api/feedback/", views.submit_feedback, name="submit_feedback"),
    path("api/cloud-db-status/", views.api_cloud_db_status, name="api_cloud_db_status"),

    # Authentication & User Profile
    path("profile/", views.profile_view, name="profile_view"),
    path("about/", views.about_view, name="about_view"),
    path("login/", views.login_view, name="login_view"),
    path("signup/", views.signup_view, name="signup_view"),
    path("logout/", views.logout_view, name="logout_view"),
]
