from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class LanguageTrack(models.Model):
    DIFFICULTY_CHOICES = [
        ('Beginner', 'Beginner (1st/2nd Year)'),
        ('Intermediate', 'Intermediate (3rd Year Sessional)'),
        ('Advanced', 'Advanced (Competitive / Project)'),
    ]

    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True)
    description = models.TextField()
    icon = models.CharField(max_length=60, default='💻', help_text='Emoji or DevIcon CSS class')
    badge_color = models.CharField(max_length=50, default='from-blue-600 to-indigo-600')
    difficulty = models.CharField(max_length=30, choices=DIFFICULTY_CHOICES, default='Intermediate')
    order = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.title} ({self.difficulty})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def level_count(self):
        return self.levels.count()

    @property
    def total_xp(self):
        return sum(lvl.xp_reward for lvl in self.levels.all())


class ChallengeLevel(models.Model):
    ENGINE_CHOICES = [
        ('ROVER_3D', 'Mode 1: 3D Rover Odyssey (Three.js WebGL) 🚀'),
        ('ROVER_MAZE', 'Mode 1: 3D Rover Odyssey (Legacy) 🤖'),
        ('DOM_BUILDER', 'Mode 2: Visual 3D Stage & DOM Builder 🎨'),
        ('CODE_JUDGE', 'Mode 3: Multi-Language Code Judge ⚡'),
    ]

    track = models.ForeignKey(LanguageTrack, on_delete=models.CASCADE, related_name='levels')
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=160, unique=True)
    level_number = models.PositiveIntegerField(default=1)
    engine = models.CharField(max_length=30, choices=ENGINE_CHOICES, default='CODE_JUDGE')
    story_brief = models.TextField(help_text='Gamified lore / mission scenario')
    instructions_markdown = models.TextField(help_text='Task description, inputs, and requirements')
    
    # Starter templates
    starter_code_c = models.TextField(blank=True, default='')
    starter_code_cpp = models.TextField(blank=True, default='')
    starter_code_python = models.TextField(blank=True, default='')
    starter_code_javascript = models.TextField(blank=True, default='')
    starter_code_php = models.TextField(blank=True, default='')
    solution_template = models.TextField(blank=True, default='')

    # Engine configs
    maze_grid_config = models.JSONField(
        default=dict,
        blank=True,
        help_text='Grid size, start, portal, gems, laser obstacles'
    )
    dom_builder_config = models.JSONField(
        default=dict,
        blank=True,
        help_text='Target CSS rules, pads, validation target DOM'
    )
    test_cases = models.JSONField(
        default=list,
        blank=True,
        help_text='List of {"input": "...", "expected_output": "...", "is_hidden": false}'
    )
    xp_reward = models.PositiveIntegerField(default=100)
    hints = models.JSONField(default=list, blank=True)
    order = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['track', 'order', 'level_number']
        unique_together = ('track', 'level_number')

    def __str__(self):
        return f"[{self.track.title}] Lvl {self.level_number}: {self.title} ({self.engine})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.track.slug}-{self.level_number}-{self.title}")
        super().save(*args, **kwargs)


class QuizQuestion(models.Model):
    CATEGORY_CHOICES = [
        ('HTML5', 'HTML5 Semantic & Structure'),
        ('CSS3', 'CSS3 Layout & Box Model'),
        ('JAVASCRIPT_DOM', 'JavaScript & DOM Manipulation'),
        ('PHP_MYSQL', 'PHP & MySQLi CRUD'),
        ('C_CPP', 'C & C++ Pointer/Logic Output'),
        ('PYTHON', 'Python Automation & Syntax'),
    ]

    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy (+10 pts)'),
        ('Medium', 'Medium (+20 pts)'),
        ('Hard', 'Hard (+30 pts)'),
    ]

    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES, default='HTML5')
    question_text = models.TextField()
    code_snippet = models.TextField(blank=True, default='')
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=2, choices=[('A','A'), ('B','B'), ('C','C'), ('D','D')])
    explanation = models.TextField(help_text='Instant pedagogical explanation upon answer')
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='Medium')
    points = models.PositiveIntegerField(default=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.category}] {self.question_text[:50]}... ({self.correct_option})"


class StudentSubmission(models.Model):
    STATUS_CHOICES = [
        ('ACCEPTED', 'Accepted ✅'),
        ('WRONG_ANSWER', 'Wrong Answer ❌'),
        ('SYNTAX_ERROR', 'Syntax Error ⚠️'),
        ('RUNTIME_ERROR', 'Runtime Error 💥'),
        ('TIMEOUT', 'Time Limit Exceeded ⏳'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    level = models.ForeignKey(ChallengeLevel, on_delete=models.CASCADE, related_name='submissions')
    language = models.CharField(max_length=30)
    submitted_code = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='ACCEPTED')
    stdout = models.TextField(blank=True, default='')
    stderr = models.TextField(blank=True, default='')
    execution_time_ms = models.PositiveIntegerField(default=0)
    xp_earned = models.PositiveIntegerField(default=0)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.user.username} - {self.level.title} - {self.status} (+{self.xp_earned} XP)"


class LabAnnouncement(models.Model):
    BADGE_CHOICES = [
        ('CSE 324 Final', 'CSE 324 Final 🎓'),
        ('PHP Evaluation', 'PHP Evaluation 🐘'),
        ('Leaderboard Update', 'Leaderboard Update 🏆'),
        ('System Notice', 'System Notice ⚡'),
    ]

    title = models.CharField(max_length=150)
    message = models.TextField()
    badge = models.CharField(max_length=40, choices=BADGE_CHOICES, default='CSE 324 Final')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"[{self.badge}] {self.title}"
