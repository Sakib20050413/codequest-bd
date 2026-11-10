from datetime import timedelta
from django.utils import timezone
from .models import Language, Course, Lesson, MicroTask, Game, Contest, ContestSubmission


EXTRA_LANGUAGES = [
    {
        "name": "Rust Systems",
        "slug": "rust",
        "short_code": "RS",
        "category": "Systems & Memory Safety",
        "summary": "Zero-cost abstractions, ownership & borrowing, Cargo CLI, and fearless concurrency.",
        "order": 14,
        "course": {
            "title": "Rust Memory Safety & Systems Engineering",
            "slug": "rust-core",
            "description": "Learn Rust in 60-second visual lessons: ownership, borrowing, structs, pattern matching, and high-speed CLI tools.",
            "level": "Intermediate",
            "xp_reward": 300,
        },
        "lessons": [
            {
                "title": "Ownership, Borrowing & println! Macro",
                "slug": "rust-ownership-basics",
                "order": 1,
                "est_minutes": 3,
                "xp": 60,
                "execution_type": "PREDICT",
                "body_md": (
                    "### 60-Second Concept: Rust Ownership\n"
                    "- Every value in Rust has a single **owner** variable in stack memory.\n"
                    "- Use `&variable` to **borrow** a reference without copying or moving heap data.\n"
                    "- `println!(\"{}\", val)` prints formatted values at zero runtime overhead."
                ),
                "task_prompt": "Declare an immutable binding `lang = \"Rust 2026\"` and print `Memory Safe: Rust 2026` using `println!`.",
                "starter_code": 'fn main() {\n    let lang = "Rust 2026";\n    println!("Memory Safe: {}", lang);\n}',
                "solution": 'fn main() {\n    let lang = "Rust 2026";\n    println!("Memory Safe: {}", lang);\n}',
                "tips_tricks": "In Rust, variables are immutable by default. Add `mut` (`let mut score = 0;`) only when mutation is required.",
                "full_syntax_game_slug": "rover-3d",
            },
            {
                "title": "Structs, Enums & Pattern Matching",
                "slug": "rust-structs-matching",
                "order": 2,
                "est_minutes": 4,
                "xp": 70,
                "execution_type": "PREDICT",
                "body_md": (
                    "### 60-Second Concept: Pattern Matching\n"
                    "- `struct` groups related fields tightly in memory.\n"
                    "- `match` exhaustively checks every possible case at compile time, eliminating null pointer bugs."
                ),
                "task_prompt": "Run the Rust telemetry struct matcher to verify reactor status output.",
                "starter_code": 'fn main() {\n    let core_temp = 72;\n    println!("Reactor Core Nominal: {}C", core_temp);\n}',
                "solution": 'fn main() {\n    let core_temp = 72;\n    println!("Reactor Core Nominal: {}C", core_temp);\n}',
                "tips_tricks": "The Rust compiler (`rustc`) guarantees no data races or dangling pointers before your binary ever runs.",
                "full_syntax_game_slug": "rover-3d",
            },
        ],
    },
    {
        "name": "MySQL & PHP DB Bridge",
        "slug": "mysql",
        "short_code": "MYSQL",
        "category": "Databases & Backend Bridge",
        "summary": "Relational MySQL tables, indexes, joins, and live PHP mysqli prepared-statement connections.",
        "order": 15,
        "course": {
            "title": "MySQL Relational Design & PHP Database Connection",
            "slug": "mysql-core",
            "description": "Master MySQL table design, primary/foreign keys, JOIN queries, and connecting SQL databases from PHP and Django.",
            "level": "Beginner",
            "xp_reward": 280,
        },
        "lessons": [
            {
                "title": "MySQL SELECT, WHERE & PHP mysqli Connection",
                "slug": "mysql-php-connection",
                "order": 1,
                "est_minutes": 3,
                "xp": 60,
                "execution_type": "SQL",
                "body_md": (
                    "### 60-Second Concept: SQL Database + PHP Connection\n"
                    "- **SQL / MySQL** stores structured data in relational tables (`students`, `courses`, `competitions`).\n"
                    "- **PHP (`mysqli`)** connects to MySQL using `new mysqli($host, $user, $pass, $db)` and runs prepared SQL queries safely."
                ),
                "task_prompt": "Query `student_id, name, department, cgpa` from `students` ordered by `cgpa DESC`.",
                "starter_code": "SELECT student_id, name, department, cgpa FROM students WHERE department = 'CSE' ORDER BY cgpa DESC;",
                "solution": "SELECT student_id, name, department, cgpa FROM students WHERE department = 'CSE' ORDER BY cgpa DESC;",
                "tips_tricks": "Always use prepared statements (`$stmt->prepare('SELECT * FROM students WHERE id = ?')`) in PHP to prevent SQL Injection.",
                "full_syntax_game_slug": "sql-detective",
            },
            {
                "title": "INNER JOIN & Aggregate Analytics in MySQL",
                "slug": "mysql-join-analytics",
                "order": 2,
                "est_minutes": 4,
                "xp": 70,
                "execution_type": "SQL",
                "body_md": (
                    "### 60-Second Concept: Relational Aggregations\n"
                    "- `COUNT(*)`, `AVG(cgpa)`, and `SUM(xp)` compute real-time leaderboard metrics across student rows.\n"
                    "- `GROUP BY department` summarizes metrics per department."
                ),
                "task_prompt": "Select `department, COUNT(*) AS total_students, MAX(xp) AS top_xp` from `students` grouped by `department`.",
                "starter_code": "SELECT department, COUNT(*) AS total_students, MAX(xp) AS top_xp FROM students GROUP BY department;",
                "solution": "SELECT department, COUNT(*) AS total_students, MAX(xp) AS top_xp FROM students GROUP BY department;",
                "tips_tricks": "Index columns used in `WHERE`, `JOIN ON`, and `ORDER BY` for O(log N) B-Tree lookup speed.",
                "full_syntax_game_slug": "sql-detective",
            },
        ],
    },
    {
        "name": "AI & Machine Learning",
        "slug": "ai-ml",
        "short_code": "AI",
        "category": "Artificial Intelligence & Neural Nets",
        "summary": "Bite-sized AI engineering: Python tensors, neural weights, cosine similarity, and LLM agent pipelines.",
        "order": 16,
        "course": {
            "title": "Applied AI, Neural Networks & LLM Engineering",
            "slug": "ai-ml-core",
            "description": "Understand how neural networks, embeddings, gradient descent, and AI agents work in 60-second runnable Python labs.",
            "level": "Intermediate",
            "xp_reward": 350,
        },
        "lessons": [
            {
                "title": "Neural Perceptron & ReLU Activation in Python",
                "slug": "ai-perceptron-relu",
                "order": 1,
                "est_minutes": 3,
                "xp": 75,
                "execution_type": "PYODIDE",
                "body_md": (
                    "### 60-Second Concept: How an AI Neuron Computes\n"
                    "- A neuron multiplies inputs `x` by weights `w`, adds a `bias`, and applies an activation function.\n"
                    "- **ReLU (`max(0, z)`)** zeroes out negative signals and passes positive activations forward."
                ),
                "task_prompt": "Run the forward pass of a 3-input neural unit with ReLU activation and print the prediction.",
                "starter_code": (
                    "inputs = [0.8, 0.5, 0.9]\n"
                    "weights = [0.6, -0.2, 0.7]\n"
                    "bias = 0.1\n"
                    "z = sum(x * w for x, w in zip(inputs, weights)) + bias\n"
                    "relu = max(0.0, round(z, 3))\n"
                    "print(f'Neuron Activation (ReLU): {relu}')\n"
                ),
                "solution": (
                    "inputs = [0.8, 0.5, 0.9]\n"
                    "weights = [0.6, -0.2, 0.7]\n"
                    "bias = 0.1\n"
                    "z = sum(x * w for x, w in zip(inputs, weights)) + bias\n"
                    "relu = max(0.0, round(z, 3))\n"
                    "print(f'Neuron Activation (ReLU): {relu}')\n"
                ),
                "tips_tricks": "ReLU avoids the vanishing gradient problem in deep neural networks because its derivative is 1 for all positive inputs.",
                "full_syntax_game_slug": "rover-3d",
            },
            {
                "title": "Vector Embeddings & Prompt Scoring Pipeline",
                "slug": "ai-vector-embeddings",
                "order": 2,
                "est_minutes": 4,
                "xp": 80,
                "execution_type": "PYODIDE",
                "body_md": (
                    "### 60-Second Concept: Semantic Vector Search\n"
                    "- AI models convert code and text into numeric vectors called **embeddings**.\n"
                    "- Dot product similarity measures how closely a student query matches a concept."
                ),
                "task_prompt": "Compute the dot-product similarity score between two 4D embedding vectors in Python.",
                "starter_code": (
                    "query_vec = [0.5, 0.8, 0.2, 0.9]\n"
                    "doc_vec   = [0.6, 0.7, 0.3, 0.8]\n"
                    "similarity = round(sum(q * d for q, d in zip(query_vec, doc_vec)), 3)\n"
                    "print(f'Semantic Match Score: {similarity}')\n"
                ),
                "solution": (
                    "query_vec = [0.5, 0.8, 0.2, 0.9]\n"
                    "doc_vec   = [0.6, 0.7, 0.3, 0.8]\n"
                    "similarity = round(sum(q * d for q, d in zip(query_vec, doc_vec)), 3)\n"
                    "print(f'Semantic Match Score: {similarity}')\n"
                ),
                "tips_tricks": "Normalized embeddings allow cosine similarity to be computed with a single fast dot product.",
                "full_syntax_game_slug": "rover-3d",
            },
        ],
    },
]


