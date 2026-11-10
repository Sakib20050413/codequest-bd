/* ==========================================================================
   CodeQuest — Visual 1-Minute Lesson Player & Animated Code-to-Game Engine
   Zero Robotic TTS • Real Step-by-Step Canvas Animations • 16 Languages
   ========================================================================== */

(function () {
  "use strict";

  const LANG_META = {
    python: {
      name: "Python 3",
      badge: "Backend, Automation & AI",
      cli: "python3 rover_move.py",
      color: "#10b981",
      whatItDoes: "Python uses simple, readable English-like commands to automate tasks, build backends, and control AI.",
      gameTitle: "Rover Maze Pathfinder Game",
      gameGoal: "Run the Python loop below to move the Rover step-by-step from Start (1,1) to the Green Flag (6,2)!",
      videoChapters: [
        { t: "0:00", title: "1. What is Python?", caption: "Python lets you write clean instructions without complex brackets. A list stores steps, and a 'for' loop runs each step one by one." },
        { t: "0:15", title: "2. How the Code Works", caption: "steps = ['RIGHT', 'RIGHT', 'DOWN', 'GOAL'] creates a list of 4 moves for our game rover." },
        { t: "0:30", title: "3. Loop Execution", caption: "for move in steps: repeats the print() command for every item in the list automatically." },
        { t: "0:45", title: "4. Play the Game Below", caption: "Click 'Run Code & Play Game' to execute this Python loop and watch the Rover drive to the Flag!" }
      ],
      starter: "# Move the Rover to the Green Flag using a Python list and loop\nsteps = ['MOVE_RIGHT', 'MOVE_RIGHT', 'MOVE_DOWN', 'REACH_FLAG']\n\nfor idx, action in enumerate(steps, 1):\n    print(f'Step {idx}: Rover -> {action}')"
    },
    html: {
      name: "HTML5",
      badge: "Webpage Structure",
      cli: "browser-render index.html",
      color: "#ea580c",
      whatItDoes: "HTML5 builds the structure of every website using tags like <h1> for headings, <p> for text, and <button> for buttons.",
      gameTitle: "Bridge Builder DOM Game",
      gameGoal: "Run the HTML code below to build the 3 bridge sections so the character can cross the river!",
      videoChapters: [
        { t: "0:00", title: "1. What is HTML?", caption: "Every webpage you visit is built with HTML tags. Tags tell the browser what is a heading, a paragraph, or a button." },
        { t: "0:15", title: "2. Opening & Closing Tags", caption: "Most elements start with an opening tag like <h2> and finish with a closing tag like </h2>." },
        { t: "0:30", title: "3. Nesting Elements", caption: "Putting a <h2> and <button> inside a <section> groups them together into a webpage card." },
        { t: "0:45", title: "4. Play the Game Below", caption: "Click 'Run Code & Play Game' to assemble the HTML bridge blocks across the river!" }
      ],
      starter: "<!-- Build the bridge card using HTML5 tags -->\n<section class=\"bridge-deck\">\n  <h2>River Crossing Bridge</h2>\n  <p>Bridge planks connected safely.</p>\n  <button>Cross Bridge</button>\n</section>"
    },
    css: {
      name: "CSS3 Flexbox",
      badge: "Website Styling & Layout",
      cli: "css-engine style.css",
      color: "#0284c7",
      whatItDoes: "CSS3 controls colors, spacing, and layout. Flexbox aligns items side-by-side in just 3 lines of code.",
      gameTitle: "Flexbox River Alignment Game",
      gameGoal: "Use display: flex and justify-content: space-between to line up the 3 floating planks into a straight bridge!",
      videoChapters: [
        { t: "0:00", title: "1. Why CSS Flexbox?", caption: "Without CSS, webpage boxes stack vertically or scatter. Flexbox lines them up cleanly across a row." },
        { t: "0:15", title: "2. display: flex", caption: "Adding display: flex; to a parent container turns all child boxes into flexible row items." },
        { t: "0:30", title: "3. Centering & Spacing", caption: "justify-content: space-between spreads the planks evenly; align-items: center lines them up vertically." },
        { t: "0:45", title: "4. Play the Game Below", caption: "Run the CSS code below to watch the crooked bridge planks snap into a straight line!" }
      ],
      starter: "/* Align the 3 bridge planks in a straight horizontal row */\n.river-bridge {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n  gap: 16px;\n}"
    },
    javascript: {
      name: "JavaScript (ES6+)",
      badge: "Interactive Web Logic",
      cli: "node game_controller.js",
      color: "#eab308",
      whatItDoes: "JavaScript makes websites and browser games interactive—handling clicks, animations, and live calculations.",
      gameTitle: "Energy Core Activator Game",
      gameGoal: "Run the JavaScript array loop to charge all 4 energy nodes to 100% power!",
      videoChapters: [
        { t: "0:00", title: "1. What is JavaScript?", caption: "HTML is the skeleton, CSS is the clothing, and JavaScript is the brain that makes a website respond to actions." },
        { t: "0:15", title: "2. Variables & Arrays", caption: "const nodes = ['Core-1', 'Core-2', 'Core-3'] stores multiple game objects in an array." },
        { t: "0:30", title: "3. Arrow Functions & Loops", caption: "nodes.forEach(node => console.log(...)) runs a function on every single item in the array." },
        { t: "0:45", title: "4. Play the Game Below", caption: "Run the JavaScript code to power up all 4 energy cores on the game board!" }
      ],
      starter: "// Activate all energy cores using JavaScript\nconst cores = ['Core-A', 'Core-B', 'Core-C', 'Core-D'];\ncores.forEach((name, idx) => {\n  console.log(`Node ${idx + 1} (${name}): Charged to 100%`);\n});"
    },
    react: {
      name: "React.js",
      badge: "Modern Frontend UI",
      cli: "vite build App.jsx",
      color: "#06b6d4",
      whatItDoes: "React builds modern web apps out of reusable components that automatically update when data (state) changes.",
      gameTitle: "React State Circuit Game",
      gameGoal: "Run the React component function to render the live voltage state on the circuit board!",
      videoChapters: [
        { t: "0:00", title: "1. What is React?", caption: "React lets you build custom UI components like <PowerGrid /> that automatically refresh when numbers change." },
        { t: "0:15", title: "2. Props & State", caption: "Components take inputs called 'props' (like voltage = 240) and return HTML-like JSX markup." },
        { t: "0:30", title: "3. Automatic UI Updates", caption: "When state changes, React updates only the exact part of the screen that changed." },
        { t: "0:45", title: "4. Play the Game Below", caption: "Run the React component below to sync the UI circuit nodes!" }
      ],
      starter: "// React Component returning JSX markup\nfunction PowerGrid({ voltage = 240 }) {\n  console.log(`React Component Rendered: ${voltage}V Online`);\n  return `<div class='grid-active'>${voltage}V</div>`;\n}\nPowerGrid({});"
    },
    django: {
      name: "Python Django 5",
      badge: "Full-Stack Python Backend",
      cli: "python3 manage.py shell",
      color: "#059669",
      whatItDoes: "Django is the Python web framework powering this site—connecting URLs, database models, and HTML templates.",
      gameTitle: "Server Route & ORM Game",
      gameGoal: "Run the Django route script to connect all web URLs to the database and guide the packet to the goal!",
      videoChapters: [
        { t: "0:00", title: "1. What is Django?", caption: "Django handles user login, database tables (ORM), and URL routing using Python." },
        { t: "0:15", title: "2. Model-View-Template (MVT)", caption: "Models define database tables, Views run Python logic, and Templates render the HTML page." },
        { t: "0:30", title: "3. URL Routing", caption: "When a user visits /courses/ or /games/, Django routes the request to the matching Python view." },
        { t: "0:45", title: "4. Play the Game Below", caption: "Run the Django script below to verify all server routes and move the data rover to the goal!" }
      ],
      starter: "# Verify Django web server routes\nroutes = ['/courses/', '/games/', '/playground/', '/contests/']\nfor r in routes:\n    print(f'[Django Server] Route {r:14s} -> 200 OK (Connected)')"
    },
    php: {
      name: "PHP 8 & MySQL",
      badge: "Server & Database Scripting",
      cli: "php php_sessional_crud/db.php",
      color: "#4f46e5",
      whatItDoes: "PHP runs on the web server and connects directly to MySQL databases using mysqli to save and load user records.",
      gameTitle: "PHP & MySQL Data Vault Game",
      gameGoal: "Run the PHP mysqli script below to connect to the SQL database and unlock the student records table!",
      videoChapters: [
        { t: "0:00", title: "1. What is PHP?", caption: "PHP is a server-side language widely used in web development labs to connect HTML forms to MySQL databases." },
        { t: "0:15", title: "2. mysqli_connect()", caption: "$conn = mysqli_connect('localhost', 'root', '', 'codequest_sql') opens a live link to the SQL database." },
        { t: "0:30", title: "3. Running SQL from PHP", caption: "PHP sends a SELECT query to MySQL and loops over the returned student rows." },
        { t: "0:45", title: "4. Play the Game Below", caption: "Click 'Run Code & Play Game' to execute the PHP-to-SQL connection and unlock the vault!" }
      ],
      starter: "<?php\n// Connect PHP 8 to the SQL Database using MySQLi\n$conn = mysqli_connect('localhost', 'root', '', 'codequest_sql');\necho \"[PHP MySQLi] Connected to SQL Database Successfully!\";\n$sql = \"SELECT student_id, name, department, cgpa, xp FROM students ORDER BY xp DESC\";\n?>"
    },
    sql: {
      name: "SQL & MySQL",
      badge: "Relational Databases",
      cli: "mysql -u root -e \"SELECT ...\"",
      color: "#0284c7",
      whatItDoes: "SQL (Structured Query Language) retrieves, filters, and sorts data stored in relational database tables.",
      gameTitle: "SQL Database Detective Game",
      gameGoal: "Run the SQL SELECT query below to scan the 'students' table and reveal the top-scoring students!",
      videoChapters: [
        { t: "0:00", title: "1. What is SQL?", caption: "Every app stores users, courses, and scores in database tables. SQL is the language used to ask questions of those tables." },
        { t: "0:15", title: "2. SELECT & FROM", caption: "SELECT name, xp FROM students tells the database which columns and which table you want to read." },
        { t: "0:30", title: "3. ORDER BY", caption: "ORDER BY xp DESC sorts the results from highest XP score to lowest." },
        { t: "0:45", title: "4. Play the Game Below", caption: "Run the SQL query below to scan the database table and unlock the records!" }
      ],
      starter: "-- Query the live students table in the database\nSELECT student_id, name, department, cgpa, course_streak, game_streak, xp\nFROM students\nORDER BY xp DESC;"
    },
    mongodb: {
      name: "MongoDB (NoSQL)",
      badge: "Document Database",
      cli: "mongosh --eval \"db.students.find()\"",
      color: "#16a34a",
      whatItDoes: "MongoDB stores data as flexible JSON documents instead of traditional rows and columns.",
      gameTitle: "NoSQL Document Scanner Game",
      gameGoal: "Run the mongosh query below to find all CSE department student documents in the collection!",
      videoChapters: [
        { t: "0:00", title: "1. What is MongoDB?", caption: "Instead of SQL tables, MongoDB stores JSON-like objects called documents inside collections." },
        { t: "0:15", title: "2. db.collection.find()", caption: "db.students.find({ dept: 'CSE' }) searches the students collection for matching JSON documents." },
        { t: "0:30", title: "3. Flexible Fields", caption: "Each document can hold arrays, nested objects, and dynamic fields without altering a rigid table schema." },
        { t: "0:45", title: "4. Play the Game Below", caption: "Run the mongosh command below to unlock the CSE student documents!" }
      ],
      starter: "// Find all students in the CSE department using MongoDB\ndb.students.find({\"dept\": \"CSE\"})"
    },
    c: {
      name: "C Programming",
      badge: "Systems & Hardware Core",
      cli: "gcc main.c -o main && ./main",
      color: "#0ea5e9",
      whatItDoes: "C is the foundational language of computer science—teaching you how memory, pointers, and CPUs work.",
      gameTitle: "Reactor Core Stabilizer (C)",
      gameGoal: "Compile and run the C program with printf() to lock the reactor voltage at 1200 mV!",
      videoChapters: [
        { t: "0:00", title: "1. Why Learn C?", caption: "C is the mother of modern programming languages and the foundation of university CSE labs." },
        { t: "0:15", title: "2. int main()", caption: "Every C program begins executing inside the int main() { ... } function." },
        { t: "0:30", title: "3. Variables & printf()", caption: "int voltage = 1200; stores a whole number in memory, and printf() prints it to the terminal." },
        { t: "0:45", title: "4. Play the Game Below", caption: "Compile and run the C code below to stabilize the 4 reactor rings!" }
      ],
      starter: "#include <stdio.h>\n\nint main() {\n    int core_voltage = 1200;\n    printf(\"C Reactor Stabilized at %d mV\\n\", core_voltage);\n    return 0;\n}"
    },
    cpp: {
      name: "C++ (Competitive & OOP)",
      badge: "IUPC Contests & Game Engines",
      cli: "g++ -std=c++20 main.cpp -o main && ./main",
      color: "#2563eb",
      whatItDoes: "C++ adds fast Standard Template Library (STL) data structures and Object-Oriented Programming to C.",
      gameTitle: "Rocket Trajectory Calculator (C++)",
      gameGoal: "Compile and run the C++ program with std::cout to launch the rocket into orbit!",
      videoChapters: [
        { t: "0:00", title: "1. Why Learn C++?", caption: "C++ is the #1 language for university IUPC competitive programming and high-speed game engines." },
        { t: "0:15", title: "2. #include <iostream>", caption: "iostream provides cout (character output) and cin (character input) for fast terminal I/O." },
        { t: "0:30", title: "3. std::cout <<", caption: "The << operator sends text and calculated numbers directly to the output screen." },
        { t: "0:45", title: "4. Play the Game Below", caption: "Run the C++ code below to compute the trajectory and power up the orbital nodes!" }
      ],
      starter: "#include <iostream>\nusing namespace std;\n\nint main() {\n    cout << \"C++20 Engine: Orbit Trajectory Locked (100%)\" << endl;\n    return 0;\n}"
    },
    java: {
      name: "Java (OOP)",
      badge: "Enterprise & Android OOP",
      cli: "javac Main.java && java Main",
      color: "#dc2626",
      whatItDoes: "Java organizes software into Classes and Objects, running anywhere via the Java Virtual Machine (JVM).",
      gameTitle: "JVM Shield Defense Game",
      gameGoal: "Compile and run the Java Main class to activate all 4 OOP shield generators!",
      videoChapters: [
        { t: "0:00", title: "1. What is Java?", caption: "Java is an Object-Oriented Programming (OOP) language used for Android apps and large backend systems." },
        { t: "0:15", title: "2. Class & main Method", caption: "In Java, all code lives inside a class (public class Main), and execution starts at public static void main." },
        { t: "0:30", title: "3. System.out.println()", caption: "System.out.println() prints your result line to the console output." },
        { t: "0:45", title: "4. Play the Game Below", caption: "Run the Java class below to activate the JVM defense matrix!" }
      ],
      starter: "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Java JVM Shield: All 4 OOP Nodes Active!\");\n    }\n}"
    },
    rust: {
      name: "Rust",
      badge: "Memory-Safe Systems",
      cli: "cargo run",
      color: "#d97706",
      whatItDoes: "Rust gives you C/C++ speed while guaranteeing zero memory crashes at compile time.",
      gameTitle: "Orbital Memory Core (Rust)",
      gameGoal: "Run the Rust fn main() program with println!() to lock the memory-safe orbital core!",
      videoChapters: [
        { t: "0:00", title: "1. What is Rust?", caption: "Rust is a modern systems language that prevents memory bugs before your program even runs." },
        { t: "0:15", title: "2. fn main() & let", caption: "Functions start with fn, and variables are created with let (immutable by default for safety)." },
        { t: "0:30", title: "3. println! Macro", caption: "println!(\"Status: {}\", status) safely formats and prints variables to the terminal." },
        { t: "0:45", title: "4. Play the Game Below", caption: "Run the Rust code below to synchronize the orbital rings!" }
      ],
      starter: "fn main() {\n    let status = \"Memory Safety Verified\";\n    println!(\"Rust Cargo Engine: {}\", status);\n}"
    },
    "ai-ml": {
      name: "AI & Machine Learning",
      badge: "Neural Networks & Data",
      cli: "python3 neural_net.py",
      color: "#0d9488",
      whatItDoes: "AI & Machine Learning programs multiply inputs by weights to recognize patterns and make smart predictions.",
      gameTitle: "AI Neural Pathfinder Game",
      gameGoal: "Run the Python neural network forward-pass below to guide the AI Rover to the goal!",
      videoChapters: [
        { t: "0:00", title: "1. How Does AI Learn?", caption: "A neural network takes input numbers, multiplies them by learned weights, adds a bias, and outputs a decision." },
        { t: "0:15", title: "2. Inputs & Weights", caption: "Each input feature is multiplied by its weight: sum(x * w for x, w in zip(inputs, weights))." },
        { t: "0:30", title: "3. ReLU Activation", caption: "max(0.0, total) is the ReLU activation function—keeping positive signals and zeroing out negative noise." },
        { t: "0:45", title: "4. Play the Game Below", caption: "Run the AI script below to compute the neuron output and steer the AI Rover to the flag!" }
      ],
      starter: "# Single Neuron Forward Pass (AI & Machine Learning)\ninputs = [0.9, 0.4, 0.8]\nweights = [0.5, 0.3, 0.7]\nbias = 0.12\n\noutput = round(max(0.0, sum(x * w for x, w in zip(inputs, weights)) + bias), 3)\nprint(f'AI Neuron Output = {output} -> Move Rover to Goal!')"
    }
  };

  function resolveLangKey(raw) {
    const s = (raw || "python").toLowerCase();
    if (s.includes("html")) return "html";
    if (s.includes("css")) return "css";
    if (s.includes("react")) return "react";
    if (s.includes("js") || s.includes("javascript") || s.includes("ts")) return "javascript";
    if (s.includes("django")) return "django";
    if (s.includes("ai") || s.includes("ml") || s.includes("neural")) return "ai-ml";
    if (s.includes("python") || s.includes("py")) return "python";
    if (s.includes("php")) return "php";
    if (s.includes("mongo") || s.includes("nosql")) return "mongodb";
    if (s.includes("sql") || s.includes("mysql") || s.includes("postgres")) return "sql";
    if (s.includes("rust") || s.includes("rs")) return "rust";
    if (s.includes("cpp") || s.includes("c++")) return "cpp";
    if (s === "c" || s.includes("c-lang") || s.includes("c prog")) return "c";
    if (s.includes("java")) return "java";
    return "python";
  }

  function getCsrfToken() {
    const match = document.cookie.match(/csrftoken=([^;]+)/);
    if (match) return match[1];
    const input = document.querySelector("[name=csrfmiddlewaretoken]");
    return input ? input.value : "";
  }

  // --------------------------------------------------------------------------
  // ANIMATED VISUAL GAME ENGINE (60fps Step-by-Step Animation When Code Runs!)
  // --------------------------------------------------------------------------
  const activeCanvasTimers = {};

  window.CQRenderGameCanvas = function (canvasId, rawLang, progressState, codeText) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;

    if (activeCanvasTimers[canvasId]) {
      cancelAnimationFrame(activeCanvasTimers[canvasId]);
      delete activeCanvasTimers[canvasId];
    }

    const langKey = resolveLangKey(rawLang);
    const meta = LANG_META[langKey] || LANG_META.python;
    const isSuccess = progressState >= 0.8;

    let animProgress = isSuccess ? 0.0 : 0.0;
    const targetProgress = isSuccess ? 1.0 : 0.15;

    function drawStep() {
      const ctx = canvas.getContext("2d");
      const rect = canvas.parentElement ? canvas.parentElement.getBoundingClientRect() : { width: 520 };
      const w = Math.max(300, rect.width || 520);
      const h = canvas.height || 220;
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = w * dpr;
      canvas.height = h * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

      // Background
      ctx.fillStyle = "#0f172a";
      ctx.fillRect(0, 0, w, h);

      // Top Game Mission Banner
      ctx.fillStyle = "#1e293b";
      ctx.fillRect(0, 0, w, 36);
      ctx.fillStyle = "#f8fafc";
      ctx.font = "700 12px 'Inter', sans-serif";
      ctx.fillText("🎮 " + meta.gameTitle + " (" + meta.name + ")", 12, 23);

      ctx.fillStyle = animProgress >= 0.95 ? "#34d399" : "#fbbf24";
      ctx.textAlign = "right";
      ctx.font = "600 11.5px 'Inter', sans-serif";
      ctx.fillText(animProgress >= 0.95 ? "✔ Goal Reached! (+XP & Game Streak)" : "▶ Run Code to Complete Mission", w - 12, 23);
      ctx.textAlign = "left";

      if (langKey === "html" || langKey === "css") {
        // River + Animated Bridge Planks + Character Crossing
        ctx.fillStyle = "#0369a1";
        ctx.fillRect(70, 50, w - 140, h - 75);

        // Left & Right River Banks
        ctx.fillStyle = "#15803d";
        ctx.fillRect(14, 50, 56, h - 75);
        ctx.fillRect(w - 70, 50, 56, h - 75);

        ctx.fillStyle = "#ffffff";
        ctx.font = "700 11px 'Inter', sans-serif";
        ctx.fillText("START", 22, 72);
        ctx.fillText("GOAL 🏁", w - 64, 72);

        const planks = 3;
        const bridgeW = w - 156;
        const pw = bridgeW / planks - 8;
        const targetY = h / 2 - 10;

        for (let i = 0; i < planks; i++) {
          const startY = 58 + i * 38;
          const py = startY + (targetY - startY) * animProgress;
          const px = 78 + i * (pw + 8);
          ctx.fillStyle = animProgress >= 0.9 ? "#10b981" : "#f59e0b";
          ctx.fillRect(px, py, pw, 32);
          ctx.strokeStyle = "#ffffff";
          ctx.strokeRect(px, py, pw, 32);
          ctx.fillStyle = "#0f172a";
          ctx.font = "700 11px 'JetBrains Mono', monospace";
          ctx.fillText("Plank " + (i + 1), px + 10, py + 20);
        }

        // Character moving across the bridge once aligned
        const charX = 36 + (w - 82) * Math.max(0, (animProgress - 0.3) / 0.7);
        const charY = targetY - 10;
        ctx.fillStyle = "#38bdf8";
        ctx.beginPath();
        ctx.arc(charX, charY, 10, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = "#ffffff";
        ctx.stroke();

      } else if (langKey === "python" || langKey === "ai-ml" || langKey === "django") {
        // Grid Maze where Rover drives step-by-step from (1,1) to Goal Flag (6,2)
        const cols = 8, rows = 4;
        const cw = Math.min(44, (w - 80) / cols);
        const sx = (w - cols * cw) / 2;
        const sy = 46;

        const pathWaypoints = [
          { c: 1, r: 1 },
          { c: 2, r: 1 },
          { c: 3, r: 1 },
          { c: 4, r: 1 },
          { c: 5, r: 1 },
          { c: 6, r: 1 },
          { c: 6, r: 2 }
        ];
        const activeStepIdx = Math.min(
          pathWaypoints.length - 1,
          Math.floor(animProgress * (pathWaypoints.length - 1))
        );

        for (let r = 0; r < rows; r++) {
          for (let c = 0; c < cols; c++) {
            const x = sx + c * cw, y = sy + r * cw;
            const isGoal = (c === 6 && r === 2);
            const isVisited = pathWaypoints.slice(0, activeStepIdx + 1).some(p => p.c === c && p.r === r);
            ctx.fillStyle = isGoal ? "rgba(16, 185, 129, 0.35)" : (isVisited ? "rgba(56, 189, 248, 0.28)" : "#1e293b");
            ctx.fillRect(x, y, cw - 4, cw - 4);
            ctx.strokeStyle = isGoal ? "#10b981" : (isVisited ? "#38bdf8" : "#334155");
            ctx.strokeRect(x, y, cw - 4, cw - 4);
            if (isGoal) {
              ctx.fillStyle = "#10b981";
              ctx.font = "700 12px 'Inter', sans-serif";
              ctx.fillText("🏁", x + cw * 0.25, y + cw * 0.62);
            }
          }
        }

        const currPos = pathWaypoints[activeStepIdx];
        const rx = sx + currPos.c * cw + (cw - 4) / 2;
        const ry = sy + currPos.r * cw + (cw - 4) / 2;
        ctx.fillStyle = animProgress >= 0.95 ? "#10b981" : "#38bdf8";
        ctx.beginPath();
        ctx.arc(rx, ry, cw * 0.34, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = "#0f172a";
        ctx.font = "700 9px 'JetBrains Mono', monospace";
        ctx.fillText("BOT", rx - 10, ry + 3);

      } else if (langKey === "sql" || langKey === "mongodb" || langKey === "php") {
        // Animated Database Table Scanner
        const rows = [
          ["STUDENT ID", "NAME", "DEPT", "SCORE / STATUS"],
          ["1119003", "Md Najmus Sakib", "CSE", animProgress > 0.3 ? "✔ 2,450 XP (Unlocked)" : "🔒 Locked Row"],
          ["1119026", "Nusrat Jahan", "CSE", animProgress > 0.6 ? "✔ 2,720 XP (Unlocked)" : "🔒 Locked Row"],
          ["1119014", "Tahmid Hasan", "CSE", animProgress > 0.9 ? "✔ 1,890 XP (Unlocked)" : "🔒 Locked Row"]
        ];
        rows.forEach(function (r, idx) {
          const y = 46 + idx * 36;
          const rowUnlocked = (idx === 1 && animProgress > 0.3) || (idx === 2 && animProgress > 0.6) || (idx === 3 && animProgress > 0.9);
          ctx.fillStyle = idx === 0 ? "#1e293b" : (rowUnlocked ? "rgba(16, 185, 129, 0.2)" : "#111827");
          ctx.fillRect(20, y, w - 40, 30);
          ctx.strokeStyle = rowUnlocked ? "#10b981" : "#334155";
          ctx.strokeRect(20, y, w - 40, 30);
          ctx.fillStyle = idx === 0 ? "#38bdf8" : "#f8fafc";
          ctx.font = (idx === 0 ? "700 " : "500 ") + "11px 'JetBrains Mono', monospace";
          r.forEach(function (cell, cIdx) {
            ctx.fillText(cell, 30 + cIdx * ((w - 60) / 4), y + 19);
          });
        });

      } else {
        // C / C++ / Java / Rust / JS / React Animated Energy Nodes & Rocket Core
        const cx = w / 2, cy = h / 2 + 8;
        for (let ring = 1; ring <= 3; ring++) {
          ctx.beginPath();
          ctx.arc(cx, cy, ring * 24, 0, Math.PI * 2);
          ctx.strokeStyle = animProgress >= ring * 0.3 ? "#10b981" : "#334155";
          ctx.lineWidth = 2;
          ctx.stroke();
        }
        for (let i = 0; i < 4; i++) {
          const ang = (i * Math.PI) / 2 + animProgress * 1.2;
          const nx = cx + Math.cos(ang) * 70;
          const ny = cy + Math.sin(ang) * 70;
          const activeNode = animProgress >= (i + 1) * 0.22;
          ctx.fillStyle = activeNode ? "#10b981" : "#f59e0b";
          ctx.beginPath();
          ctx.arc(nx, ny, 14, 0, Math.PI * 2);
          ctx.fill();
          ctx.fillStyle = "#0f172a";
          ctx.font = "700 9.5px 'JetBrains Mono', monospace";
          ctx.fillText(activeNode ? "ON" : "N" + (i + 1), nx - 8, ny + 3);
        }
      }

      // Bottom Mission Help Bar inside Canvas
      ctx.fillStyle = "rgba(15, 23, 42, 0.92)";
      ctx.fillRect(0, h - 24, w, 24);
      ctx.fillStyle = "#cbd5e1";
      ctx.font = "500 11px 'Inter', sans-serif";
      ctx.fillText(meta.gameGoal.slice(0, 88), 12, h - 8);

      if (animProgress < targetProgress) {
        animProgress = Math.min(targetProgress, animProgress + 0.035);
        activeCanvasTimers[canvasId] = requestAnimationFrame(drawStep);
      }
    }

    drawStep();
  };

  // --------------------------------------------------------------------------
  // VISUAL 1-MINUTE LESSON WALKTHROUGH PLAYER (Zero Robotic TTS!)
  // --------------------------------------------------------------------------
  window.CQInitMicroVideo = function (containerId, rawLang, lessonTitle) {
    const root = document.getElementById(containerId);
    if (!root) return;

    const langKey = resolveLangKey(rawLang);
    const meta = LANG_META[langKey] || LANG_META.python;
    const titleText = lessonTitle || (meta.name + " — 1-Minute Visual Guide");

    root.innerHTML = `
      <div style="background:var(--bg-surface); border:1px solid var(--border-medium); border-radius:8px; overflow:hidden; margin-bottom:14px;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px; padding:8px 14px; background:var(--bg-surface-elevated); border-bottom:1px solid var(--border-medium); font-size:0.82rem;">
          <div>
            <strong style="color:var(--text-primary);">🎬 1-Minute Visual Lesson Guide: ${meta.name}</strong>
            <span style="color:var(--text-muted); margin-left:6px; font-size:0.76rem;">(${meta.badge})</span>
          </div>
          <div style="display:flex; gap:6px; align-items:center;">
            <span id="${containerId}_timer" style="color:var(--text-secondary); font-family:var(--font-mono); font-size:0.75rem;">Step 1 of 4 (0:00 / 1:00)</span>
            <button type="button" id="${containerId}_speedBtn" class="w3-btn-outline" style="padding:2px 8px; font-size:0.72rem;">1.0x</button>
          </div>
        </div>

        <div style="position:relative;">
          <canvas id="${containerId}_canvas" height="175" style="width:100%; height:175px; display:block;"></canvas>
          <div id="${containerId}_caption" style="padding:10px 14px; background:var(--bg-surface); border-top:1px solid var(--border-subtle); color:var(--text-primary); font-size:0.86rem; line-height:1.55;">
            <strong>${meta.videoChapters[0].title}:</strong> ${meta.videoChapters[0].caption}
          </div>
        </div>

        <div style="padding:8px 14px; background:var(--bg-surface-elevated); border-top:1px solid var(--border-subtle); display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:8px;">
          <div style="display:flex; flex-wrap:wrap; gap:6px; align-items:center;">
            <button type="button" id="${containerId}_playBtn" class="w3-btn-green" style="padding:5px 12px; font-size:0.78rem;">▶ Play 1-Min Visual Guide</button>
            <div style="display:flex; flex-wrap:wrap; gap:4px;" id="${containerId}_chapters">
              ${meta.videoChapters.map((c, idx) => `<button type="button" data-ch="${idx}" class="w3-btn-outline" style="padding:3px 8px; font-size:0.74rem;">${c.title}</button>`).join("")}
            </div>
          </div>
          <input type="range" id="${containerId}_scrub" min="0" max="60" value="0" style="width:130px; accent-color:#04aa6d; cursor:pointer;" aria-label="Lesson timeline">
        </div>
      </div>
    `;

    let sec = 0;
    let playing = false;
    let speed = 1;
    let timerId = null;

    const canvas = document.getElementById(containerId + "_canvas");
    const captionEl = document.getElementById(containerId + "_caption");
    const timerEl = document.getElementById(containerId + "_timer");
    const scrubEl = document.getElementById(containerId + "_scrub");
    const playBtn = document.getElementById(containerId + "_playBtn");
    const speedBtn = document.getElementById(containerId + "_speedBtn");

    function drawFrame() {
      if (!canvas) return;
      const ctx = canvas.getContext("2d");
      const rect = canvas.parentElement.getBoundingClientRect();
      const w = Math.max(300, rect.width || 500);
      const h = 175;
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = w * dpr;
      canvas.height = h * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

      ctx.fillStyle = "#0f172a";
      ctx.fillRect(0, 0, w, h);

      const chIdx = Math.min(3, Math.floor(sec / 15));
      const ch = meta.videoChapters[chIdx];

      // Step Title
      ctx.fillStyle = "#34d399";
      ctx.font = "700 12px 'Inter', sans-serif";
      ctx.fillText(ch.title + " — " + titleText.slice(0, 48), 16, 24);

      // Plain-English Summary Line
      ctx.fillStyle = "#cbd5e1";
      ctx.font = "400 11.5px 'Inter', sans-serif";
      ctx.fillText(meta.whatItDoes.slice(0, 86), 16, 44);

      // Visual Code Box with Highlighted Active Line
      ctx.fillStyle = "#1e293b";
      ctx.fillRect(16, 54, w - 32, 102);
      ctx.strokeStyle = "#475569";
      ctx.lineWidth = 1;
      ctx.strokeRect(16, 54, w - 32, 102);

      const codeLines = meta.starter.split("\n").filter(Boolean).slice(0, 4);
      ctx.font = "500 11.5px 'JetBrains Mono', monospace";
      codeLines.forEach(function (ln, idx) {
        const isCurrentLine = idx === (chIdx % codeLines.length);
        if (isCurrentLine) {
          ctx.fillStyle = "rgba(16, 185, 129, 0.18)";
          ctx.fillRect(18, 62 + idx * 21, w - 36, 19);
        }
        ctx.fillStyle = isCurrentLine ? "#34d399" : "#e2e8f0";
        ctx.fillText((idx + 1) + "  " + ln.slice(0, 68), 26, 76 + idx * 21);
      });

      // Bottom Progress Bar
      ctx.fillStyle = "#334155";
      ctx.fillRect(0, h - 5, w, 5);
      ctx.fillStyle = "#10b981";
      ctx.fillRect(0, h - 5, (sec / 60) * w, 5);

      captionEl.innerHTML = "<strong>" + ch.title + ":</strong> " + ch.caption;
      const sPad = sec < 10 ? "0" + sec : sec;
      timerEl.textContent = "Step " + (chIdx + 1) + " of 4 (0:" + sPad + " / 1:00)";
      scrubEl.value = sec;
    }

    playBtn.addEventListener("click", function () {
      playing = !playing;
      if (playing) {
        playBtn.textContent = "⏸ Pause Guide";
        timerId = setInterval(function () {
          sec += 1;
          if (sec >= 60) {
            sec = 60;
            playing = false;
            playBtn.textContent = "↺ Replay Guide";
            clearInterval(timerId);
          }
          drawFrame();
        }, Math.round(1000 / speed));
      } else {
        playBtn.textContent = "▶ Resume Guide";
        clearInterval(timerId);
      }
    });

    scrubEl.addEventListener("input", function () {
      sec = parseInt(this.value, 10) || 0;
      drawFrame();
    });

    root.querySelectorAll("[data-ch]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        const idx = parseInt(this.getAttribute("data-ch"), 10) || 0;
        sec = idx * 15;
        drawFrame();
      });
    });

    speedBtn.addEventListener("click", function () {
      speed = speed === 1 ? 1.5 : (speed === 1.5 ? 2 : 1);
      this.textContent = speed.toFixed(1) + "x";
    });

    drawFrame();
  };

  // --------------------------------------------------------------------------
  // UNIVERSAL TERMINAL & GAME EXECUTION CLIENT
  // --------------------------------------------------------------------------
  window.CQExecuteTerminal = function (opts) {
    const lang = opts.language || "python";
    const code = opts.code || "";
    const cliCommand = opts.cliCommand || "";
    const outputEl = typeof opts.outputEl === "string" ? document.getElementById(opts.outputEl) : opts.outputEl;
    const canvasId = opts.canvasId || null;

    if (outputEl) {
      outputEl.textContent = "Running your code...";
    }

    return fetch("/api/terminal/execute/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCsrfToken()
      },
      body: JSON.stringify({
        language: lang,
        code: code,
        cli_command: cliCommand,
        submit_task: Boolean(opts.submitTask),
        task_title: opts.taskTitle || ""
      })
    })
      .then(function (r) { return r.json(); })
      .then(function (data) {
        if (outputEl) {
          outputEl.textContent = data.stdout || "Program executed successfully.";
        }
        if (canvasId) {
          window.CQRenderGameCanvas(canvasId, lang, data.ok ? 1.0 : 0.3, code);
        }
        if (data.xp_total && document.getElementById("xpCount")) {
          document.getElementById("xpCount").textContent = data.xp_total;
        }
        if (data.course_streak && document.getElementById("streakCount")) {
          document.getElementById("streakCount").textContent = data.course_streak + "d";
        }
        if (data.game_streak && document.getElementById("gameStreakCount")) {
          document.getElementById("gameStreakCount").textContent = data.game_streak + "d";
        }
        return data;
      })
      .catch(function (err) {
        if (outputEl) outputEl.textContent = "Error: " + err;
      });
  };

  window.CQLangMeta = LANG_META;
  window.CQResolveLangKey = resolveLangKey;
})();
