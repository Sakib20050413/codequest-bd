from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Language(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    short_code = models.CharField(max_length=16, default="CODE")
    category = models.CharField(max_length=80, default="Core Foundations")
    summary = models.CharField(max_length=240)
    icon_svg = models.TextField(blank=True, default="")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class Course(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name="courses")
    title = models.CharField(max_length=160)
    slug = models.SlugField(max_length=160, unique=True)
    description = models.TextField()
    level = models.CharField(max_length=40, default="Beginner")
    order = models.PositiveIntegerField(default=0)
    xp_reward = models.PositiveIntegerField(default=200)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.language.name} — {self.title}"

    @property
    def lesson_count(self):
        return self.lessons.count()

    @property
    def total_minutes(self):
        mins = sum(l.est_minutes for l in self.lessons.all())
        return mins if mins > 0 else 30

    @property
    def estimated_time_minutes(self):
        return self.total_minutes

    @property
    def interactive_task_count(self):
        return self.lessons.count()

    @property
    def tags_list(self):
        tag_map = {
            "html-core": ["Semantic HTML5", "DOM Skeletons", "Forms & Input", "Accessible Web"],
            "css-core": ["Box Model", "Flexbox Pond", "CSS Grid", "Responsive Layouts"],
            "javascript-core": ["DOM Reactivity", "Event Listeners", "Async / Await", "ES6+ Modules"],
            "python-core": ["Algorithmic Logic", "Comprehensions", "OOP & Dictionaries", "Data Pipelines"],
            "sql-core": ["Relational Schemas", "JOIN Algorithms", "Aggregates & Filters", "Query Tuning"],
            "c-lang-stubs": ["Memory & Pointers", "Format Strings", "Structs & Arrays", "Deterministic AST"],
            "c-core": ["Memory & Pointers", "Format Strings", "Structs & Arrays", "Deterministic AST"],
            "java-stubs": ["OOP Hierarchy", "Static Typing", "JVM Memory Model", "Exception Guard"],
            "php-stubs": ["Server Request API", "CRUD Operations", "Header Routing", "Database Bridges"],
            "bash-stubs": ["Linux Pipeline", "Regex & Grep", "Stream Redirection", "Shell Automation"],
        }
        return tag_map.get(self.slug, ["Core Fundamentals", "Syntax Fluency", "Hands-on Labs", "Verified Certificate"])


class Lesson(models.Model):
    EXECUTION_TYPES = [
        ("IFRAME", "HTML/CSS/JS Live Preview (Sandboxed iframe)"),
        ("PYODIDE", "Python 3 Client-Side WASM (Pyodide)"),
        ("SQL", "SQL Browser Database (sql.js WASM)"),
        ("PREDICT", "Predict the Output (C, Java, PHP, Bash)"),
        ("QUIZ", "Fill-the-Blank & Multiple Choice"),
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    order = models.PositiveIntegerField(default=1)
    est_minutes = models.PositiveIntegerField(default=5, help_text="Bite-sized duration (3-7 min)")
    xp = models.PositiveIntegerField(default=50)
    execution_type = models.CharField(max_length=20, choices=EXECUTION_TYPES, default="IFRAME")
    
    # Lesson Content (under 150 words + diagram/mental model)
    body_md = models.TextField(help_text="Short markdown explanation (max ~150 words + diagram/example)")
    diagram_svg = models.TextField(blank=True, default="", help_text="Optional clean inline SVG diagram")
    
    # Interactive Task
    task_prompt = models.TextField(help_text="Clear single task description")
    starter_code = models.TextField(help_text="Initial code placed in editor")
    solution = models.TextField(help_text="Working solution code")
    
    # Auto-Checking & Hint Ladder (stored as JSON)
    tests_json = models.JSONField(
        default=list,
        blank=True,
        help_text="List of test checks: [{'id': 'c1', 'desc': 'Has <h1> tag', 'type': 'dom_exists', 'query': 'h1'}]"
    )
    hints_json = models.JSONField(
        default=list,
        blank=True,
        help_text="Hint ladder: ['Hint 1: Check your syntax', 'Hint 2: Use display: flex']"
    )

    class Meta:
        ordering = ["course__order", "order", "id"]
        unique_together = ("course", "slug")

    def __str__(self):
        return f"{self.course.slug} // {self.order}. {self.title}"


class Game(models.Model):
    slug = models.SlugField(max_length=60, unique=True)
    title = models.CharField(max_length=120)
    tagline = models.CharField(max_length=240)
    description = models.TextField()
    category = models.CharField(max_length=80, default="Syntax Drill")
    difficulty = models.CharField(max_length=40, default="Beginner (1-2 min)")
    icon_svg = models.TextField(blank=True, default="")
    xp_per_win = models.PositiveIntegerField(default=50)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    xp = models.PositiveIntegerField(default=0)
    streak = models.PositiveIntegerField(default=1)
    last_active = models.DateField(default=timezone.now)
    theme_pref = models.CharField(max_length=10, default="dark", choices=[("dark", "Dark"), ("light", "Light")])
    sound_enabled = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} ({self.xp} XP, {self.streak}d streak)"

    def record_activity(self):
        today = timezone.now().date()
        if self.last_active == today:
            return
        elif self.last_active == today - timezone.timedelta(days=1):
            self.streak += 1
        elif self.last_active < today - timezone.timedelta(days=1):
            self.streak = 1
        self.last_active = today
        self.save(update_fields=["streak", "last_active"])


class UserProgress(models.Model):
    STATUS_CHOICES = [
        ("NOT_STARTED", "Not Started"),
        ("IN_PROGRESS", "In Progress"),
        ("COMPLETED", "Completed"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="progress")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="user_progress")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="IN_PROGRESS")
    best_score = models.IntegerField(default=100)
    attempts = models.PositiveIntegerField(default=1)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("user", "lesson")
        ordering = ["-completed_at", "-id"]

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title} ({self.status})"


class Badge(models.Model):
    slug = models.SlugField(max_length=80, unique=True)
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    icon_svg = models.TextField(blank=True, default="")
    xp_required = models.PositiveIntegerField(default=100)
    earned_by = models.ManyToManyField(User, related_name="badges", blank=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    CATEGORY_CHOICES = [
        ("CONTENT", "Lesson Content / Typo"),
        ("BUG", "Editor / Test Bug"),
        ("SUGGESTION", "Feature Suggestion"),
        ("GENERAL", "General Praise / Thoughts"),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="feedback")
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, blank=True, related_name="feedback")
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default="CONTENT")
    message = models.TextField()
    email = models.EmailField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"[{self.category}] {self.message[:40]}"
