import os
import json
import django

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    django.setup()


def seed_all():
    from django.contrib.auth.models import User
    from learn.models import (
        Language,
        Course,
        Lesson,
        CodingGame,
        PracticeTask,
        UserProfile,
        Submission,
    )

    # 1. Admin & Demo Student Accounts
    admin_user, _ = User.objects.get_or_create(
        username="sakib_admin",
        defaults={"email": "mdnajmussakib2003@gmail.com", "is_staff": True, "is_superuser": True},
    )
    admin_user.set_password("baiust1119003")
    admin_user.is_staff = True
    admin_user.is_superuser = True
    admin_user.save()
    UserProfile.objects.get_or_create(
        user=admin_user,
        defaults={
            "student_id": "1119003",
            "department": "Department of CSE, BAIUST (Level 3, Term 2, Section A)",
            "xp": 1450,
            "streak_days": 9,
            "rank_title": "Lead Full-Stack & LMS Architect",
        },
    )

    student_user, _ = User.objects.get_or_create(
        username="student_demo",
        defaults={"email": "student@baiust.ac.bd", "is_staff": False},
    )
    student_user.set_password("cse324pass")
    student_user.save()
    UserProfile.objects.get_or_create(
        user=student_user,
        defaults={
            "student_id": "1119026",
            "department": "Department of CSE, BAIUST (Level 3, Term 2)",
            "xp": 680,
            "streak_days": 5,
            "rank_title": "Active Problem Solver",
        },
    )

    # 2. 12 Core Languages & Stacks across 4 Pillars
    if Language.objects.count() == 0:
        curriculum_data = [
            {
                "slug": "html5",
                "name": "HTML5 Semantic & Tables",
                "code": "HTML5",
                "pillar": "FRONTEND",
                "runtime": "Sandboxed DOM Preview",
                "summary": "Semantic landmarks (<header>, <nav>, <main>), accessible forms, and table cell merging (rowspan & colspan).",
                "course_title": "HTML5 Document Structure, Forms & Table Architecture",
                "module_title": "Module 1: Semantic Landmarks & Table Spanning",
                "lesson_title": "1.1 Mastering Table Rowspan, Colspan & Semantic Tags",
                "concept": (
                    "HTML5 defines the structural skeleton of a webpage using semantic tags (<header>, <nav>, <main>, <section>, <footer>) "
                    "instead of generic <div> soup. In academic and financial tables, rowspan='N' merges cells vertically across N rows, "
                    "while colspan='M' merges cells horizontally across M columns."
                ),
                "anatomy": (
                    "Line 1 | <table class='result-table'> | Initializes a structured 2D table grid\n"
                    "Line 3 | <td rowspan='3'>CSE</td> | Merges the Department cell vertically across 3 student rows\n"
                    "Line 8 | <td colspan='2'>Average: 165</td> | Merges 2 columns horizontally in the summary footer row"
                ),
                "tips": (
                    "Exam & Viva Tip (CSE 324 Slide 21 & 28): When you put rowspan='3' in the first <tr>, do NOT write that <td> again in the next 2 rows—otherwise the columns will shift to the right!"
                ),
                "trace": "DOM Parser reads <table> -> allocates 3 row nodes -> binds rowspan='3' cell to rows [0..2], col [0] -> aligns summary colspan='2' across cols [1..2].",
                "game_key": "FLEX_BRIDGE",
                "game_prompt": "Write complete HTML5 table markup using both rowspan=\"2\" and colspan=\"2\" so the bridge blueprint aligns across the river canyon.",
                "starter": "<table border=\"1\">\n  <tr>\n    <td rowspan=\"2\">CSE Dept</td>\n    <td colspan=\"2\">Semester Scores</td>\n  </tr>\n  <tr>\n    <td>Mid: 85</td>\n    <td>Final: 90</td>\n  </tr>\n</table>",
                "solution": "<table border=\"1\">\n  <tr>\n    <td rowspan=\"2\">CSE Dept</td>\n    <td colspan=\"2\">Semester Scores</td>\n  </tr>\n  <tr>\n    <td>Mid: 85</td>\n    <td>Final: 90</td>\n  </tr>\n</table>",
                "judge_prompt": "Ensure your HTML code contains a valid <table>, at least one rowspan attribute, and at least one colspan attribute.",
                "hint": "Keep both rowspan=\"2\" and colspan=\"2\" inside your <td> tags."
            },
            {
                "slug": "css3",
                "name": "CSS3 Box Model, Flexbox & RWD",
                "code": "CSS3",
                "pillar": "FRONTEND",
                "runtime": "Live CSS Layout Engine",
                "summary": "Universal box-sizing: border-box, 1D Flexbox alignment, 2D CSS Grid, and 4-breakpoint responsive media queries.",
                "course_title": "CSS3 Box Model, Flexbox Alignment & Responsive Design",
                "module_title": "Module 1: Flexbox Axis Control & Responsive Breakpoints",
                "lesson_title": "1.1 Parent-Child Flexbox Alignment & Media Queries",
                "concept": (
                    "Setting display: flex on a parent container turns its direct children into flex items along the Main Axis (horizontal for row) "
                    "and Cross Axis (vertical). Use justify-content to space items along the Main Axis and align-items to center them on the Cross Axis."
                ),
                "anatomy": (
                    "Line 1 | * { box-sizing: border-box; } | Includes padding & border inside declared width (200px stays 200px)\n"
                    "Line 3 | display: flex; justify-content: space-between; | Pushes logo left and nav links right\n"
                    "Line 6 | @media (max-width: 768px) { flex-direction: column; } | Stacks items vertically on mobile/tablet screens"
                ),
                "tips": (
                    "Exam & Viva Tip (Slide 18–24): Use flex: 1 0 250px on cards so they share space equally and wrap cleanly without media queries, and use order: -1 to move any card to the front visually!"
                ),
                "trace": "CSSOM computes parent .bridge-stage -> sets Main Axis = row -> distributes 3 bridge planks with space-between -> locks Y-axis center.",
                "game_key": "FLEX_BRIDGE",
                "game_prompt": "Write the complete CSS rule for .bridge-stage using display: flex, justify-content: space-between, and align-items: center to lock the bridge planks across the river.",
                "starter": ".bridge-stage {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n  gap: 16px;\n}",
                "solution": ".bridge-stage {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n  gap: 16px;\n}",
                "judge_prompt": "Verify that your CSS includes display: flex, justify-content: space-between, and align-items: center.",
                "hint": "Write display: flex; justify-content: space-between; align-items: center; inside .bridge-stage."
            },
            {
                "slug": "javascript",
                "name": "JavaScript ES6+ & DOM Model",
                "code": "JS",
                "pillar": "FRONTEND",
                "runtime": "Browser JS & DOM Sandbox",
                "summary": "Live DOM selection (querySelector), event listeners, dynamic node creation (createElement), and ES6+ array methods.",
                "course_title": "JavaScript ES6+ & Interactive DOM Manipulation",
                "module_title": "Module 1: DOM Tree Selection, Events & Class Toggling",
                "lesson_title": "1.1 Selecting Elements & Wiring Event Listeners",
                "concept": (
                    "The Document Object Model (DOM) represents HTML as a live tree of nodes in memory. JavaScript uses "
                    "document.querySelector() to locate any element, classList.add()/toggle() to update its visual state, and addEventListener() to react to user input."
                ),
                "anatomy": (
                    "Line 1 | const gate = document.querySelector('#circuit-gate'); | Selects the DOM element with id='circuit-gate'\n"
                    "Line 2 | gate.classList.add('powered'); | Attaches the .powered CSS state class immediately\n"
                    "Line 3 | for (let i = 0; i < 4; i++) { pulseNode(i); } | Iterates 4 times to energize all circuit nodes"
                ),
                "tips": (
                    "CSE 324 Evaluation (iii) Tip: Always check if an input value is empty (input.value.trim() === '') before calling document.createElement('li') and list.appendChild(li)."
                ),
                "trace": "Call Stack pushes main() -> Heap resolves #circuit-gate DOM reference (0x7f8a10) -> mutates classList -> runs 4 loop iterations.",
                "game_key": "DOM_CIRCUIT",
                "game_prompt": "Write real JavaScript DOM code using document.querySelector('#circuit-gate').classList.add('powered') and a loop to energize the 4 circuit nodes.",
                "starter": "const gate = document.querySelector('#circuit-gate');\ngate.classList.add('powered');\nfor (let i = 0; i < 4; i++) {\n  pulseNode(i);\n}",
                "solution": "const gate = document.querySelector('#circuit-gate');\ngate.classList.add('powered');\nfor (let i = 0; i < 4; i++) {\n  pulseNode(i);\n}",
                "judge_prompt": "Ensure your script calls document.querySelector, classList.add, and runs a 4-step loop.",
                "hint": "Keep document.querySelector('#circuit-gate') and the for loop from 0 to 3."
            },
            {
                "slug": "react",
                "name": "React Components & State",
                "code": "REACT",
                "pillar": "FRONTEND",
                "runtime": "JSX & State Simulator",
                "summary": "Declarative UI components, props, unidirectional data flow, and reactive state hooks (useState, useEffect).",
                "course_title": "React Frontend Architecture & Reactive State",
                "module_title": "Module 1: Functional Components & useState Hook",
                "lesson_title": "1.1 Managing Interactive UI State with useState",
                "concept": (
                    "Instead of manually mutating DOM nodes, React declares UI as a function of state: UI = f(state). "
                    "Calling setCount(count + 1) schedules a fast Virtual DOM diff and updates only the changed elements."
                ),
                "anatomy": (
                    "Line 1 | const [power, setPower] = useState(0); | Declares reactive state variable initialized to 0\n"
                    "Line 2 | setPower(prev => prev + 25); | Safely increments power level using functional state update\n"
                    "Line 3 | return <div className='meter'>{power}%</div>; | Renders current state declaratively"
                ),
                "tips": "Never mutate React state directly (e.g. power = 100); always invoke the setter function returned by useState.",
                "trace": "Component mount -> Fiber allocates hook cell [state=0] -> dispatch setPower(100) -> re-render diffs Virtual DOM.",
                "game_key": "DOM_CIRCUIT",
                "game_prompt": "Write the state update logic to charge all 4 reactor cells to 100%.",
                "starter": "let power = 0;\nfor (let cell = 1; cell <= 4; cell++) {\n  power += 25;\n  pulseNode(cell - 1);\n}",
                "solution": "let power = 0;\nfor (let cell = 1; cell <= 4; cell++) {\n  power += 25;\n  pulseNode(cell - 1);\n}",
                "judge_prompt": "Ensure your loop charges power to 100 across 4 steps.",
                "hint": "Loop 4 times, adding 25 to power on each step."
            },
            {
                "slug": "python",
                "name": "Python 3 Core & Algorithms",
                "code": "PY",
                "pillar": "BACKEND",
                "runtime": "Pyodide WebAssembly",
                "summary": "Clean algorithmic loops, functions, recursion, list comprehensions, and data structures running in-browser via WebAssembly.",
                "course_title": "Python 3 Programming, Recursion & Algorithmic Problem Solving",
                "module_title": "Module 1: Deterministic Loops & Recursive Tree Growth",
                "lesson_title": "1.1 Loops, Functions & Organic 3D Fractal Tree Generation",
                "concept": (
                    "Python uses indentation to define code blocks and range(start, stop) to generate deterministic sequences. "
                    "When combined with functions and loops, a few lines of Python can model complex natural structures like branching trees."
                ),
                "anatomy": (
                    "Line 1 | def grow_canopy(levels, angle): | Defines a reusable Python function with 2 parameters\n"
                    "Line 2 |     for depth in range(1, levels + 1): | Iterates from depth 1 up to levels (inclusive)\n"
                    "Line 3 |         grow_branch(depth, angle) | Expands the 3D fractal tree canopy at each depth level"
                ),
                "tips": "Remember that range(1, 7) produces 1, 2, 3, 4, 5, 6 (the stop value 7 is excluded).",
                "trace": "Stack frame [grow_canopy: levels=6, angle=26] -> range iterator yields depth=1..6 -> renders 64 3D branches.",
                "game_key": "FRACTAL_TREE",
                "game_prompt": "Write a complete Python function grow_canopy(levels, angle) with a for loop over range(1, levels + 1) to grow all 6 levels of the 3D Fractal Tree!",
                "starter": "def grow_canopy(levels, angle):\n    for depth in range(1, levels + 1):\n        grow_branch(depth, angle)\n    bloom_leaves()\n\ngrow_canopy(6, 26)",
                "solution": "def grow_canopy(levels, angle):\n    for depth in range(1, levels + 1):\n        grow_branch(depth, angle)\n    bloom_leaves()\n\ngrow_canopy(6, 26)",
                "judge_prompt": "Verify that grow_canopy(6, 26) defines a function, uses a for loop with range(), and calls grow_branch.",
                "hint": "Keep def grow_canopy(levels, angle): and the for depth in range(1, levels + 1): loop."
            },
            {
                "slug": "django",
                "name": "Django 5 Full-Stack & ORM",
                "code": "DJ",
                "pillar": "BACKEND",
                "runtime": "Django ORM & MVT Verifier",
                "summary": "Model-View-Template (MVT) architecture, ORM querysets, authentication, CSRF security, and REST JSON endpoints.",
                "course_title": "Django 5 Full-Stack Web Engineering & Relational ORM",
                "module_title": "Module 1: Models, Views & QuerySet Filtering",
                "lesson_title": "1.1 Querying Database Models with filter() & order_by()",
                "concept": (
                    "Django's Object-Relational Mapper (ORM) lets you query SQLite and PostgreSQL databases using Python classes "
                    "instead of raw SQL strings, automatically protecting against SQL injection via parameterized queries."
                ),
                "anatomy": (
                    "Line 1 | top_students = Student.objects.filter(dept='CSE', cgpa__gte=3.5) | Filters CSE students with CGPA >= 3.5\n"
                    "Line 2 |     .order_by('-cgpa')[:5] | Sorts descending by CGPA and slices top 5 records\n"
                    "Line 3 | return JsonResponse({'count': len(top_students)}) | Serializes result as a JSON HTTP response"
                ),
                "tips": "Use field__gte for >=, field__lte for <=, and field__icontains for case-insensitive search in Django ORM.",
                "trace": "ORM AST compiles .filter(dept='CSE') -> SELECT * FROM students WHERE dept='CSE' AND cgpa >= 3.5 ORDER BY cgpa DESC LIMIT 5.",
                "game_key": "SQL_DETECTIVE",
                "game_prompt": "Write the Django ORM query using Student.objects.filter(dept='CSE') and .order_by('-cgpa') to retrieve the verified honor-roll records.",
                "starter": "records = Student.objects.filter(dept='CSE', cgpa__gte=3.50).order_by('-cgpa')\nverify_orm_records(records)",
                "solution": "records = Student.objects.filter(dept='CSE', cgpa__gte=3.50).order_by('-cgpa')\nverify_orm_records(records)",
                "judge_prompt": "Ensure your code uses .objects.filter() and .order_by().",
                "hint": "Chain .filter(dept='CSE', cgpa__gte=3.50) with .order_by('-cgpa')."
            },
            {
                "slug": "php-crud",
                "name": "PHP 8 & MySQLi CRUD",
                "code": "PHP",
                "pillar": "BACKEND",
                "runtime": "PHP & MySQLi Simulator",
                "summary": "Server-side form handling ($_POST, $_GET) and the 4 core MySQLi CRUD operations (INSERT, SELECT, UPDATE, DELETE).",
                "course_title": "PHP 8 & MySQLi Database CRUD Operations (CSE 324 Sessional)",
                "module_title": "Module 1: Complete MySQLi Connection & CRUD Lifecycle",
                "lesson_title": "1.1 Executing INSERT, SELECT, UPDATE & DELETE in PHP",
                "concept": (
                    "In procedural PHP + MySQLi, mysqli_connect() opens the database socket, and mysqli_query($conn, $sql) executes "
                    "CREATE (INSERT INTO), READ (SELECT), UPDATE (UPDATE ... SET), and DELETE (DELETE FROM) statements."
                ),
                "anatomy": (
                    "Line 1 | $conn = mysqli_connect('localhost', 'root', '', 'baiust_db'); | Connects to MySQL server\n"
                    "Line 2 | $sql = \"INSERT INTO students (id, name, dept) VALUES (1119003, 'Sakib', 'CSE')\"; | Prepares SQL INSERT\n"
                    "Line 3 | mysqli_query($conn, $sql); | Executes the query against the active connection"
                ),
                "tips": (
                    "20-Mark Handwritten Quiz Tip: Memorize the 3 functions: mysqli_connect(), mysqli_query($conn, $sql), and mysqli_fetch_assoc($result)!"
                ),
                "trace": "PHP Zend Engine opens socket 3306 -> dispatches INSERT tuple (1119003, 'Sakib', 'CSE') -> commits transaction in Data Vault.",
                "game_key": "PHP_VAULT",
                "game_prompt": "Write a complete PHP script using mysqli_connect() and mysqli_query() with INSERT INTO and SELECT to populate the Server Data-Vault.",
                "starter": "<?php\n$conn = mysqli_connect(\"localhost\", \"root\", \"\", \"baiust_db\");\n$sql = \"INSERT INTO students (id, name, dept) VALUES (1119003, 'Sakib', 'CSE')\";\nmysqli_query($conn, $sql);\n$res = mysqli_query($conn, \"SELECT * FROM students WHERE dept='CSE'\");\n?>",
                "solution": "<?php\n$conn = mysqli_connect(\"localhost\", \"root\", \"\", \"baiust_db\");\n$sql = \"INSERT INTO students (id, name, dept) VALUES (1119003, 'Sakib', 'CSE')\";\nmysqli_query($conn, $sql);\n$res = mysqli_query($conn, \"SELECT * FROM students WHERE dept='CSE'\");\n?>",
                "judge_prompt": "Verify that your PHP script calls mysqli_connect, mysqli_query, INSERT INTO, and SELECT.",
                "hint": "Keep mysqli_connect and both mysqli_query calls."
            },
            {
                "slug": "sql",
                "name": "SQL (SQLite & PostgreSQL)",
                "code": "SQL",
                "pillar": "DATABASE",
                "runtime": "sql.js In-Browser Engine",
                "summary": "Relational schemas, SELECT filtering, INNER/LEFT JOINs, GROUP BY aggregations, and ACID transactions.",
                "course_title": "SQL & Relational Database Query Engineering",
                "module_title": "Module 1: Relational Filtering, Joins & Aggregations",
                "lesson_title": "1.1 Investigating Relational Tables with SELECT, WHERE & JOIN",
                "concept": (
                    "SQL is a declarative language: you specify the exact columns and filtering predicates you want (`SELECT ... FROM ... WHERE ... ORDER BY`), "
                    "and the relational query planner computes the result set."
                ),
                "anatomy": (
                    "Line 1 | SELECT id, name, dept, clearance_level | Projects specific columns from the table\n"
                    "Line 2 | FROM suspects WHERE dept = 'CyberSec' AND clearance_level >= 4 | Filters rows matching both conditions\n"
                    "Line 3 | ORDER BY clearance_level DESC; | Sorts matching records from highest to lowest clearance"
                ),
                "tips": "Always place WHERE before GROUP BY, HAVING after GROUP BY, and ORDER BY at the very end of your query.",
                "trace": "Query Planner scans relation `suspects` (6 rows) -> applies predicate (dept='CyberSec' AND clearance>=4) -> returns 2 matching tuples.",
                "game_key": "SQL_DETECTIVE",
                "game_prompt": "Write a complete SQL query using SELECT, FROM suspects, WHERE, and ORDER BY to identify the high-clearance suspect in the Crime Lab.",
                "starter": "SELECT id, name, role, access_Time\nFROM suspects\nWHERE clearance >= 4 AND zone = 'ServerVault'\nORDER BY access_time DESC;",
                "solution": "SELECT id, name, role, access_Time\nFROM suspects\nWHERE clearance >= 4 AND zone = 'ServerVault'\nORDER BY access_time DESC;",
                "judge_prompt": "Ensure your SQL query contains SELECT, FROM suspects, WHERE, and ORDER BY.",
                "hint": "Keep SELECT, FROM suspects, WHERE clearance >= 4, and ORDER BY."
            },
            {
                "slug": "mongodb",
                "name": "MongoDB & Document NoSQL",
                "code": "MONGO",
                "pillar": "DATABASE",
                "runtime": "JSON Document Query Engine",
                "summary": "Flexible JSON/BSON document schemas, find() filter operators ($gt, $in), and aggregation pipelines.",
                "course_title": "MongoDB NoSQL Document Modeling & Query Pipelines",
                "module_title": "Module 1: Document Filtering & Comparison Operators",
                "lesson_title": "1.1 Querying Nested JSON Documents with db.collection.find()",
                "concept": (
                    "MongoDB stores data as flexible BSON documents instead of rigid rows. You query collections by passing a JSON filter object "
                    "such as db.Logs.find({ status: 'ACTIVE', latency_ms: { $lt: 50 } })."
                ),
                "anatomy": (
                    "Line 1 | db.sensor_nodes.find({ | Targets the sensor_nodes document collection\n"
                    "Line 2 |   zone: 'Cumilla-Grid', battery: { $gte: 80 } | Matches documents with battery >= 80%\n"
                    "Line 3 | }).sort({ battery: -1 }) | Sorts matching JSON documents descending"
                ),
                "tips": "In MongoDB, 1 means ascending sort and -1 means descending sort inside .sort({ field: -1 }).",
                "trace": "BSON Index scan on `sensor_nodes` -> matches 3 JSON documents -> projects fields to Data Vault.",
                "game_key": "SQL_DETECTIVE",
                "game_prompt": "Write the MongoDB find() query with a comparison operator ($gte) and .sort() to filter active telemetry documents.",
                "starter": "db.sensor_nodes.find({\n  status: \"ONLINE\",\n  battery: { $gte: 80 }\n}).sort({ battery: -1 });",
                "solution": "db.sensor_nodes.find({\n  status: \"ONLINE\",\n  battery: { $gte: 80 }\n}).sort({ battery: -1 });",
                "judge_prompt": "Ensure your query uses .find( and $gte.",
                "hint": "Keep db.sensor_nodes.find({ status: \"ONLINE\", battery: { $gte: 80 } })."
            },
            {
                "slug": "c-lang",
                "name": "C Programming & Pointers",
                "code": "C",
                "pillar": "SYSTEMS",
                "runtime": "C AST & Stack Visualizer",
                "summary": "Deterministic loops, arrays, memory addresses (&x), pointers (*ptr), and low-level systems control.",
                "course_title": "C Programming, Memory Addresses & Algorithmic Control",
                "module_title": "Module 1: Counted Loops, Arrays & Pointer Dereferencing",
                "lesson_title": "1.1 Navigating the Isometric Grid with C Loops & Conditionals",
                "concept": (
                    "C gives you direct control over memory addresses and CPU loops. A for(int i = 0; i < N; i++) loop compiles "
                    "to a tight machine-code branch with zero runtime overhead."
                ),
                "anatomy": (
                    "Line 1 | for (int step = 0; step < 4; step++) { | Initializes 32-bit counter step on the Stack (0x7ffee4)\n"
                    "Line 2 |     move_forward(); | Advances the rover 1 tile along its current heading\n"
                    "Line 3 |     collect_core(); } | Harvests energy core on the active tile"
                ),
                "tips": "In C, an array name like arr decays to a pointer to its first element (&arr[0]), so *(arr + i) is identical to arr[i].",
                "trace": "Stack frame main() @ 0x7ffee0 -> int step=0..3 -> dispatches 4 MOVE + COLLECT hardware commands.",
                "game_key": "ROVER_GRID",
                "game_prompt": "Write a complete C for-loop that moves the rover 4 steps East, collects the data core, turns right, and moves 2 steps South to the goal!",
                "starter": "#include <stdio.h>\n\nint main() {\n    for (int i = 0; i < 4; i++) {\n        move_forward();\n        collect_core();\n    }\n    turn_right();\n    for (int j = 0; j < 2; j++) {\n        move_forward();\n    }\n    return 0;\n}",
                "solution": "#include <stdio.h>\n\nint main() {\n    for (int i = 0; i < 4; i++) {\n        move_forward();\n        collect_core();\n    }\n    turn_right();\n    for (int j = 0; j < 2; j++) {\n        move_forward();\n    }\n    return 0;\n}",
                "judge_prompt": "Ensure your C code uses for loops, move_forward(), collect_core(), and turn_right().",
                "hint": "Move 4 steps East, call turn_right(), then move 2 steps South."
            },
            {
                "slug": "cpp",
                "name": "C++20 STL & Object-Oriented",
                "code": "C++",
                "pillar": "SYSTEMS",
                "runtime": "C++ AST & OOP Simulator",
                "summary": "Classes, encapsulation, std::vector, std::map, sorting algorithms, and zero-cost abstractions.",
                "course_title": "C++20 Object-Oriented Programming & STL Algorithms",
                "module_title": "Module 1: Classes, Member Methods & STL Vectors",
                "lesson_title": "1.1 Autonomous Path-Planning with C++ Objects",
                "concept": (
                    "C++ combines C's hardware speed with object-oriented encapsulation and the Standard Template Library (STL). "
                    "You invoke methods directly on an object instance such as rover.moveForward() and rover.collectCore()."
                ),
                "anatomy": (
                    "Line 1 | for (int i = 0; i < 4; i++) { | Standard counted loop over 4 grid steps\n"
                    "Line 2 |     rover.moveForward(); | Invokes member function on the Rover instance\n"
                    "Line 3 |     rover.collectCore(); } | Pushes collected crystal into std::vector<Core>"
                ),
                "tips": "Pass large std::vector objects by const reference (const vector<int>& v) to avoid expensive deep copies.",
                "trace": "Object `rover` @ 0x7ffdf0 -> std::vector capacity=4 -> executes 4东 steps + 2南 steps to reach portal.",
                "game_key": "ROVER_GRID",
                "game_prompt": "Write C++ OOP code using rover.moveForward(), rover.collectCore(), and rover.turnRight() to reach the target portal at (5, 4).",
                "starter": "// C++20 OOP Rover Controller\nfor (int i = 0; i < 4; i++) {\n    rover.moveForward();\n    rover.collectCore();\n}\nrover.turnRight();\nfor (int j = 0; j < 2; j++) {\n    rover.moveForward();\n}",
                "solution": "for (int i = 0; i < 4; i++) {\n    rover.moveForward();\n    rover.collectCore();\n}\nrover.turnRight();\nfor (int j = 0; j < 2; j++) {\n    rover.moveForward();\n}",
                "judge_prompt": "Verify that your C++ code calls rover.moveForward(), rover.collectCore(), and rover.turnRight().",
                "hint": "Keep both for loops and rover.turnRight() between them."
            },
            {
                "slug": "java",
                "name": "Java OOP & Collections",
                "code": "JAVA",
                "pillar": "SYSTEMS",
                "runtime": "JVM Bytecode & OOP Simulator",
                "summary": "Strongly-typed classes, interfaces, inheritance, ArrayList, HashMap, and FIFO queues.",
                "course_title": "Java Object-Oriented Engineering & Collections Framework",
                "module_title": "Module 1: Classes, Methods & Loop Control",
                "lesson_title": "1.1 Commanding Autonomous Units with Java Loops",
                "concept": (
                    "Java enforces strict object-oriented structure where every method lives inside a class and references "
                    "objects allocated on the JVM Heap."
                ),
                "anatomy": (
                    "Line 1 | for (int step = 0; step < 4; step++) { | JVM counted loop\n"
                    "Line 2 |     rover.moveForward(); | Dispatches method call to Heap object\n"
                    "Line 3 |     rover.collectCore(); } | Adds core to ArrayList<Core>"
                ),
                "tips": "Use StringBuilder instead of + concatenation inside Java loops to avoid creating O(N) temporary String objects on the Heap.",
                "trace": "JVM Stack main() -> Heap ref Rover@4a574795 -> executes 4 East steps, turns right, 2 South steps.",
                "game_key": "ROVER_GRID",
                "game_prompt": "Complete the Java controller loop to guide the unit 4 steps East and 2 steps South to the goal.",
                "starter": "public class MissionController {\n    public static void run(Rover rover) {\n        for (int i = 0; i < 4; i++) {\n            rover.moveForward();\n            rover.collectCore();\n        }\n        rover.turnRight();\n        for (int j = 0; j < 2; j++) {\n            rover.moveForward();\n        }\n    }\n}",
                "solution": "public class MissionController {\n    public static void run(Rover rover) {\n        for (int i = 0; i < 4; i++) {\n            rover.moveForward();\n            rover.collectCore();\n        }\n        rover.turnRight();\n        for (int j = 0; j < 2; j++) {\n            rover.moveForward();\n        }\n    }\n}",
                "judge_prompt": "Verify that your Java code includes the two loops and rover.turnRight().",
                "hint": "Keep both for loops and rover.turnRight() inside run()."
            },
        ]

        for idx, item in enumerate(curriculum_data, start=1):
            lang = Language.objects.create(
                slug=item["slug"],
                name=item["name"],
                short_code=item["code"],
                pillar=item["pillar"],
                runtime_engine=item["runtime"],
                summary=item["summary"],
                order=idx,
            )
            course = Course.objects.create(
                language=lang,
                slug=f"{item['slug']}-mastery",
                title=item["course_title"],
                level_badge="Structured 4-Part Modules",
                module_count_label="4 Modules • Full-Code Lab",
                overview=item["summary"],
                order=idx,
            )
            Lesson.objects.create(
                course=course,
                module_number=1,
                module_title=item["module_title"],
                step_number=1,
                slug=f"{item['slug']}-lesson-1",
                title=item["lesson_title"],
                part1_concept=item["concept"],
                syntax_anatomy_rows=item["anatomy"],
                tips_and_tricks=item["tips"],
                part2_trace_explanation=item["trace"],
                game_engine_key=item["game_key"],
                part3_game_prompt=item["game_prompt"],
                starter_code=item["starter"],
                solution_code=item["solution"],
                part4_judge_prompt=item["judge_prompt"],
                hint_text=item["hint"],
                xp_reward=100,
            )

    # 3. 6 Full-Code Playable Visual Games ("Gaming with Learning")
    if CodingGame.objects.count() == 0:
        games_seed = [
            (
                "flexbox-bridge-architect",
                "1. CSS Flexbox & Grid Bridge Architect",
                "FLEX_BRIDGE",
                "HTML5 & CSS3",
                "Easy",
                "Write complete CSS Flexbox rules (display: flex; justify-content: space-between; align-items: center;) to align the 3 bridge planks across the canyon.",
                "Must include display: flex, justify-content: space-between, and align-items: center.",
                ".bridge-stage {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n  gap: 16px;\n}",
                ".bridge-stage {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n  gap: 16px;\n}",
                120,
            ),
            (
                "fractal-tree-ecosystem",
                "2. Bio-Genesis 3D Fractal Tree & Canopy Grower",
                "FRACTAL_TREE",
                "Python 3 / JS / C++",
                "Medium",
                "Write a real Python function and range() loop to organically grow a 6-generation 3D branching tree with glowing leaves and fireflies.",
                "Must define a loop or function calling grow_branch(depth, angle) and bloom_leaves().",
                "def grow_canopy(levels, angle):\n    for depth in range(1, levels + 1):\n        grow_branch(depth, angle)\n    bloom_leaves()\n\ngrow_canopy(6, 26)",
                "def grow_canopy(levels, angle):\n    for depth in range(1, levels + 1):\n        grow_branch(depth, angle)\n    bloom_leaves()\n\ngrow_canopy(6, 26)",
                150,
            ),
            (
                "isometric-rover-pathfinder",
                "3. Isometric Rover Algorithmic Pathfinder",
                "ROVER_GRID",
                "C / C++ / Python / Java",
                "Medium",
                "Write full loops and turn commands to navigate the rover 4 tiles East (collecting the core at (3,1)), turn right, and advance 2 tiles South to the portal at (5,3).",
                "Must execute 4 East steps, collect_core(), turn_right(), and 2 South steps.",
                "for (int i = 0; i < 4; i++) {\n    move_forward();\n    collect_core();\n}\nturn_right();\nfor (int j = 0; j < 2; j++) {\n    move_forward();\n}",
                "for (int i = 0; i < 4; i++) {\n    move_forward();\n    collect_core();\n}\nturn_right();\nfor (int j = 0; j < 2; j++) {\n    move_forward();\n}",
                140,
            ),
            (
                "sql-crime-scene-detective",
                "4. SQL Crime Scene & Relational Detective",
                "SQL_DETECTIVE",
                "SQL / PostgreSQL / SQLite",
                "Medium",
                "Query the live suspects relation using SELECT, WHERE clearance >= 4 AND zone = 'ServerVault', and ORDER BY to uncover the unauthorized intruder.",
                "Must write a complete SELECT ... FROM suspects WHERE ... ORDER BY query.",
                "SELECT id, name, role, access_time\nFROM suspects\nWHERE clearance >= 4 AND zone = 'ServerVault'\nORDER BY access_time DESC;",
                "SELECT id, name, role, access_time\nFROM suspects\nWHERE clearance >= 4 AND zone = 'ServerVault'\nORDER BY access_time DESC;",
                150,
            ),
            (
                "dom-react-circuit-lab",
                "5. JavaScript DOM & React Hardware Circuit Lab",
                "DOM_CIRCUIT",
                "JavaScript ES6+ / React",
                "Easy",
                "Select #circuit-gate using document.querySelector, attach the .powered class, and run a 4-iteration loop calling pulseNode(i) to bring the board online.",
                "Must use document.querySelector, classList.add, and a 4-step loop.",
                "const gate = document.querySelector('#circuit-gate');\ngate.classList.add('powered');\nfor (let i = 0; i < 4; i++) {\n  pulseNode(i);\n}",
                "const gate = document.querySelector('#circuit-gate');\ngate.classList.add('powered');\nfor (let i = 0; i < 4; i++) {\n  pulseNode(i);\n}",
                130,
            ),
            (
                "php-mysqli-data-vault",
                "6. PHP 8 & MySQLi Server Data-Vault CRUD",
                "PHP_VAULT",
                "PHP 8 & MySQLi",
                "Medium",
                "Connect to baiust_db with mysqli_connect() and execute INSERT INTO and SELECT queries via mysqli_query() to synchronize the server rack.",
                "Must include mysqli_connect, mysqli_query, INSERT INTO, and SELECT.",
                "<?php\n$conn = mysqli_connect(\"localhost\", \"root\", \"\", \"baiust_db\");\n$sql = \"INSERT INTO students (id, name, dept) VALUES (1119003, 'Sakib', 'CSE')\";\nmysqli_query($conn, $sql);\n$res = mysqli_query($conn, \"SELECT * FROM students WHERE dept='CSE'\");\n?>",
                "<?php\n$conn = mysqli_connect(\"localhost\", \"root\", \"\", \"baiust_db\");\n$sql = \"INSERT INTO students (id, name, dept) VALUES (1119003, 'Sakib', 'CSE')\";\nmysqli_query($conn, $sql);\n$res = mysqli_query($conn, \"SELECT * FROM students WHERE dept='CSE'\");\n?>",
                150,
            ),
        ]
        for idx, (slug, title, eng, ltag, diff, brief, req, st, sol, xp) in enumerate(games_seed, start=1):
            CodingGame.objects.create(
                slug=slug,
                title=title,
                engine_key=eng,
                language_tag=ltag,
                difficulty=diff,
                scenario_brief=brief,
                real_code_requirement=req,
                starter_code=st,
                solution_code=sol,
                xp_reward=xp,
                order=idx,
            )

    # 4. Multi-Platform Practice Tasks & Weekly Contest Problems (HackerRank / Codeforces / LeetCode / CSE 324 Style)
    if PracticeTask.objects.count() == 0:
        tasks_seed = [
            (
                "CQ-101",
                "responsive-flexbox-navbar-task",
                "Responsive Flexbox Navbar with Hidden Checkbox Toggle",
                "HTML5 & CSS3",
                "Flexbox & RWD",
                "Easy",
                "CSE 324 Lab 04 / freeCodeCamp",
                "Build a desktop-first navigation bar (.navbar) with display: flex, justify-content: space-between, and a @media (max-width: 768px) rule that reveals the hamburger icon and stacks links vertically when #menu-toggle:checked is active.",
                "Desktop (>768px) & Mobile (<=768px)",
                "Logo Left, Links Right -> Stacks Vertically on Mobile",
                ".navbar {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n}\n@media (max-width: 768px) {\n  .nav-links { flex-direction: column; }\n  .menu-toggle:checked + .menu-icon + .nav-links { display: flex; }\n}",
                ".navbar {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n}\n@media (max-width: 768px) {\n  .nav-links { flex-direction: column; }\n  .menu-toggle:checked + .menu-icon + .nav-links { display: flex; }\n}",
                100,
            ),
            (
                "CQ-102",
                "even-subarray-sum-filter",
                "Even Harmonics Array Filter & Sum",
                "Python 3 / C++ / JS",
                "Arrays & Loops",
                "Easy",
                "HackerRank / Codeforces Div. 4",
                "Given an array of integers [12, 7, 18, 5, 24, 9, 30], write a function or loop that filters only the even numbers and prints their total sum (84).",
                "[12, 7, 18, 5, 24, 9, 30]",
                "84",
                "nums = [12, 7, 18, 5, 24, 9, 30]\neven_sum = sum(x for x in nums if x % 2 == 0)\nprint(even_sum)",
                "nums = [12, 7, 18, 5, 24, 9, 30]\neven_sum = sum(x for x in nums if x % 2 == 0)\nprint(even_sum)",
                80,
            ),
            (
                "CQ-103",
                "department-grade-table-rowspan",
                "University Result Table with Rowspan & Colspan",
                "HTML5",
                "HTML5 Tables",
                "Easy",
                "CSE 324 Lab 01 / Slide 28",
                "Create a student result table where the 'CSE' department cell spans 3 rows vertically (rowspan='3') and the 'Class Average' footer cell spans 3 columns horizontally (colspan='3').",
                "3 Student Rows + 1 Summary Row",
                "Valid HTML5 Table with rowspan='3' and colspan='3'",
                "<table>\n  <tr><td rowspan=\"3\">CSE</td><td>1119003</td><td>Sakib</td><td>165</td></tr>\n  <tr><td>1119026</td><td>Fahim</td><td>155</td></tr>\n  <tr><td>1119004</td><td>Nesar</td><td>175</td></tr>\n  <tr><td colspan=\"3\">Class Average</td><td>165.0</td></tr>\n</table>",
                "<table>\n  <tr><td rowspan=\"3\">CSE</td><td>1119003</td><td>Sakib</td><td>165</td></tr>\n  <tr><td>1119026</td><td>Fahim</td><td>155</td></tr>\n  <tr><td>1119004</td><td>Nesar</td><td>175</td></tr>\n  <tr><td colspan=\"3\">Class Average</td><td>165.0</td></tr>\n</table>",
                90,
            ),
            (
                "CQ-104",
                "sql-top-department-gpa",
                "Department Honor-Roll SQL Aggregation",
                "SQL (PostgreSQL / SQLite)",
                "GROUP BY & HAVING",
                "Medium",
                "LeetCode SQL 50 / HackerRank",
                "Write a SQL query to select dept and AVG(cgpa) as avg_cgpa from the students table, grouped by dept, having AVG(cgpa) >= 3.50, ordered descending.",
                "Table: students(id, name, dept, cgpa)",
                "CSE | 3.78",
                "SELECT dept, ROUND(AVG(cgpa), 2) AS avg_cgpa\nFROM students\nGROUP BY dept\nHAVING AVG(cgpa) >= 3.50\nORDER BY avg_cgpa DESC;",
                "SELECT dept, ROUND(AVG(cgpa), 2) AS avg_cgpa\nFROM students\nGROUP BY dept\nHAVING AVG(cgpa) >= 3.50\nORDER BY avg_cgpa DESC;",
                120,
            ),
            (
                "CQ-105",
                "two-pointer-palindrome-check",
                "Two-Pointer String Palindrome Verifier",
                "Python / C / C++ / Java",
                "Two Pointers & Strings",
                "Medium",
                "LeetCode / Codeforces",
                "Write a function that checks whether the string 'level' is a palindrome using two pointers (left and right) and prints 'PALINDROME'.",
                "level",
                "PALINDROME",
                "s = 'level'\nis_pal = (s == s[::-1])\nprint('PALINDROME' if is_pal else 'NOT_PALINDROME')",
                "s = 'level'\nis_pal = (s == s[::-1])\nprint('PALINDROME' if is_pal else 'NOT_PALINDROME')",
                110,
            ),
            (
                "CQ-106",
                "php-mysqli-update-student-record",
                "PHP & MySQLi Safe Record Update",
                "PHP 8 & MySQLi",
                "Backend CRUD",
                "Medium",
                "CSE 324 Evaluation (iv)",
                "Write the PHP MySQLi code to update a student's cgpa to 3.92 where id = 1119003 using mysqli_query($conn, $sql).",
                "id=1119003, cgpa=3.92",
                "1 Row Updated in students",
                "<?php\n$conn = mysqli_connect('localhost', 'root', '', 'baiust_db');\n$sql = \"UPDATE students SET cgpa = 3.92 WHERE id = 1119003\";\nmysqli_query($conn, $sql);\n?>",
                "<?php\n$conn = mysqli_connect('localhost', 'root', '', 'baiust_db');\n$sql = \"UPDATE students SET cgpa = 3.92 WHERE id = 1119003\";\nmysqli_query($conn, $sql);\n?>",
                120,
            ),
        ]
        for idx, (cid, slug, title, ltag, ttag, diff, insp, stmt, sin, sout, st, sol, xp) in enumerate(tasks_seed, start=1):
            PracticeTask.objects.create(
                code_id=cid,
                slug=slug,
                title=title,
                language_tag=ltag,
                topic_tag=ttag,
                difficulty=diff,
                inspired_by=insp,
                problem_statement=stmt,
                sample_input=sin,
                sample_output=sout,
                starter_code=st,
                solution_code=sol,
                xp_reward=xp,
                order=idx,
            )

    if Submission.objects.count() == 0:
        Submission.objects.create(
            student_name="Md Najmus Sakib Rahatul (1119003)",
            item_type="Full-Code Game",
            item_title="1. CSS Flexbox & Grid Bridge Architect",
            language_used="HTML5 & CSS3",
            submitted_code=".bridge-stage { display: flex; justify-content: space-between; align-items: center; }",
            passed=True,
            xp_earned=120,
        )
        Submission.objects.create(
            student_name="Md Najmus Sakib Rahatul (1119003)",
            item_type="Course Module",
            item_title="1.1 Loops, Functions & Organic 3D Fractal Tree Generation",
            language_used="Python 3",
            submitted_code="def grow_canopy(levels, angle): ...",
            passed=True,
            xp_earned=100,
        )


if __name__ == "__main__":
    seed_all()
    print("Seeded CodeQuest LMS (12 Languages, 4-Part Lessons, 6 Full-Code Games, 6 Multi-Site Tasks) successfully!")
