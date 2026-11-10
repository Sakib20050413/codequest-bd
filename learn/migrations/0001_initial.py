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
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('short_code', models.CharField(default='PY', max_length=16)),
                ('pillar', models.CharField(choices=[('FRONTEND', 'Frontend & Interactive Web'), ('BACKEND', 'Backend & Web Frameworks'), ('DATABASE', 'Databases & Data Queries'), ('SYSTEMS', 'Core Systems & OOP')], default='FRONTEND', max_length=30)),
                ('runtime_engine', models.CharField(default='Pyodide WASM / AST', max_length=60)),
                ('summary', models.CharField(max_length=260)),
                ('order', models.PositiveIntegerField(default=1)),
            ],
            options={'ordering': ['order', 'id']},
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=80, unique=True)),
                ('title', models.CharField(max_length=180)),
                ('level_badge', models.CharField(default='Beginner to Intermediate', max_length=40)),
                ('module_count_label', models.CharField(default='4 Modules • 16 Parts', max_length=40)),
                ('overview', models.TextField()),
                ('order', models.PositiveIntegerField(default=1)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='learn.language')),
            ],
            options={'ordering': ['order', 'id']},
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_number', models.PositiveIntegerField(default=1)),
                ('module_title', models.CharField(default='Module 1: Core Foundations', max_length=140)),
                ('step_number', models.PositiveIntegerField(default=1)),
                ('slug', models.SlugField(max_length=90)),
                ('title', models.CharField(max_length=180)),
                ('part1_concept', models.TextField()),
                ('syntax_anatomy_rows', models.TextField(help_text='Line | Syntax | Explanation (pipe-separated)')),
                ('tips_and_tricks', models.TextField(help_text='Practical exam & production tips')),
                ('part2_trace_explanation', models.TextField()),
                ('memory_trace_json', models.TextField(default='[]')),
                ('game_engine_key', models.CharField(default='FLEX_BRIDGE', max_length=40)),
                ('part3_game_prompt', models.TextField()),
                ('starter_code', models.TextField()),
                ('solution_code', models.TextField()),
                ('part4_judge_prompt', models.TextField()),
                ('test_cases_json', models.TextField(default='[]')),
                ('hint_text', models.CharField(default='Check the syntax table in Part 1.', max_length=280)),
                ('xp_reward', models.PositiveIntegerField(default=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='learn.course')),
            ],
            options={'ordering': ['course__order', 'module_number', 'step_number', 'id']},
        ),
        migrations.CreateModel(
            name='CodingGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=80, unique=True)),
                ('title', models.CharField(max_length=180)),
                ('engine_key', models.CharField(choices=[('FLEX_BRIDGE', 'CSS Flexbox & Grid Bridge Architect'), ('FRACTAL_TREE', 'Bio-Genesis 3D Fractal Tree & Canopy'), ('ROVER_GRID', 'Isometric Rover Algorithmic Pathfinder'), ('SQL_DETECTIVE', 'SQL Crime Scene & Relational Detective'), ('DOM_CIRCUIT', 'JavaScript DOM & React Circuit Builder'), ('PHP_VAULT', 'PHP & MySQLi Server Data-Vault CRUD')], default='FLEX_BRIDGE', max_length=40)),
                ('language_tag', models.CharField(default='HTML5 / CSS3', max_length=60)),
                ('difficulty', models.CharField(default='Easy', max_length=30)),
                ('scenario_brief', models.TextField()),
                ('real_code_requirement', models.CharField(max_length=260)),
                ('starter_code', models.TextField()),
                ('solution_code', models.TextField()),
                ('xp_reward', models.PositiveIntegerField(default=120)),
                ('order', models.PositiveIntegerField(default=1)),
            ],
            options={'ordering': ['order', 'id']},
        ),
        migrations.CreateModel(
            name='PracticeTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_id', models.CharField(default='CQ-101', max_length=20)),
                ('slug', models.SlugField(max_length=80, unique=True)),
                ('title', models.CharField(max_length=180)),
                ('language_tag', models.CharField(default='Python / C++ / JS', max_length=60)),
                ('topic_tag', models.CharField(default='Arrays & Loops', max_length=60)),
                ('difficulty', models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], default='Easy', max_length=20)),
                ('inspired_by', models.CharField(default='HackerRank / Codeforces', max_length=80)),
                ('problem_statement', models.TextField()),
                ('sample_input', models.TextField(default='5\n1 2 3 4 5')),
                ('sample_output', models.TextField(default='15')),
                ('starter_code', models.TextField()),
                ('solution_code', models.TextField()),
                ('xp_reward', models.PositiveIntegerField(default=80)),
                ('order', models.PositiveIntegerField(default=1)),
            ],
            options={'ordering': ['order', 'id']},
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(default='1119003', max_length=40)),
                ('department', models.CharField(default='CSE, BAIUST (Level 3, Term 2)', max_length=120)),
                ('xp', models.PositiveIntegerField(default=640)),
                ('streak_days', models.PositiveIntegerField(default=7)),
                ('streak_freeze_count', models.PositiveIntegerField(default=2)),
                ('rank_title', models.CharField(default='Full-Stack Problem Solver', max_length=80)),
                ('personal_notes', models.TextField(default='My Study Notes:\n1. Flexbox: display: flex; justify-content: space-between; align-items: center;\n2. SQL: SELECT name, cgpa FROM students WHERE cgpa >= 3.50 ORDER BY cgpa DESC;')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(default='Md Najmus Sakib Rahatul', max_length=120)),
                ('item_type', models.CharField(default='Course Module', max_length=40)),
                ('item_title', models.CharField(max_length=180)),
                ('language_used', models.CharField(default='Python 3', max_length=60)),
                ('submitted_code', models.TextField()),
                ('passed', models.BooleanField(default=True)),
                ('xp_earned', models.PositiveIntegerField(default=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={'ordering': ['-created_at']},
        ),
    ]
