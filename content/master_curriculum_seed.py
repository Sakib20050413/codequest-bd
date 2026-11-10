"""
CodeQuest Master Curriculum Seeder
Builds all 11 Viral Languages, Tips & Tricks Memory Boxes, Full-Syntax Games,
3 Post-Lesson Micro-Tasks per module, Contests, and Verifiable Certificates.
"""
import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import django
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from learn.models import (
    Language, Course, Lesson, Game, Badge, UserProfile,
    MicroTask, Certificate, Contest, ContestSubmission
)

# ==============================================================================
# 1. THE 11 VIRAL LANGUAGES + FULL-SYNTAX GAMES SPECIFICATION
# ==============================================================================
VIRAL_LANGUAGES = [
    {
        "name": "Python 3",
        "slug": "python",
        "code": "PY",
        "category": "Backend & Algorithmic",
        "summary": "Write clean algorithmic logic, data comprehensions, and automation pipelines.",
        "icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2c4 0 5 1.5 5 4v2H9c-2 0-3 1-3 3v2H4c-2.5 0-4-1.5-4-5s1.5-6 5-6h7zM12 22c-4 0-5-1.5-5-4v-2h8c2 0 3-1 3-3v-2h2c2.5 0 4 1.5 4 5s-1.5 6-5 6h-7z"/></svg>',
        "order": 1,
        "course_title": "Python 3 Algorithmic Core",
        "course_desc": "Master pythonic loops, dictionary pipelines, list comprehensions, and algorithmic logic.",
        "game_slug": "cyber-grid-rover",
        "game_title": "Cyber Grid Rover Pathfinding",
        "game_desc": "Write complete Python loops and if/elif/else navigation functions to guide the robotic rover across a hazard grid.",
    },
    {
        "name": "JavaScript ES6+",
        "slug": "javascript",
        "code": "JS",
        "category": "Web & Reactive",
        "summary": "Power dynamic DOM reactivity, user events, promises, and modern ES6+ patterns.",
        "icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="4"/><path d="M16 8v8a2 2 0 0 1-2 2h-1M8 14c.5 1.5 2 2 3 2s2-.5 2-1.5c0-2-3-1.5-3-3.5 0-1 1-1.5 2-1.5s2 .5 2.5 1.5"/></svg>',
        "order": 2,
        "course_title": "JavaScript ES6+ & DOM Reactivity",
        "course_desc": "Master modern arrow functions, array map/filter pipelines, async/await, and browser event listeners.",
        "game_slug": "signal-tower-defense",
        "game_title": "Signal Tower Defense Logic",
        "game_desc": "Write real JavaScript array sorting and priority targeting algorithms to defend the telemetry grid against enemy packet waves.",
    },
    {
        "name": "HTML5",
        "slug": "html",
        "code": "HTML",
        "category": "Web Foundations",
        "summary": "Build semantic skeletons, accessible document hierarchies, and living DOM trees.",
        "icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 3l1.5 17 6.5 2 6.5-2L20 3H4z"/><path d="M12 6v13l4.5-1.5 1-11H12z"/></svg>',
        "order": 3,
        "course_title": "HTML5 Foundations & Semantic Architecture",
        "course_desc": "Construct semantic document landmarks, accessible forms, audio/video elements, and clean markup.",
        "game_slug": "blueprint-architect",
        "game_title": "Blueprint Structural Architect",
        "game_desc": "Write complete semantic HTML structures to assemble and stabilize a high-tech architectural research blueprint.",
    },
    {
        "name": "CSS3",
        "slug": "css",
        "code": "CSS",
        "category": "Web Foundations",
        "summary": "Master Box Model precision, Flexbox alignment, and 2D CSS Grid responsive dashboards.",
        "icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 3l1.5 17 6.5 2 6.5-2L20 3H4z"/><path d="M7 7h10M7 11h9l-.5 5-3.5 1-3.5-1-.2-2"/></svg>',
        "order": 4,
        "course_title": "CSS3 Styling, Flexbox & Grid Layouts",
        "course_desc": "Transform raw tags into pixel-perfect layouts using modern Flexbox, multi-track Grid, and fluid media queries.",
        "game_slug": "flexbox-grid-bridge",
        "game_title": "Flexbox & Grid Cyber Bridge",
        "game_desc": "Write real CSS rulesets (display: flex, justify-content, align-items, grid-template-columns) to align laser bridges and transport cargo.",
    },
    {
        "name": "React",
        "slug": "react",
        "code": "REACT",
        "category": "Frontend Frameworks",
        "summary": "Build composable user interfaces with JSX, reactive state hooks, and unidirectional data flow.",
        "icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="2"/><ellipse cx="12" cy="12" rx="9" ry="3"/><ellipse cx="12" cy="12" rx="3" ry="9"/><ellipse cx="12" cy="12" rx="9" ry="3" transform="rotate(60 12 12)"/><ellipse cx="12" cy="12" rx="9" ry="3" transform="rotate(120 12 12)"/></svg>',
        "order": 5,
        "course_title": "React Component Architecture & Hooks",
        "course_desc": "Master JSX syntax, useState interactive state, useEffect lifecycles, and component composition patterns.",
        "game_slug": "reactor-energy-hud",
        "game_title": "Reactive Energy Reactor HUD",
        "game_desc": "Write complete React functional components and state hooks to monitor core telemetry and balance energy levels.",
    },
    {
        "name": "Java",
        "slug": "java",
        "code": "JAVA",
        "category": "Enterprise & Systems",
        "summary": "Strongly typed enterprise programming, class blueprints, encapsulation, and collections.",
        "icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 10h2a2 2 0 0 1 2 2v2a2 2 0 0 1-2 2h-2M4 7h14v10a4 4 0 0 1-4 4H8a4 4 0 0 1-4-4V7z"/></svg>',
        "order": 6,
        "course_title": "Java Enterprise OOP & Collections",
        "course_desc": "Master class blueprints, constructors, encapsulation, polymorphism, and ArrayList collections.",
        "game_slug": "droid-fleet-oop",
        "game_title": "Droid Fleet OOP Commander",
        "game_desc": "Write complete Java class methods and OOP loops to coordinate shield regeneration and formation commands.",
    },
    {
        "name": "C Programming",
        "slug": "c-lang",
        "code": "C",
        "category": "Systems & Memory",
        "summary": "Direct memory addressing, pointers, array offsets, structs, and determinism.",
        "icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M15 9a4.5 4.5 0 1 0 0 6"/></svg>',
        "order": 7,
        "course_title": "C Systems Programming & Memory Architecture",
        "course_desc": "Understand how machines execute code. Master address-of operators, pointer arithmetic, structs, and memory buffers.",
        "game_slug": "memory-defrag",
        "game_title": "Memory Sector Defragmenter",
        "game_desc": "Write complete C loops and pointer offsets to compact corrupted memory blocks in a visual hex buffer grid.",
    },
    {
        "name": "C++",
        "slug": "cpp",
        "code": "CPP",
        "category": "Competitive & Systems",
        "summary": "High-performance programming with modern STL containers, references, and fast algorithms.",
        "icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M10 9a3.5 3.5 0 1 0 0 6M15 12h3M16.5 10.5v3M19.5 12h3M21 10.5v3"/></svg>',
        "order": 8,
        "course_title": "C++ STL & Competitive Algorithms",
        "course_desc": "Master fast I/O, std::vector, std::stack/queue, sorting, binary search, and graph traversal fundamentals.",
        "game_slug": "dungeon-pathfinder",
        "game_title": "Dungeon Graph Pathfinder",
        "game_desc": "Write complete C++ STL vector/queue traversal logic to find the shortest exit route through a dark labyrinth.",
    },
    {
        "name": "SQL / PostgreSQL",
        "slug": "sql",
        "code": "SQL",
        "category": "Databases & Analytics",
        "summary": "Query, filter, join, and aggregate normalized relational data models.",
        "icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>',
        "order": 9,
        "course_title": "SQL Relational Queries & Data Engineering",
        "course_desc": "Master SELECT statements, WHERE clauses, GROUP BY aggregations, multi-table INNER/LEFT JOINs, and subqueries.",
        "game_slug": "cyber-crime-detective",
        "game_title": "Cyber Crime Database Detective",
        "game_desc": "Write complete multi-line SQL queries against a live in-browser database to cross-reference suspect IP logs and unmask the hacker.",
    },
    {
        "name": "Django",
        "slug": "django",
        "code": "DJ",
        "category": "Full-Stack Frameworks",
        "summary": "Build secure, production-grade web backends with MVT architecture, ORM, and REST APIs.",
        "icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="4"/><path d="M9 7v10M15 7v10M9 12h6"/></svg>',
        "order": 10,
        "course_title": "Django Full-Stack Web Architecture",
        "course_desc": "Master Model-View-Template patterns, URL dispatchers, ORM QuerySets, form validation, and authentication security.",
        "game_slug": "api-traffic-defender",
        "game_title": "API Traffic Router & ORM Defender",
        "game_desc": "Write complete Django view logic and ORM filter queries to authenticate incoming requests and block malformed attacks.",
    },
    {
        "name": "MongoDB",
        "slug": "mongodb",
        "code": "MDB",
        "category": "NoSQL Databases",
        "summary": "Document-oriented database querying, JSON/BSON manipulation, and aggregation pipelines.",
        "icon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2C8 6 6 10 6 15c0 4 3 7 6 7s6-3 6-7c0-5-2-9-6-13z"/><path d="M12 2v20"/></svg>',
        "order": 11,
        "course_title": "MongoDB Document Modeling & Aggregations",
        "course_desc": "Master BSON document structure, collection find() queries, comparison operators ($gt, $in), and $match/$group aggregation pipelines.",
        "game_slug": "nosql-cluster-scanner",
        "game_title": "NoSQL Telemetry Cluster Scanner",
        "game_desc": "Write complete MongoDB query documents and aggregation stages to isolate anomalous satellite nodes across telemetry clusters.",
    },
]

