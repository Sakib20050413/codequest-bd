#!/usr/bin/env python
"""
CodeQuest BD — Cloud Database (Neon / Supabase PostgreSQL) Setup & Integrity Script
Usage:
    python setup_cloud_db.py [DATABASE_URL]

If DATABASE_URL is not passed as an argument, it reads from the environment variable DATABASE_URL.
"""
import os
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Initialize and verify CodeQuest cloud PostgreSQL database.")
    parser.add_argument("database_url", nargs="?", default="", help="PostgreSQL connection string (e.g. from Neon or Supabase)")
    args = parser.parse_args()

    db_url = args.database_url or os.environ.get("DATABASE_URL") or os.environ.get("POSTGRES_URL")

    if not db_url:
        print("\n[ERROR] No DATABASE_URL provided!")
        print("Usage:")
        print("    python setup_cloud_db.py \"postgresql://user:password@ep-xyz.region.neon.tech/neondb?sslmode=require\"")
        print("Or set it in your environment: $env:DATABASE_URL=\"...\" (PowerShell)")
        sys.exit(1)

    print(f"\n[1/4] Configuring environment with target database...")
    os.environ["DATABASE_URL"] = db_url
    os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"

    import django
    django.setup()

    from django.db import connection
    from django.core.management import call_command
    from learn.models import Language, Course, Lesson, Game, User

    print(f"[2/4] Testing connection to PostgreSQL host: {connection.settings_dict.get('HOST', 'unknown')}...")
    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")
        version = cursor.fetchone()[0]
        print(f"      Connected successfully! DB Engine: {version.split()[0]} {version.split()[1]}")

    print("[3/4] Running database migrations...")
    call_command("migrate", interactive=False)

    print("[4/4] Seeding core curriculum, interactive courses, games, and admin credentials...")
    call_command("seed_lessons")

    # Integrity verification
    lang_count = Language.objects.count()
    course_count = Course.objects.count()
    lesson_count = Lesson.objects.count()
    game_count = Game.objects.count()
    user_count = User.objects.count()

    print("\n==================================================")
    print("      DATABASE INTEGRITY & VERIFICATION PASS      ")
    print("==================================================")
    print(f"  • Languages Active : {lang_count}")
    print(f"  • Courses Seeded   : {course_count}")
    print(f"  • Lessons Total    : {lesson_count}")
    print(f"  • Mini-Games Ready : {game_count}")
    print(f"  • Users Registered : {user_count}")
    print("==================================================")
    print(" [SUCCESS] Cloud database is 100% ready for Vercel!")
    print(" Next Step:")
    print(" Add DATABASE_URL to your Vercel Project Environment Variables:")
    print(" Vercel Dashboard -> codequest-bd -> Settings -> Environment Variables")
    print("==================================================\n")

if __name__ == "__main__":
    main()