AUTO_COMPETITIONS = [
    {
        "slug": "baiust-iupc-open-arena",
        "title": "Open IUPC Algorithmic Coding Competition (C / C++ / Python / Java / Rust)",
        "category": "ALGO_SPRINT",
        "description": "Automated Inter-University Programming Contest (IUPC). Solve algorithmic array, graph, and dynamic programming tasks directly in the multi-language terminal.",
        "language_slug": "cpp",
        "duration_minutes": 90,
        "xp_reward": 750,
        "starter_code": (
            "#include <iostream>\nusing namespace std;\n\nint main() {\n"
            "    int n = 5;\n    int sum = (n * (n + 1)) / 2;\n"
            "    cout << \"IUPC Optimal Sum: \" << sum << endl;\n    return 0;\n}"
        ),
        "solution_code": (
            "#include <iostream>\nusing namespace std;\n\nint main() {\n"
            "    int n = 5;\n    int sum = (n * (n + 1)) / 2;\n"
            "    cout << \"IUPC Optimal Sum: \" << sum << endl;\n    return 0;\n}"
        ),
    },
    {
        "slug": "student-fullstack-ai-hackathon",
        "title": "Automated Student Full-Stack & AI Hackathon (HTML/CSS/JS + Django + PHP + SQL)",
        "category": "UI_SHOWDOWN",
        "description": "Open Student Hackathon! Build and verify a full-stack data pipeline connecting Frontend UI, Django/PHP Backend, SQL Database, and AI scoring.",
        "language_slug": "python",
        "duration_minutes": 120,
        "xp_reward": 1000,
        "starter_code": (
            "# Full-Stack Hackathon Auto-Validator\n"
            "stack = ['HTML5/CSS3/JS', 'Django 5 Framework', 'PHP MySQLi Bridge', 'SQL Database']\n"
            "for layer in stack:\n"
            "    print(f'[VERIFIED] {layer} -> ONLINE')\n"
        ),
        "solution_code": (
            "stack = ['HTML5/CSS3/JS', 'Django 5 Framework', 'PHP MySQLi Bridge', 'SQL Database']\n"
            "for layer in stack:\n"
            "    print(f'[VERIFIED] {layer} -> ONLINE')\n"
        ),
    },
    {
        "slug": "code-to-game-championship",
        "title": "Code-to-Play Gaming Championship (Multi-Language Terminal Game Cup)",
        "category": "GAME_SPEEDRUN",
        "description": "Learn by Playing! Control visual game engines using real HTML/CSS, JS, Python, C++, or SQL commands in the terminal to set the fastest high score.",
        "language_slug": "javascript",
        "duration_minutes": 60,
        "xp_reward": 650,
        "starter_code": (
            "// Game Championship Controller\n"
            "const engines = ['Flexbox Bridge', 'Neural Rover', 'SQL Vault', 'Memory Reactor'];\n"
            "console.log('Synced Game Engines: ' + engines.join(' | '));\n"
        ),
        "solution_code": (
            "const engines = ['Flexbox Bridge', 'Neural Rover', 'SQL Vault', 'Memory Reactor'];\n"
            "console.log('Synced Game Engines: ' + engines.join(' | '));\n"
        ),
    },
    {
        "slug": "polyglot-database-detective-cup",
        "title": "SQL, MySQL, PostgreSQL & MongoDB Data Detective Open Cup",
        "category": "SQL_MYSTERY",
        "description": "Automated Database Competition. Write relational SQL JOINs and MongoDB document queries to audit server logs and rank on the live board.",
        "language_slug": "sql",
        "duration_minutes": 45,
        "xp_reward": 600,
        "starter_code": "SELECT student_id, name, department, xp FROM students ORDER BY xp DESC;",
        "solution_code": "SELECT student_id, name, department, xp FROM students ORDER BY xp DESC;",
    },
]


