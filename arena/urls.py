from django.urls import path
from . import views

app_name = 'arena'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('tracks/', views.tracks_view, name='tracks'),
    path('tracks/<slug:slug>/', views.track_detail_view, name='track_detail'),
    path('play/<slug:slug>/', views.level_play_view, name='level_play'),
    path('blitz/', views.blitz_view, name='blitz'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
    path('proposal/', views.proposal_view, name='proposal'),

    # AJAX APIs
    path('api/run-code/', views.run_code_api, name='api_run_code'),
    path('api/submit-level/', views.submit_level_api, name='api_submit_level'),
    path('api/submit-blitz/', views.blitz_submit_api, name='api_submit_blitz'),
]
