from django.db import models
from django.contrib.auth.models import User


class LanguageTrack(models.Model):
    slug = models.SlugField(max_length=60, unique=True)
    name = models.CharField(max_length=100)
    short_code = models.CharField(max_length=16, default="PY")
    category = models.CharField(max_length=80, default="Systems & AI")
    compiler_runtime = models.CharField(max_length=100, default="CPython 3.12 WASM + AST")
    engine_mode = models.CharField(max_length=40, default="TREE_3D")
    accent_hex = models.CharField(max_length=20, default="#10b981")
    summary = models.CharField(max_length=280)
    architecture_note = models.TextField(default="Executes in zero-setup browser sandbox with real-time Stack, Heap, and DOM visualization.")
    total_modules = models.PositiveIntegerField(default=6)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.name} ({self.short_code})"


class MicroLesson(models.Model):
    track = models.ForeignKey(LanguageTrack, on_delete=models.CASCADE, related_name="lessons")
    slug = models.SlugField(max_length=100)
    step_number = models.PositiveIntegerField(default=1)
    title = models.CharField(max_length=180)
    duration_badge = models.CharField(max_length=40, default="3 Min Visual Class")
    cs50_mental_model = models.TextField()
    ai_video_narration = models.TextField(
        default="Watch how each line of code allocates a stack frame, updates heap pointers, and mutates the live 3D/DOM scene in real time."
    )
    stack_heap_snapshot_json = models.TextField(
        default='[{"frame":"main()","var":"depth","val":"6","addr":"0x7ffee1"},{"frame":"heap","var":"TreeNodes","val":"64 branches","addr":"0x104a00"}]'
    )
    cheat_sheet_rows = models.TextField()
    task_1_prompt = models.CharField(max_length=260, default="Task 1: Run the starter code to observe the Stack/Heap & 3D scene.")
    task_2_prompt = models.CharField(max_length=260, default="Task 2: Modify the loop count or parameter to expand the structure.")
    task_3_prompt = models.CharField(max_length=260, default="Task 3: Complete the full verification challenge to claim +100 XP.")
    starter_code = models.TextField()
    solution_code = models.TextField()
    hint_text = models.CharField(max_length=280)
    xp_reward = models.PositiveIntegerField(default=100)

    class Meta:
        ordering = ["track__order", "step_number", "id"]

    def parsed_cheats(self):
        rows = []
        for line in self.cheat_sheet_rows.splitlines():
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 3:
                rows.append({"syntax": parts[0], "meaning": parts[1], "example": parts[2]})
        return rows

    def __str__(self):
        return f"{self.track.short_code} - {self.title}"


class CodingGameChallenge(models.Model):
    GAME_ENGINE_CHOICES = [
        ("ROVER_3D", "CyberPunk 3D Rover & Drone Odyssey"),
        ("TREE_3D", "Bio-Genesis 3D Fractal Forest"),
        ("SOLAR_3D", "Starfield 3D Orbital Gravity Fleet"),
        ("DOM_TOWER", "Flexbox & Grid 3D Hologram Defense"),
        ("SQL_HEIST", "WatchDogs SQL & PHP Vault Heist"),
        ("BOSS_BLITZ", "Boss-Battle 60s Bug-Hunter & Memory Arena"),
    ]
    game_number = models.PositiveIntegerField(default=1)
    slug = models.SlugField(max_length=120, unique=True)
    title = models.CharField(max_length=180)
    category_name = models.CharField(max_length=100, default="CyberPunk 3D Rover")
    engine_mode = models.CharField(max_length=30, choices=GAME_ENGINE_CHOICES, default="ROVER_3D")
    language_tag = models.CharField(max_length=40, default="Python / C / JS")
    difficulty = models.CharField(max_length=30, default="Beginner")
    duration_Label = models.CharField(max_length=30, default="2 Min")
    xp_reward = models.PositiveIntegerField(default=75)
    mission_brief = models.TextField()
    starter_code = models.TextField()
    solution_code = models.TextField()
    target_keyword = models.CharField(max_length=80, default="for")

    class Meta:
        ordering = ["game_number", "id"]

    def __str__(self):
        return f"Game #{self.game_number:03d}: {self.title}"


class StudentProfile(models.Model):
    ROLE_CHOICES = [
        ("STUDENT", "Pro Learner / Student"),
        ("ADMIN", "Platform Architect / Instructor Admin"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="STUDENT")
    xp = models.PositiveIntegerField(default=650)
    streak_days = models.PositiveIntegerField(default=7)
    streak_freeze_shields = models.PositiveIntegerField(default=2)
    league_tier = models.CharField(max_length=40, default="Emerald Samurai")
    active_track_slug = models.CharField(max_length=60, default="python")
    solved_games_count = models.PositiveIntegerField(default=12)
    completed_lessons_count = models.PositiveIntegerField(default=8)
    personal_scratchpad = models.TextField(
        default="# Personal Dev Notes & Algorithm Scratchpad\n# Saved automatically to your Student Dashboard\n"
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} ({self.role} - {self.xp} XP)"


class TelemetryAndSecurityLog(models.Model):
    session_hash = models.CharField(max_length=64, default="verified-session")
    event_type = models.CharField(max_length=50, default="CODE_EXECUTION")
    language_slug = models.CharField(max_length=50, default="python")
    module_title = models.CharField(max_length=180, default="Interactive Sandbox")
    engine_mode = models.CharField(max_length=40, default="TREE_3D")
    ttc_seconds = models.FloatField(default=39.4)
    latency_ms = models.FloatField(default=4.2)
    security_status = models.CharField(max_length=60, default="SANDBOX_CLEAN_PASS")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
