"""
CodeQuest BD — Master Database Seeder
Seeds 6 Language Tracks, 18 Playable Levels, 15 Bug Blitz Questions,
Campus Leaderboard Profiles, Announcements, and Admin Superuser (sakib_admin).
"""

import os
import sys

# Configure UTF-8 encoding for Windows console compatibility
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codequest_cms.settings')
django.setup()

from django.contrib.auth.models import User
from accounts.models import StudentProfile
from arena.models import LanguageTrack, ChallengeLevel, QuizQuestion, LabAnnouncement, StudentSubmission


def run_seed():
    print("🚀 Initializing CodeQuest BD Database Seeding...")

    # 1. Create Superuser / Lead Student: sakib_admin
    admin_user, created = User.objects.get_or_create(username='sakib_admin', defaults={
        'email': 'sakib.1119003@baiust.edu.bd',
        'first_name': 'Md Najmus Sakib',
        'last_name': 'Rahatul',
        'is_staff': True,
        'is_superuser': True,
    })
    admin_user.set_password('baiust1119003')
    admin_user.is_staff = True
    admin_user.is_superuser = True
    admin_user.save()

    profile = admin_user.profile
    profile.student_id = '1119003'
    profile.batch_section = 'CSE 3-2 Section A'
    profile.university = 'BAIUST, Cumilla'
    profile.xp = 1850
    profile.level = 5
    profile.avatar = 'cyber_rover'
    profile.badges = [
        "First Blood (1st Solve)",
        "DOM Master",
        "PHP CRUD Ninja",
        "Polyglot Programmer (Solved in 4+ Languages)",
        "Blitz Champion",
        "Century Pioneer (1000+ XP)"
    ]
    profile.solved_levels = [
        'c-programming-fundamentals-1-rover-linear-loop',
        'c-programming-fundamentals-2-array-reversal-matrix',
        'javascript-dom-manipulation-1-drone-docking-flexbox',
        'php-mysqli-crud-mastery-1-student-record-inserter'
    ]
    profile.save()
    print(f"✅ Lead Student & Admin account configured: sakib_admin / baiust1119003 (ID: {profile.student_id}, {profile.xp} XP)")

    # 2. Seed Classmates for Vibrant Leaderboard
    classmates = [
        {
            'username': 'tanvir_cse', 'name': 'Tanvir Ahmed', 'id': '1119001',
            'section': 'CSE 3-2 Section A', 'xp': 1420, 'level': 4, 'avatar': 'syntax_ninja',
            'badges': ['First Blood (1st Solve)', 'DOM Master', 'Blitz Champion']
        },
        {
            'username': 'nusrat_jahan', 'name': 'Nusrat Jahan', 'id': '1119014',
            'section': 'CSE 3-2 Section A', 'xp': 1250, 'level': 4, 'avatar': 'code_wizard',
            'badges': ['First Blood (1st Solve)', 'Polyglot Programmer']
        },
        {
            'username': 'farhan_kabir', 'name': 'Farhan Kabir', 'id': '1119022',
            'section': 'CSE 3-2 Section B', 'xp': 950, 'level': 3, 'avatar': 'dom_knight',
            'badges': ['First Blood (1st Solve)', 'PHP CRUD Ninja']
        },
        {
            'username': 'sadia_afrin', 'name': 'Sadia Afrin', 'id': '1119035',
            'section': 'CSE 3-2 Section B', 'xp': 720, 'level': 3, 'avatar': 'scholar',
            'badges': ['First Blood (1st Solve)']
        },
        {
            'username': 'mehedi_hasan', 'name': 'Mehedi Hasan', 'id': '1119041',
            'section': 'CSE 3-2 Section A', 'xp': 480, 'level': 2, 'avatar': 'cyber_rover',
            'badges': ['First Blood (1st Solve)']
        },
    ]

    for cm in classmates:
        u, _ = User.objects.get_or_create(username=cm['username'], defaults={
            'first_name': cm['name'].split()[0],
            'last_name': cm['name'].split()[-1],
        })
        u.set_password('baiust1234')
        u.save()
        p = u.profile
        p.student_id = cm['id']
        p.batch_section = cm['section']
        p.xp = cm['xp']
        p.level = cm['level']
        p.avatar = cm['avatar']
        p.badges = cm['badges']
        p.save()
    print("✅ BAIUST Classmates seeded on leaderboard.")

    # 3. Seed Announcements
    LabAnnouncement.objects.all().delete()
    LabAnnouncement.objects.create(
        title="CSE 324 Lab Evaluation 4 on PHP CRUD Scheduled",
        message="Review prepared MySQLi statements and table CRUD operations. Standalone module available under /php_sessional_crud/.",
        badge="PHP Evaluation",
        is_active=True
    )
    LabAnnouncement.objects.create(
        title="20-Mark Code Quiz & Project Viva Defense",
        message="Practice with 60s Bug-Hunter Blitz to build rapid output prediction speed for handwritten exam questions.",
        badge="CSE 324 Final",
        is_active=True
    )
    print("✅ Lab Announcements seeded.")

    # 4. Seed 6 Language Tracks
    tracks_data = [
        {
            'title': 'C Programming Fundamentals',
            'slug': 'c-programming-fundamentals',
            'icon': '⚙️',
            'difficulty': 'Beginner',
            'order': 1,
            'description': 'Master core procedural thinking: arrays, pointers, loops, and 2D Rover logic grids.'
        },
        {
            'title': 'C++ OOP & STL Arena',
            'slug': 'cpp-oop-stl-arena',
            'icon': '⚡',
            'difficulty': 'Intermediate',
            'order': 2,
            'description': 'Object-oriented programming, standard template library (vectors, maps), and algorithmic efficiency.'
        },
        {
            'title': 'Python Logic & Automation',
            'slug': 'python-logic-automation',
            'icon': '🐍',
            'difficulty': 'Beginner',
            'order': 3,
            'description': 'String manipulation, list comprehensions, dictionary mappings, and rapid script development.'
        },
        {
            'title': 'JavaScript & DOM Manipulation',
            'slug': 'javascript-dom-manipulation',
            'icon': '🌐',
            'difficulty': 'Intermediate',
            'order': 4,
            'description': 'Event listeners, dynamic DOM element creation, class toggles, and live client-side game loops.'
        },
        {
            'title': 'PHP & MySQLi CRUD Mastery',
            'slug': 'php-mysqli-crud-mastery',
            'icon': '🐘',
            'difficulty': 'Intermediate',
            'order': 5,
            'description': 'Continuous Evaluation iv focus: secure database connectivity, prepared queries, and table operations.'
        },
        {
            'title': 'HTML5 & CSS3 Layout Games',
            'slug': 'html5-css3-layout-games',
            'icon': '🎨',
            'difficulty': 'Beginner',
            'order': 6,
            'description': 'Flexbox froggy-style alignment, CSS Grid matrices, and high-contrast responsive styling.'
        },
    ]

    track_objs = {}
    for td in tracks_data:
        t, _ = LanguageTrack.objects.update_or_create(slug=td['slug'], defaults=td)
        track_objs[td['slug']] = t
    print("✅ 6 Language Tracks created.")

    # 5. Seed 18 Playable Levels (3 per track)
    ChallengeLevel.objects.all().delete()

    levels_data = [
        # Track 1: C Programming
        {
            'track': track_objs['c-programming-fundamentals'],
            'level_number': 1,
            'title': 'Rover Linear Loop',
            'slug': 'c-programming-fundamentals-1-rover-linear-loop',
            'engine': 'ROVER_MAZE',
            'story_brief': 'The Cyber Rover has rebooted at coordinate (0,0). Guide it straight east to reach the extraction portal at (3,0).',
            'instructions_markdown': 'Use a C `for` loop to print `MOVE_FORWARD` 3 times. The live animation engine will translate each output into rover steps.',
            'starter_code_c': '#include <stdio.h>\n\nint main() {\n    // Task: Print MOVE_FORWARD 3 times\n    for (int i = 0; i < 3; i++) {\n        printf("MOVE_FORWARD\\n");\n    }\n    return 0;\n}',
            'starter_code_python': 'for i in range(3):\n    print("MOVE_FORWARD")',
            'starter_code_javascript': 'for(let i=0; i<3; i++) {\n    console.log("MOVE_FORWARD");\n}',
            'maze_grid_config': {
                'rows': 8, 'cols': 8,
                'start': {'x': 0, 'y': 0, 'dir': 'east'},
                'portal': {'x': 3, 'y': 0},
                'obstacles': [{'x': 1, 'y': 1}, {'x': 2, 'y': 1}],
                'gems': [{'x': 1, 'y': 0}, {'x': 2, 'y': 0}]
            },
            'test_cases': [
                {'input': '', 'expected_output': 'MOVE_FORWARD\nMOVE_FORWARD\nMOVE_FORWARD', 'is_hidden': False}
            ],
            'xp_reward': 100,
            'hints': ['Use `printf("MOVE_FORWARD\\n");` inside a for loop with loop counter i = 0 to 2.']
        },
        {
            'track': track_objs['c-programming-fundamentals'],
            'level_number': 2,
            'title': 'Array Inversion in C',
            'slug': 'c-programming-fundamentals-2-array-inversion',
            'engine': 'CODE_JUDGE',
            'story_brief': 'Invert the telemetry sensor buffer array before feeding it to the navigation computer.',
            'instructions_markdown': 'Read an integer N, followed by N integers. Print the array in reverse order separated by spaces.',
            'starter_code_c': '#include <stdio.h>\n\nint main() {\n    int n;\n    if (scanf("%d", &n) != 1) return 0;\n    int arr[100];\n    for (int i = 0; i < n; i++) {\n        scanf("%d", &arr[i]);\n    }\n    // Print in reverse order:\n    for (int i = n - 1; i >= 0; i--) {\n        printf("%d%s", arr[i], (i == 0) ? "" : " ");\n    }\n    printf("\\n");\n    return 0;\n}',
            'test_cases': [
                {'input': '5\n10 20 30 40 50', 'expected_output': '50 40 30 20 10', 'is_hidden': False},
                {'input': '3\n7 14 21', 'expected_output': '21 14 7', 'is_hidden': True}
            ],
            'xp_reward': 120,
            'hints': ['Loop from `n - 1` down to `0` with `i--`.']
        },
        {
            'track': track_objs['c-programming-fundamentals'],
            'level_number': 3,
            'title': 'Rover Obstacle Bypass (Loop & Turns)',
            'slug': 'c-programming-fundamentals-3-obstacle-bypass',
            'engine': 'ROVER_MAZE',
            'story_brief': 'A laser obstacle blocks coordinate (2,0). Steer the rover around it to reach the portal at (3,2).',
            'instructions_markdown': 'Print sequential commands (`MOVE_FORWARD`, `TURN_RIGHT`, `TURN_LEFT`) to safely reach portal at (3,2).',
            'starter_code_c': '#include <stdio.h>\n\nint main() {\n    printf("MOVE_FORWARD\\n");\n    printf("TURN_RIGHT\\n");\n    printf("MOVE_FORWARD\\n");\n    printf("MOVE_FORWARD\\n");\n    printf("TURN_LEFT\\n");\n    printf("MOVE_FORWARD\\n");\n    printf("MOVE_FORWARD\\n");\n    return 0;\n}',
            'maze_grid_config': {
                'rows': 8, 'cols': 8,
                'start': {'x': 0, 'y': 0, 'dir': 'east'},
                'portal': {'x': 3, 'y': 2},
                'obstacles': [{'x': 2, 'y': 0}, {'x': 2, 'y': 1}],
                'gems': [{'x': 1, 'y': 0}, {'x': 1, 'y': 2}]
            },
            'test_cases': [
                {'input': '', 'expected_output': 'MOVE_FORWARD\nTURN_RIGHT\nMOVE_FORWARD\nMOVE_FORWARD\nTURN_LEFT\nMOVE_FORWARD\nMOVE_FORWARD', 'is_hidden': False}
            ],
            'xp_reward': 150,
            'hints': ['Turn right to step southward around the obstacle, then turn left to resume eastward movement.']
        },

        # Track 2: C++ OOP & STL
        {
            'track': track_objs['cpp-oop-stl-arena'],
            'level_number': 1,
            'title': 'Vector Ascending Sort',
            'slug': 'cpp-oop-stl-arena-1-vector-sort',
            'engine': 'CODE_JUDGE',
            'story_brief': 'Sort university student merit scores in ascending order using C++ STL `std::vector` and `<algorithm>`.',
            'instructions_markdown': 'Given N scores, populate a `std::vector<int>`, sort them using `std::sort()`, and print space-separated.',
            'starter_code_cpp': '#include <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nint main() {\n    int n;\n    if (!(cin >> n)) return 0;\n    vector<int> scores(n);\n    for (int i = 0; i < n; i++) cin >> scores[i];\n    sort(scores.begin(), scores.end());\n    for (int i = 0; i < n; i++) {\n        cout << scores[i] << (i == n - 1 ? "" : " ");\n    }\n    cout << endl;\n    return 0;\n}',
            'test_cases': [
                {'input': '5\n88 45 92 70 60', 'expected_output': '45 60 70 88 92', 'is_hidden': False},
                {'input': '4\n100 20 80 40', 'expected_output': '20 40 80 100', 'is_hidden': True}
            ],
            'xp_reward': 120,
            'hints': ['Include `<algorithm>` and call `sort(vec.begin(), vec.end())`.']
        },
        {
            'track': track_objs['cpp-oop-stl-arena'],
            'level_number': 2,
            'title': 'Student Class OOP Encapsulation',
            'slug': 'cpp-oop-stl-arena-2-student-oop',
            'engine': 'CODE_JUDGE',
            'story_brief': 'Create a `Student` class with attributes `name` and `id`, and a member function `display()`.',
            'instructions_markdown': 'Read string name and integer ID, instantiate a `Student` object, and call `display()` printing formatted output.',
            'starter_code_cpp': '#include <iostream>\n#include <string>\n\nusing namespace std;\n\nclass Student {\nprivate:\n    string name;\n    int id;\npublic:\n    Student(string n, int i) : name(n), id(i) {}\n    void display() {\n        cout << "ID: " << id << " | Name: " << name << endl;\n    }\n};\n\nint main() {\n    string name;\n    int id;\n    if (cin >> name >> id) {\n        Student s(name, id);\n        s.display();\n    }\n    return 0;\n}',
            'test_cases': [
                {'input': 'Sakib 1119003', 'expected_output': 'ID: 1119003 | Name: Sakib', 'is_hidden': False}
            ],
            'xp_reward': 140,
            'hints': ['Encapsulate variables in private scope and expose a public constructor.']
        },
        {
            'track': track_objs['cpp-oop-stl-arena'],
            'level_number': 3,
            'title': 'Frequency Map Counter',
            'slug': 'cpp-oop-stl-arena-3-frequency-map',
            'engine': 'CODE_JUDGE',
            'story_brief': 'Count the frequency of programming language selections using `std::map<string, int>`.',
            'instructions_markdown': 'Given N words, print the distinct words and their counts in alphabetical order.',
            'starter_code_cpp': '#include <iostream>\n#include <map>\n#include <string>\n\nusing namespace std;\n\nint main() {\n    int n;\n    if (!(cin >> n)) return 0;\n    map<string, int> freq;\n    for (int i = 0; i < n; i++) {\n        string lang;\n        cin >> lang;\n        freq[lang]++;\n    }\n    for (auto const& [key, val] : freq) {\n        cout << key << ": " << val << endl;\n    }\n    return 0;\n}',
            'test_cases': [
                {'input': '4\nC++ Python C++ JavaScript', 'expected_output': 'C++: 2\nJavaScript: 1\nPython: 1', 'is_hidden': False}
            ],
            'xp_reward': 160,
            'hints': ['`std::map` automatically sorts keys in ascending order.']
        },

        # Track 3: Python Logic & Automation
        {
            'track': track_objs['python-logic-automation'],
            'level_number': 1,
            'title': 'List Comprehension Evens Filter',
            'slug': 'python-logic-automation-1-list-comp',
            'engine': 'CODE_JUDGE',
            'story_brief': 'Filter out odd numbers from a telemetry stream using Python list comprehension.',
            'instructions_markdown': 'Read space-separated integers from stdin and print only the even numbers separated by spaces.',
            'starter_code_python': 'import sys\n\nline = sys.stdin.read().strip()\nif line:\n    nums = [int(x) for x in line.split()]\n    evens = [x for x in nums if x % 2 == 0]\n    print(*(evens))\n',
            'test_cases': [
                {'input': '1 2 3 4 5 6 7 8', 'expected_output': '2 4 6 8', 'is_hidden': False},
                {'input': '11 22 33 44', 'expected_output': '22 44', 'is_hidden': True}
            ],
            'xp_reward': 100,
            'hints': ['Use `[x for x in nums if x % 2 == 0]` and `print(*evens)`.']
        },
        {
            'track': track_objs['python-logic-automation'],
            'level_number': 2,
            'title': 'BAIUST Student ID Validator',
            'slug': 'python-logic-automation-2-id-validator',
            'engine': 'CODE_JUDGE',
            'story_brief': 'Validate if an input string is a valid 7-digit BAIUST Student ID starting with 111.',
            'instructions_markdown': 'Print "VALID" if the string has length 7, is all digits, and starts with "111", else "INVALID".',
            'starter_code_python': 'import sys\n\nsid = sys.stdin.read().strip()\nif len(sid) == 7 and sid.isdigit() and sid.startswith("111"):\n    print("VALID")\nelse:\n    print("INVALID")\n',
            'test_cases': [
                {'input': '1119003', 'expected_output': 'VALID', 'is_hidden': False},
                {'input': '1234567', 'expected_output': 'INVALID', 'is_hidden': False}
            ],
            'xp_reward': 110,
            'hints': ['Check `len(sid) == 7`, `sid.isdigit()`, and `sid.startswith("111")`.']
        },
        {
            'track': track_objs['python-logic-automation'],
            'level_number': 3,
            'title': 'Python Rover Diagonal Sweep',
            'slug': 'python-logic-automation-3-rover-diagonal',
            'engine': 'ROVER_MAZE',
            'story_brief': 'Navigate the rover in a zigzag stair pattern from (0,0) to target portal at (2,2).',
            'instructions_markdown': 'Output alternating forward and right/left moves to reach (2,2) dodging laser barriers.',
            'starter_code_python': 'moves = ["MOVE_FORWARD", "TURN_RIGHT", "MOVE_FORWARD", "TURN_LEFT", "MOVE_FORWARD", "TURN_RIGHT", "MOVE_FORWARD"]\nfor m in moves:\n    print(m)\n',
            'maze_grid_config': {
                'rows': 8, 'cols': 8,
                'start': {'x': 0, 'y': 0, 'dir': 'east'},
                'portal': {'x': 2, 'y': 2},
                'obstacles': [{'x': 1, 'y': 0}, {'x': 2, 'y': 1}],
                'gems': [{'x': 0, 'y': 1}, {'x': 1, 'y': 2}]
            },
            'test_cases': [
                {'input': '', 'expected_output': 'MOVE_FORWARD\nTURN_RIGHT\nMOVE_FORWARD\nTURN_LEFT\nMOVE_FORWARD\nTURN_RIGHT\nMOVE_FORWARD', 'is_hidden': False}
            ],
            'xp_reward': 150,
            'hints': ['Step forward, turn south, step forward, turn east to create a stair climb.']
        },

        # Track 4: JavaScript & DOM Manipulation
        {
            'track': track_objs['javascript-dom-manipulation'],
            'level_number': 1,
            'title': 'Cyber Drone Docking (Flexbox Alignment)',
            'slug': 'javascript-dom-manipulation-1-drone-docking-flexbox',
            'engine': 'DOM_BUILDER',
            'story_brief': 'Align the 3 Cyber Drones onto the target landing pads using CSS Flexbox rules.',
            'instructions_markdown': 'Set `justify-content` and `align-items` so the drones sit squarely on the pads.',
            'starter_code_javascript': 'justify-content: space-between;\nalign-items: center;\n',
            'dom_builder_config': {
                'type': 'FLEXBOX',
                'item_count': 3,
                'target_styles': {'justifyContent': 'space-between', 'alignItems': 'center'},
                'target_css': 'justify-content: space-between; align-items: center;'
            },
            'test_cases': [
                {'input': '', 'expected_output': 'justify-content: space-between;\nalign-items: center;', 'is_hidden': False}
            ],
            'xp_reward': 130,
            'hints': ['Use `justify-content: space-between;` and `align-items: center;`.']
        },
        {
            'track': track_objs['javascript-dom-manipulation'],
            'level_number': 2,
            'title': 'DOM Element Creation & ClassList',
            'slug': 'javascript-dom-manipulation-2-dom-create',
            'engine': 'CODE_JUDGE',
            'story_brief': 'Write JavaScript logic simulating dynamic badge generation on student profiles.',
            'instructions_markdown': 'Output a simulated DOM node string representing `<span class="badge active">DOM Explorer</span>`.',
            'starter_code_javascript': 'const tag = "span";\nconst className = "badge active";\nconst text = "DOM Explorer";\nconsole.log(`<${tag} class="${className}">${text}</${tag}>`);\n',
            'test_cases': [
                {'input': '', 'expected_output': '<span class="badge active">DOM Explorer</span>', 'is_hidden': False}
            ],
            'xp_reward': 120,
            'hints': ['Construct template literal with tag, class, and inner text.']
        },
        {
            'track': track_objs['javascript-dom-manipulation'],
            'level_number': 3,
            'title': 'Flex Column Center Stage',
            'slug': 'javascript-dom-manipulation-3-flex-column',
            'engine': 'DOM_BUILDER',
            'story_brief': 'Stack the Cyber Drones vertically in the center of the visual stage.',
            'instructions_markdown': 'Apply `flex-direction: column;` and center them horizontally and vertically.',
            'starter_code_javascript': 'flex-direction: column;\njustify-content: center;\nalign-items: center;\ngap: 1rem;\n',
            'dom_builder_config': {
                'type': 'FLEXBOX',
                'item_count': 3,
                'target_styles': {'flexDirection': 'column', 'justifyContent': 'center', 'alignItems': 'center'},
                'target_css': 'flex-direction: column; justify-content: center; align-items: center; gap: 1rem;'
            },
            'test_cases': [
                {'input': '', 'expected_output': 'flex-direction: column;\njustify-content: center;\nalign-items: center;', 'is_hidden': False}
            ],
            'xp_reward': 150,
            'hints': ['Change main axis with `flex-direction: column;` and center on both axes.']
        },

        # Track 5: PHP & MySQLi CRUD Mastery
        {
            'track': track_objs['php-mysqli-crud-mastery'],
            'level_number': 1,
            'title': 'Student Record Inserter (INSERT SQL)',
            'slug': 'php-mysqli-crud-mastery-1-student-record-inserter',
            'engine': 'CODE_JUDGE',
            'story_brief': 'Demonstrate procedural PHP MySQLi query preparation for inserting a student record.',
            'instructions_markdown': 'Formulate the prepared query string: `INSERT INTO students (id, name, dept) VALUES (1119003, "Sakib", "CSE");` and echo "SUCCESS_INSERT".',
            'starter_code_php': '<?php\n// CSE 324 Lab Evaluation iv - Prepared Insert\n$student_id = 1119003;\n$name = "Sakib";\n$dept = "CSE";\n\n// Simulate execution\necho "SUCCESS_INSERT";\n?>',
            'test_cases': [
                {'input': '', 'expected_output': 'SUCCESS_INSERT', 'is_hidden': False}
            ],
            'xp_reward': 140,
            'hints': ['Ensure the PHP opening tag `<?php` is included.']
        },
        {
            'track': track_objs['php-mysqli-crud-mastery'],
            'level_number': 2,
            'title': 'MySQLi Fetch Associative Array (SELECT)',
            'slug': 'php-mysqli-crud-mastery-2-fetch-assoc',
            'engine': 'CODE_JUDGE',
            'story_brief': 'Iterate through a simulated database result set using PHP associative arrays.',
            'instructions_markdown': 'Given an array representing student rows, loop through with `foreach` and print `ID: <id> - <name>`.',
            'starter_code_php': '<?php\n$rows = [\n    ["id" => "1119003", "name" => "Sakib"],\n    ["id" => "1119001", "name" => "Tanvir"]\n];\n\nforeach ($rows as $row) {\n    echo "ID: " . $row["id"] . " - " . $row["name"] . "\\n";\n}\n?>',
            'test_cases': [
                {'input': '', 'expected_output': 'ID: 1119003 - Sakib\nID: 1119001 - Tanvir', 'is_hidden': False}
            ],
            'xp_reward': 150,
            'hints': ['Access values with `$row["id"]` and `$row["name"]`.']
        },
        {
            'track': track_objs['php-mysqli-crud-mastery'],
            'level_number': 3,
            'title': 'Student Score Updater (UPDATE SQL)',
            'slug': 'php-mysqli-crud-mastery-3-update-score',
            'engine': 'CODE_JUDGE',
            'story_brief': 'Update student lab evaluation score using `UPDATE student_scores SET score = 100 WHERE student_id = ?`.',
            'instructions_markdown': 'Echo "SCORE_UPDATED: 100" to verify successful update query execution.',
            'starter_code_php': '<?php\n$score = 100;\n$sid = "1119003";\necho "SCORE_UPDATED: " . $score;\n?>',
            'test_cases': [
                {'input': '', 'expected_output': 'SCORE_UPDATED: 100', 'is_hidden': False}
            ],
            'xp_reward': 160,
            'hints': ['Bind parameter to the UPDATE statement in MySQLi.']
        },

        # Track 6: HTML5 & CSS3 Layout Games
        {
            'track': track_objs['html5-css3-layout-games'],
            'level_number': 1,
            'title': 'Flexbox Space-Around Stage',
            'slug': 'html5-css3-layout-games-1-space-around',
            'engine': 'DOM_BUILDER',
            'story_brief': 'Distribute the 3 Cyber Drones evenly across the visual pad container.',
            'instructions_markdown': 'Apply `justify-content: space-around;` to give equal spacing around each element.',
            'starter_code_javascript': 'justify-content: space-around;\nalign-items: center;\n',
            'dom_builder_config': {
                'type': 'FLEXBOX',
                'item_count': 3,
                'target_styles': {'justifyContent': 'space-around', 'alignItems': 'center'},
                'target_css': 'justify-content: space-around; align-items: center;'
            },
            'test_cases': [
                {'input': '', 'expected_output': 'justify-content: space-around;\nalign-items: center;', 'is_hidden': False}
            ],
            'xp_reward': 110,
            'hints': ['Use `justify-content: space-around;` to allocate half-size space on the outer edges.']
        },
        {
            'track': track_objs['html5-css3-layout-games'],
            'level_number': 2,
            'title': 'Semantic Table Structure in HTML5',
            'slug': 'html5-css3-layout-games-2-semantic-table',
            'engine': 'CODE_JUDGE',
            'story_brief': 'Construct a clean HTML5 table with `<thead>`, `<tbody>`, and `colspan="2"`.',
            'instructions_markdown': 'Output a semantic table row string `<th colspan="2">BAIUST CSE</th>`.',
            'starter_code_python': 'print(\'<th colspan="2">BAIUST CSE</th>\')\n',
            'test_cases': [
                {'input': '', 'expected_output': '<th colspan="2">BAIUST CSE</th>', 'is_hidden': False}
            ],
            'xp_reward': 100,
            'hints': ['Check `colspan="2"` casing and quotation.']
        },
        {
            'track': track_objs['html5-css3-layout-games'],
            'level_number': 3,
            'title': 'Flex End Ground Landing',
            'slug': 'html5-css3-layout-games-3-flex-end',
            'engine': 'DOM_BUILDER',
            'story_brief': 'Land the cyber drones onto the bottom right pads of the stage area.',
            'instructions_markdown': 'Align elements to the end of both main and cross axes using `justify-content: flex-end;` and `align-items: flex-end;`.',
            'starter_code_javascript': 'justify-content: flex-end;\nalign-items: flex-end;\n gap: 1rem;\n',
            'dom_builder_config': {
                'type': 'FLEXBOX',
                'item_count': 3,
                'target_styles': {'justifyContent': 'flex-end', 'alignItems': 'flex-end'},
                'target_css': 'justify-content: flex-end; align-items: flex-end; gap: 1rem;'
            },
            'test_cases': [
                {'input': '', 'expected_output': 'justify-content: flex-end;\nalign-items: flex-end;', 'is_hidden': False}
            ],
            'xp_reward': 130,
            'hints': ['Use `flex-end` for both justify-content and align-items.']
        },
    ]

    for ld in levels_data:
        lvl, created = ChallengeLevel.objects.update_or_create(
            slug=ld['slug'],
            defaults=ld
        )
    print("✅ 18 Playable Levels seeded across all 6 tracks.")

    # 6. Seed 15 Bug Blitz Quiz Questions
    QuizQuestion.objects.all().delete()
    quizzes = [
        {
            'category': 'PHP_MYSQL',
            'question_text': 'Which function is used in procedural PHP to establish a connection to a MySQL database?',
            'code_snippet': '$conn = ____________("localhost", "root", "", "codequest_db");',
            'option_a': 'mysql_open()',
            'option_b': 'mysqli_connect()',
            'option_c': 'pdo_connect()',
            'option_d': 'db_connect()',
            'correct_option': 'B',
            'explanation': 'In procedural PHP, mysqli_connect() creates a new MySQL connection. The older mysql_connect() has been completely removed in modern PHP.',
            'difficulty': 'Easy',
            'points': 20
        },
        {
            'category': 'PHP_MYSQL',
            'question_text': 'What function fetches a result row from a MySQLi query as an associative array?',
            'code_snippet': '$row = mysqli_fetch_assoc($result);',
            'option_a': 'mysqli_fetch_assoc()',
            'option_b': 'mysqli_get_row()',
            'option_c': 'mysqli_array()',
            'option_d': 'mysqli_fetch_all_assoc()',
            'correct_option': 'A',
            'explanation': 'mysqli_fetch_assoc() returns an associative array where keys correspond to column names.',
            'difficulty': 'Medium',
            'points': 20
        },
        {
            'category': 'HTML5',
            'question_text': 'What HTML5 table attribute causes a cell to span across multiple columns horizontally?',
            'code_snippet': '<td ________="2">Student Information</td>',
            'option_a': 'rowspan',
            'option_b': 'colspan',
            'option_c': 'span-col',
            'option_d': 'col-width',
            'correct_option': 'B',
            'explanation': 'colspan specifies the number of columns a cell should span, whereas rowspan spans vertically across rows.',
            'difficulty': 'Easy',
            'points': 15
        },
        {
            'category': 'CSS3',
            'question_text': 'In CSS Flexbox, which property aligns items along the cross axis (vertically in a row container)?',
            'code_snippet': '.container {\n  display: flex;\n  ________: center;\n}',
            'option_a': 'justify-content',
            'option_b': 'align-items',
            'option_c': 'flex-direction',
            'option_d': 'text-align',
            'correct_option': 'B',
            'explanation': 'justify-content aligns items along the main axis, while align-items aligns them along the cross axis.',
            'difficulty': 'Easy',
            'points': 15
        },
        {
            'category': 'JAVASCRIPT_DOM',
            'question_text': 'Which DOM method selects the first element matching a specified CSS selector string?',
            'code_snippet': 'const drone = document.________("#cyber-drone");',
            'option_a': 'getElementById()',
            'option_b': 'querySelector()',
            'option_c': 'getElementsByClassName()',
            'option_d': 'selectElement()',
            'correct_option': 'B',
            'explanation': 'document.querySelector() accepts standard CSS selector syntax (e.g. #id, .class) and returns the first matching Element node.',
            'difficulty': 'Easy',
            'points': 20
        },
        {
            'category': 'JAVASCRIPT_DOM',
            'question_text': 'How do you add a CSS class "active" to an element node in modern JavaScript?',
            'code_snippet': 'el.classList.________("active");',
            'option_a': 'add()',
            'option_b': 'append()',
            'option_c': 'push()',
            'option_d': 'insert()',
            'correct_option': 'A',
            'explanation': 'el.classList.add("active") is the standard API. el.classList also provides remove(), toggle(), and contains().',
            'difficulty': 'Easy',
            'points': 15
        },
        {
            'category': 'C_CPP',
            'question_text': 'What will be printed by this C pointer snippet?',
            'code_snippet': 'int x = 42;\nint *ptr = &x;\n*ptr = 99;\nprintf("%d", x);',
            'option_a': '42',
            'option_b': '99',
            'option_c': 'Garbage address value',
            'option_d': 'Compilation Error',
            'correct_option': 'B',
            'explanation': 'Dereferencing the pointer with `*ptr = 99` directly modifies the memory address of variable x.',
            'difficulty': 'Medium',
            'points': 25
        },
        {
            'category': 'C_CPP',
            'question_text': 'What is the output of this C loop with prefix increment?',
            'code_snippet': 'int count = 0;\nfor (int i = 0; i < 3; ++i) {\n    count += 2;\n}\nprintf("%d", count);',
            'option_a': '4',
            'option_b': '6',
            'option_c': '8',
            'option_d': '0',
            'correct_option': 'B',
            'explanation': 'The loop executes exactly 3 times (i=0, 1, 2). Count increments by 2 each time: 0 + 2 + 2 + 2 = 6.',
            'difficulty': 'Medium',
            'points': 20
        },
        {
            'category': 'PYTHON',
            'question_text': 'What is the result of evaluating this Python list comprehension?',
            'code_snippet': '[x ** 2 for x in [1, 2, 3] if x > 1]',
            'option_a': '[1, 4, 9]',
            'option_b': '[4, 9]',
            'option_c': '[2, 3]',
            'option_d': '[4]',
            'correct_option': 'B',
            'explanation': 'Only 2 and 3 satisfy the filter `if x > 1`. 2**2 is 4 and 3**2 is 9, yielding [4, 9].',
            'difficulty': 'Medium',
            'points': 20
        },
        {
            'category': 'PHP_MYSQL',
            'question_text': 'What SQL statement is used to modify existing records in a database table?',
            'code_snippet': '________ student_scores SET score = 95 WHERE student_id = "1119003";',
            'option_a': 'MODIFY',
            'option_b': 'UPDATE',
            'option_c': 'ALTER',
            'option_d': 'CHANGE',
            'correct_option': 'B',
            'explanation': 'UPDATE is used to modify data in existing rows. ALTER modifies table schema (columns/types).',
            'difficulty': 'Easy',
            'points': 15
        },
        {
            'category': 'HTML5',
            'question_text': 'Which semantic HTML5 element represents the primary, non-repeating content of a webpage document?',
            'code_snippet': '<________>\n  <h1>CodeQuest BD</h1>\n</________>',
            'option_a': '<section>',
            'option_b': '<main>',
            'option_c': '<article>',
            'option_d': '<div>',
            'correct_option': 'B',
            'explanation': '<main> is specifically reserved for the central topic of the document, excluding headers, footers, and sidebars.',
            'difficulty': 'Easy',
            'points': 15
        },
        {
            'category': 'CSS3',
            'question_text': 'Which CSS box-sizing value ensures that padding and borders are included within the specified element width?',
            'code_snippet': '* {\n  box-sizing: ________;\n}',
            'option_a': 'content-box',
            'option_b': 'border-box',
            'option_c': 'padding-box',
            'option_d': 'margin-box',
            'correct_option': 'B',
            'explanation': 'border-box includes padding and borders in total width and height calculations, eliminating unexpected sizing bugs.',
            'difficulty': 'Medium',
            'points': 20
        },
        {
            'category': 'JAVASCRIPT_DOM',
            'question_text': 'What method is used to register an event handler on a DOM button element?',
            'code_snippet': 'btn.________("click", (e) => { ... });',
            'option_a': 'attachEvent()',
            'option_b': 'addEventListener()',
            'option_c': 'on()',
            'option_d': 'registerListener()',
            'correct_option': 'B',
            'explanation': 'addEventListener() is the standard W3C method for attaching event listeners without overwriting existing handlers.',
            'difficulty': 'Easy',
            'points': 15
        },
        {
            'category': 'C_CPP',
            'question_text': 'In C++, which header file must be included to use the std::vector dynamic array container?',
            'code_snippet': '#include <________>\nstd::vector<int> numbers;',
            'option_a': 'array',
            'option_b': 'vector',
            'option_c': 'list',
            'option_d': 'stl_vector',
            'correct_option': 'B',
            'explanation': 'The C++ Standard Library header `<vector>` defines the `std::vector` template class.',
            'difficulty': 'Easy',
            'points': 15
        },
        {
            'category': 'PHP_MYSQL',
            'question_text': 'Which MySQLi function is used to prevent SQL injection by escaping special characters in a user-supplied string?',
            'code_snippet': '$clean_id = ________($conn, $_POST["student_id"]);',
            'option_a': 'mysqli_escape()',
            'option_b': 'mysqli_real_escape_string()',
            'option_c': 'mysqli_sanitize()',
            'option_d': 'htmlspecialchars()',
            'correct_option': 'B',
            'explanation': 'mysqli_real_escape_string() escapes special characters taking into account the current character set of the database connection.',
            'difficulty': 'Medium',
            'points': 20
        },
    ]

    for qd in quizzes:
        QuizQuestion.objects.create(**qd)
    print("✅ 15 Bug Blitz Questions seeded into Bug-Hunter Bank.")

    print("\n🎉 ALL CODEQUEST BD DATA SUCCESSFULLY SEEDED!")
    print("----------------------------------------------------------------")
    print("Student Name:    Md Najmus Sakib Rahatul (ID: 1119003)")
    print("Course:          CSE 324 Web Technologies Sessional")
    print("Superuser/Admin: sakib_admin / baiust1119003")
    print("Playable Levels: 18 levels across 6 tracks")
    print("Bug Blitz Bank:  15 exam-readiness questions")
    print("----------------------------------------------------------------")


if __name__ == '__main__':
    run_seed()