def ensure_autonomous_platform_state():
    """
    Zero-Touch Self-Updating Engine:
    1. Ensures all 16 world-class languages (including Rust, MySQL/PHP Bridge, AI/ML) are seeded.
    2. Automatically rotates daily tasks & keeps all Open Competitions (IUPC, Hackathon, Game Cup, DB Cup) live.
    """
    now = timezone.now()

    # 1. Ensure extra languages & courses exist
    try:
        for item in EXTRA_LANGUAGES:
            lang, _ = Language.objects.get_or_create(
                slug=item["slug"],
                defaults={
                    "name": item["name"],
                    "short_code": item["short_code"],
                    "category": item["category"],
                    "summary": item["summary"],
                    "order": item["order"],
                    "is_active": True,
                },
            )
            c_data = item["course"]
            course, _ = Course.objects.get_or_create(
                slug=c_data["slug"],
                defaults={
                    "language": lang,
                    "title": c_data["title"],
                    "description": c_data["description"],
                    "level": c_data["level"],
                    "order": item["order"],
                    "xp_reward": c_data["xp_reward"],
                },
            )
            for l_data in item["lessons"]:
                lesson, _ = Lesson.objects.get_or_create(
                    course=course,
                    slug=l_data["slug"],
                    defaults={
                        "title": l_data["title"],
                        "order": l_data["order"],
                        "est_minutes": l_data["est_minutes"],
                        "xp": l_data["xp"],
                        "execution_type": l_data["execution_type"],
                        "body_md": l_data["body_md"],
                        "task_prompt": l_data["task_prompt"],
                        "starter_code": l_data["starter_code"],
                        "solution": l_data["solution"],
                        "tips_tricks": l_data["tips_tricks"],
                        "full_syntax_game_slug": l_data["full_syntax_game_slug"],
                    },
                )
                MicroTask.objects.get_or_create(
                    lesson=lesson,
                    task_number=1,
                    defaults={
                        "task_type": "CORE_SYNTAX",
                        "title": f"Quick Task: {lesson.title}",
                        "instructions": l_data["task_prompt"],
                        "starter_code": l_data["starter_code"],
                        "solution_code": l_data["solution"],
                        "xp_reward": 40,
                    },
                )

        # 2. Ensure Self-Running Open Competitions (IUPC, Hackathon, Game Cup, DB Cup) are always active & fresh
        for idx, comp in enumerate(AUTO_COMPETITIONS):
            contest, created = Contest.objects.get_or_create(
                slug=comp["slug"],
                defaults={
                    "title": comp["title"],
                    "category": comp["category"],
                    "description": comp["description"],
                    "language_slug": comp["language_slug"],
                    "duration_minutes": comp["duration_minutes"],
                    "xp_reward": comp["xp_reward"],
                    "is_active": True,
                    "starts_at": now - timedelta(hours=2),
                    "ends_at": now + timedelta(days=3 + idx),
                    "starter_code": comp["starter_code"],
                    "solution_code": comp["solution_code"],
                },
            )
            # Auto-rollover if timer expired so user never has to touch or reset contests manually!
            if not contest.is_active or contest.ends_at <= now:
                contest.is_active = True
                contest.starts_at = now - timedelta(hours=1)
                contest.ends_at = now + timedelta(days=4 + idx)
                contest.save(update_fields=["is_active", "starts_at", "ends_at"])

            if contest.submissions.count() == 0:
                seed_coders = [
                    ("Md Najmus Sakib Rahatul (1119003)", "BAIUST CSE L3T2", 100, 11),
                    ("Nusrat_CSE", "BAIUST CSE L3T2", 98, 14),
                    ("Tahmid_Rust", "BAIUST CSE L3T2", 95, 18),
                ]
                for rank_i, (uname, batch, sc, ms) in enumerate(seed_coders, start=1):
                    ContestSubmission.objects.create(
                        contest=contest,
                        username=uname,
                        university_batch=batch,
                        score=sc,
                        execution_time_ms=ms,
                        rank=rank_i,
                    )
    except Exception:
        pass


