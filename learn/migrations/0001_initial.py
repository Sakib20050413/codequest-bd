from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="LanguageTrack",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("slug", models.SlugField(max_length=60, unique=True)),
                ("name", models.CharField(max_length=100)),
                ("short_code", models.CharField(default="PY", max_length=16)),
                ("category", models.CharField(default="Systems & AI", max_length=80)),
                ("compiler_runtime", models.CharField(default="CPython 3.12 WASM + AST", max_length=100)),
                ("engine_mode", models.CharField(default="TREE_3D", max_length=40)),
                ("accent_hex", models.CharField(default="#10b981", max_length=20)),
                ("summary", models.CharField(max_length=280)),
                ("architecture_note", models.TextField(default="Executes in zero-setup browser sandbox with real-time Stack, Heap, and DOM visualization.")),
                ("total_modules", models.PositiveIntegerField(default=6)),
                ("order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["order", "id"]},
        ),
        migrations.CreateModel(
            name="CodingGameChallenge",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("game_number", models.PositiveIntegerField(default=1)),
                ("slug", models.SlugField(max_length=120, unique=True)),
                ("title", models.CharField(max_length=180)),
                ("category_name", models.CharField(default="CyberPunk 3D Rover", max_length=100)),
                ("engine_mode", models.CharField(default="ROVER_3D", max_length=30)),
                ("language_tag", models.CharField(default="Python / C / JS", max_length=40)),
                ("difficulty", models.CharField(default="Beginner", max_length=30)),
                ("duration_Label", models.CharField(default="2 Min", max_length=30)),
                ("xp_reward", models.PositiveIntegerField(default=75)),
                ("mission_brief", models.TextField()),
                ("starter_code", models.TextField()),
                ("solution_code", models.TextField()),
                ("target_keyword", models.CharField(default="for", max_length=80)),
            ],
            options={"ordering": ["game_number", "id"]},
        ),
        migrations.CreateModel(
            name="TelemetryAndSecurityLog",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("session_hash", models.CharField(default="verified-session", max_length=64)),
                ("event_type", models.CharField(default="CODE_EXECUTION", max_length=50)),
                ("language_slug", models.CharField(default="python", max_length=50)),
                ("module_title", models.CharField(default="Interactive Sandbox", max_length=180)),
                ("engine_mode", models.CharField(default="TREE_3D", max_length=40)),
                ("ttc_seconds", models.FloatField(default=39.4)),
                ("latency_ms", models.FloatField(default=4.2)),
                ("security_status", models.CharField(default="SANDBOX_CLEAN_PASS", max_length=60)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-created_at"]},
        ),
        migrations.CreateModel(
            name="MicroLesson",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("slug", models.SlugField(max_length=100)),
                ("step_number", models.PositiveIntegerField(default=1)),
                ("title", models.CharField(max_length=180)),
                ("duration_badge", models.CharField(default="3 Min Visual Class", max_length=40)),
                ("cs50_mental_model", models.TextField()),
                ("ai_video_narration", models.TextField(default="Watch how each line of code allocates a stack frame.")),
                ("stack_heap_snapshot_json", models.TextField(default="[]")),
                ("cheat_sheet_rows", models.TextField()),
                ("task_1_prompt", models.CharField(default="Task 1", max_length=260)),
                ("task_2_prompt", models.CharField(default="Task 2", max_length=260)),
                ("task_3_prompt", models.CharField(default="Task 3", max_length=260)),
                ("starter_code", models.TextField()),
                ("solution_code", models.TextField()),
                ("hint_text", models.CharField(max_length=280)),
                ("xp_reward", models.PositiveIntegerField(default=100)),
                ("track", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="lessons", to="learn.languagetrack")),
            ],
            options={"ordering": ["track__order", "step_number", "id"]},
        ),
        migrations.CreateModel(
            name="StudentProfile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("role", models.CharField(default="STUDENT", max_length=20)),
                ("xp", models.PositiveIntegerField(default=650)),
                ("streak_days", models.PositiveIntegerField(default=7)),
                ("streak_freeze_shields", models.PositiveIntegerField(default=2)),
                ("league_tier", models.CharField(default="Emerald Samurai", max_length=40)),
                ("active_track_slug", models.CharField(default="python", max_length=60)),
                ("solved_games_count", models.PositiveIntegerField(default=12)),
                ("completed_lessons_count", models.PositiveIntegerField(default=8)),
                ("personal_scratchpad", models.TextField(default="# Personal Dev Notes\n")),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("user", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name="student_profile", to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
