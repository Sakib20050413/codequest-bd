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
            "react-core": ["JSX Components", "useState & Hooks", "Props & State", "SPA Architecture"],
            "python-core": ["Algorithmic Logic", "Comprehensions", "OOP & Dictionaries", "Data Pipelines"],
            "django-core": ["MVT Architecture", "ORM Models", "URLs & Views", "REST APIs"],
            "sql-core": ["Relational Schemas", "JOIN Algorithms", "Aggregates & Filters", "Query Tuning"],
            "mysql-core": ["InnoDB Tables", "PHP MySQLi/PDO", "Foreign Keys", "Indexed Queries"],
            "postgresql-core": ["ACID Transactions", "JSONB Indexing", "Window Functions", "Cloud Neon DB"],
            "mongodb-core": ["NoSQL Documents", "BSON Schemas", "Aggregation Pipelines", "mongosh CRUD"],
            "c-lang-stubs": ["Memory & Pointers", "Format Strings", "Structs & Arrays", "Deterministic AST"],
            "c-lang-core": ["Memory & Pointers", "Format Strings", "Structs & Arrays", "Deterministic AST"],
            "c-core": ["Memory & Pointers", "Format Strings", "Structs & Arrays", "Deterministic AST"],
            "cpp-core": ["STL Containers", "Vectors & Maps", "Fast I/O", "Competitive Coding"],
            "rust-core": ["Ownership & Borrowing", "Zero-Cost Safety", "Pattern Matching", "Cargo Systems"],
            "java-stubs": ["OOP Hierarchy", "Static Typing", "JVM Memory Model", "Exception Guard"],
            "java-core": ["OOP Hierarchy", "Static Typing", "JVM Memory Model", "Collections API"],
            "php-stubs": ["Server Request API", "CRUD Operations", "Header Routing", "Database Bridges"],
            "php-core": ["Server Request API", "MySQLi & PDO", "Session Auth", "Dynamic Web"],
            "bash-stubs": ["Linux Pipeline", "Regex & Grep", "Stream Redirection", "Shell Automation"],
            "bash-core": ["Linux Pipeline", "Regex & Grep", "Stream Redirection", "Shell Automation"],
            "ai-ml-core": ["Neural Networks", "PyTorch Tensors", "Gradient Descent", "LLM Prompts"],
        }
        return tag_map.get(self.slug, ["Core Fundamentals", "1-Min Visual Studio", "Hands-on Labs", "Verified Certificate"])


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
    tips_tricks = models.TextField(
        blank=True,
        default="",
        help_text="Pro Shortcuts, Interview Tips and Common Traps Memory Box"
    )
    full_syntax_game_slug = models.CharField(
        max_length=60,
        blank=True,
        default="",
        help_text="Slug of associated Full-Syntax Game"
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
    daily_goal_minutes = models.PositiveIntegerField(default=15)
    daily_goal_xp = models.PositiveIntegerField(default=100)
    freeze_shields = models.PositiveIntegerField(default=1)
    activity_heatmap_json = models.JSONField(default=dict, blank=True)

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


class MicroTask(models.Model):
    TASK_TYPES = [
        ("CORE_SYNTAX", "Task 1: Core Syntax Implementation (+30 XP)"),
        ("EDGE_CASE_OPT", "Task 2: Edge-Case and Optimization (+40 XP)"),
        ("MINI_BOSS", "Task 3: Mini Boss Challenge (+50 XP)"),
    ]

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="micro_tasks")
    task_number = models.PositiveSmallIntegerField(default=1)
    task_type = models.CharField(max_length=30, choices=TASK_TYPES, default="CORE_SYNTAX")
    title = models.CharField(max_length=160)
    instructions = models.TextField()
    starter_code = models.TextField(blank=True, default="")
    solution_code = models.TextField(blank=True, default="")
    xp_reward = models.PositiveIntegerField(default=30)
    test_cases_json = models.JSONField(
        default=list,
        blank=True,
        help_text="List of 3 automated test cases: Normal, Edge, Stress"
    )

    class Meta:
        ordering = ["lesson", "task_number", "id"]
        unique_together = ("lesson", "task_number")

    @property
    def description(self):
        return self.instructions

    def __str__(self):
        return f"{self.lesson.title} - Task {self.task_number}: {self.title}"


class Certificate(models.Model):
    credential_id = models.CharField(max_length=64, unique=True, db_index=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="certificates")
    student_name = models.CharField(max_length=150)
    student_id_str = models.CharField(max_length=40, default="1119003")
    track_slug = models.CharField(max_length=80, db_index=True)
    track_title = models.CharField(max_length=160)
    mastery_score = models.PositiveIntegerField(default=96)
    issued_at = models.DateTimeField(default=timezone.now)
    is_verified = models.BooleanField(default=True)
    qr_data = models.TextField(blank=True, default="")

    class Meta:
        ordering = ["-issued_at"]

    def __str__(self):
        return f"{self.credential_id} - {self.student_name} ({self.track_title})"


class Contest(models.Model):
    CATEGORY_CHOICES = [
        ("ALGO_SPRINT", "Algorithm Sprint"),
        ("SQL_MYSTERY", "SQL Detective Mystery"),
        ("UI_SHOWDOWN", "UI Layout Showdown"),
        ("GAME_SPEEDRUN", "Full-Syntax Game Speedrun"),
    ]

    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(max_length=160)
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES, default="ALGO_SPRINT")
    description = models.TextField()
    language_slug = models.CharField(max_length=40, default="python")
    duration_minutes = models.PositiveIntegerField(default=45)
    xp_reward = models.PositiveIntegerField(default=500)
    is_active = models.BooleanField(default=True)
    starts_at = models.DateTimeField(default=timezone.now)
    ends_at = models.DateTimeField()
    starter_code = models.TextField(blank=True, default="")
    solution_code = models.TextField(blank=True, default="")
    test_cases_json = models.JSONField(default=list, blank=True)

    class Meta:
        ordering = ["-is_active", "starts_at"]

    @property
    def difficulty(self):
        return f"{self.get_category_display()} • {self.language_slug.upper()}"

    @property
    def problem_statement(self):
        return self.description

    def __str__(self):
        return f"[{self.get_category_display()}] {self.title}"


class ContestSubmission(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, related_name="submissions")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="contest_submissions")
    username = models.CharField(max_length=150)
    university_batch = models.CharField(max_length=100, default="BAIUST CSE Batch 11")
    score = models.PositiveIntegerField(default=100)
    execution_time_ms = models.PositiveIntegerField(default=15)
    rank = models.PositiveIntegerField(default=1)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-score", "execution_time_ms", "submitted_at"]

    def __str__(self):
        return f"{self.username} - {self.contest.title} (Score: {self.score}, Time: {self.execution_time_ms}ms)"
