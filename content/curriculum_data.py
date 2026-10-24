import re
from django.utils.text import slugify

# 16 World-Class Programming Languages + 108 AAA-Inspired Coding Games Catalog

LANGUAGES_16 = [
    {
        "slug": "python", "name": "Python 3.12", "code": "PY", "cat": "AI, Data & Backend",
        "runtime": "Pyodide WASM + AST Sandbox", "engine": "TREE_3D", "color": "#10b981",
        "summary": "Master loops, recursion, data structures, and AI scripting by growing living 3D fractal ecosystems.",
        "lesson_title": "Recursive Loops & Memory Frames in Python",
        "mental": "In Harvard CS50 style: every loop iteration updates the local variable `d` in the Stack Frame while allocating new 3D branch objects in the Heap.",
        "video_script": "00:00 — Stack Frame `main()` initializes `d = 0`. 00:15 — `range(6)` pushes 6 branch calls onto the call stack. 00:30 — Heap memory renders 64 bioluminescent 3D limbs!",
        "cheats": "for d in range(6): | Iterates d from 0 to 5 in stack memory | for d in range(6):\ngrow_branch(26) | Allocates 3D branch node on heap | grow_branch(26)\nbloom_canopy() | Triggers 3D leaf & firefly particle shader | bloom_canopy()",
        "starter": "# Python 3.12 — Grow 3D Fractal Canopy & Inspect Stack/Heap\nfor d in range(6):\n    grow_branch(26)\nbloom_canopy()",
        "solution": "for d in range(6):\n    grow_branch(26)\nbloom_canopy()",
        "hint": "Keep grow_branch(26) indented inside for d in range(6): and call bloom_canopy()."
    },
    {
        "slug": "javascript", "name": "JavaScript ES2026", "code": "JS", "cat": "Web & Interactive DOM",
        "runtime": "V8 Sandboxed DOM + WebGL", "engine": "SOLAR_3D", "color": "#f59e0b",
        "summary": "Command asynchronous events, closures, Live DOM trees, and 3D orbital physics in real time.",
        "lesson_title": "V8 Call Stack, Event Loop & Live DOM Mutation",
        "mental": "JavaScript executes synchronous loops on the Call Stack while mutating live DOM nodes (`querySelector`) and WebGL orbital vectors in the Heap.",
        "video_script": "00:00 — V8 Call Stack runs `ignite_star()`. 00:15 — `for (let p=1; p<=5; p++)` spawns 5 orbital bodies in Heap memory. 00:30 — DOM Inspector updates live telemetry!",
        "cheats": "document.querySelector(s) | Selects live DOM node from document tree | document.querySelector('#shield')\nspawn_planet(r, v) | Pushes 3D planet vector to WebGL scene | spawn_planet(p * 24, 2.2);\nadd_rings('#38bdf8') | Attaches particle ring shader | add_rings('#38bdf8');",
        "starter": "// JavaScript ES2026 — 3D Solar Physics & DOM Sync\nignite_star();\nfor (let p = 1; p <= 5; p++) {\n  spawn_planet(p * 24, 2.4 / p);\n}\nadd_rings('#38bdf8');",
        "solution": "ignite_star();\nfor (let p = 1; p <= 5; p++) {\n  spawn_planet(p * 24, 2.4 / p);\n}\nadd_rings('#38bdf8');",
        "hint": "Call ignite_star() and loop p from 1 to 5."
    },
    {
        "slug": "typescript", "name": "TypeScript 5.x", "code": "TS", "cat": "Web & Interactive DOM",
        "runtime": "Static Type Checker + AST", "engine": "TREE_3D", "color": "#38bdf8",
        "summary": "Write strictly typed interfaces, generics, and zero-bug full-stack architecture.",
        "lesson_title": "Compile-Time Type Safety & Generic Contracts",
        "mental": "TypeScript erases type annotations after verifying that every function argument (`angle: number`) satisfies its memory contract before execution.",
        "video_script": "00:00 — Type Checker validates `angle: number`. 00:15 — Zero runtime type errors guaranteed. 00:30 — 3D Fractal Tree renders at 60 FPS.",
        "cheats": "let depth: number = 6; | Explicit primitive type contract | let depth: number = 6;\ninterface Node3D { ... } | Defines structural object shape | interface Node3D { id: number; }\ngrow_branch(28); | Type-checked 3D call | grow_branch(28);",
        "starter": "// TypeScript 5 — Type-Safe 3D Canopy\nfor (let d: number = 0; d < 6; d++) {\n  grow_branch(28);\n}\nbloom_canopy();",
        "solution": "for (let d: number = 0; d < 6; d++) {\n  grow_branch(28);\n}\nbloom_canopy();",
        "hint": "Loop d from 0 to 5 calling grow_branch(28)."
    },
    {
        "slug": "c-lang", "name": "C (GCC / Pointers)", "code": "C", "cat": "Systems & Embedded",
        "runtime": "CS50 Stack/Heap Pointer Simulator", "engine": "BOSS_BLITZ", "color": "#6366f1",
        "summary": "Visualize raw memory addresses, pointers (`*p`, `&x`), arrays, and embedded register loops.",
        "lesson_title": "CS50 Pointers, Stack Addresses & Hardware Loops",
        "mental": "In C, every variable lives at an exact hexadecimal memory address (`0x7ffee0`). A `for` loop increments the register counter directly at machine speed.",
        "video_script": "00:00 — Stack allocates `int i = 0` at `0x7ffee4`. 00:15 — Each iteration fires a hardware interrupt beam. 00:30 — `shatter_core()` clears the reactor!",
        "cheats": "int *ptr = &x; | Stores memory address of x | int *ptr = &core;\nfor(int i=0; i<6; i++) | Hardware-speed register loop | for(int i=0; i<6; i++)\nfire_laser(i); | Emits 3D plasma pulse | fire_laser(i);",
        "starter": "// C (CS50 Memory & Pointer Mode)\nfor (int i = 0; i < 6; i++) {\n    fire_laser(i);\n}\nshatter_core();",
        "solution": "for (int i = 0; i < 6; i++) {\n    fire_laser(i);\n}\nshatter_core();",
        "hint": "Run 6 iterations of fire_laser(i); then call shatter_core();"
    },
    {
        "slug": "cpp", "name": "C++20 (STL & OOP)", "code": "C++", "cat": "Systems & Embedded",
        "runtime": "C++20 STL Vector & Wave Engine", "engine": "ROVER_3D", "color": "#8b5cf6",
        "summary": "Command high-frequency 3D physics, `std::vector`, RAII memory, and autonomous drone flight.",
        "lesson_title": "RAII Objects, STL Vectors & 3D Wave Flight",
        "mental": "`std::vector` manages contiguous Heap memory automatically while methods on stack-allocated objects control the 3D quadcopter.",
        "video_script": "00:00 — `set_wave(2.4, 18)` initializes the 3D terrain mesh. 00:15 — `fly_waypoint(w)` interpolates 3D quaternion attitude.",
        "cheats": "std::vector<int> v; | Dynamic contiguous heap array | std::vector<int> path;\nset_wave(2.4, 18); | Modulates 3D wave terrain | set_wave(2.4, 18);\nfly_waypoint(w); | Pilots 3D drone through ring w | fly_waypoint(w);",
        "starter": "// C++20 — 3D Wave Terrain & Autonomous Drone\nset_wave(2.4, 18);\nfor (int w = 0; w < 5; w++) {\n    fly_waypoint(w);\n}\nstabilize();",
        "solution": "set_wave(2.4, 18);\nfor (int w = 0; w < 5; w++) {\n    fly_waypoint(w);\n}\nstabilize();",
        "hint": "Loop w from 0 to 4 calling fly_waypoint(w)."
    },
    {
        "slug": "java", "name": "Java 21 (JVM OOP)", "code": "JAVA", "cat": "Enterprise & Backend",
        "runtime": "JVM Bytecode & Object Heap Inspector", "engine": "SOLAR_3D", "color": "#ec4899",
        "summary": "Master classes, inheritance, collections, and JVM heap garbage-collection visualization.",
        "lesson_title": "JVM Object References & Planetary Simulation",
        "mental": "In Java, object references sit on the Thread Stack while `new Planet()` instances live inside the JVM Garbage-Collected Heap.",
        "video_script": "00:00 — JVM loads class bytecode. 00:15 — 5 `Planet` instances allocate on the JVM Heap.",
        "cheats": "class OrbitSystem { ... } | Encapsulates state and behavior | class OrbitSystem {}\nignite_star(); | Initializes central solar mass | ignite_star();\nspawn_planet(r, v); | Instantiates 3D planet object | spawn_planet(p * 24, 2.4);",
        "starter": "// Java 21 OOP — 3D Orbital Controller\nignite_star();\nfor (int p = 1; p <= 5; p++) {\n    spawn_planet(p * 24, 2.4);\n}\nadd_rings(\"#10b981\");",
        "solution": "ignite_star();\nfor (int p = 1; p <= 5; p++) {\n    spawn_planet(p * 24, 2.4);\n}\nadd_rings(\"#10b981\");",
        "hint": "Keep ignite_star() and the 5-planet loop."
    },
    {
        "slug": "rust", "name": "Rust (Borrow Checker)", "code": "RS", "cat": "Systems & Embedded",
        "runtime": "Zero-Cost Ownership & Lifetime Verifier", "engine": "ROVER_3D", "color": "#f97316",
        "summary": "Write fearless concurrency and memory-safe systems without a garbage collector.",
        "lesson_title": "Ownership, Borrowing (`&mut`) & Zero-Cost Flight",
        "mental": "Rust enforces single ownership of Heap data at compile time, freeing memory deterministically the instant its owner leaves scope.",
        "video_script": "00:00 — Borrow checker verifies `&mut drone`. 00:20 — Zero GC pauses during 60 FPS flight.",
        "cheats": "let mut x = 5; | Mutable stack binding | let mut alt = 20;\nfor w in 0..5 { ... } | Zero-cost iterator range | for w in 0..5\nfly_waypoint(w); | Safe 3D telemetry dispatch | fly_waypoint(w);",
        "starter": "// Rust — Memory-Safe 3D Flight Controller\nset_wave(2.8, 20);\nfor (let w = 0; w < 5; w++) {\n    fly_waypoint(w);\n}\nstabilize();",
        "solution": "set_wave(2.8, 20);\nfor (let w = 0; w < 5; w++) {\n    fly_waypoint(w);\n}\nstabilize();",
        "hint": "Run fly_waypoint(w) across all 5 waypoints."
    },
    {
        "slug": "golang", "name": "Go (Concurrency)", "code": "GO", "cat": "Enterprise & Backend",
        "runtime": "Goroutine Scheduler & Channel Tracer", "engine": "BOSS_BLITZ", "color": "#06b6d4",
        "summary": "Build cloud-native microservices, goroutines (`go fn()`), and channels.",
        "lesson_title": "Goroutines, Channels & Concurrent Laser Dispatch",
        "mental": "Go multiplexes lightweight 2 KB Goroutines onto OS threads, communicating safely via typed channels.",
        "video_script": "00:00 — Main goroutine spawns 6 concurrent workers. 00:20 — Channels synchronize 3D laser impact.",
        "cheats": "go fire_laser(i) | Spawns lightweight goroutine | fire_laser(i)\nch <- val | Sends value into channel | ch <- 1\nshatter_core() | Completes reactor takedown | shatter_core()",
        "starter": "// Go — Concurrent 3D Boss Core Takedown\nfor (let i = 0; i < 6; i++) {\n    fire_laser(i);\n}\nshatter_core();",
        "solution": "for (let i = 0; i < 6; i++) {\n    fire_laser(i);\n}\nshatter_core();",
        "hint": "Call fire_laser(i) 6 times and shatter_core()."
    },
    {
        "slug": "sql", "name": "SQL (PostgreSQL / SQLite)", "code": "SQL", "cat": "AI, Data & Backend",
        "runtime": "In-Memory Relational B-Tree + 3D Helix", "engine": "SQL_HEIST", "color": "#14b8a6",
        "summary": "Execute `SELECT`, `JOIN`, `GROUP BY`, and ACID transactions visualized on a 3D DNA Data Helix.",
        "lesson_title": "Relational B-Tree Indexing & 3D Helix Queries",
        "mental": "SQL is declarative: you specify the target dataset (`WHERE state = 'ACTIVE'`), and the query planner traverses the B-Tree index.",
        "video_script": "00:00 — `INSERT INTO` appends tuple to B-Tree page. 00:20 — `SELECT` lights up matching 3D Helix rungs.",
        "cheats": "INSERT INTO tbl VALUES (..) | Appends row to relational table | INSERT INTO helix_nodes VALUES (1, 'ACTIVE');\nSELECT * FROM tbl WHERE .. | Filters rows matching predicate | SELECT * FROM helix_nodes WHERE state = 'ACTIVE';\nINNER JOIN | Combines related tables on key | JOIN users ON ...",
        "starter": "-- SQL — Energize 3D Neural Double-Helix\nINSERT INTO helix_nodes (id, state) VALUES (1, 'ACTIVE');\nSELECT * FROM helix_nodes WHERE state = 'ACTIVE';",
        "solution": "INSERT INTO helix_nodes (id, state) VALUES (1, 'ACTIVE');\nSELECT * FROM helix_nodes WHERE state = 'ACTIVE';",
        "hint": "Keep both INSERT INTO and SELECT * FROM helix_nodes."
    },
    {
        "slug": "php", "name": "PHP 8.3 (MySQLi CRUD)", "code": "PHP", "cat": "Enterprise & Backend",
        "runtime": "Zend Engine + Live MySQLi Vault Simulator", "engine": "SQL_HEIST", "color": "#a855f7",
        "summary": "Master server-side web engineering, `mysqli_query` CRUD, and session security.",
        "lesson_title": "Server-Side MySQLi CRUD & 3D Data Vault",
        "mental": "PHP opens a socket to MySQL (`mysqli_connect`) and commits `INSERT`, `UPDATE`, and `DELETE` transactions.",
        "video_script": "00:00 — `$conn` handshakes with MySQL. 00:20 — `mysqli_query()` mutates the 3D Server Vault.",
        "cheats": "mysqli_connect(...) | Connects to MySQL server | $c = mysqli_connect('localhost','root','','db');\nmysqli_query($c, $sql) | Runs SQL CRUD statement | mysqli_query($c, \"INSERT INTO ...\");\nmysqli_fetch_assoc($r) | Reads row as key-value array | $row = mysqli_fetch_assoc($r);",
        "starter": "<?php\n$conn = mysqli_connect('localhost', 'root', '', 'helix_db');\nmysqli_query($conn, \"INSERT INTO helix_nodes VALUES (101, 'ONLINE')\");\n?>",
        "solution": "<?php\n$conn = mysqli_connect('localhost', 'root', '', 'helix_db');\nmysqli_query($conn, \"INSERT INTO helix_nodes VALUES (101, 'ONLINE')\");\n?>",
        "hint": "Keep mysqli_connect and mysqli_query with INSERT INTO."
    },
    {
        "slug": "html5", "name": "HTML5 (Semantic DOM)", "code": "HTML", "cat": "Web & Interactive DOM",
        "runtime": "Live DOM Tree & Accessibility Inspector", "engine": "DOM_TOWER", "color": "#ef4444",
        "summary": "Construct semantic document trees, accessible forms, and `rowspan`/`colspan` matrices.",
        "lesson_title": "DOM Tree Hierarchy, Landmarks & Table Spanning",
        "mental": "The browser parses HTML5 tags into an in-memory Tree of Element Nodes (`Document -> html -> body -> table`).",
        "video_script": "00:00 — Parser builds `<table>` root node. 00:20 — `rowspan` and `colspan` merge 3D grid cells.",
        "cheats": "<main> / <section> | Semantic landmark regions | <main>...</main>\nrowspan=\"2\" | Spans cell vertically across 2 rows | <td rowspan=\"2\">Root</td>\ncolspan=\"2\" | Spans cell horizontally across 2 cols | <td colspan=\"2\">Canopy</td>",
        "starter": "<!-- HTML5 DOM Tree & Table Matrix -->\n<table>\n  <tr>\n    <td rowspan=\"2\">Core</td>\n    <td colspan=\"2\">3D DOM Branches</td>\n  </tr>\n</table>",
        "solution": "<table>\n  <tr>\n    <td rowspan=\"2\">Core</td>\n    <td colspan=\"2\">3D DOM Branches</td>\n  </tr>\n</table>",
        "hint": "Include both rowspan=\"2\" and colspan=\"2\"."
    },
    {
        "slug": "css3", "name": "CSS3 (Flexbox & Grid)", "code": "CSS", "cat": "Web & Interactive DOM",
        "runtime": "Box-Model, Flexbox & 12-Col Grid Visualizer", "engine": "DOM_TOWER", "color": "#3b82f6",
        "summary": "Master Flexbox, CSS Grid, `oklch()` color tokens, and GPU-accelerated animations.",
        "lesson_title": "CSS Box Model, Flexbox Axis & Spatial Grid",
        "mental": "Every DOM element is a rectangular box (`Content -> Padding -> Border -> Margin`) aligned along main and cross axes.",
        "video_script": "00:00 — `display: flex` activates main-axis layout. 00:20 — `justify-content: space-between` locks 3D towers.",
        "cheats": "display: flex; | Enables flexible box layout | .stage { display: flex; }\njustify-content: space-between; | Distributes free space evenly | justify-content: space-between;\nalign-items: center; | Centers along cross-axis | align-items: center;",
        "starter": "/* CSS3 Spatial Flexbox Alignment */\n.solar-system {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n}",
        "solution": ".solar-system {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n}",
        "hint": "Keep display: flex and justify-content: space-between."
    },
    {
        "slug": "csharp", "name": "C# (.NET 9 / Unity)", "code": "C#", "cat": "Enterprise & Backend",
        "runtime": ".NET CLR & Unity 3D Entity Component Engine", "engine": "SOLAR_3D", "color": "#6366f1",
        "summary": "Build enterprise APIs, LINQ queries, and 3D game physics scripts.",
        "lesson_title": ".NET CLR Value vs Reference Types & 3D Physics",
        "mental": "`struct` value types live directly on the Stack while `class` instances allocate on the Managed CLR Heap.",
        "video_script": "00:00 — CLR JIT compiles C# loop. 00:20 — 5 orbital entities spawn in 3D space.",
        "cheats": "foreach (var x in list) | Iterates collection safely | for (int p=1; p<=5; p++)\nignite_star(); | Starts 3D solar core | ignite_star();\nspawn_planet(r, v); | Spawns 3D orbital body | spawn_planet(p*24, 2.2);",
        "starter": "// C# .NET — 3D Orbital Physics\nignite_star();\nfor (int p = 1; p <= 5; p++) {\n    spawn_planet(p * 24, 2.2);\n}",
        "solution": "ignite_star();\nfor (int p = 1; p <= 5; p++) {\n    spawn_planet(p * 24, 2.2);\n}",
        "hint": "Run ignite_star() and the 5-planet loop."
    },
    {
        "slug": "swift", "name": "Swift 6 (iOS / Apple)", "code": "SWIFT", "cat": "Mobile & Apple HIG",
        "runtime": "ARC Memory & SwiftUI Spatial Canvas", "engine": "TREE_3D", "color": "#f43f5e",
        "summary": "Craft ultra-smooth Apple HIG interfaces, optionals, and Automatic Reference Counting (ARC).",
        "lesson_title": "Swift Optionals, Value Types & 3D Canopy Animation",
        "mental": "Swift uses deterministic Automatic Reference Counting (ARC) instead of a stop-the-world garbage collector.",
        "video_script": "00:00 — ARC tracks reference count `rc = 1`. 00:20 — Smooth 60 FPS 3D tree bloom.",
        "cheats": "for d in 0..<6 { ... } | Half-open range loop | for (let d=0; d<6; d++)\ngrow_branch(26) | Expands 3D limb | grow_branch(26);\nbloom_canopy() | Triggers spring animation | bloom_canopy();",
        "starter": "// Swift 6 — 3D Spring Canopy\nfor (let d = 0; d < 6; d++) {\n    grow_branch(26);\n}\nbloom_canopy();",
        "solution": "for (let d = 0; d < 6; d++) {\n    grow_branch(26);\n}\nbloom_canopy();",
        "hint": "Call grow_branch(26) inside the loop and bloom_canopy()."
    },
    {
        "slug": "kotlin", "name": "Kotlin (Coroutines)", "code": "KT", "cat": "Mobile & Apple HIG",
        "runtime": "JVM/Native Coroutine State Machine", "engine": "ROVER_3D", "color": "#a855f7",
        "summary": "Write expressive null-safe Android and multiplatform systems with structured concurrency.",
        "lesson_title": "Null Safety (`?.`) & Coroutine Flight Control",
        "mental": "Kotlin's compiler forbids raw `null` dereferences at compile time, eliminating `NullPointerException` crashes.",
        "video_script": "00:00 — Compiler verifies non-null flight path. 00:20 — 3D Drone glides across wave mesh.",
        "cheats": "val x: String? = null | Nullable type declaration | set_wave(2.5, 18);\nfor (w in 0..4) | Inclusive range loop | for (let w=0; w<5; w++)\nfly_waypoint(w) | Advances 3D drone | fly_waypoint(w);",
        "starter": "// Kotlin — Null-Safe 3D Drone Flight\nset_wave(2.5, 18);\nfor (let w = 0; w < 5; w++) {\n    fly_waypoint(w);\n}\nstabilize();",
        "solution": "set_wave(2.5, 18);\nfor (let w = 0; w < 5; w++) {\n    fly_waypoint(w);\n}\nstabilize();",
        "hint": "Loop w from 0 to 4 calling fly_waypoint(w)."
    },
    {
        "slug": "bash", "name": "Bash & Linux CLI", "code": "SH", "cat": "Systems & Embedded",
        "runtime": "POSIX Shell & Process Pipeline Simulator", "engine": "BOSS_BLITZ", "color": "#10b981",
        "summary": "Automate Linux servers, pipes (`|`), permissions, and DevSecOps deployment pipelines.",
        "lesson_title": "POSIX Process Pipes, Exit Codes & Reactor Defense",
        "mental": "Every Linux command runs in a child process (`fork/exec`), reading `stdin` (0) and streaming to `stdout` (1).",
        "video_script": "00:00 — Shell spawns pipeline processes. 00:20 — Automated defense barrage clears Boss Core.",
        "cheats": "for i in {0..5}; do .. | POSIX loop | for (let i=0; i<6; i++)\nfire_laser(i) | Dispatches signal packet | fire_laser(i);\nshatter_core() | Verifies exit code 0 | shatter_core();",
        "starter": "// Bash / DevSecOps Automation Loop\nfor (let i = 0; i < 6; i++) {\n    fire_laser(i);\n}\nshatter_core();",
        "solution": "for (let i = 0; i < 6; i++) {\n    fire_laser(i);\n}\nshatter_core();",
        "hint": "Execute 6 iterations of fire_laser(i) and shatter_core()."
    },
]


