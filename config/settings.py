import os
import shutil
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-codequest-modern-learning-platform-key")
DEBUG = os.environ.get("DEBUG", "False" if "VERCEL" in os.environ else "True").lower() in ("true", "1", "yes")

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")
if "*" not in ALLOWED_HOSTS and "localhost" not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.extend(["localhost", "127.0.0.1", ".onrender.com", ".vercel.app"])

CSRF_TRUSTED_ORIGINS = [
    origin.strip() for origin in os.environ.get(
        "CSRF_TRUSTED_ORIGINS",
        "https://*.onrender.com,https://*.vercel.app,http://localhost:8000,http://127.0.0.1:8000"
    ).split(",") if origin.strip()
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "learn",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "learn.context_processors.global_stats",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database Configuration (Neon / Supabase PostgreSQL on Cloud or SQLite for Local Dev)
db_url = os.environ.get("DATABASE_URL") or os.environ.get("POSTGRES_URL")
if db_url:
    # On serverless (Vercel), conn_max_age=0 prevents connection leaks / dropped sockets
    conn_max_age = int(os.environ.get("CONN_MAX_AGE", "0" if "VERCEL" in os.environ else "600"))
    DATABASES = {
        "default": dj_database_url.config(
            default=db_url,
            conn_max_age=conn_max_age,
            conn_health_checks=True,
            ssl_require=True,
        )
    }
elif "VERCEL" in os.environ:
    tmp_db = Path("/tmp/db.sqlite3")
    bundled_db = BASE_DIR / "db.sqlite3"
    if not tmp_db.exists() and bundled_db.exists():
        shutil.copy2(bundled_db, tmp_db)
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": str(tmp_db),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", "OPTIONS": {"min_length": 6}},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Dhaka"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
WHITENOISE_MANIFEST_STRICT = False

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Hidden Admin slug (from env var, e.g. /hidden-core-cms/)
ADMIN_URL = os.environ.get("ADMIN_URL", "hidden-core-cms").strip("/")

LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/profile/"
LOGOUT_REDIRECT_URL = "/"

# Security Headers & Client Sandboxing
X_FRAME_OPTIONS = "SAMEORIGIN"
SECURE_CONTENT_TYPE_NOSNIFF = True

# Session & Authentication Integrity (Persistent 30-Day Login State)
SESSION_ENGINE = "django.contrib.sessions.backends.db"
SESSION_COOKIE_AGE = 60 * 60 * 24 * 30  # 30-Day persistent session
SESSION_SAVE_EVERY_REQUEST = True        # Auto-refresh session expiration on learner activity
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # Keep learner signed in across browser sessions
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_SAMESITE = "Lax"

if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