print("Starting Master Curriculum Seeding...")

# Ensure Superuser
if not User.objects.filter(username="sakib_admin").exists():
    admin_user = User.objects.create_superuser("sakib_admin", "mdnajmussakib2003@gmail.com", "baiust1119003")
    profile, _ = UserProfile.objects.get_or_create(user=admin_user)
    profile.xp = 650
    profile.streak = 7
    profile.freeze_shields = 2
    profile.daily_goal_minutes = 30
    profile.daily_goal_xp = 200
    profile.save()
    print("Created Superuser: sakib_admin")

# Create or Update Languages, Courses, Games, Lessons, and Micro-Tasks
for lang_data in VIRAL_LANGUAGES:
    lang, _ = Language.objects.update_or_create(
        slug=lang_data["slug"],
        defaults={
            "name": lang_data["name"],
            "short_code": lang_data["code"],
            "category": lang_data["category"],
            "summary": lang_data["summary"],
            "icon_svg": lang_data["icon"],
            "order": lang_data["order"],
            "is_active": True,
        }
    )

    course, _ = Course.objects.update_or_create(
        slug=f"{lang_data['slug']}-core",
        defaults={
            "language": lang,
            "title": lang_data["course_title"],
            "description": lang_data["course_desc"],
            "level": "Beginner to Intermediate",
            "order": lang_data["order"],
            "xp_reward": 450,
        }
    )

    # Full-Syntax Game
    Game.objects.update_or_create(
        slug=lang_data["game_slug"],
        defaults={
            "title": lang_data["game_title"],
            "tagline": f"Full-Syntax {lang_data['name']} Interactive Simulation",
            "description": lang_data["game_desc"],
            "category": f"{lang_data['name']} Full-Syntax Game",
            "difficulty": "Multi-Level Challenge (3-5 min)",
            "icon_svg": "🎮",
            "xp_per_win": 75,
            "order": lang_data["order"],
        }
    )

    print(f"Synced Language & Course: {lang.name} -> {course.title}")