def generate_108_aaa_games():
    """Generates 108 playable, AAA-inspired 3D/2D coding games across 6 categories (18 per category)."""
    categories = [
        (
            "CyberPunk 3D Rover & Drone Odyssey",
            "ROVER_3D",
            "Python / C / C++ / Rust",
            [
                "Neon Alley Thruster Ignition", "Laser Grid Telemetry Bypass", "Autonomous Quadcopter Canyon Run",
                "Subway Tunnel Sensor Sweep", "EMP Tower Disarm Protocol", "Skybridge Waypoint Interpolation",
                "Quantum Battery Harvest Loop", "Night-City Rooftop Relay", "Drone Swarm Formation Lock",
                "Magnetic Rail Acceleration", "Firewall Gate Brute-Force", "Encrypted Beacon Triangulation",
                "Thermal Vent Evasion Loop", "Cargo Pod Autonomous Docking", "Orbital Elevator Ascent",
                "Zero-Visibility Radar Navigation", "Cyber-Hound Pursuit Escape", "Apex Nexus Citadel Breach"
            ],
            "set_wave(2.4, 18);\nfor (let w = 0; w < 5; w++) {\n  fly_waypoint(w);\n}\nstabilize();"
        ),
        (
            "Bio-Genesis 3D Fractal Forest",
            "TREE_3D",
            "Python / JS / TypeScript / Swift",
            [
                "Seedling Trunk Recursion", "Binary Canopy Bifurcation", "Sakura Blossom Particle Bloom",
                "Bioluminescent Firefly Orbit", "Golden-Ratio Phyllotaxis Spiral", "Wind-Sway Sinusoidal Physics",
                "Mycelium Root Network Graph", "Rainforest Multi-Tier Canopy", "Coral Reef 3D Fractal Growth",
                "Crystal Cave Dendrite Branching", "Solar Photosynthesis Energy Flow", "Autumn Leaf Gravity Cascade",
                "Bonsai Asymmetric Pruning", "Ancient Sequoia 6-Level Recursion", "Alpine Pine Snow-Load Balance",
                "Mangrove Tidal Root Lattice", "Lotus Pond Ripple Harmonics", "World-Tree Yggdrasil Awakening"
            ],
            "for d in range(6):\n    grow_branch(26)\nbloom_canopy()"
        ),
        (
            "Starfield 3D Orbital Gravity Fleet",
            "SOLAR_3D",
            "JavaScript / Java / C# / C++",
            [
                "Solar Corona Ignition", "Mercury High-Velocity Orbit", "Twin-Star Binary Resonance",
                "Saturnian Particle Ring Shader", "Lagrange Point Satellite Lock", "Hohmann Transfer Orbit Calc",
                "Asteroid Belt Kestrel Dodge", "Exoplanet Atmospheric Entry", "Pulsar Timing Array Sync",
                "Dyson Swarm Mirror Alignment", "Comet Tail Ion Deflection", "Black Hole Event-Horizon Slingshot",
                "Jupiter Galilean Moon Dance", "Kuiper Belt Relay Network", "Warp Gate Tachyon Alignment",
                "Supernova Shockwave Shielding", "Galactic Spiral Arm Simulation", "Omega Starfleet Command Finale"
            ],
            "ignite_star();\nfor (let p = 1; p <= 5; p++) {\n  spawn_planet(p * 24, 2.4 / p);\n}\nadd_rings('#38bdf8');"
        ),
        (
            "Flexbox & Grid 3D Hologram Defense",
            "DOM_TOWER",
            "HTML5 / CSS3 / JS DOM",
            [
                "Main-Axis Laser Turret Center", "Space-Between Shield Generators", "Cross-Axis Elevation Lock",
                "Flex-Wrap Bunker Formation", "Column-Reverse Drone Interceptor", "12-Column Bento Fortress Grid",
                "Rowspan & Colspan Radar Matrix", "DOM querySelector Target Lock", "classList Active Shield Toggle",
                "createElement Bridge Spawner", "Event-Bubbling Firewall Trap", "CSS Custom Property Power Surge",
                "Grid-Template-Areas Command Deck", "Sticky HUD Telemetry Bar", "Z-Index Hologram Layering",
                "Clamp() Fluid Armor Scaling", "Keyframes Pulse Cannon", "Grandmaster DOM Citadel Defense"
            ],
            ".solar-system {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n}"
        ),
        (
            "WatchDogs SQL & PHP Vault Heist",
            "SQL_HEIST",
            "SQL / PHP 8 / PostgreSQL",
            [
                "Vault Socket Handshake (mysqli)", "INSERT Credential Pod Injection", "SELECT Active Mainframe Nodes",
                "WHERE Clause Firewall Filter", "UPDATE Security Clearance Level", "DELETE Corrupted Tracker Logs",
                "INNER JOIN Syndicate Ledger", "GROUP BY Encrypted Sector Traffic", "ORDER BY High-Value Vaults",
                "COUNT & SUM Crypto Treasury", "Prepared Statement SQLi Shield", "ACID Transaction Rollback Guard",
                "B-Tree Index Speedup Heist", "HAVING Clause Anomaly Hunt", "Subquery Phantom Account Trace",
                "LEFT JOIN Orphaned Server Audit", "DISTINCT Access Token Sweep", "Zero-Day Mainframe Exfiltration"
            ],
            "INSERT INTO helix_nodes (id, state) VALUES (1, 'ACTIVE');\nSELECT * FROM helix_nodes WHERE state = 'ACTIVE';"
        ),
        (
            "Boss-Battle 60s Bug-Hunter & Memory Arena",
            "BOSS_BLITZ",
            "C / Go / Bash / Polyglot",
            [
                "Null-Pointer Dereference Shield", "Off-By-One Loop Boundary Sniper", "Stack-Overflow Recursion Breaker",
                "Memory-Leak Heap Purifier", "Race-Condition Mutex Lock", "Deadlock Goroutine Unbeaker",
                "Buffer-Overflow Canary Guard", "Dangling-Pointer Sanitizer", "Floating-Point Precision Fix",
                "XSS Payload Sanitization Laser", "CSRF Token Verification Strike", "Infinite-While-Loop Terminator",
                "Uninitialized Register Zeroer", "Signed-Integer Overflow Catch", "Double-Free Heap Protector",
                "Type-Coercion Bug Eliminator", "Async Promise Rejection Catch", "Final Boss: Omega Core Overload"
            ],
            "for (int i = 0; i < 6; i++) {\n    fire_laser(i);\n}\nshatter_core();"
        ),
    ]

    games = []
    num = 1
    diffs = ["Beginner", "Intermediate", "Advanced", "Boss Tier"]
    for cat_name, eng, lang_tag, titles, code_tpl in categories:
        for idx, t in enumerate(titles):
            diff = diffs[min(3, idx // 5)]
            clean_s = slugify(t)[:40].strip("-")
            games.append({
                "game_number": num,
                "slug": f"game-{num:03d}-{clean_s}",
                "title": f"#{num:03d} — {t}",
                "category_name": cat_name,
                "engine_mode": eng,
                "language_tag": lang_tag,
                "difficulty": diff,
                "duration_Label": f"{2 + (idx % 3)} Min",
                "xp_reward": 50 + (idx * 10),
                "mission_brief": f"[{cat_name}] Write or execute the {lang_tag} control logic to complete '{t}' in the 60 FPS {eng} simulation engine.",
                "starter_code": code_tpl,
                "solution_code": code_tpl,
                "target_keyword": "for" if "for" in code_tpl else ("display" if "display" in code_tpl else "INSERT"),
            })
            num += 1
    return games
