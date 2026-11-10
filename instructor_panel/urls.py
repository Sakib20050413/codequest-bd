from django.urls import path
from . import views

app_name = 'instructor_panel'

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('tracks/', views.tracks_crud_view, name='tracks'),
    path('levels/', views.levels_crud_view, name='levels'),
    path('quizzes/', views.quizzes_crud_view, name='quizzes'),
    path('submissions/', views.submissions_crud_view, name='submissions'),
    path('students/', views.students_crud_view, name='students'),
    path('announcements/', views.announcements_crud_view, name='announcements'),
]