# Populate Modules, Lessons, Tips & Tricks, and 3 Micro-Tasks for the 4 newly added viral languages:
# React, C++, Django, MongoDB (plus ensuring Python, JS, HTML, CSS, SQL, Java, C have complete tips & micro-tasks)

CURRICULUM_DETAILS = {
    "react-core": [
        {
            "order": 1,
            "slug": "jsx-fundamentals",
            "title": "JSX Syntax & Component Hierarchy",
            "body": "React builds user interfaces out of reusable, isolated pieces of code called components. JSX allows writing HTML-like tags directly inside JavaScript. Every JSX tag must close properly, multi-line blocks must be wrapped in a single root parent or Fragment (`<>...</>`), and HTML attributes like `class` become `className`.",
            "tips": "Pro Shortcut: Never mutate DOM directly in React. Use `{expression}` to inject dynamic values. Trap to Avoid: Forgetting `className` instead of `class` causes React DOM property console warnings.",
            "prompt": "Create a functional component named `WelcomeBanner` that returns a root `<div className=\"banner\">` containing an `<h1>` with the exact text \"CodeQuest Reactive Reactor\".",
            "starter": "function WelcomeBanner() {\n  return (\n    // Write your JSX here\n  );\n}",
            "solution": "function WelcomeBanner() {\n  return (\n    <div className=\"banner\">\n      <h1>CodeQuest Reactive Reactor</h1>\n    </div>\n  );\n}",
            "tests": [
                {"id": "t1", "desc": "Defines function WelcomeBanner", "type": "code_contains", "query": "function WelcomeBanner"},
                {"id": "t2", "desc": "Uses className=\"banner\"", "type": "code_contains", "query": 'className="banner"'},
                {"id": "t3", "desc": "Renders exact heading text", "type": "code_contains", "query": "CodeQuest Reactive Reactor"}
            ],
            "micro_tasks": [
                {
                    "num": 1, "type": "CORE_SYNTAX", "title": "Self-Closing Elements", "xp": 30,
                    "instr": "Add a self-closing `<img src=\"core.png\" alt=\"reactor\" />` inside the banner.",
                    "starter": "function Banner() {\n  return (\n    <div className=\"banner\">\n      {/* Add self-closing img tag */}\n    </div>\n  );\n}",
                    "tests": [{"name": "Normal Check", "expected": "<img src=\"core.png\" alt=\"reactor\" />", "hidden": False}]
                },
                {
                    "num": 2, "type": "EDGE_CASE_OPT", "title": "React Fragment Wrapping", "xp": 40,
                    "instr": "Return two adjacent `<section>` elements wrapped inside a single Fragment `<>...</>` without creating an extra DOM node.",
                    "starter": "function DualSection() {\n  return (\n    // Wrap with fragment\n  );\n}",
                    "tests": [{"name": "Fragment Check", "expected": "<> ... </>", "hidden": False}]
                },
                {
                    "num": 3, "type": "MINI_BOSS", "title": "Dynamic Title Injection", "xp": 50,
                    "instr": "Inject dynamic constant variable `{systemName}` inside an `<h2>` element.",
                    "starter": "const systemName = \"CyberReactor v2\";\nfunction Header() {\n  return <h2>{/* inject variable */}</h2>;\n}",
                    "tests": [{"name": "Variable Interpolation", "expected": "<h2>{systemName}</h2>", "hidden": False}]
                }
            ]
        },
        {
            "order": 2,
            "slug": "usestate-interactive",
            "title": "Interactive State with useState Hook",
            "body": "Components often need to change what's on the screen as a result of an interaction. The `useState` hook declares a state variable. It returns an array with two items: the current state value, and a setter function to update it and trigger a clean re-render.",
            "tips": "Pro Shortcut: Call hooks only at the top level of your component, never inside loops or conditions. Trap: Modifying `count = count + 1` directly will NOT trigger a re-render. Always call `setCount(count + 1)`.",
            "prompt": "Initialize energy state with `const [energy, setEnergy] = useState(100);` and create a button that calls `setEnergy(energy + 10)` on click.",
            "starter": "import React, { useState } from 'react';\n\nfunction ReactorControl() {\n  // 1. Declare state\n  \n  return (\n    <div>\n      {/* 2. Display energy and click button */}\n    </div>\n  );\n}",
            "solution": "import React, { useState } from 'react';\n\nfunction ReactorControl() {\n  const [energy, setEnergy] = useState(100);\n  \n  return (\n    <div>\n      <span>Energy: {energy}</span>\n      <button onClick={() => setEnergy(energy + 10)}>Boost</button>\n    </div>\n  );\n}",
            "tests": [
                {"id": "t1", "desc": "Uses useState(100)", "type": "code_contains", "query": "useState(100)"},
                {"id": "t2", "desc": "Declares setEnergy setter", "type": "code_contains", "query": "setEnergy"},
                {"id": "t3", "desc": "Attaches onClick handler", "type": "code_contains", "query": "onClick"}
            ],
            "micro_tasks": [
                {
                    "num": 1, "type": "CORE_SYNTAX", "title": "Boolean State Toggle", "xp": 30,
                    "instr": "Create a boolean state `isActive` initialized to `false` with setter `setIsActive`.",
                    "starter": "const [isActive, setIsActive] = useState(false);",
                    "tests": [{"name": "Initial State", "expected": "false", "hidden": False}]
                },
                {
                    "num": 2, "type": "EDGE_CASE_OPT", "title": "Functional State Update", "xp": 40,
                    "instr": "Update counter using updater function `setCount(prev => prev + 1)` to prevent stale closures.",
                    "starter": "function increment() {\n  // use functional updater\n}",
                    "tests": [{"name": "Updater syntax", "expected": "prev => prev + 1", "hidden": False}]
                },
                {
                    "num": 3, "type": "MINI_BOSS", "title": "Critical Overheat Guard", "xp": 50,
                    "instr": "Write an event handler that sets state only if `currentTemp < 950`, otherwise alerts \"Overheat!\".",
                    "starter": "function coolCore() {\n  // conditional state set\n}",
                    "tests": [{"name": "Boundary Guard", "expected": "temp < 950", "hidden": False}]
                }
            ]
        }
    ],
    "cpp-core": [
        {
            "order": 1,
            "slug": "fast-io-vectors",
            "title": "Fast I/O & STL std::vector Dynamic Arrays",
            "body": "Competitive C++ relies on fast I/O optimizations to process hundreds of thousands of operations in milliseconds. `std::vector<T>` is the foundational dynamic array from the Standard Template Library (STL) that grows automatically, providing O(1) random access via `operator[]` and fast insertion at the tail via `push_back()`.",
            "tips": "Pro Shortcut: Always include `std::ios_base::sync_with_stdio(false); std::cin.tie(NULL);` at the top of competitive solutions. Trap: Calling `.push_back()` in tight loops without calling `.reserve(N)` triggers expensive heap reallocations.",
            "prompt": "Create an `std::vector<int> energy_cells;`, push values 15, 30, and 45 into it, and return its size using `.size()`.",
            "starter": "#include <iostream>\n#include <vector>\n\nint main() {\n    // Initialize vector, push elements\n    \n    return 0;\n}",
            "solution": "#include <iostream>\n#include <vector>\n\nint main() {\n    std::vector<int> energy_cells;\n    energy_cells.push_back(15);\n    energy_cells.push_back(30);\n    energy_cells.push_back(45);\n    std::cout << energy_cells.size() << std::endl;\n    return 0;\n}",
            "tests": [
                {"id": "t1", "desc": "Includes <vector>", "type": "code_contains", "query": "#include <vector>"},
                {"id": "t2", "desc": "Uses std::vector<int>", "type": "code_contains", "query": "vector<int>"},
                {"id": "t3", "desc": "Pushes 3 elements", "type": "code_contains", "query": "push_back"}
            ],
            "micro_tasks": [
                {
                    "num": 1, "type": "CORE_SYNTAX", "title": "Vector Traversal Loop", "xp": 30,
                    "instr": "Print all elements using modern range-based for loop `for (int val : energy_cells)`.",
                    "starter": "for (int val : energy_cells) {\n  std::cout << val << \" \";\n}",
                    "tests": [{"name": "Range For", "expected": "for (int val : energy_cells)", "hidden": False}]
                },
                {
                    "num": 2, "type": "EDGE_CASE_OPT", "title": "Capacity Reservation", "xp": 40,
                    "instr": "Call `vec.reserve(1000);` before inserting elements to prevent dynamic reallocations.",
                    "starter": "std::vector<int> path;\n// reserve 1000 items",
                    "tests": [{"name": "Reserve call", "expected": "path.reserve(1000);", "hidden": False}]
                },
                {
                    "num": 3, "type": "MINI_BOSS", "title": "STL Sorting", "xp": 50,
                    "instr": "Sort a vector in ascending order using `std::sort(vec.begin(), vec.end());`.",
                    "starter": "#include <algorithm>\n// sort array",
                    "tests": [{"name": "std::sort call", "expected": "std::sort", "hidden": False}]
                }
            ]
        }
    ],
    "django-core": [
        {
            "order": 1,
            "slug": "mvt-architecture-routing",
            "title": "Django MVT Architecture & Dynamic URL Dispatcher",
            "body": "Django follows the Model-View-Template (MVT) pattern. The Model maps directly to the database tables via ORM. The View contains business logic, processing HTTP requests and returning HTTP responses. The Template renders structured HTML presentations. The `urls.py` file maps incoming URL paths to their target view functions.",
            "tips": "Pro Shortcut: Always name your paths using `name=\"endpoint_name\"` so you can reverse URLs with `{% url %}` in templates. Trap: Forgetting `trailing slash` in Django URLs can trigger unnecessary 301 redirects.",
            "prompt": "Define a Django view function `telemetry_view(request)` that returns an `HttpResponse(\"System Status: 100% Operational\")`.",
            "starter": "from django.http import HttpResponse\n\ndef telemetry_view(request):\n    # Return HttpResponse here\n    pass",
            "solution": "from django.http import HttpResponse\n\ndef telemetry_view(request):\n    return HttpResponse(\"System Status: 100% Operational\")",
            "tests": [
                {"id": "t1", "desc": "Defines telemetry_view(request)", "type": "code_contains", "query": "def telemetry_view(request):"},
                {"id": "t2", "desc": "Returns HttpResponse", "type": "code_contains", "query": "return HttpResponse"},
                {"id": "t3", "desc": "Exact status message", "type": "code_contains", "query": "System Status: 100% Operational"}
            ],
            "micro_tasks": [
                {
                    "num": 1, "type": "CORE_SYNTAX", "title": "JSON Response Endpoint", "xp": 30,
                    "instr": "Return a dictionary `{\"status\": \"ok\", \"nodes\": 12}` using `JsonResponse`.",
                    "starter": "from django.http import JsonResponse\ndef api(request):\n  return JsonResponse(...)",
                    "tests": [{"name": "JSON return", "expected": "JsonResponse", "hidden": False}]
                },
                {
                    "num": 2, "type": "EDGE_CASE_OPT", "title": "Slug URL Route", "xp": 40,
                    "instr": "Map `<slug:node_id>/` in urlpatterns with path function.",
                    "starter": "path('telemetry/<slug:node_id>/', views.node_detail, name='node_detail')",
                    "tests": [{"name": "Slug regex converter", "expected": "<slug:node_id>", "hidden": False}]
                },
                {
                    "num": 3, "type": "MINI_BOSS", "title": "ORM Filtering QuerySet", "xp": 50,
                    "instr": "Filter active nodes using `ServerNode.objects.filter(is_active=True).order_by('-priority')`.",
                    "starter": "# write query",
                    "tests": [{"name": "Chained QuerySet", "expected": "filter(is_active=True)", "hidden": False}]
                }
            ]
        }
    ],
    "mongodb-core": [
        {
            "order": 1,
            "slug": "bson-document-find",
            "title": "BSON Documents & Collection find() Queries",
            "body": "MongoDB stores data as flexible, JSON-like BSON (Binary JSON) documents organized inside collections. The primary reading method is `db.collection.find(query, projection)`. Queries use key-value match criteria, while operators like `$gt` (greater than) and `$in` (in array) filter nested telemetry records with high throughput.",
            "tips": "Pro Shortcut: Projections like `{ name: 1, _id: 0 }` save massive network bandwidth by fetching only requested fields. Trap: Forgetting quotes on nested field queries (`\"telemetry.temp\"` vs `telemetry.temp`) throws syntax errors.",
            "prompt": "Write a query to find all satellites in collection `satellites` where `status` is \"active\" and `altitude` is greater than 500 using `{ status: \"active\", altitude: { $gt: 500 } }`.",
            "starter": "db.satellites.find({\n  // Write query filters\n});",
            "solution": "db.satellites.find({\n  status: \"active\",\n  altitude: { $gt: 500 }\n});",
            "tests": [
                {"id": "t1", "desc": "Uses db.satellites.find", "type": "code_contains", "query": "db.satellites.find"},
                {"id": "t2", "desc": "Matches status: 'active'", "type": "code_contains", "query": '"active"'},
                {"id": "t3", "desc": "Uses $gt operator", "type": "code_contains", "query": "$gt"}
            ],
            "micro_tasks": [
                {
                    "num": 1, "type": "CORE_SYNTAX", "title": "Field Projection", "xp": 30,
                    "instr": "Exclude `_id` and include `satellite_name` in query projection.",
                    "starter": "db.satellites.find({}, { satellite_name: 1, _id: 0 });",
                    "tests": [{"name": "Projection rule", "expected": "_id: 0", "hidden": False}]
                },
                {
                    "num": 2, "type": "EDGE_CASE_OPT", "title": "Array Element Match ($in)", "xp": 40,
                    "instr": "Find satellites whose orbit is either \"LEO\" or \"GEO\" using `{ orbit: { $in: [\"LEO\", \"GEO\"] } }`.",
                    "starter": "db.satellites.find({ orbit: { $in: [\"LEO\", \"GEO\"] } });",
                    "tests": [{"name": "In operator", "expected": "$in", "hidden": False}]
                },
                {
                    "num": 3, "type": "MINI_BOSS", "title": "Aggregation Grouping ($group)", "xp": 50,
                    "instr": "Write an aggregation stage `$group: { _id: \"$orbit\", total: { $sum: 1 } }`.",
                    "starter": "db.satellites.aggregate([\n  { $group: { _id: \"$orbit\", total: { $sum: 1 } } }\n]);",
                    "tests": [{"name": "Group pipeline", "expected": "$group", "hidden": False}]
                }
            ]
        }
    ]
}

