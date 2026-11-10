from django.db import models
from django.contrib.auth.models import User


class Language(models.Model):
    PILLAR_CHOICES = [
        ("FRONTEND", "Frontend & Interactive Web"),
        ("BACKEND", "Backend & Web Frameworks"),
        ("DATABASE", "Databases & Data Queries"),
        ("SYSTEMS", "Core Systems & OOP"),
    ]
    slug = models.SlugField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    short_code = models.CharField(max_length=16, default="PY")
    pillar = models.CharField(max_length=30, choices=PILLAR_CHOICES, default="FRONTEND")
    runtime_engine = models.CharField(max_length=60, default="Pyodide WASM / AST")
    summary = models.CharField(max_length=260)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.name} ({self.short_code})"


class Course(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name="courses")
    slug = models.SlugField(max_length=80, unique=True)
    title = models.CharField(max_length=180)
    level_badge = models.CharField(max_length=40, default="Beginner to Intermediate")
    module_count_label = models.CharField(max_length=40, default="4 Modules • 16 Parts")
    overview = models.TextField()
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    module_number = models.PositiveIntegerField(default=1)
    module_title = models.CharField(max_length=140, default="Module 1: Core Foundations")
    step_number = models.PositiveIntegerField(default=1)
    slug = models.SlugField(max_length=90)
    title = models.CharField(max_length=180)
    # Part 1: Deep Concept, Line-by-Line Syntax Anatomy & Tips/Tricks Box
    part1_concept = models.TextField()
    syntax_anatomy_rows = models.TextField(help_text="Line | Syntax | Explanation (pipe-separated)")
    tips_and_tricks = models.TextField(help_text="Practical exam & production tips")
    # Part 2: Interactive Memory Stack/Heap & DOM Trace
    part2_trace_explanation = models.TextField()
    memory_trace_json = models.TextField(default="[]")
    # Part 3: Full-Code Interactive Game Lab
    game_engine_key = models.CharField(max_length=40, default="FLEX_BRIDGE")
    part3_game_prompt = models.TextField()
    starter_code = models.TextField()
    solution_code = models.TextField()
    # Part 4: Module Coding Challenge & 3-Test-Case Judge
    part4_judge_prompt = models.TextField()
    test_cases_json = models.TextField(default="[]")
    hint_text = models.CharField(max_length=280, default="Check the syntax table in Part 1.")
    xp_reward = models.PositiveIntegerField(default=100)

    class Meta:
        ordering = ["course__order", "module_number", "step_number", "id"]

    def parsed_syntax_rows(self):
        rows = []
        for line in self.syntax_anatomy_rows.splitlines():
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 3:
                rows.append({"line": parts[0], "code": parts[1], "meaning": parts[2]})
        return rows

    def __str__(self):
        return f"{self.course.title} — {self.title}"


class CodingGame(models.Model):
    ENGINE_CHOICES = [
        ("FLEX_BRIDGE", "CSS Flexbox & Grid Bridge Architect"),
        ("FRACTAL_TREE", "Bio-Genesis 3D Fractal Tree & Canopy"),
        ("ROVER_GRID", "Isometric Rover Algorithmic Pathfinder"),
        ("SQL_DETECTIVE", "SQL Crime Scene & Relational Detective"),
        ("DOM_CIRCUIT", "JavaScript DOM & React Circuit Builder"),
        ("PHP_VAULT", "PHP & MySQLi Server Data-Vault CRUD"),
    ]
    slug = models.SlugField(max_length=80, unique=True)
    title = models.CharField(max_length=180)
    engine_key = models.CharField(max_length=40, choices=ENGINE_CHOICES, default="FLEX_BRIDGE")
    language_tag = models.CharField(max_length=60, default="HTML5 / CSS3")
    difficulty = models.CharField(max_length=30, default="Easy")
    scenario_brief = models.TextField()
    real_code_requirement = models.CharField(max_length=260)
    starter_code = models.TextField()
    solution_code = models.TextField()
    xp_reward = models.PositiveIntegerField(default=120)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class PracticeTask(models.Model):
    DIFF_CHOICES = [("Easy", "Easy"), ("Medium", "Medium"), ("Hard", "Hard")]
    code_id = models.CharField(max_length=20, default="CQ-101")
    slug = models.SlugField(max_length=80, unique=True)
    title = models.CharField(max_length=180)
    language_tag = models.CharField(max_length=60, default="Python / C++ / JS")
    topic_tag = models.CharField(max_length=60, default="Arrays & Loops")
    difficulty = models.CharField(max_length=20, choices=DIFF_CHOICES, default="Easy")
    inspired_by = models.CharField(max_length=80, default="HackerRank / Codeforces")
    problem_statement = models.TextField()
    sample_input = models.TextField(default="5\n1 2 3 4 5")
    sample_output = models.TextField(default="15")
    starter_code = models.TextField()
    solution_code = models.TextField()
    xp_reward = models.PositiveIntegerField(default=80)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.code_id}: {self.title}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    student_id = models.CharField(max_length=40, default="1119003")
    department = models.CharField(max_length=120, default="CSE, BAIUST (Level 3, Term 2)")
    xp = models.PositiveIntegerField(default=640)
    streak_days = models.PositiveIntegerField(default=7)
    streak_freeze_count = models.PositiveIntegerField(default=2)
    rank_title = models.CharField(max_length=80, default="Full-Stack Problem Solver")
    personal_notes = models.TextField(
        default="My Study Notes:\n1. Flexbox: display: flex; justify-content: space-between; align-items: center;\n2. SQL: SELECT name, cgpa FROM students WHERE cgpa >= 3.50 ORDER BY cgpa DESC;"
    )

    def __str__(self):
        return f"{self.user.username} ({self.xp} XP)"


class Submission(models.Model):
    student_name = models.CharField(max_length=120, default="Md Najmus Sakib Rahatul")
    item_type = models.CharField(max_length=40, default="Course Module")
    item_title = models.CharField(max_length=180)
    language_used = models.CharField(max_length=60, default="Python 3")
    submitted_code = models.TextField()
    passed = models.BooleanField(default=True)
    xp_earned = models.PositiveIntegerField(default=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.student_name} - {self.item_title}"
