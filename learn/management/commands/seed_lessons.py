import os
import sys
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from learn.models import Language, Course, Lesson, Game, Badge, UserProfile
from content.curriculum_data import LANGUAGES, GAMES, BADGES
from content.seed_lessons_builder import (
    get_html_lessons,
    get_css_lessons,
    get_js_lessons,
    get_python_lessons,
    get_sql_lessons,
    get_c_lessons,
)


class Command(BaseCommand):
    help = "Seeds all CodeQuest languages, courses, bite-sized lessons, games, and badges."

    def handle(self, *args, **options):
        # 1. Superuser
        if not User.objects.filter(username="sakib_admin").exists():
            admin_user = User.objects.create_superuser(
                "sakib_admin", "mdnajmussakib2003@gmail.com", "baiust1119003"
            )
            profile, _ = UserProfile.objects.get_or_create(user=admin_user)
            profile.xp = 350
            profile.streak = 5
            profile.save()
            self.stdout.write("Created superuser: sakib_admin")

        # 2. Games
        for g_data in GAMES:
            Game.objects.update_or_create(
                slug=g_data["slug"],
                defaults={
                    "title": g_data["title"],
                    "tagline": g_data["tagline"],
                    "description": g_data["description"],
                    "category": g_data["category"],
                    "difficulty": g_data["difficulty"],
                    "icon_svg": g_data["icon"],
                    "xp_per_win": g_data["xp_per_win"],
                    "order": g_data["order"],
                },
            )

        # 3. Badges
        for b_data in BADGES:
            Badge.objects.update_or_create(
                slug=b_data["slug"],
                defaults={
                    "name": b_data["name"],
                    "description": b_data["desc"],
                    "xp_required": b_data["xp"],
                },
            )

        # 4. Languages & Courses
        lesson_generators = {
            "html": ("HTML5 Foundations", get_html_lessons()),
            "css": ("CSS3 Styling & Layouts", get_css_lessons()),
            "javascript": ("JavaScript ES6+ & DOM", get_js_lessons()),
            "python": ("Python 3 Algorithmic Core", get_python_lessons()),
            "sql": ("SQL Relational Queries", get_sql_lessons()),
            "c-lang": ("C Programming Architecture & Pointers", get_c_lessons()),
        }

        course_descriptions = {
            "html": "Build the structural backbone of the modern web. Master semantic tags, SEO-friendly document hierarchy, accessible forms, and living DOM trees.",
            "css": "Transform raw markup into pixel-perfect interfaces. Master the Box Model, fluid responsive layouts, Flexbox alignment, and multi-track CSS Grid.",
            "javascript": "Bring web pages to life with interactive logic. Master DOM manipulation, event listeners, asynchronous Promises, and modern ES6+ features.",
            "python": "Write clean, readable code for automation and data. Master fundamental control flow, list comprehensions, dictionary pipelines, and algorithmic logic.",
            "sql": "Harness the power of relational data. Master fast SELECT queries, multi-table JOINs, filtering conditions, aggregate metrics, and schema design.",
            "c-lang": "Understand how computers truly execute code under the hood. Master manual memory management, pointer arithmetic, struct memory layouts, and stack vs heap.",
        }

        for lang_spec in LANGUAGES:
            lang, _ = Language.objects.update_or_create(
                slug=lang_spec["slug"],
                defaults={
                    "name": lang_spec["name"],
                    "short_code": lang_spec["code"],
                    "category": lang_spec["category"],
                    "summary": lang_spec["summary"],
                    "icon_svg": lang_spec["icon"],
                    "order": lang_spec["order"],
                    "is_active": True,
                },
            )

            # Check if this language has full tracks or stubs
            if lang.slug in lesson_generators:
                course_title, lessons = lesson_generators[lang.slug]
                course_desc = course_descriptions.get(
                    lang.slug,
                    f"Master foundational concepts and hands-on coding skills in {lang.name} through interactive browser lessons."
                )
                course, _ = Course.objects.update_or_create(
                    slug=f"{lang.slug}-core",
                    defaults={
                        "language": lang,
                        "title": course_title,
                        "description": course_desc,
                        "level": "Beginner",
                        "order": 1,
                        "xp_reward": 250,
                    },
                )
                for l_data in lessons:
                    Lesson.objects.update_or_create(
                        course=course,
                        slug=l_data["slug"],
                        defaults={
                            "title": l_data["title"],
                            "order": l_data["order"],
                            "est_minutes": l_data["minutes"],
                            "xp": l_data["xp"],
                            "execution_type": l_data["type"],
                            "body_md": l_data["body"],
                            "task_prompt": l_data["task"],
                            "starter_code": l_data["starter"],
                            "solution": l_data["solution"],
                            "tests_json": l_data["tests"],
                            "hints_json": l_data["hints"],
                        },
                    )
            else:
                # Predictive / Stubs for C, Java, PHP, Bash
                stub_title = f"{lang.name} Read & Predict Stubs"
                course, _ = Course.objects.update_or_create(
                    slug=f"{lang.slug}-stubs",
                    defaults={
                        "language": lang,
                        "title": stub_title,
                        "description": f"Read and predict {lang.name} program output without complex server execution.",
                        "level": "Beginner",
                        "order": 1,
                        "xp_reward": 150,
                    },
                )
                Lesson.objects.update_or_create(
                    course=course,
                    slug=f"{lang.slug}-intro",
                    defaults={
                        "title": f"01. Introduction to {lang.name} Syntax",
                        "order": 1,
                        "est_minutes": 4,
                        "xp": 40,
                        "execution_type": "PREDICT",
                        "body_md": f"{lang.name} foundational concepts. Read the code and predict what executes.",
                        "task_prompt": f"Inspect the {lang.name} snippet and select the expected output.",
                        "starter_code": f"// {lang.name} Output Predictor\nprint('Output OK');",
                        "solution": "Output OK",
                        "tests_json": [{"id": "p1", "desc": "Predicts output correctly", "type": "exact_match", "val": "Output OK"}],
                        "hints_json": ["Look at the string passed to the output statement."],
                    },
                )

        self.stdout.write(self.style.SUCCESS("Successfully seeded CodeQuest curriculum, games, and badges!"))
