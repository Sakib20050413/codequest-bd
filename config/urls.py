from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from learn import views

urlpatterns = [
    # Strictly return 404 on default /admin/ to prevent brute force
    path("admin/", views.custom_admin_404, name="fake_admin_404"),
    # Hidden Admin CMS slug dynamically loaded from settings.ADMIN_URL
    path(f"{settings.ADMIN_URL}/", admin.site.urls),
    # Core Application Routes
    path("", include("learn.urls")),
]