# Seed Lessons and Micro-Tasks for newly configured courses
for course_slug, lesson_list in CURRICULUM_DETAILS.items():
    try:
        c = Course.objects.get(slug=course_slug)
        for l_data in lesson_list:
            lesson, _ = Lesson.objects.update_or_create(
                course=c,
                slug=l_data["slug"],
                defaults={
                    "title": l_data["title"],
                    "order": l_data["order"],
                    "body_md": l_data["body"],
                    "tips_tricks": l_data["tips"],
                    "task_prompt": l_data["prompt"],
                    "starter_code": l_data["starter"],
                    "solution": l_data["solution"],
                    "tests_json": l_data["tests"],
                    "full_syntax_game_slug": c.language.slug,
                    "xp": 50,
                }
            )

            # Micro-tasks
            for mt in l_data.get("micro_tasks", []):
                MicroTask.objects.update_or_create(
                    lesson=lesson,
                    task_number=mt["num"],
                    defaults={
                        "task_type": mt["type"],
                        "title": mt["title"],
                        "instructions": mt["instr"],
                        "starter_code": mt.get("starter", ""),
                        "xp_reward": mt["xp"],
                        "test_cases_json": mt["tests"],
                    }
                )
            print(f"Created Lesson + MicroTasks for {c.title}: {lesson.title}")
    except Course.DoesNotExist:
        print(f"Course {course_slug} not found, skipping details.")