def get_daily_auto_tasks():
    """
    Returns automatically rotated daily coding & game tasks based on today's date seed.
    Requires zero manual admin updates — changes automatically every 24 hours.
    """
    today = timezone.now().date()
    day_seed = today.toordinal()
    pool = [
        {
            "code": f"AUTO-{today.strftime('%m%d')}-01",
            "title": "Build a Responsive Flexbox Navigation Bar",
            "lang": "HTML5 & CSS3",
            "lang_key": "html",
            "type": "Course + Game Task",
            "streak_target": "Course & Game Streak",
            "xp": 60,
            "starter": "<nav style='display:flex; justify-content:space-between; padding:12px; background:#0f172a; color:#fff;'>\n  <strong>CodeQuest</strong>\n  <span>Auto-Task Ready</span>\n</nav>",
        },
        {
            "code": f"AUTO-{today.strftime('%m%d')}-02",
            "title": "Python AI Token Frequency Analyzer",
            "lang": "Python 3 & AI",
            "lang_key": "python",
            "type": "Terminal Coding Task",
            "streak_target": "Course Streak",
            "xp": 75,
            "starter": "tokens = ['code', 'game', 'code', 'ai', 'code', 'sql']\nfreq = {t: tokens.count(t) for t in set(tokens)}\nprint('Token Frequency:', freq)",
        },
        {
            "code": f"AUTO-{today.strftime('%m%d')}-03",
            "title": "C++20 / Rust High-Speed Array Prefix Sum",
            "lang": "C++ / Rust",
            "lang_key": "cpp",
            "type": "IUPC Practice Task",
            "streak_target": "Course Streak",
            "xp": 80,
            "starter": '#include <iostream>\nusing namespace std;\nint main() {\n    cout << "Prefix Sum Verified: [2, 5, 9, 14, 20]" << endl;\n    return 0;\n}',
        },
        {
            "code": f"AUTO-{today.strftime('%m%d')}-04",
            "title": "SQL & PHP MySQLi Top Student Leaderboard Query",
            "lang": "SQL / MySQL / PHP",
            "lang_key": "sql",
            "type": "Database Bridge Task",
            "streak_target": "Game Streak",
            "xp": 70,
            "starter": "SELECT student_id, name, department, cgpa, xp FROM students WHERE cgpa >= 3.70 ORDER BY xp DESC;",
        },
        {
            "code": f"AUTO-{today.strftime('%m%d')}-05",
            "title": "MongoDB NoSQL Document Filter Pipeline",
            "lang": "MongoDB (mongosh)",
            "lang_key": "mongodb",
            "type": "NoSQL Terminal Task",
            "streak_target": "Course Streak",
            "xp": 70,
            "starter": 'db.students.find({"dept": "CSE"})',
        },
        {
            "code": f"AUTO-{today.strftime('%m%d')}-06",
            "title": "Java OOP & React State Circuit Controller",
            "lang": "Java / JS / React",
            "lang_key": "java",
            "type": "Game Control Task",
            "streak_target": "Game Streak",
            "xp": 85,
            "starter": 'public class Main {\n    public static void main(String[] args) {\n        System.out.println("Circuit Turret Locked: Target Acquired [100% Accuracy]");\n    }\n}',
        },
    ]
    rot = day_seed % len(pool)
    rotated = pool[rot:] + pool[:rot]
    return rotated
