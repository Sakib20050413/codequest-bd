from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class StudentProfile(models.Model):
    AVATAR_CHOICES = [
        ('cyber_rover', 'Cyber Rover 🤖'),
        ('code_wizard', 'Code Wizard 🧙'),
        ('syntax_ninja', 'Syntax Ninja 🥷'),
        ('dom_knight', 'DOM Knight ⚔️'),
        ('scholar', 'BAIUST Scholar 🎓'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    student_id = models.CharField(max_length=20, default='1119003')
    batch_section = models.CharField(max_length=50, default='CSE 3-2 Section A')
    university = models.CharField(max_length=100, default='BAIUST, Cumilla')
    xp = models.PositiveIntegerField(default=0)
    level = models.PositiveIntegerField(default=1)
    streak = models.PositiveIntegerField(default=1)
    avatar = models.CharField(max_length=50, choices=AVATAR_CHOICES, default='cyber_rover')
    badges = models.JSONField(default=list, blank=True)
    preferred_track = models.CharField(max_length=50, blank=True, default='c-programming')
    solved_levels = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} ({self.student_id}) - {self.xp} XP"

    @property
    def rank_name(self):
        if self.xp >= 1500:
            return "Level 5: BAIUST Grandmaster 👑"
        elif self.xp >= 1000:
            return "Level 4: Full-Stack Samurai 🥷"
        elif self.xp >= 600:
            return "Level 3: Logic Knight ⚔️"
        elif self.xp >= 250:
            return "Level 2: DOM Explorer 🚀"
        else:
            return "Level 1: Syntax Rookie 🛡️"

    @property
    def rank_badge_color(self):
        if self.xp >= 1500:
            return "bg-amber-500 text-amber-950 border-amber-300"
        elif self.xp >= 1000:
            return "bg-purple-500 text-white border-purple-300"
        elif self.xp >= 600:
            return "bg-blue-500 text-white border-blue-300"
        elif self.xp >= 250:
            return "bg-emerald-500 text-white border-emerald-300"
        else:
            return "bg-slate-600 text-slate-100 border-slate-500"

    @property
    def next_level_xp(self):
        if self.xp < 250:
            return 250
        elif self.xp < 600:
            return 600
        elif self.xp < 1000:
            return 1000
        elif self.xp < 1500:
            return 1500
        else:
            return 2500

    @property
    def xp_progress_percent(self):
        milestones = [0, 250, 600, 1000, 1500, 2500]
        cur = self.xp
        if cur >= 2500:
            return 100
        for i in range(len(milestones) - 1):
            low = milestones[i]
            high = milestones[i + 1]
            if low <= cur < high:
                pct = int(((cur - low) / (high - low)) * 100)
                return max(5, min(100, pct))
        return 100

    def add_xp(self, amount, level_slug=None):
        self.xp += amount
        if level_slug and level_slug not in self.solved_levels:
            self.solved_levels.append(level_slug)
        
        # Check badge rewards
        badges = list(self.badges)
        if len(self.solved_levels) >= 1 and "First Blood (1st Solve)" not in badges:
            badges.append("First Blood (1st Solve)")
        if len(self.solved_levels) >= 5 and "Pentakill Coder" not in badges:
            badges.append("Pentakill Coder")
        if self.xp >= 1000 and "Century Pioneer (1000+ XP)" not in badges:
            badges.append("Century Pioneer (1000+ XP)")
        self.badges = badges

        # Update Level
        if self.xp >= 1500:
            self.level = 5
        elif self.xp >= 1000:
            self.level = 4
        elif self.xp >= 600:
            self.level = 3
        elif self.xp >= 250:
            self.level = 2
        else:
            self.level = 1

        self.save()


@receiver(post_save, sender=User)
def create_or_update_student_profile(sender, instance, created, **kwargs):
    if created:
        StudentProfile.objects.create(
            user=instance,
            student_id=getattr(instance, '_student_id', '1119003'),
            batch_section=getattr(instance, '_batch_section', 'CSE 3-2 Section A'),
            university='BAIUST, Cumilla'
        )
    else:
        if hasattr(instance, 'profile'):
            instance.profile.save()
