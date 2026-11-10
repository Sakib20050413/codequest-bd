import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()
app = application  # Required for @vercel/python serverless runtime


def init_cloud_db_if_needed():
    """
    Self-healing Cloud Database Initializer.
    When DATABASE_URL or POSTGRES_URL is configured (e.g. Neon or Supabase)
    and the database is fresh, this automatically runs migrations and seeds lessons.
    Subsequent cold boots detect existing tables and return in <5ms.
    """
    db_url = os.environ.get("DATABASE_URL") or os.environ.get("POSTGRES_URL")
    if not db_url:
        return
    try:
        from django.db import connection
        from django.core.management import call_command
        tables = connection.introspection.table_names()
        if "learn_lesson" not in tables:
            print("[CodeQuest Vercel] Empty PostgreSQL database detected. Running migrations and seed data...")
            call_command("migrate", interactive=False)
            call_command("seed_lessons")
            print("[CodeQuest Vercel] PostgreSQL initialization complete.")
    except Exception as e:
        print(f"[CodeQuest Vercel DB Init] Notice: {e}")


# Run initial check once on worker launch
init_cloud_db_if_needed()
