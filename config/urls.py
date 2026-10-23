from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.views.generic.base import RedirectView
from learn import views

urlpatterns = [
    # Favicon redirect to prevent 404 noise
    path("favicon.ico", RedirectView.as_view(url="/static/img/favicon.svg", permanent=True)),
    # Strictly return 404 on default /admin/ to prevent brute force
    path("admin/", views.custom_admin_404, name="fake_admin_404"),
    # Hidden Admin CMS slug dynamically loaded from settings.ADMIN_URL
    path(f"{settings.ADMIN_URL}/", admin.site.urls),
    # Core Application Routes
    path("", include("learn.urls")),
    # Fallback static files serving for serverless environments (e.g. Vercel)
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]
