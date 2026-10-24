from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("learn.urls")),
    path("instructor-panel/", include("instructor_panel.urls")),
    path("django-admin/", admin.site.urls),
]
