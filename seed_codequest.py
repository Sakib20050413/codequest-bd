"""
CodeQuest 3D — Master Database Seeder
Seeds 6 Language Tracks, 10 Progressive 3D Rover Odyssey Levels, DOM Builder & Code Judge Levels,
15 Bug Blitz Questions, Campus Leaderboard Profiles, and sakib_admin superuser.
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
from arena.models import LanguageTrack, ChallengeLevel, QuizQuestion, LabAnnouncement


def run_seed():
    print("🚀 Initializing CodeQuest 3D Database Seeding...")

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
    profile.xp = 1950
    profile.level = 5
    profile.avatar = 'cyber_rover'
    profile.badges = [
        "First Blood (1st Solve)",
        "3D Rover Commander",
        "DOM Master",
        "PHP CRUD Ninja",
        "Polyglot Programmer (Solved in 4+ Languages)",
        "Blitz Champion",
        "Century Pioneer (1000+ XP)"
    ]
    profile.solved_levels = [
        '3d-rover-odyssey-1-linear-sequence',
        '3d-rover-odyssey-2-for-loops-repeat',
        '3d-rover-odyssey-3-while-loops-sensors',
        'javascript-dom-manipulation-1-drone-docking-flexbox',
        'php-mysqli-crud-mastery-1-student-record-inserter'
    ]
    profile.save()
    print(f"✅ Lead Student & Admin configured: sakib_admin / baiust1119003 (ID: {profile.student_id}, {profile.xp} XP)")

    # 2. Seed Classmates for Leaderboard
    classmates = [
        {
            'username': 'tanvir_cse', 'name': 'Tanvir Ahmed', 'id': '1119001',
            'section': 'CSE 3-2 Section A', 'xp': 1480, 'level': 4, 'avatar': 'syntax_ninja',
            'badges': ['First Blood (1st Solve)', '3D Rover Commander', 'Blitz Champion']
        },
        {
            'username': 'nusrat_jahan', 'name': 'Nusrat Jahan', 'id': '1119014',
            'section': 'CSE 3-2 Section A', 'xp': 1290, 'level': 4, 'avatar': 'code_wizard',
            'badges': ['First Blood (1st Solve)', 'Polyglot Programmer']
        },
        {
            'username': 'farhan_kabir', 'name': 'Farhan Kabir', 'id': '1119022',
            'section': 'CSE 3-2 Section B', 'xp': 980, 'level': 3, 'avatar': 'dom_knight',
            'badges': ['First Blood (1st Solve)', 'PHP CRUD Ninja']
        },
        {
            'username': 'sadia_afrin', 'name': 'Sadia Afrin', 'id': '1119035',
            'section': 'CSE 3-2 Section B', 'xp': 740, 'level': 3, 'avatar': 'scholar',
            'badges': ['First Blood (1st Solve)']
        },
        {
            'username': 'mehedi_hasan', 'name': 'Mehedi Hasan', 'id': '1119041',
            'section': 'CSE 3-2 Section A', 'xp': 510, 'level': 2, 'avatar': 'cyber_rover',
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
        title="CodeQuest 3D Three.js WebGL Engine Launched",
        message="Interact with real-time 3D Rover worlds, OrbitControls, and in-browser loop step execution.",
        badge="System Notice",
        is_active=True
    )
    LabAnnouncement.objects.create(
        title="CSE 324 Lab Evaluation 4 on PHP CRUD Scheduled",
        message="Review prepared MySQLi statements and table CRUD operations. Standalone module available under /php_sessional_crud/.",
        badge="PHP Evaluation",
        is_active=True
    )
    print("✅ Lab Announcements seeded.")

    # 4. Seed 6 Language Tracks
    tracks_data = [
        {
            'title': '3D Rover Odyssey (Algorithms & Logic)',
            'slug': '3d-rover-odyssey',
            'icon': '🚀',
            'difficulty': 'Beginner',
            'order': 1,
            'description': 'Real-time Three.js WebGL coding game. Write real loops in Python, JS, and C to navigate 3D rovers.'
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

    # 5. Seed 10 Progressive 3D Rover Odyssey Levels
    ChallengeLevel.objects.all().delete()

    levels_3d = [
        # Level 1: Sequences & Basic Movement
        {
            'track': track_objs['3d-rover-odyssey'],
            'level_number': 1,
            'title': 'Level 1: Linear Thrust (Sequences)',
            'slug': '3d-rover-odyssey-1-linear-sequence',
            'engine': 'ROVER_3D',
            'story_brief': 'The 3D Cyber Rover has touched down on Sector Alpha at coordinate (0,0). Drive straight east across the 3D tile bridge to reach the Warp Portal at (4,0).',
            'instructions_markdown': 'Call `rover.move_forward()` 4 times in sequence, or use a loop. Collect the crystal on the path and enter the warp portal.',
            'starter_code_python': '# Level 1: Linear Thrust\nfor i in range(4):\n    rover.move_forward()\n',
            'starter_code_javascript': '// Level 1: Linear Thrust\nfor (let i = 0; i < 4; i++) {\n    rover.moveForward();\n}\n',
            'starter_code_c': '// Level 1: Linear Thrust\nfor (int i = 0; i < 4; i++) {\n    move_forward();\n}\n',
            'maze_grid_config': {
                'cols': 8, 'rows': 8,
                'start': {'x': 0, 'z': 0, 'dir': 'east'},
                'portal': {'x': 4, 'z': 0},
                'obstacles': [{'x': 2, 'z': 1}, {'x': 3, 'z': 1}],
                'gems': [{'x': 2, 'z': 0}]
            },
            'xp_reward': 100,
            'hints': ['Use `for i in range(4): rover.move_forward()` to advance 4 tiles eastward.']
        },
        # Level 2: For Loops & Repeating Patterns
        {
            'track': track_objs['3d-rover-odyssey'],
            'level_number': 2,
            'title': 'Level 2: The Crystal Corridor (For Loops)',
            'slug': '3d-rover-odyssey-2-for-loops-repeat',
            'engine': 'ROVER_3D',
            'story_brief': 'Energy crystals are lined up along coordinate row Z=0. Traverse the corridor and harvest all 3 crystals before entering the extraction portal.',
            'instructions_markdown': 'Use a `for` loop to advance 5 tiles and collect each crystal along the way.',
            'starter_code_python': '# Level 2: Harvest all crystals\nfor i in range(5):\n    rover.move_forward()\n    rover.collect()\n',
            'starter_code_javascript': '// Level 2: Harvest all crystals\nfor (let i = 0; i < 5; i++) {\n    rover.moveForward();\n    rover.collect();\n}\n',
            'starter_code_c': 'for (int i = 0; i < 5; i++) {\n    move_forward();\n    collect();\n}\n',
            'maze_grid_config': {
                'cols': 8, 'rows': 8,
                'start': {'x': 0, 'z': 0, 'dir': 'east'},
                'portal': {'x': 5, 'z': 0},
                'obstacles': [{'x': 1, 'z': 1}, {'x': 3, 'z': 1}],
                'gems': [{'x': 1, 'z': 0}, {'x': 3, 'z': 0}, {'x': 4, 'z': 0}]
            },
            'xp_reward': 120,
            'hints': ['Collect is automatically triggered on stepping, or explicitly called with `rover.collect()`.']
        },
        # Level 3: While Loops & Dynamic Distance Sensors
        {
            'track': track_objs['3d-rover-odyssey'],
            'level_number': 3,
            'title': 'Level 3: Dynamic Distance Sensors (While Loops)',
            'slug': '3d-rover-odyssey-3-while-loops-sensors',
            'engine': 'ROVER_3D',
            'story_brief': 'The distance to the warp portal is unknown. Use the front sensor to stop exactly before the laser barrier, turn right, and reach the portal.',
            'instructions_markdown': 'Use `while rover.sensor_front() != "laser":` to drive forward dynamically, then turn right and advance.',
            'starter_code_python': '# Level 3: Dynamic Sensors with While Loop\nwhile rover.sensor_front() != "laser":\n    rover.move_forward()\n\nrover.turn_right()\nfor i in range(3):\n    rover.move_forward()\n',
            'starter_code_javascript': 'while (rover.sensorFront() !== "laser") {\n    rover.moveForward();\n}\nrover.turnRight();\nfor (let i = 0; i < 3; i++) {\n    rover.moveForward();\n}\n',
            'starter_code_c': 'while (sensor_front() != "laser") {\n    move_forward();\n}\nturn_right();\nfor(int i=0; i<3; i++) move_forward();\n',
            'maze_grid_config': {
                'cols': 8, 'rows': 8,
                'start': {'x': 0, 'z': 0, 'dir': 'east'},
                'portal': {'x': 4, 'z': 3},
                'obstacles': [{'x': 5, 'z': 0}],
                'gems': [{'x': 2, 'z': 0}, {'x': 4, 'z': 1}]
            },
            'xp_reward': 140,
            'hints': ['The front sensor returns "laser", "gem", "portal", or "clear".']
        },
        # Level 4: Conditionals & Hazard Avoidance
        {
            'track': track_objs['3d-rover-odyssey'],
            'level_number': 4,
            'title': 'Level 4: Hazard Avoidance (Conditionals)',
            'slug': '3d-rover-odyssey-4-conditionals-hazards',
            'engine': 'ROVER_3D',
            'story_brief': 'Pulsing laser hazards block the direct path. Use an `if/else` conditional or sensor check to bypass the laser barrier safely.',
            'instructions_markdown': 'Dodge around laser obstacles at (2,0) by navigating through row Z=1 and returning to the portal.',
            'starter_code_python': '# Level 4: Bypass Laser\nrover.move_forward()\nrover.turn_right()\nrover.move_forward()\nrover.turn_left()\nfor i in range(3):\n    rover.move_forward()\nrover.turn_left()\nrover.move_forward()\n',
            'starter_code_javascript': 'rover.moveForward();\nrover.turnRight();\nrover.moveForward();\nrover.turnLeft();\nfor(let i=0; i<3; i++) rover.moveForward();\nrover.turnLeft();\nrover.moveForward();\n',
            'starter_code_c': 'move_forward();\nturn_right();\nmove_forward();\nturn_left();\nfor(int i=0; i<3; i++) move_forward();\nturn_left();\nmove_forward();\n',
            'maze_grid_config': {
                'cols': 8, 'rows': 8,
                'start': {'x': 0, 'z': 0, 'dir': 'east'},
                'portal': {'x': 4, 'z': 0},
                'obstacles': [{'x': 2, 'z': 0}, {'x': 3, 'z': 0}],
                'gems': [{'x': 1, 'z': 1}, {'x': 3, 'z': 1}]
            },
            'xp_reward': 150,
            'hints': ['Step southward to row Z=1, drive eastward, then step northward to portal row Z=0.']
        },
        # Level 5: Functions & Modular Navigation
        {
            'track': track_objs['3d-rover-odyssey'],
            'level_number': 5,
            'title': 'Level 5: Modular Step Functions',
            'slug': '3d-rover-odyssey-5-modular-functions',
            'engine': 'ROVER_3D',
            'story_brief': 'Define a reusable helper function `stair_step()` to climb a 3D diagonal terrace of energy crystals.',
            'instructions_markdown': 'Define a function that moves forward and turns in a zigzag stair pattern.',
            'starter_code_python': 'def stair_step():\n    rover.move_forward()\n    rover.turn_right()\n    rover.move_forward()\n    rover.turn_left()\n\nfor i in range(3):\n    stair_step()\n',
            'starter_code_javascript': 'function stairStep() {\n    rover.moveForward();\n    rover.turnRight();\n    rover.moveForward();\n    rover.turnLeft();\n}\n\nfor (let i = 0; i < 3; i++) {\n    stairStep();\n}\n',
            'starter_code_c': 'for(int i=0; i<3; i++) {\n    move_forward();\n    turn_right();\n    move_forward();\n    turn_left();\n}\n',
            'maze_grid_config': {
                'cols': 8, 'rows': 8,
                'start': {'x': 0, 'z': 0, 'dir': 'east'},
                'portal': {'x': 3, 'z': 3},
                'obstacles': [{'x': 1, 'z': 0}, {'x': 2, 'z': 1}],
                'gems': [{'x': 0, 'z': 1}, {'x': 1, 'z': 2}, {'x': 2, 'z': 3}]
            },
            'xp_reward': 160,
            'hints': ['Functions encapsulate repetitive movement pairs.']
        },
        # Level 6: The Zigzag Trench
        {
            'track': track_objs['3d-rover-odyssey'],
            'level_number': 6,
            'title': 'Level 6: The Zigzag Trench',
            'slug': '3d-rover-odyssey-6-zigzag-trench',
            'engine': 'ROVER_3D',
            'story_brief': 'Laser barriers flank both sides of a narrow serpentine trench. Execute timed turns to maintain clearance.',
            'instructions_markdown': 'Navigate through the serpentine trench from (0,0) to (5,2) collecting 3 energy crystals.',
            'starter_code_python': '# Level 6: Serpentine Trench\nfor step in range(3):\n    for i in range(2):\n        rover.move_forward()\n    rover.turn_right()\n    rover.move_forward()\n    rover.turn_left()\n',
            'starter_code_javascript': 'for (let step = 0; step < 3; step++) {\n    rover.moveForward();\n    rover.moveForward();\n    rover.turnRight();\n    rover.moveForward();\n    rover.turnLeft();\n}\n',
            'starter_code_c': 'for(int s=0; s<3; s++) {\n    move_forward(); move_forward();\n    turn_right(); move_forward(); turn_left();\n}\n',
            'maze_grid_config': {
                'cols': 8, 'rows': 8,
                'start': {'x': 0, 'z': 0, 'dir': 'east'},
                'portal': {'x': 5, 'z': 2},
                'obstacles': [{'x': 0, 'z': 1}, {'x': 2, 'z': 0}, {'x': 3, 'z': 2}],
                'gems': [{'x': 1, 'z': 0}, {'x': 3, 'z': 1}, {'x': 4, 'z': 2}]
            },
            'xp_reward': 180,
            'hints': ['Use nested loops to traverse alternating straight and turn segments.']
        },
        # Level 7: The Chamber of Four Crystals
        {
            'track': track_objs['3d-rover-odyssey'],
            'level_number': 7,
            'title': 'Level 7: Chamber of Four Crystals',
            'slug': '3d-rover-odyssey-7-chamber-four-crystals',
            'engine': 'ROVER_3D',
            'story_brief': 'Four energy crystals are placed at the 4 cardinal compass corners around a central laser barrier.',
            'instructions_markdown': 'Sweep around the perimeter of the chamber in a full 360-degree loop and reach the portal.',
            'starter_code_python': '# Perimeter Sweep\nfor side in range(4):\n    for i in range(3):\n        rover.move_forward()\n    rover.turn_right()\nrover.move_forward()\n',
            'starter_code_javascript': 'for (let side = 0; side < 4; side++) {\n    for (let i = 0; i < 3; i++) rover.moveForward();\n    rover.turnRight();\n}\nrover.moveForward();\n',
            'starter_code_c': 'for(int s=0; s<4; s++) {\n    for(int i=0; i<3; i++) move_forward();\n    turn_right();\n}\nmove_forward();\n',
            'maze_grid_config': {
                'cols': 8, 'rows': 8,
                'start': {'x': 1, 'z': 1, 'dir': 'east'},
                'portal': {'x': 2, 'z': 1},
                'obstacles': [{'x': 2, 'z': 2}, {'x': 3, 'z': 2}],
                'gems': [{'x': 4, 'z': 1}, {'x': 4, 'z': 4}, {'x': 1, 'z': 4}, {'x': 1, 'z': 2}]
            },
            'xp_reward': 200,
            'hints': ['A 4-iteration loop with `turn_right()` creates a closed square perimeter scan.']
        },
        # Level 8: Precision Spiral
        {
            'track': track_objs['3d-rover-odyssey'],
            'level_number': 8,
            'title': 'Level 8: Precision Inward Spiral',
            'slug': '3d-rover-odyssey-8-precision-spiral',
            'engine': 'ROVER_3D',
            'story_brief': 'Spiral inwards toward the central warp portal at (3,3) while harvesting crystals along the inward radius.',
            'instructions_markdown': 'Drive with decreasing segment lengths: 5 steps, 4 steps, 3 steps, 2 steps, and 1 step.',
            'starter_code_python': '# Inward Spiral\nfor length in [5, 4, 3, 2, 1]:\n    for step in range(length):\n        rover.move_forward()\n    rover.turn_right()\n',
            'starter_code_javascript': 'const lengths = [5, 4, 3, 2, 1];\nfor (let len of lengths) {\n    for (let i = 0; i < len; i++) rover.moveForward();\n    rover.turnRight();\n}\n',
            'starter_code_c': 'int lens[5] = {5, 4, 3, 2, 1};\nfor(int l=0; l<5; l++) {\n    for(int i=0; i<lens[l]; i++) move_forward();\n    turn_right();\n}\n',
            'maze_grid_config': {
                'cols': 8, 'rows': 8,
                'start': {'x': 0, 'z': 0, 'dir': 'east'},
                'portal': {'x': 3, 'z': 3},
                'obstacles': [{'x': 1, 'z': 1}, {'x': 4, 'z': 2}],
                'gems': [{'x': 5, 'z': 0}, {'x': 5, 'z': 4}, {'x': 2, 'z': 4}, {'x': 2, 'z': 2}]
            },
            'xp_reward': 220,
            'hints': ['Use an array of step lengths: `[5, 4, 3, 2, 1]`.']
        },
        # Level 9: Dynamic Sensor Maze Solver
        {
            'track': track_objs['3d-rover-odyssey'],
            'level_number': 9,
            'title': 'Level 9: Wall-Follower Sensor Algorithm',
            'slug': '3d-rover-odyssey-9-wall-follower',
            'engine': 'ROVER_3D',
            'story_brief': 'The maze path contains multiple obstacles. Use continuous sensor checking to auto-navigate past obstacles until reaching the portal.',
            'instructions_markdown': 'Loop while not at portal: if front is blocked, turn right, else move forward.',
            'starter_code_python': '# Wall-Follower Algorithm\nwhile not rover.is_at_portal():\n    if rover.has_obstacle_ahead():\n        rover.turn_right()\n    else:\n        rover.move_forward()\n',
            'starter_code_javascript': 'while (!rover.isAtPortal()) {\n    if (rover.hasObstacleAhead()) {\n        rover.turnRight();\n    } else {\n        rover.moveForward();\n    }\n}\n',
            'starter_code_c': 'while (!is_at_portal()) {\n    if (detect_gem()) collect();\n    move_forward();\n}\n',
            'maze_grid_config': {
                'cols': 8, 'rows': 8,
                'start': {'x': 0, 'z': 0, 'dir': 'east'},
                'portal': {'x': 6, 'z': 4},
                'obstacles': [{'x': 3, 'z': 0}, {'x': 3, 'z': 1}, {'x': 5, 'z': 3}],
                'gems': [{'x': 2, 'z': 0}, {'x': 4, 'z': 2}, {'x': 6, 'z': 2}]
            },
            'xp_reward': 250,
            'hints': ['`rover.has_obstacle_ahead()` inspects the tile immediately in front.']
        },
        # Level 10: Grandmaster Labyrinth
        {
            'track': track_objs['3d-rover-odyssey'],
            'level_number': 10,
            'title': 'Level 10: Grandmaster 3D Labyrinth',
            'slug': '3d-rover-odyssey-10-grandmaster-labyrinth',
            'engine': 'ROVER_3D',
            'story_brief': 'The ultimate test for the BAIUST Grandmaster badge. Solve a multi-room 3D labyrinth, harvest all 5 power crystals, and unlock the final Warp Gateway.',
            'instructions_markdown': 'Synthesize loops, conditionals, and sensors to conquer the 8x8 Grandmaster maze.',
            'starter_code_python': '# Grandmaster Labyrinth Solution\nfor i in range(4):\n    rover.move_forward()\nrover.turn_right()\nfor i in range(5):\n    rover.move_forward()\nrover.turn_left()\nfor i in range(3):\n    rover.move_forward()\n',
            'starter_code_javascript': 'for (let i = 0; i < 4; i++) rover.moveForward();\nrover.turnRight();\nfor (let i = 0; i < 5; i++) rover.moveForward();\nrover.turnLeft();\nfor (let i = 0; i < 3; i++) rover.moveForward();\n',
            'starter_code_c': 'for(int i=0; i<4; i++) move_forward();\nturn_right();\nfor(int i=0; i<5; i++) move_forward();\nturn_left();\nfor(int i=0; i<3; i++) move_forward();\n',
            'maze_grid_config': {
                'cols': 8, 'rows': 8,
                'start': {'x': 0, 'z': 0, 'dir': 'east'},
                'portal': {'x': 7, 'z': 5},
                'obstacles': [{'x': 5, 'z': 0}, {'x': 2, 'z': 2}, {'x': 4, 'z': 3}, {'x': 6, 'z': 4}],
                'gems': [{'x': 2, 'z': 0}, {'x': 4, 'z': 1}, {'x': 4, 'z': 4}, {'x': 5, 'z': 5}, {'x': 6, 'z': 5}]
            },
            'xp_reward': 300,
            'hints': ['Map your route carefully through corridor checkpoints.']
        },
    ]

    for ld in levels_3d:
        ChallengeLevel.objects.update_or_create(slug=ld['slug'], defaults=ld)
    print("✅ 10 Progressive 3D Rover Odyssey Levels seeded.")

    # 6. Seed DOM Builder & Code Judge Levels for other tracks
    other_levels = [
        # JavaScript DOM
        {
            'track': track_objs['javascript-dom-manipulation'],
            'level_number': 1,
            'title': 'Drone Docking (Flexbox Alignment)',
            'slug': 'javascript-dom-manipulation-1-drone-docking-flexbox',
            'engine': 'DOM_BUILDER',
            'story_brief': 'Align the 3 Cyber Drones onto target landing pads using CSS Flexbox rules.',
            'instructions_markdown': 'Set `justify-content` and `align-items` so drones dock on target pads.',
            'starter_code_javascript': 'justify-content: space-between;\nalign-items: center;\n',
            'dom_builder_config': {
                'type': 'FLEXBOX',
                'item_count': 3,
                'target_styles': {'justifyContent': 'space-between', 'alignItems': 'center'},
                'target_css': 'justify-content: space-between; align-items: center;'
            },
            'test_cases': [{'input': '', 'expected_output': 'justify-content: space-between;\nalign-items: center;', 'is_hidden': False}],
            'xp_reward': 130,
            'hints': ['Use `justify-content: space-between;` and `align-items: center;`.']
        },
        # PHP & MySQLi CRUD
        {
            'track': track_objs['php-mysqli-crud-mastery'],
            'level_number': 1,
            'title': 'Student Record Inserter (INSERT SQL)',
            'slug': 'php-mysqli-crud-mastery-1-student-record-inserter',
            'engine': 'CODE_JUDGE',
            'story_brief': 'Demonstrate procedural PHP MySQLi query preparation for inserting a student record.',
            'instructions_markdown': 'Formulate the prepared query string: `INSERT INTO students (id, name, dept) VALUES (1119003, "Sakib", "CSE");` and echo "SUCCESS_INSERT".',
            'starter_code_php': '<?php\n// CSE 324 Lab Evaluation iv - Prepared Insert\n$student_id = 1119003;\n$name = "Sakib";\n$dept = "CSE";\n\necho "SUCCESS_INSERT";\n?>',
            'test_cases': [{'input': '', 'expected_output': 'SUCCESS_INSERT', 'is_hidden': False}],
            'xp_reward': 140,
            'hints': ['Include `<?php` tag and echo `SUCCESS_INSERT`.']
        },
        # C++ Vector Sort
        {
            'track': track_objs['cpp-oop-stl-arena'],
            'level_number': 1,
            'title': 'Vector Ascending Sort',
            'slug': 'cpp-oop-stl-arena-1-vector-sort',
            'engine': 'CODE_JUDGE',
            'story_brief': 'Sort university student merit scores in ascending order using C++ STL `std::vector` and `<algorithm>`.',
            'instructions_markdown': 'Given N scores, sort them using `std::sort()` and print space-separated.',
            'starter_code_cpp': '#include <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nint main() {\n    int n;\n    if (!(cin >> n)) return 0;\n    vector<int> scores(n);\n    for (int i = 0; i < n; i++) cin >> scores[i];\n    sort(scores.begin(), scores.end());\n    for (int i = 0; i < n; i++) cout << scores[i] << (i == n - 1 ? "" : " ");\n    cout << endl;\n    return 0;\n}',
            'test_cases': [{'input': '5\n88 45 92 70 60', 'expected_output': '45 60 70 88 92', 'is_hidden': False}],
            'xp_reward': 120,
            'hints': ['Use `sort(scores.begin(), scores.end())`.']
        },
    ]

    for ol in other_levels:
        ChallengeLevel.objects.update_or_create(slug=ol['slug'], defaults=ol)
    print("✅ Supplementary DOM Builder and Code Judge levels seeded.")

    # 7. Seed 15 Bug Blitz Quiz Questions
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
            'explanation': 'In procedural PHP, mysqli_connect() creates a new MySQL connection.',
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
            'explanation': 'mysqli_fetch_assoc() returns an associative array matching column names.',
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
            'explanation': 'colspan specifies the number of columns a cell should span horizontally.',
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
            'explanation': 'align-items aligns items along the cross axis in Flexbox.',
            'difficulty': 'Easy',
            'points': 15
        },
        {
            'category': 'JAVASCRIPT_DOM',
            'question_text': 'Which DOM method selects the first element matching a specified CSS selector string?',
            'code_snippet': 'const rover = document.________("#cyber-rover");',
            'option_a': 'getElementById()',
            'option_b': 'querySelector()',
            'option_c': 'getElementsByClassName()',
            'option_d': 'selectElement()',
            'correct_option': 'B',
            'explanation': 'document.querySelector() accepts CSS selector strings and returns the first matching element.',
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
            'explanation': 'el.classList.add("active") is the standard method for adding a class.',
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
            'explanation': 'Dereferencing the pointer modifies the memory address of x directly.',
            'difficulty': 'Medium',
            'points': 25
        },
        {
            'category': 'PYTHON',
            'question_text': 'What is the output of evaluating this Python list comprehension?',
            'code_snippet': '[x ** 2 for x in [1, 2, 3] if x > 1]',
            'option_a': '[1, 4, 9]',
            'option_b': '[4, 9]',
            'option_c': '[2, 3]',
            'option_d': '[4]',
            'correct_option': 'B',
            'explanation': 'Only 2 and 3 are > 1; their squares are 4 and 9.',
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
            'explanation': 'UPDATE modifies data in existing rows of a database table.',
            'difficulty': 'Easy',
            'points': 15
        },
        {
            'category': 'HTML5',
            'question_text': 'Which semantic HTML5 element represents the primary, non-repeating content of a webpage document?',
            'code_snippet': '<________>\n  <h1>CodeQuest 3D</h1>\n</________>',
            'option_a': '<section>',
            'option_b': '<main>',
            'option_c': '<article>',
            'option_d': '<div>',
            'correct_option': 'B',
            'explanation': '<main> is specifically designated for the primary content of a document.',
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
            'explanation': 'border-box includes padding and border in width calculations.',
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
            'explanation': 'addEventListener() is the standard W3C method for event registration.',
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
            'explanation': '<vector> defines the std::vector class template.',
            'difficulty': 'Easy',
            'points': 15
        },
        {
            'category': 'PHP_MYSQL',
            'question_text': 'Which MySQLi function escapes special characters in a string for use in an SQL query?',
            'code_snippet': '$clean_id = ________($conn, $_POST["student_id"]);',
            'option_a': 'mysqli_escape()',
            'option_b': 'mysqli_real_escape_string()',
            'option_c': 'mysqli_sanitize()',
            'option_d': 'htmlspecialchars()',
            'correct_option': 'B',
            'explanation': 'mysqli_real_escape_string() escapes special characters for safe SQL execution.',
            'difficulty': 'Medium',
            'points': 20
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
            'explanation': 'The loop runs 3 times; 0 + 2 + 2 + 2 = 6.',
            'difficulty': 'Medium',
            'points': 20
        },
    ]

    for qd in quizzes:
        QuizQuestion.objects.create(**qd)
    print("✅ 15 Bug Blitz Questions seeded into Bug-Hunter Bank.")

    print("\n🎉 ALL CODEQUEST 3D DATA SUCCESSFULLY SEEDED!")
    print("----------------------------------------------------------------")
    print("Student Name:    Md Najmus Sakib Rahatul (ID: 1119003)")
    print("Course:          CSE 324 Web Technologies Sessional")
    print("Superuser/Admin: sakib_admin / baiust1119003")
    print("3D Rover Levels: 10 Progressive 3D WebGL Mazes")
    print("Bug Blitz Bank:  15 exam-readiness questions")
    print("----------------------------------------------------------------")


if __name__ == '__main__':
    run_seed()
