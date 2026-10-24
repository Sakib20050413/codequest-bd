import os
import django

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    django.setup()


def seed_all():
    from django.contrib.auth.models import User
    from learn.models import (
        LanguageTrack,
        MicroLesson,
        CodingGameChallenge,
        StudentProfile,
        TelemetryAndSecurityLog,
    )
    from content.curriculum_data import LANGUAGES_16, generate_108_aaa_games

    # 1. Admin & Demo Student Accounts (Req #19, #22, #24)
    admin_user, _ = User.objects.get_or_create(
        username="sakib_admin",
        defaults={"email": "mdnajmussakib2003@gmail.com", "is_staff": True, "is_superuser": True},
    )
    admin_user.set_password("baiust1119003")
    admin_user.is_staff = True
    admin_user.is_superuser = True
    admin_user.save()
    StudentProfile.objects.get_or_create(
        user=admin_user,
        defaults={
            "role": "ADMIN",
            "xp": 9850,
            "streak_days": 42,
            "streak_freeze_shields": 5,
            "league_tier": "Grandmaster Architect",
            "solved_games_count": 108,
            "completed_lessons_count": 48,
        },
    )

    student_user, _ = User.objects.get_or_create(
        username="pro_learner",
        defaults={"email": "student@codequest.bd"},
    )
    student_user.set_password("codequest2026")
    student_user.save()
    StudentProfile.objects.get_or_create(
        user=student_user,
        defaults={
            "role": "STUDENT",
            "xp": 1450,
            "streak_days": 12,
            "streak_freeze_shields": 3,
            "league_tier": "Diamond Coder",
            "solved_games_count": 24,
            "completed_lessons_count": 16,
        },
    )

    # 2. Seed all 16 World-Class Programming Languages & Harvard CS50 Visual Lessons (Req #10, #11, #13, #15, #17, #18)
    if LanguageTrack.objects.count() < 16:
        LanguageTrack.objects.all().delete()
        for idx, item in enumerate(LANGUAGES_16, start=1):
            tr = LanguageTrack.objects.create(
                slug=item["slug"],
                name=item["name"],
                short_code=item["code"],
                category=item["cat"],
                compiler_runtime=item["runtime"],
                engine_mode=item["engine"],
                accent_hex=item["color"],
                summary=item["summary"],
                total_modules=6,
                order=idx,
            )
            MicroLesson.objects.create(
                track=tr,
                slug="core-architecture-and-3d-control",
                step_number=1,
                title=item["lesson_title"],
                duration_badge="3 Min Visual Class",
                cs50_mental_model=item["mental"],
                ai_video_narration=item["video_script"],
                cheat_sheet_rows=item["cheats"],
                starter_code=item["starter"],
                solution_code=item["solution"],
                hint_text=item["hint"],
                xp_reward=100,
            )

    # 3. Seed all 108 Playable AAA-Inspired Coding Games (Req #16)
    if CodingGameChallenge.objects.count() < 100:
        CodingGameChallenge.objects.all().delete()
        games_list = generate_108_aaa_games()
        objs = [CodingGameChallenge(**g) for g in games_list]
        CodingGameChallenge.objects.bulk_create(objs)

    # 4. Seed Telemetry & Security Audit Logs (Req #26, #27)
    if TelemetryAndSecurityLog.objects.count() == 0:
        samples = [
            ("sess-a101", "CODE_EXECUTION", "python", "Recursive Loops & Memory Frames", "TREE_3D", 38.4, 3.8, "SANDBOX_CLEAN_PASS"),
            ("sess-b202", "GAME_VICTORY", "javascript", "Game #037 — Solar Corona Ignition", "SOLAR_3D", 44.1, 4.1, "SANDBOX_CLEAN_PASS"),
            ("sess-c303", "SECURITY_AUDIT", "sql", "SQLi & XSS Boundary Verification", "SQL_HEIST", 12.0, 1.9, "ZERO_VULNERABILITIES"),
            ("sess-d404", "CODE_EXECUTION", "c-lang", "CS50 Pointers & Hardware Loops", "BOSS_BLITZ", 41.2, 3.5, "SANDBOX_CLEAN_PASS"),
        ]
        for sh, ev, lg, mod, eng, ttc, lat, sec in samples:
            TelemetryAndSecurityLog.objects.create(
                session_hash=sh, event_type=ev, language_slug=lg,
                module_title=mod, engine_mode=eng, ttc_seconds=ttc,
                latency_ms=lat, security_status=sec
            )


if __name__ == "__main__":
    seed_all()
    print("Seeded CodeQuest BD V10.0: 16 Languages, CS50 Visual Lessons, 108 Games & Student/Admin Portals!")
