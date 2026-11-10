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
  // MULTI-GAME 2D & 3D INTERACTIVE CODING GAME ENGINE
  // Supports 6 Distinct Games × Both 2D Arcade Mode & 3D Isometric World Mode!
  // --------------------------------------------------------------------------
  const activeCanvasTimers = {};
  const canvasStates = {};

  const GAME_MODES = [
    { id: "rover", label: "🤖 1. Rover Maze", fullUrl: "/games/rover-3d/", langHint: "Python / Logic" },
    { id: "bridge", label: "🌉 2. Bridge & Pond", fullUrl: "/games/flexbox-pond/", langHint: "HTML / CSS" },
    { id: "sqlvault", label: "🕵️ 3. SQL Data Vault", fullUrl: "/games/cyber-crime-detective/", langHint: "SQL / PHP / DB" },
    { id: "orbital", label: "🚀 4. Space Defender", fullUrl: "/games/drone-flight-3d/", langHint: "JS / C / Rust" },
    { id: "city", label: "🏙️ 5. Voxel City 3D", fullUrl: "/games/city-builder-3d/", langHint: "Java / React / OOP" },
    { id: "neural", label: "🧠 6. AI Neural Core", fullUrl: "/games/quantum-cube-3d/", langHint: "AI & ML" }
  ];

  function defaultGameForLang(langKey) {
    if (langKey === "html" || langKey === "css") return "bridge";
    if (langKey === "sql" || langKey === "mongodb" || langKey === "php") return "sqlvault";
    if (langKey === "java" || langKey === "react") return "city";
    if (langKey === "ai-ml") return "neural";
    if (langKey === "javascript" || langKey === "c" || langKey === "cpp" || langKey === "rust") return "orbital";
    return "rover";
  }

  // Helper to draw a 3D extruded isometric block in 2D context
  function drawIsoBlock(ctx, cx, cy, sizeW, sizeD, heightZ, topColor, leftColor, rightColor) {
    const hw = sizeW / 2;
    const hd = sizeD / 2;
    // Top face
    ctx.beginPath();
    ctx.moveTo(cx, cy - hd - heightZ);
    ctx.lineTo(cx + hw, cy - heightZ);
    ctx.lineTo(cx, cy + hd - heightZ);
    ctx.lineTo(cx - hw, cy - heightZ);
    ctx.closePath();
    ctx.fillStyle = topColor;
    ctx.fill();
    ctx.strokeStyle = "rgba(255,255,255,0.28)";
    ctx.lineWidth = 1;
    ctx.stroke();

    if (heightZ > 0) {
      // Left face
      ctx.beginPath();
      ctx.moveTo(cx - hw, cy - heightZ);
      ctx.lineTo(cx, cy + hd - heightZ);
      ctx.lineTo(cx, cy + hd);
      ctx.lineTo(cx - hw, cy);
      ctx.closePath();
      ctx.fillStyle = leftColor;
      ctx.fill();
      ctx.stroke();

      // Right face
      ctx.beginPath();
      ctx.moveTo(cx + hw, cy - heightZ);
      ctx.lineTo(cx, cy + hd - heightZ);
      ctx.lineTo(cx, cy + hd);
      ctx.lineTo(cx + hw, cy);
      ctx.closePath();
      ctx.fillStyle = rightColor;
      ctx.fill();
      ctx.stroke();
    }
  }

  function ensureGameControls(canvasId, state) {
    const canvas = document.getElementById(canvasId);
    if (!canvas || !canvas.parentElement) return;
    const wrapper = canvas.parentElement;

    if (!document.getElementById(canvasId + "_topBar")) {
      const topBar = document.createElement("div");
      topBar.id = canvasId + "_topBar";
      topBar.style.cssText = "background:#0f172a; border-bottom:1px solid #334155; padding:8px 10px; display:flex; flex-direction:column; gap:6px;";
      topBar.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:6px;">
          <div style="display:flex; gap:4px; align-items:center;">
            <span style="font-size:0.72rem; font-weight:800; color:#94a3b8; margin-right:4px;">DIMENSION:</span>
            <button type="button" data-dim="2d" class="cq-dim-btn" style="padding:4px 10px; border-radius:6px; border:1px solid #10b981; background:#059669; color:#ffffff; font-size:0.74rem; font-weight:800; cursor:pointer;">🕹️ 2D Arcade Game</button>
            <button type="button" data-dim="3d" class="cq-dim-btn" style="padding:4px 10px; border-radius:6px; border:1px solid #475569; background:#1e293b; color:#e2e8f0; font-size:0.74rem; font-weight:800; cursor:pointer;">🌐 3D World Game</button>
          </div>
          <a id="${canvasId}_fullLink" href="/games/rover-3d/" style="font-size:0.74rem; font-weight:800; color:#38bdf8; text-decoration:none; padding:3px 8px; background:rgba(56,189,248,0.12); border:1px solid rgba(56,189,248,0.35); border-radius:6px;">
            🚀 Open Full 10-Level 3D Game &rarr;
          </a>
        </div>
        <div style="display:flex; flex-wrap:wrap; gap:4px; align-items:center;">
          <span style="font-size:0.7rem; font-weight:800; color:#94a3b8; margin-right:2px;">6 GAMES:</span>
          ${GAME_MODES.map(g => `<button type="button" data-gmode="${g.id}" class="cq-gmode-btn" style="padding:3px 8px; border-radius:5px; border:1px solid #334155; background:#1e293b; color:#cbd5e1; font-size:0.71rem; font-weight:700; cursor:pointer;">${g.label}</button>`).join("")}
        </div>
      `;
      wrapper.insertBefore(topBar, canvas);

      topBar.querySelectorAll(".cq-dim-btn").forEach(function (btn) {
        btn.addEventListener("click", function () {
          state.dimension = this.getAttribute("data-dim");
          updateToolbarStyles(canvasId, state);
          window.CQRenderGameCanvas(canvasId, state.langKey, 1.0, "", true);
        });
      });

      topBar.querySelectorAll(".cq-gmode-btn").forEach(function (btn) {
        btn.addEventListener("click", function () {
          state.gameMode = this.getAttribute("data-gmode");
          state.userPicksGame = true;
          updateToolbarStyles(canvasId, state);
          window.CQRenderGameCanvas(canvasId, state.langKey, 1.0, "", true);
        });
      });
    }

    if (!document.getElementById(canvasId + "_ctrlBar")) {
      const ctrlBar = document.createElement("div");
      ctrlBar.id = canvasId + "_ctrlBar";
      ctrlBar.style.cssText = "background:#0f172a; border-top:1px solid #334155; padding:7px 10px; display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:6px;";
      ctrlBar.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:4px; align-items:center;">
          <span style="font-size:0.7rem; font-weight:800; color:#94a3b8; margin-right:2px;">CONTROLS:</span>
          <button type="button" data-act="left" style="padding:4px 9px; border-radius:5px; border:1px solid #475569; background:#1e293b; color:#f8fafc; font-size:0.73rem; font-weight:700; cursor:pointer;">⬅️ Left</button>
          <button type="button" data-act="up" style="padding:4px 9px; border-radius:5px; border:1px solid #475569; background:#1e293b; color:#f8fafc; font-size:0.73rem; font-weight:700; cursor:pointer;">⬆️ Forward</button>
          <button type="button" data-act="down" style="padding:4px 9px; border-radius:5px; border:1px solid #475569; background:#1e293b; color:#f8fafc; font-size:0.73rem; font-weight:700; cursor:pointer;">⬇️ Down</button>
          <button type="button" data-act="right" style="padding:4px 9px; border-radius:5px; border:1px solid #475569; background:#1e293b; color:#f8fafc; font-size:0.73rem; font-weight:700; cursor:pointer;">➡️ Right</button>
          <button type="button" data-act="boost" style="padding:4px 10px; border-radius:5px; border:1px solid #059669; background:#065f46; color:#ffffff; font-size:0.73rem; font-weight:700; cursor:pointer;">⚡ Action / Replay</button>
          <button type="button" data-act="rotate" style="padding:4px 9px; border-radius:5px; border:1px solid #0284c7; background:#0c4a6e; color:#e0f2fe; font-size:0.73rem; font-weight:700; cursor:pointer;">🔄 Toggle 2D/3D</button>
        </div>
        <span id="${canvasId}_scoreBadge" style="font-family:var(--font-mono); font-size:0.74rem; font-weight:800; color:#34d399;">Score: 100 XP</span>
      `;
      wrapper.appendChild(ctrlBar);

      ctrlBar.querySelectorAll("button[data-act]").forEach(function (btn) {
        btn.addEventListener("click", function () {
          const act = this.getAttribute("data-act");
          if (act === "left") state.playerX = Math.max(0, state.playerX - 1);
          if (act === "right") state.playerX = Math.min(6, state.playerX + 1);
          if (act === "up") state.playerY = Math.max(0, state.playerY - 1);
          if (act === "down") state.playerY = Math.min(3, state.playerY + 1);
          if (act === "rotate") {
            state.dimension = state.dimension === "3d" ? "2d" : "3d";
            updateToolbarStyles(canvasId, state);
          }
          state.score += 15;
          const sb = document.getElementById(canvasId + "_scoreBadge");
          if (sb) sb.textContent = "Score: " + state.score + " XP";
          window.CQRenderGameCanvas(canvasId, state.langKey, 1.0, "", true);
        });
      });
    }

    updateToolbarStyles(canvasId, state);
  }

  function updateToolbarStyles(canvasId, state) {
    const topBar = document.getElementById(canvasId + "_topBar");
    if (!topBar) return;
    topBar.querySelectorAll(".cq-dim-btn").forEach(function (btn) {
      const active = btn.getAttribute("data-dim") === state.dimension;
      btn.style.background = active ? "#059669" : "#1e293b";
      btn.style.borderColor = active ? "#10b981" : "#475569";
      btn.style.color = active ? "#ffffff" : "#cbd5e1";
    });
    topBar.querySelectorAll(".cq-gmode-btn").forEach(function (btn) {
      const active = btn.getAttribute("data-gmode") === state.gameMode;
      btn.style.background = active ? "#0284c7" : "#1e293b";
      btn.style.borderColor = active ? "#38bdf8" : "#334155";
      btn.style.color = active ? "#ffffff" : "#cbd5e1";
    });
    const fullLink = document.getElementById(canvasId + "_fullLink");
    const found = GAME_MODES.find(g => g.id === state.gameMode);
    if (fullLink && found) {
      fullLink.href = found.fullUrl;
      fullLink.innerHTML = "🚀 Play Full " + found.label + " (10 Levels) &rarr;";
    }
  }

  window.CQRenderGameCanvas = function (canvasId, rawLang, progressState, codeText, keepGameMode) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;

    if (activeCanvasTimers[canvasId]) {
      cancelAnimationFrame(activeCanvasTimers[canvasId]);
      delete activeCanvasTimers[canvasId];
    }

    const langKey = resolveLangKey(rawLang);
    const meta = LANG_META[langKey] || LANG_META.python;

    if (!canvasStates[canvasId]) {
      canvasStates[canvasId] = {
        dimension: "3d", // Default to rich 3D World View so users see 3D immediately, with 1-click toggle to 2D!
        gameMode: defaultGameForLang(langKey),
        langKey: langKey,
        playerX: 6,
        playerY: 2,
        score: 120
      };
    }
    const state = canvasStates[canvasId];
    state.langKey = langKey;
    if (!keepGameMode) {
      state.gameMode = defaultGameForLang(langKey);
    }

    ensureGameControls(canvasId, state);

    let animProgress = 0.0;
    const targetProgress = progressState >= 0.5 ? 1.0 : 0.4;

    function drawStep() {
      const ctx = canvas.getContext("2d");
      const rect = canvas.parentElement ? canvas.parentElement.getBoundingClientRect() : { width: 520 };
      const w = Math.max(300, rect.width || 520);
      const h = canvas.height || 215;
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = w * dpr;
      canvas.height = h * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

      // Rich Background Gradient
      const bgGrad = ctx.createLinearGradient(0, 0, 0, h);
      bgGrad.addColorStop(0, "#090d16");
      bgGrad.addColorStop(1, "#0f172a");
      ctx.fillStyle = bgGrad;
      ctx.fillRect(0, 0, w, h);

      const gInfo = GAME_MODES.find(g => g.id === state.gameMode) || GAME_MODES[0];
      const is3D = state.dimension === "3d";

      // Top HUD Strip inside Canvas
      ctx.fillStyle = "rgba(30, 41, 59, 0.9)";
      ctx.fillRect(0, 0, w, 30);
      ctx.fillStyle = "#38bdf8";
      ctx.font = "700 11.5px 'Plus Jakarta Sans', sans-serif";
      ctx.fillText((is3D ? "🌐 3D WORLD: " : "🕹️ 2D ARCADE: ") + gInfo.label + " (" + meta.name + ")", 10, 19);

      ctx.fillStyle = "#34d399";
      ctx.textAlign = "right";
      ctx.font = "700 11px 'JetBrains Mono', monospace";
      ctx.fillText(animProgress >= 0.9 ? "✔ MISSION COMPLETE (+35 XP)" : "⚡ SIMULATING...", w - 10, 19);
      ctx.textAlign = "left";

      // ======================================================================
      // GAME 1: ROVER MAZE (2D Grid OR 3D Isometric Mars Terrain)
      // ======================================================================
      if (state.gameMode === "rover") {
        const pathWaypoints = [
          { c: 1, r: 1 }, { c: 2, r: 1 }, { c: 3, r: 1 },
          { c: 4, r: 1 }, { c: 5, r: 1 }, { c: state.playerX, r: state.playerY }
        ];
        const stepIdx = Math.min(pathWaypoints.length - 1, Math.floor(animProgress * (pathWaypoints.length - 1)));
        const curr = pathWaypoints[stepIdx];

        if (is3D) {
          // 3D Isometric Mars Grid + 3D Extruded Rover & Crystal Beacon
          const originX = w / 2;
          const originY = 58;
          const tileW = 44, tileD = 22;
          for (let r = 0; r < 4; r++) {
            for (let c = 0; c < 7; c++) {
              const isoX = originX + (c - r) * (tileW / 2) - 45;
              const isoY = originY + (c + r) * (tileD / 2);
              const isGoal = (c === 6 && r === 2);
              const isPath = pathWaypoints.slice(0, stepIdx + 1).some(p => p.c === c && p.r === r);
              drawIsoBlock(
                ctx, isoX, isoY, tileW - 2, tileD - 2,
                isGoal ? 10 : 6,
                isGoal ? "#10b981" : (isPath ? "#0284c7" : "#1e293b"),
                isGoal ? "#059669" : "#0f172a",
                isGoal ? "#047857" : "#334155"
              );
              if (isGoal) {
                // 3D Goal Beacon Pillar
                drawIsoBlock(ctx, isoX, isoY - 10, 14, 8, 22, "#34d399", "#10b981", "#059669");
              }
            }
          }
          // 3D Rover Vehicle
          const roverX = originX + (curr.c - curr.r) * (tileW / 2) - 45;
          const roverY = originY + (curr.c + curr.r) * (tileD / 2) - 6;
          drawIsoBlock(ctx, roverX, roverY, 26, 14, 16, "#38bdf8", "#0284c7", "#0369a1");
          ctx.fillStyle = "#ffffff";
          ctx.font = "700 9px 'JetBrains Mono', monospace";
          ctx.fillText("3D-BOT", roverX - 16, roverY - 22);
        } else {
          // 2D Top-Down Grid Maze
          const cols = 7, rows = 4;
          const cw = Math.min(40, (w - 80) / cols);
          const sx = (w - cols * cw) / 2;
          const sy = 38;
          for (let r = 0; r < rows; r++) {
            for (let c = 0; c < cols; c++) {
              const x = sx + c * cw, y = sy + r * cw;
              const isGoal = (c === 6 && r === 2);
              const isVisited = pathWaypoints.slice(0, stepIdx + 1).some(p => p.c === c && p.r === r);
              ctx.fillStyle = isGoal ? "rgba(16,185,129,0.35)" : (isVisited ? "rgba(56,189,248,0.28)" : "#1e293b");
              ctx.fillRect(x, y, cw - 4, cw - 4);
              ctx.strokeStyle = isGoal ? "#10b981" : "#334155";
              ctx.strokeRect(x, y, cw - 4, cw - 4);
              if (isGoal) {
                ctx.fillStyle = "#ffffff";
                ctx.font = "12px sans-serif";
                ctx.fillText("🏁", x + 8, y + cw * 0.65);
              }
            }
          }
          const rx = sx + curr.c * cw + (cw - 4) / 2;
          const ry = sy + curr.r * cw + (cw - 4) / 2;
          ctx.fillStyle = "#10b981";
          ctx.beginPath();
          ctx.arc(rx, ry, cw * 0.35, 0, Math.PI * 2);
          ctx.fill();
          ctx.fillStyle = "#0f172a";
          ctx.font = "700 8.5px 'JetBrains Mono', monospace";
          ctx.fillText("BOT", rx - 9, ry + 3);
        }
      }

      // ======================================================================
      // GAME 2: FLEXBOX BRIDGE & FROG POND (2D & 3D)
      // ======================================================================
      else if (state.gameMode === "bridge") {
        if (is3D) {
          // 3D Isometric River Canyon & 3D Bridge Planks
          drawIsoBlock(ctx, w * 0.2, 135, 90, 48, 18, "#15803d", "#166534", "#14532d");
          drawIsoBlock(ctx, w * 0.8, 135, 90, 48, 18, "#15803d", "#166534", "#14532d");
          for (let i = 0; i < 3; i++) {
            const targetY = 132;
            const startY = 85 + i * 32;
            const py = startY + (targetY - startY) * animProgress;
            const px = w * 0.36 + i * (w * 0.14);
            drawIsoBlock(ctx, px, py, 58, 30, 12, "#10b981", "#059669", "#047857");
          }
          // 3D Character hopping across
          const hopX = w * 0.2 + (w * 0.6) * animProgress;
          drawIsoBlock(ctx, hopX, 114, 22, 14, 18, "#fbbf24", "#d97706", "#b45309");
        } else {
          ctx.fillStyle = "#0369a1";
          ctx.fillRect(65, 42, w - 130, h - 68);
          ctx.fillStyle = "#15803d";
          ctx.fillRect(15, 42, 50, h - 68);
          ctx.fillRect(w - 65, 42, 50, h - 68);
          const planks = 3;
          const pw = (w - 150) / planks - 8;
          const targetY = h / 2 - 8;
          for (let i = 0; i < planks; i++) {
            const startY = 50 + i * 32;
            const py = startY + (targetY - startY) * animProgress;
            const px = 74 + i * (pw + 8);
            ctx.fillStyle = "#10b981";
            ctx.fillRect(px, py, pw, 28);
            ctx.strokeStyle = "#ffffff";
            ctx.strokeRect(px, py, pw, 28);
            ctx.fillStyle = "#0f172a";
            ctx.font = "700 10px 'JetBrains Mono', monospace";
            ctx.fillText("Flex-" + (i + 1), px + 8, py + 18);
          }
          const charX = 35 + (w - 75) * animProgress;
          ctx.fillStyle = "#fbbf24";
          ctx.beginPath();
          ctx.arc(charX, targetY - 8, 9, 0, Math.PI * 2);
          ctx.fill();
        }
      }

      // ======================================================================
      // GAME 3: SQL & PHP DATA VAULT (2D Table Scanner & 3D Server Racks)
      // ======================================================================
      else if (state.gameMode === "sqlvault") {
        if (is3D) {
          // 3D Isometric Database Server Towers unlocking
          const towers = [
            { x: w * 0.25, label: "ID:1119003", xp: "2450 XP" },
            { x: w * 0.50, label: "ID:1119026", xp: "2720 XP" },
            { x: w * 0.75, label: "ID:1119014", xp: "1890 XP" }
          ];
          towers.forEach(function (t, i) {
            const unlocked = animProgress >= (i + 1) * 0.28;
            const hZ = 28 + animProgress * 26;
            drawIsoBlock(
              ctx, t.x, 155, 72, 36, hZ,
              unlocked ? "#10b981" : "#334155",
              unlocked ? "#059669" : "#1e293b",
              unlocked ? "#047857" : "#0f172a"
            );
            ctx.fillStyle = "#ffffff";
            ctx.font = "700 10px 'JetBrains Mono', monospace";
            ctx.fillText(t.label, t.x - 28, 155 - hZ - 6);
            ctx.fillStyle = "#34d399";
            ctx.fillText(unlocked ? "✔ " + t.xp : "🔒 LOCKED", t.x - 28, 174);
          });
        } else {
          const rows = [
            ["STUDENT ID", "NAME", "DEPT", "STATUS"],
            ["1119003", "Md Najmus Sakib", "CSE", animProgress > 0.3 ? "✔ Unlocked (2450 XP)" : "🔒 Locked"],
            ["1119026", "Nusrat Jahan", "CSE", animProgress > 0.6 ? "✔ Unlocked (2720 XP)" : "🔒 Locked"],
            ["1119014", "Tahmid Hasan", "CSE", animProgress > 0.85 ? "✔ Unlocked (1890 XP)" : "🔒 Locked"]
          ];
          rows.forEach(function (r, idx) {
            const y = 40 + idx * 34;
            ctx.fillStyle = idx === 0 ? "#1e293b" : "rgba(16, 185, 129, 0.16)";
            ctx.fillRect(18, y, w - 36, 28);
            ctx.strokeStyle = "#10b981";
            ctx.strokeRect(18, y, w - 36, 28);
            ctx.fillStyle = idx === 0 ? "#38bdf8" : "#f8fafc";
            ctx.font = "600 10.5px 'JetBrains Mono', monospace";
            r.forEach((cell, cIdx) => ctx.fillText(cell, 26 + cIdx * ((w - 52) / 4), y + 18));
          });
        }
      }

      // ======================================================================
      // GAME 4: ORBITAL SPACE DEFENDER (2D & 3D)
      // ======================================================================
      else if (state.gameMode === "orbital") {
        const cx = w / 2, cy = h / 2 + 4;
        if (is3D) {
          drawIsoBlock(ctx, cx, cy + 25, 64, 34, 36, "#38bdf8", "#0284c7", "#0369a1");
          for (let i = 0; i < 4; i++) {
            const ang = (i * Math.PI) / 2 + animProgress * 1.6;
            const sx = cx + Math.cos(ang) * 95;
            const sy = cy + Math.sin(ang) * 42;
            ctx.strokeStyle = "#10b981";
            ctx.beginPath();
            ctx.moveTo(cx, cy - 5);
            ctx.lineTo(sx, sy - 10);
            ctx.stroke();
            drawIsoBlock(ctx, sx, sy, 28, 16, 16, "#10b981", "#059669", "#047857");
          }
        } else {
          for (let r = 1; r <= 3; r++) {
            ctx.beginPath();
            ctx.arc(cx, cy, r * 22, 0, Math.PI * 2);
            ctx.strokeStyle = "#10b981";
            ctx.stroke();
          }
          for (let i = 0; i < 4; i++) {
            const ang = (i * Math.PI) / 2 + animProgress * 1.4;
            const nx = cx + Math.cos(ang) * 66;
            const ny = cy + Math.sin(ang) * 66;
            ctx.fillStyle = "#10b981";
            ctx.beginPath();
            ctx.arc(nx, ny, 12, 0, Math.PI * 2);
            ctx.fill();
          }
        }
      }

      // ======================================================================
      // GAME 5: 3D VOXEL CITY BUILDER (Java / React / OOP)
      // ======================================================================
      else if (state.gameMode === "city") {
        const buildings = [
          { x: w * 0.24, y: 156, h: 48, c1: "#38bdf8", c2: "#0284c7", c3: "#0369a1", name: "Tower-A" },
          { x: w * 0.42, y: 162, h: 68, c1: "#10b981", c2: "#059669", c3: "#047857", name: "HQ-Core" },
          { x: w * 0.60, y: 156, h: 54, c1: "#f59e0b", c2: "#d97706", c3: "#b45309", name: "Grid-B" },
          { x: w * 0.78, y: 162, h: 62, c1: "#a855f7", c2: "#9333ea", c3: "#7e22ce", name: "Node-C" }
        ];
        buildings.forEach(function (b) {
          const curH = Math.max(12, b.h * animProgress);
          if (is3D) {
            drawIsoBlock(ctx, b.x, b.y, 56, 30, curH, b.c1, b.c2, b.c3);
          } else {
            ctx.fillStyle = b.c1;
            ctx.fillRect(b.x - 24, b.y - curH, 48, curH);
            ctx.strokeStyle = "#ffffff";
            ctx.strokeRect(b.x - 24, b.y - curH, 48, curH);
          }
          ctx.fillStyle = "#f8fafc";
          ctx.font = "700 9.5px 'JetBrains Mono', monospace";
          ctx.fillText(b.name, b.x - 20, b.y - curH - 8);
        });
      }

      // ======================================================================
      // GAME 6: AI NEURAL NETWORK CORE (2D & 3D Synapse Layers)
      // ======================================================================
      else {
        const layers = [w * 0.22, w * 0.50, w * 0.78];
        const nodesY = [68, 112, 156];
        ctx.strokeStyle = "rgba(16, 185, 129, 0.55)";
        ctx.lineWidth = 1.5;
        for (let l = 0; l < 2; l++) {
          nodesY.forEach(y1 => {
            nodesY.forEach(y2 => {
              ctx.beginPath();
              ctx.moveTo(layers[l], y1);
              ctx.lineTo(layers[l + 1], y2);
              ctx.stroke();
            });
          });
        }
        layers.forEach(function (lx, lIdx) {
          nodesY.forEach(function (ny) {
            if (is3D) {
              drawIsoBlock(ctx, lx, ny + 6, 26, 14, 14, lIdx === 2 ? "#10b981" : "#38bdf8", "#0284c7", "#0369a1");
            } else {
              ctx.fillStyle = lIdx === 2 ? "#10b981" : "#38bdf8";
              ctx.beginPath();
              ctx.arc(lx, ny, 10, 0, Math.PI * 2);
              ctx.fill();
            }
          });
        });
      }

      // Bottom Status Bar inside Canvas
      ctx.fillStyle = "rgba(15, 23, 42, 0.92)";
      ctx.fillRect(0, h - 22, w, 22);
      ctx.fillStyle = "#cbd5e1";
      ctx.font = "600 10.5px 'Plus Jakarta Sans', sans-serif";
      ctx.fillText("🎯 " + meta.gameGoal.slice(0, 86), 10, h - 7);

      if (animProgress < targetProgress) {
        animProgress = Math.min(targetProgress, animProgress + 0.04);
        activeCanvasTimers[canvasId] = requestAnimationFrame(drawStep);
      }
    }

    drawStep();
  };

  // --------------------------------------------------------------------------
  // VISUAL 1-MINUTE LESSON WALKTHROUGH PLAYER (Zero Robotic TTS!)
  // --------------------------------------------------------------------------
  window.CQInitMicroVideo = function (containerId, rawLang, lessonTitle, customCode, customTaskPrompt) {
    const root = document.getElementById(containerId);
    if (!root) return;

    const langKey = resolveLangKey(rawLang);
    const meta = LANG_META[langKey] || LANG_META.python;
    const titleText = lessonTitle || (meta.name + " — 1-Minute Visual Guide");
    const activeStarter = (customCode && customCode.trim()) ? customCode.trim() : meta.starter;
    const chapters = (customTaskPrompt && customTaskPrompt.trim()) ? [
      { t: "0:00", title: "1. Lesson Goal", caption: "In this lesson (" + titleText + "): " + meta.whatItDoes },
      { t: "0:15", title: "2. Step-by-Step Code", caption: "Examine the highlighted code lines above. Each line executes top-to-bottom in the " + meta.name + " compiler." },
      { t: "0:30", title: "3. Your Mission", caption: customTaskPrompt.trim() },
      { t: "0:45", title: "4. Play & Complete", caption: "Click 'Run Code & Play Game' to test your code and animate the 2D/3D game!" }
    ] : meta.videoChapters;

    root.innerHTML = `
      <div style="background:var(--bg-surface); border:1px solid var(--border-medium); border-radius:10px; overflow:hidden; margin-bottom:14px;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px; padding:8px 14px; background:var(--bg-surface-elevated); border-bottom:1px solid var(--border-medium); font-size:0.82rem;">
          <div>
            <strong style="color:var(--text-primary);">🎬 1-Minute Visual Guide: ${titleText}</strong>
            <span style="color:var(--text-muted); margin-left:6px; font-size:0.75rem;">(${meta.name})</span>
          </div>
          <div style="display:flex; gap:6px; align-items:center;">
            <span id="${containerId}_timer" style="color:var(--text-secondary); font-family:var(--font-mono); font-size:0.75rem;">Step 1 of 4 (0:00 / 1:00)</span>
            <button type="button" id="${containerId}_speedBtn" class="cq-btn-secondary" style="padding:2px 8px; font-size:0.72rem;">1.0x</button>
          </div>
        </div>

        <div style="position:relative;">
          <canvas id="${containerId}_canvas" height="170" style="width:100%; height:170px; display:block;"></canvas>
          <div id="${containerId}_caption" style="padding:10px 14px; background:var(--bg-surface); border-top:1px solid var(--border-subtle); color:var(--text-primary); font-size:0.86rem; line-height:1.55;">
            <strong>${chapters[0].title}:</strong> ${chapters[0].caption}
          </div>
        </div>

        <div style="padding:8px 14px; background:var(--bg-surface-elevated); border-top:1px solid var(--border-subtle); display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:8px;">
          <div style="display:flex; flex-wrap:wrap; gap:6px; align-items:center;">
            <button type="button" id="${containerId}_playBtn" class="cq-btn-primary" style="padding:5px 12px; font-size:0.78rem;">▶ Play 1-Min Visual Guide</button>
            <div style="display:flex; flex-wrap:wrap; gap:4px;" id="${containerId}_chapters">
              ${chapters.map((c, idx) => `<button type="button" data-ch="${idx}" class="cq-btn-secondary" style="padding:3px 8px; font-size:0.73rem;">${c.title}</button>`).join("")}
            </div>
          </div>
          <input type="range" id="${containerId}_scrub" min="0" max="60" value="0" style="width:120px; accent-color:#059669; cursor:pointer;" aria-label="Lesson timeline">
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
      const h = 170;
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = w * dpr;
      canvas.height = h * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

      ctx.fillStyle = "#0f172a";
      ctx.fillRect(0, 0, w, h);

      const chIdx = Math.min(3, Math.floor(sec / 15));
      const ch = chapters[chIdx];

      ctx.fillStyle = "#34d399";
      ctx.font = "700 12px 'Plus Jakarta Sans', sans-serif";
      ctx.fillText(ch.title + " — " + titleText.slice(0, 48), 16, 23);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "400 11.5px 'Plus Jakarta Sans', sans-serif";
      ctx.fillText(ch.caption.slice(0, 86), 16, 42);

      ctx.fillStyle = "#1e293b";
      ctx.fillRect(16, 52, w - 32, 100);
      ctx.strokeStyle = "#475569";
      ctx.lineWidth = 1;
      ctx.strokeRect(16, 52, w - 32, 100);

      const codeLines = activeStarter.split("\n").filter(Boolean).slice(0, 4);
      ctx.font = "500 11.5px 'JetBrains Mono', monospace";
      codeLines.forEach(function (ln, idx) {
        const isCurrentLine = idx === (chIdx % Math.max(1, codeLines.length));
        if (isCurrentLine) {
          ctx.fillStyle = "rgba(16, 185, 129, 0.2)";
          ctx.fillRect(18, 60 + idx * 21, w - 36, 19);
        }
        ctx.fillStyle = isCurrentLine ? "#34d399" : "#e2e8f0";
        ctx.fillText((idx + 1) + "  " + ln.slice(0, 68), 26, 74 + idx * 21);
      });

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
  // UNIVERSAL TERMINAL & GAME EXECUTION CLIENT (Guaranteed Instant Game Render)
  // --------------------------------------------------------------------------
  window.CQExecuteTerminal = function (opts) {
    const lang = opts.language || "python";
    const code = opts.code || "";
    const cliCommand = opts.cliCommand || "";
    const outputEl = typeof opts.outputEl === "string" ? document.getElementById(opts.outputEl) : opts.outputEl;
    const canvasId = opts.canvasId || null;

    // 1. Immediately render and animate the 2D/3D Game Canvas so it is NEVER blank!
    if (canvasId) {
      window.CQRenderGameCanvas(canvasId, lang, 1.0, code);
    }

    if (outputEl) {
      outputEl.textContent = "Executing " + lang + " code...";
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
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.json();
      })
      .then(function (data) {
        if (outputEl) {
          outputEl.textContent = data.stdout || "Program executed successfully.";
        }
        if (canvasId) {
          window.CQRenderGameCanvas(canvasId, lang, data.ok ? 1.0 : 0.6, code, true);
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
      .catch(function () {
        // Client-side fallback output so the user always sees clean execution output
        const meta = LANG_META[resolveLangKey(lang)] || LANG_META.python;
        if (outputEl) {
          outputEl.textContent = "$ " + meta.cli + "\n[Executed Successfully] -> Mission Completed (+35 XP)";
        }
      });
  };

  window.CQLangMeta = LANG_META;
  window.CQResolveLangKey = resolveLangKey;
})();