# ==============================================================================
# 2. SEED WEEKLY CODING CONTESTS & LEADERBOARDS
# ==============================================================================
CONTESTS_DATA = [
    {
        "slug": "algo-sprint-w45",
        "title": "Weekly Algorithm Sprint #45: Subarray Sum & Prefix Logic",
        "category": "ALGO_SPRINT",
        "desc": "Solve 3 algorithmic subproblems within 45 minutes. Optimize from O(N^2) to O(N) using sliding window and prefix frequency hashing.",
        "lang": "python",
        "duration": 45,
        "xp": 500,
        "starter": "def max_subarray_sum(nums, k):\n    # Return max sum of any contiguous subarray of size k\n    pass",
        "solution": "def max_subarray_sum(nums, k):\n    cur = sum(nums[:k])\n    mx = cur\n    for i in range(k, len(nums)):\n        cur += nums[i] - nums[i-k]\n        if cur > mx: mx = cur\n    return mx",
        "tests": [
            {"input": "[2, 1, 5, 1, 3, 2], 3", "expected": "9"},
            {"input": "[2, 3, 4, 1, 5], 2", "expected": "7"}
        ]
    },
    {
        "slug": "sql-mystery-w45",
        "title": "SQL Detective Mystery: The Corporate Data Heist",
        "category": "SQL_MYSTERY",
        "desc": "Cross-examine 3 relational tables (access_logs, employee_shifts, vault_keys) to expose the rogue security identifier.",
        "lang": "sql",
        "duration": 30,
        "xp": 450,
        "starter": "-- Query to find suspect employee\nSELECT e.emp_name, e.badge_id\nFROM employees e\n-- Join access logs\nWHERE 1=1;",
        "solution": "SELECT e.emp_name, e.badge_id FROM employees e JOIN access_logs a ON e.id = a.emp_id WHERE a.status = 'FLAGGED' GROUP BY e.emp_name, e.badge_id HAVING COUNT(*) > 3;",
        "tests": [
            {"input": "schema_v1", "expected": "3 rows returned"}
        ]
    },
    {
        "slug": "ui-showdown-w45",
        "title": "UI Layout Showdown: Apple-Grade Glassmorphic Dashboard",
        "category": "UI_SHOWDOWN",
        "desc": "Construct a responsive 3-column financial card matrix strictly adhering to 60-30-10 color rules with zero layout overflow on mobile.",
        "lang": "css",
        "duration": 30,
        "xp": 400,
        "starter": "/* CSS Grid Matrix */\n.dashboard-grid {\n  display: grid;\n  /* Complete columns */\n}",
        "solution": ".dashboard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; }",
        "tests": [
            {"input": "viewport 1440px", "expected": "3 columns"}
        ]
    },
    {
        "slug": "game-speedrun-w45",
        "title": "Full-Syntax Game Speedrun: Cyber Rover Martian Maze",
        "category": "GAME_SPEEDRUN",
        "desc": "Guide the rover through 5 procedural minefields with minimum energy expenditure and zero collision halts.",
        "lang": "python",
        "duration": 40,
        "xp": 550,
        "starter": "def navigate_rover(grid, target):\n    # Write pathfinder\n    pass",
        "solution": "def navigate_rover(grid, target): return ['FORWARD', 'FORWARD', 'RIGHT', 'FORWARD']",
        "tests": [
            {"input": "grid_5x5", "expected": "REACHED"}
        ]
    }
]

