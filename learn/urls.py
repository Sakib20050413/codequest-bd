from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("courses/", views.catalogue, name="catalogue"),
    path("courses/<slug:course_slug>/", views.course_detail, name="course_detail"),
    path("learn/<slug:course_slug>/<slug:lesson_slug>/", views.lesson_detail, name="lesson_detail"),
    path("playground/", views.playground, name="playground"),
    
    # 5 Interactive Mini-Games / Practice Challenges
    path("games/", views.games_hub, name="games_hub"),
    path("practice/", views.games_hub, name="practice"),
    path("games/<slug:game_slug>/", views.game_play, name="game_play"),
    path("api/games/<slug:game_slug>/score/", views.api_record_game_score, name="api_record_game_score"),

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