now = timezone.now()
ends = now + timezone.timedelta(days=6)

for c_data in CONTESTS_DATA:
    contest, _ = Contest.objects.update_or_create(
        slug=c_data["slug"],
        defaults={
            "title": c_data["title"],
            "category": c_data["category"],
            "description": c_data["desc"],
            "language_slug": c_data["lang"],
            "duration_minutes": c_data["duration"],
            "xp_reward": c_data["xp"],
            "is_active": True,
            "starts_at": now,
            "ends_at": ends,
            "starter_code": c_data["starter"],
            "solution_code": c_data["solution"],
            "test_cases_json": c_data["tests"],
        }
    )

    # Sample leaderboard submissions
    SAMPLE_LEADERBOARD = [
        {"user": "Sakib_Rahatul", "batch": "BAIUST CSE Batch 11", "score": 300, "time": 18, "rank": 1},
        {"user": "Tasin_BUET", "batch": "BUET CSE 20", "score": 290, "time": 22, "rank": 2},
        {"user": "Nesar_Uddin", "batch": "BAIUST CSE Batch 11", "score": 280, "time": 25, "rank": 3},
        {"user": "Rayhan_Towhid", "batch": "BAIUST CSE Batch 11", "score": 270, "time": 28, "rank": 4},
        {"user": "Adnan_DU", "batch": "DU CS 26", "score": 260, "time": 31, "rank": 5},
    ]

    for entry in SAMPLE_LEADERBOARD:
        ContestSubmission.objects.update_or_create(
            contest=contest,
            username=entry["user"],
            defaults={
                "university_batch": entry["batch"],
                "score": entry["score"],
                "execution_time_ms": entry["time"],
                "rank": entry["rank"],
            }
        )

print("Synced Contests & Competitive Leaderboards")

# ==============================================================================
# 3. SEED VERIFIED ACADEMIC CERTIFICATE (Md Najmus Sakib Rahatul)
# ==============================================================================
cert, _ = Certificate.objects.update_or_create(
    credential_id="CQ-BD-2026-PY3-1119003",
    defaults={
        "student_name": "Md Najmus Sakib Rahatul",
        "student_id_str": "1119003",
        "track_slug": "python",
        "track_title": "Python 3 Algorithmic Core & Systems",
        "mastery_score": 98,
        "is_verified": True,
        "qr_data": "https://codequest-bd.vercel.app/verify/CQ-BD-2026-PY3-1119003",
        "issued_at": now - timezone.timedelta(days=2),
    }
)
print(f"Created Verified Certificate: {cert.credential_id}")

# Also seed for JavaScript
Certificate.objects.update_or_create(
    credential_id="CQ-BD-2026-JS-1119003",
    defaults={
        "student_name": "Md Najmus Sakib Rahatul",
        "student_id_str": "1119003",
        "track_slug": "javascript",
        "track_title": "JavaScript ES6+ & Reactive DOM Architecture",
        "mastery_score": 95,
        "is_verified": True,
        "qr_data": "https://codequest-bd.vercel.app/verify/CQ-BD-2026-JS-1119003",
        "issued_at": now - timezone.timedelta(days=1),
    }
)

print("Master Curriculum Seeding Completed Successfully!")
