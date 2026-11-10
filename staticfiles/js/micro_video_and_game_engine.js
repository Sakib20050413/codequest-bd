/* ==========================================================================
   CodeQuest BD — Short 60s Micro-Video Studio, Polyglot Terminal & Game Engine
   Covers all 16 Tracks: HTML5, CSS3, JS, React, Python, Django, C, C++,
   Java, Rust, PHP+MySQLi, SQL, MySQL, PostgreSQL, MongoDB, AI & ML
   ========================================================================== */

(function () {
  "use strict";

  // --------------------------------------------------------------------------
  // 1. LANGUAGE METADATA & SHORT VIDEO SCRIPTS (16 WORLD-CLASS LANGUAGES)
  // --------------------------------------------------------------------------
  const LANG_META = {
    html: {
      name: "HTML5 Semantic Web",
      cli: "live-dom-renderer index.html",
      color: "#ea580c",
      gameTitle: "Bridge & DOM Structure Architect",
      videoChapters: [
        { t: "0:00", title: "1. What You Are Learning", caption: "HTML5 builds the structural skeleton of every webpage using semantic tags like <header>, <nav>, <main>, and <article>." },
        { t: "0:15", title: "2. Core Code Syntax", caption: "Each element opens with <tag>, wraps content or child nodes, and closes with </tag> to form the DOM tree." },
        { t: "0:30", title: "3. Browser DOM Tree", caption: "The browser parses your HTML into live nodes in memory that CSS styles and JavaScript updates dynamically." },
        { t: "0:45", title: "4. Game & Task Mission", caption: "Write semantic HTML tags in the terminal below to construct the bridge deck and pass all 3 automated checks!" }
      ],
      starter: "<section class=\"bridge-deck\">\n  <h2>CodeQuest Bridge Sector 01</h2>\n  <button>Activate Platform</button>\n</section>"
    },
    css: {
      name: "CSS3 Flexbox & Grid",
      cli: "postcss --env=browser layout.css",
      color: "#0284c7",
      gameTitle: "Flexbox Canyon Bridge Architect",
      videoChapters: [
        { t: "0:00", title: "1. What You Are Learning", caption: "CSS3 Flexbox & Grid align UI elements across any screen size in 2 lines of clean layout code." },
        { t: "0:15", title: "2. Core Code Syntax", caption: "Set display: flex; justify-content: space-between; and align-items: center; on the parent container." },
        { t: "0:30", title: "3. Main vs Cross Axis", caption: "justify-content distributes items along the horizontal main axis; align-items locks them on the vertical axis." },
        { t: "0:45", title: "4. Game & Task Mission", caption: "Run your CSS Flexbox code in the terminal to align the 3 bridge planks across the canyon!" }
      ],
      starter: ".canyon-bridge {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n  gap: 16px;\n}"
    },
    javascript: {
      name: "JavaScript ES6+",
      cli: "node --experimental-modules app.js",
      color: "#eab308",
      gameTitle: "Cyber Turret & Event Loop Defense",
      videoChapters: [
        { t: "0:00", title: "1. What You Are Learning", caption: "JavaScript makes websites interactive, handles events, fetches APIs, and drives real-time browser logic." },
        { t: "0:15", title: "2. Core Code Syntax", caption: "Use const/let, arrow functions (() => {}), and array methods (.map, .filter) for clean reactive code." },
        { t: "0:30", title: "3. V8 Call Stack & Event Loop", caption: "Synchronous functions run on the V8 Call Stack while async Promises resolve smoothly via the Event Queue." },
        { t: "0:45", title: "4. Game & Task Mission", caption: "Execute your JavaScript targeting loop in the terminal to energize all 4 defense turrets!" }
      ],
      starter: "const targets = ['Drone-A1', 'Drone-B2', 'Drone-C3'];\ntargets.forEach((t, idx) => {\n  console.log(`Turret #${idx + 1} locked onto ${t} -> CLEARED`);\n});"
    },
    react: {
      name: "React.js 19",
      cli: "vite build --ssr Component.jsx",
      color: "#06b6d4",
      gameTitle: "React State & Virtual DOM Circuit",
      videoChapters: [
        { t: "0:00", title: "1. What You Are Learning", caption: "React builds fast component-based UIs where UI is a pure function of state: UI = f(state)." },
        { t: "0:15", title: "2. Core Code Syntax", caption: "Use useState(initial) to track reactive data and return declarative JSX markup." },
        { t: "0:30", title: "3. Virtual DOM Diffing", caption: "When state updates, React diffs the Virtual DOM and patches only the exact changed DOM node." },
        { t: "0:45", title: "4. Game & Task Mission", caption: "Run the React state component in the terminal to synchronize all UI circuit nodes!" }
      ],
      starter: "function PowerGrid({ voltage = 240 }) {\n  console.log(`React Virtual DOM: Grid active at ${voltage}V`);\n  return `<div class='grid-online'>${voltage}V</div>`;\n}\nPowerGrid({});"
    },
    python: {
      name: "Python 3.12",
      cli: "python3 main.py",
      color: "#10b981",
      gameTitle: "Autonomous Rover Maze Pathfinder",
      videoChapters: [
        { t: "0:00", title: "1. What You Are Learning", caption: "Python 3 powers backend web servers, automation scripts, data science, and AI with clean, readable syntax." },
        { t: "0:15", title: "2. Core Code Syntax", caption: "Use def functions, for loops, list comprehensions, and f-strings for rapid problem solving." },
        { t: "0:30", title: "3. Stack Frames & Objects", caption: "Variables bind names in stack frames to typed objects allocated on the Python heap." },
        { t: "0:45", title: "4. Game & Task Mission", caption: "Run your Python pathfinding script in the terminal to guide the Rover to the goal portal!" }
      ],
      starter: "steps = ['MOVE_EAST', 'MOVE_EAST', 'SCAN_CORE', 'DOCK_PORTAL']\nfor idx, action in enumerate(steps, 1):\n    print(f'Step {idx}: Rover executed {action} -> OK')"
    },
    django: {
      name: "Python Django 5",
      cli: "python3 manage.py shell < orm_query.py",
      color: "#059669",
      gameTitle: "Django MVT & ORM Pipeline Controller",
      videoChapters: [
        { t: "0:00", title: "1. What You Are Learning", caption: "Django is our full-stack Python backend framework using the Model-View-Template (MVT) architecture." },
        { t: "0:15", title: "2. Core Code Syntax", caption: "Define models.Model classes and query SQL safely via Student.objects.filter(dept='CSE')." },
        { t: "0:30", title: "3. Request -> View -> ORM -> Template", caption: "URLs route HTTP requests to Views, which query the SQL database via ORM and render HTML templates." },
        { t: "0:45", title: "4. Game & Task Mission", caption: "Execute the Django ORM pipeline in the terminal to verify backend route & SQL synchronization!" }
      ],
      starter: "routes = ['/', '/courses/', '/games/', '/contests/', '/playground/']\nfor r in routes:\n    print(f'[Django 5 WSGI] Route {r:14s} -> HTTP 200 OK (SQL Synced)')"
    },
    php: {
      name: "PHP 8 + SQL Database Bridge",
      cli: "php -f php_sessional_crud/db.php",
      color: "#4f46e5",
      gameTitle: "PHP MySQLi Server Data-Vault Bridge",
      videoChapters: [
        { t: "0:00", title: "1. What You Are Learning", caption: "PHP 8 connects directly to SQL/MySQL databases using mysqli and PDO prepared statements." },
        { t: "0:15", title: "2. Core Code Syntax", caption: "$conn = new mysqli($host, $user, $pass, $db); followed by $stmt = $conn->prepare('SELECT ...');" },
        { t: "0:30", title: "3. PHP <-> SQL Bridge Architecture", caption: "Frontend forms send POST data to PHP/Django, which sanitizes inputs and executes ACID SQL transactions." },
        { t: "0:45", title: "4. Game & Task Mission", caption: "Run the PHP + SQL query below to fetch verified student records from the live database!" }
      ],
      starter: "<?php\n$conn = mysqli_connect('localhost', 'root', '', 'codequest_sql');\necho \"[PHP 8.3 MySQLi] Connected to SQL Database Successfully!\";\n$sql = \"SELECT student_id, name, department, cgpa, xp FROM students ORDER BY xp DESC\";\n?>"
    },
    sql: {
      name: "SQL / MySQL / PostgreSQL",
      cli: "mysql -u root -e \"SELECT ...\"",
      color: "#0284c7",
      gameTitle: "SQL Crime Scene & Data Vault Detective",
      videoChapters: [
        { t: "0:00", title: "1. What You Are Learning", caption: "SQL queries relational databases (MySQL, PostgreSQL, SQLite) to filter, join, and aggregate structured tables." },
        { t: "0:15", title: "2. Core Code Syntax", caption: "SELECT columns FROM table WHERE condition GROUP BY col ORDER BY metric DESC;" },
        { t: "0:30", title: "3. B-Tree Indexes & Execution Plan", caption: "The SQL engine scans indexed primary/foreign keys, filters rows, and projects result columns in milliseconds." },
        { t: "0:45", title: "4. Game & Task Mission", caption: "Run your live SQL query in the terminal to inspect the students and competitions tables!" }
      ],
      starter: "SELECT student_id, name, department, cgpa, course_streak, game_streak, xp FROM students ORDER BY xp DESC;"
    },
    mongodb: {
      name: "MongoDB NoSQL (mongosh)",
      cli: "mongosh --eval \"db.students.find()\"",
      color: "#16a34a",
      gameTitle: "NoSQL Document Shard Controller",
      videoChapters: [
        { t: "0:00", title: "1. What You Are Learning", caption: "MongoDB stores flexible JSON-like BSON documents in collections instead of rigid rows and columns." },
        { t: "0:15", title: "2. Core Code Syntax", caption: "Use db.students.find({ dept: 'CSE' }) and db.students.insertOne({ ... }) in mongosh." },
        { t: "0:30", title: "3. Document Indexing & Aggregation", caption: "Aggregation pipelines ($match -> $group -> $sort) transform document streams at high throughput." },
        { t: "0:45", title: "4. Game & Task Mission", caption: "Run the mongosh command in the terminal to query live BSON student documents!" }
      ],
      starter: "db.students.find({\"dept\": \"CSE\"})"
    },
    c: {
      name: "C Systems Programming",
      cli: "gcc -std=c17 -O2 main.c -o main && ./main",
      color: "#0ea5e9",
      gameTitle: "Memory Pointer & Reactor Stabilizer",
      videoChapters: [
        { t: "0:00", title: "1. What You Are Learning", caption: "C gives you direct hardware control over CPU registers, stack frames, and raw memory addresses." },
        { t: "0:15", title: "2. Core Code Syntax", caption: "Use #include <stdio.h>, int main(), pointers (int *ptr = &val), and printf()." },
        { t: "0:30", title: "3. Stack vs Heap Memory", caption: "Local variables live on the fast stack (0x7ffee0); dynamic buffers allocate on the heap via malloc()." },
        { t: "0:45", title: "4. Game & Task Mission", caption: "Compile and run your C code with gcc in the terminal to stabilize the memory reactor!" }
      ],
      starter: "#include <stdio.h>\nint main() {\n    int core_voltage = 1200;\n    printf(\"C17 Reactor Lock: %d mV [Pointer Verified]\\n\", core_voltage);\n    return 0;\n}"
    },
    cpp: {
      name: "C++20 Competitive & Systems",
      cli: "g++ -std=c++20 -O2 main.cpp -o main && ./main",
      color: "#2563eb",
      gameTitle: "IUPC Algorithmic Thrust Engine",
      videoChapters: [
        { t: "0:00", title: "1. What You Are Learning", caption: "C++ combines low-level C speed with STL containers (vector, map, priority_queue) and OOP." },
        { t: "0:15", title: "2. Core Code Syntax", caption: "Use #include <iostream>, std::vector, fast I/O, and std::cout << result << endl;" },
        { t: "0:30", title: "3. Contiguous Vector Allocation", caption: "std::vector stores elements contiguously in L1/L2 CPU cache for sub-millisecond IUPC contest speed." },
        { t: "0:45", title: "4. Game & Task Mission", caption: "Compile with g++ in the terminal to compute the optimal thrust trajectory!" }
      ],
      starter: "#include <iostream>\nusing namespace std;\nint main() {\n    cout << \"C++20 STL Engine: Trajectory Optimal [100% Accuracy]\" << endl;\n    return 0;\n}"
    },
    java: {
      name: "Java 21 Enterprise OOP",
      cli: "javac Main.java && java Main",
      color: "#dc2626",
      gameTitle: "JVM Object Defense Matrix",
      videoChapters: [
        { t: "0:00", title: "1. What You Are Learning", caption: "Java powers enterprise backends and Android systems using strict Object-Oriented Programming (OOP)." },
        { t: "0:15", title: "2. Core Code Syntax", caption: "Define public class Main with public static void main(String[] args) and System.out.println()." },
        { t: "0:30", title: "3. JVM Bytecode & JIT Compiler", caption: "javac compiles source into bytecode (.class), which the HotSpot JIT compiles to native machine code." },
        { t: "0:45", title: "4. Game & Task Mission", caption: "Compile and execute your Java class in the terminal to activate the JVM defense matrix!" }
      ],
      starter: "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Java 21 JVM Shield: All OOP Modules Online!\");\n    }\n}"
    },
    rust: {
      name: "Rust Systems & Cargo",
      cli: "cargo run --release",
      color: "#d97706",
      gameTitle: "Borrow-Checked Orbital Core",
      videoChapters: [
        { t: "0:00", title: "1. What You Are Learning", caption: "Rust delivers C/C++ speed with compile-time memory safety and zero garbage collector pauses." },
        { t: "0:15", title: "2. Core Code Syntax", caption: "Use fn main(), let bindings, references (&T), and println!(\"{}\", value)." },
        { t: "0:30", title: "3. Compile-Time Borrow Checker", caption: "Rust tracks ownership lifetimes at compile time, preventing use-after-free and data races." },
        { t: "0:45", title: "4. Game & Task Mission", caption: "Run cargo run in the terminal to verify zero-cost memory safety!" }
      ],
      starter: "fn main() {\n    let status = \"Zero-Cost Memory Safety Active\";\n    println!(\"Rust Cargo Engine: {}\", status);\n}"
    },
    "ai-ml": {
      name: "AI & Machine Learning",
      cli: "python3 neural_lab.py",
      color: "#0d9488",
      gameTitle: "Neural Network & Tensor Pathfinder",
      videoChapters: [
        { t: "0:00", title: "1. What You Are Learning", caption: "AI & ML models learn patterns by multiplying input tensors with weight matrices and optimizing loss." },
        { t: "0:15", title: "2. Core Code Syntax", caption: "Compute weighted sums z = sum(x*w) + bias and apply ReLU activation max(0, z)." },
        { t: "0:30", title: "3. Forward Pass & Gradient Update", caption: "Forward propagation predicts outputs; backpropagation adjusts weights to minimize prediction error." },
        { t: "0:45", title: "4. Game & Task Mission", caption: "Run the Python neural forward-pass in the terminal to steer the AI agent!" }
      ],
      starter: "inputs = [0.9, 0.4, 0.8]\nweights = [0.5, 0.3, 0.7]\nbias = 0.12\nactivation = round(max(0.0, sum(x*w for x, w in zip(inputs, weights)) + bias), 3)\nprint(f'[AI Neural Pass] Output Activation = {activation} (Confidence: 98.4%)')"
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
  // 2. VISUAL GAME CANVAS RENDERER (DRIVEN BY REAL TERMINAL CODE)
  // --------------------------------------------------------------------------
  window.CQRenderGameCanvas = function (canvasId, rawLang, progressState, codeText) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const rect = canvas.parentElement ? canvas.parentElement.getBoundingClientRect() : { width: 520 };
    const w = Math.max(300, rect.width || 520);
    const h = canvas.height || 240;
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = w * dpr;
    canvas.height = h * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    const langKey = resolveLangKey(rawLang);
    const meta = LANG_META[langKey] || LANG_META.python;
    const isWon = progressState >= 0.8;

    // Crisp Dark Carbon Studio Viewport
    ctx.fillStyle = "#090d16";
    ctx.fillRect(0, 0, w, h);

    // Subtle Engineering Coordinate Grid
    ctx.strokeStyle = "rgba(148, 163, 184, 0.08)";
    ctx.lineWidth = 1;
    for (let gx = 0; gx < w; gx += 28) {
      ctx.beginPath();
      ctx.moveTo(gx, 0);
      ctx.lineTo(gx, h);
      ctx.stroke();
    }
    for (let gy = 0; gy < h; gy += 28) {
      ctx.beginPath();
      ctx.moveTo(0, gy);
      ctx.lineTo(w, gy);
      ctx.stroke();
    }

    // Top HUD Bar inside Canvas
    ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
    ctx.fillRect(0, 0, w, 34);
    ctx.fillStyle = isWon ? "#10b981" : meta.color;
    ctx.font = "700 11px 'JetBrains Mono', monospace";
    ctx.fillText("GAME ENGINE // " + meta.gameTitle.toUpperCase() + " [" + meta.name + "]", 12, 21);

    ctx.fillStyle = isWon ? "#10b981" : "#f59e0b";
    ctx.textAlign = "right";
    ctx.fillText(isWon ? "STATUS: MISSION CLEARED (+XP & GAME STREAK)" : "STATUS: READY FOR TERMINAL CODE", w - 12, 21);
    ctx.textAlign = "left";

    if (langKey === "html" || langKey === "css") {
      // Canyon + Bridge Planks aligned by HTML/CSS
      ctx.fillStyle = "#0c4a6e";
      ctx.fillRect(50, 52, w - 100, h - 76);
      const planks = 3;
      const pw = Math.min(110, (w - 160) / planks);
      for (let i = 0; i < planks; i++) {
        const px = isWon ? (70 + i * ((w - 140 - pw) / 2)) : (65 + i * 42);
        const py = isWon ? (h / 2 - 14) : (62 + i * 44);
        ctx.fillStyle = isWon ? "#059669" : "#d97706";
        ctx.fillRect(px, py, pw, 38);
        ctx.strokeStyle = "#f8fafc";
        ctx.strokeRect(px, py, pw, 38);
        ctx.fillStyle = "#ffffff";
        ctx.font = "700 11px 'JetBrains Mono', monospace";
        ctx.fillText("NODE 0" + (i + 1), px + 14, py + 23);
      }
    } else if (langKey === "python" || langKey === "ai-ml" || langKey === "django") {
      // Isometric / Grid Neural Rover Maze
      const cols = 8, rows = 4;
      const cw = Math.min(46, (w - 80) / cols);
      const sx = (w - cols * cw) / 2;
      const sy = 48;
      for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
          const x = sx + c * cw, y = sy + r * cw;
          const isGoal = (c === cols - 2 && r === rows - 2);
          const isPath = isWon && ((r === 1 && c >= 1 && c <= cols - 2) || (c === cols - 2 && r >= 1 && r <= rows - 2));
          ctx.fillStyle = isGoal ? "rgba(16, 185, 129, 0.3)" : (isPath ? "rgba(14, 165, 233, 0.22)" : "#111827");
          ctx.fillRect(x, y, cw - 3, cw - 3);
          ctx.strokeStyle = isGoal ? "#10b981" : (isPath ? "#38bdf8" : "#1e293b");
          ctx.strokeRect(x, y, cw - 3, cw - 3);
        }
      }
      const rx = isWon ? (cols - 2) : 1;
      const ry = isWon ? (rows - 2) : 1;
      const cx = sx + rx * cw + cw / 2 - 1.5;
      const cy = sy + ry * cw + cw / 2 - 1.5;
      ctx.fillStyle = isWon ? "#10b981" : "#0ea5e9";
      ctx.beginPath();
      ctx.arc(cx, cy, cw * 0.34, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = "#ffffff";
      ctx.font = "700 9px 'JetBrains Mono', monospace";
      ctx.fillText("ROVER", cx - 15, cy + 3);
    } else if (langKey === "sql" || langKey === "mongodb" || langKey === "php") {
      // Live Data Vault Table Visualizer
      const rows = isWon
        ? [
            ["ID", "STUDENT / NODE", "DEPT", "STREAK / XP"],
            ["1119003", "Md Najmus Sakib", "CSE", "12d / 2450 XP"],
            ["1119026", "Nusrat Jahan", "CSE", "15d / 2720 XP"],
            ["1119014", "Tahmid Hasan", "CSE", "8d / 1890 XP"]
          ]
        : [
            ["ID", "STUDENT / NODE", "DEPT", "STATUS"],
            ["1119003", "Vault Record #01", "CSE", "LOCKED (Run Query)"],
            ["1119026", "Vault Record #02", "CSE", "LOCKED (Run Query)"]
          ];
      rows.forEach(function (r, idx) {
        const y = 48 + idx * 38;
        ctx.fillStyle = idx === 0 ? "#1e293b" : (isWon ? "rgba(5, 150, 105, 0.16)" : "#111827");
        ctx.fillRect(20, y, w - 40, 32);
        ctx.strokeStyle = isWon && idx > 0 ? "#10b981" : "#334155";
        ctx.strokeRect(20, y, w - 40, 32);
        ctx.fillStyle = idx === 0 ? "#38bdf8" : "#f8fafc";
        ctx.font = (idx === 0 ? "700 " : "500 ") + "11px 'JetBrains Mono', monospace";
        r.forEach(function (cell, cIdx) {
          ctx.fillText(cell, 32 + cIdx * ((w - 64) / 4), y + 20);
        });
      });
    } else {
      // C / C++ / Rust / Java / JS / React Orbital Reactor & Circuit Turrets
      const cx = w / 2, cy = h / 2 + 12;
      for (let ring = 1; ring <= 3; ring++) {
        ctx.beginPath();
        ctx.arc(cx, cy, ring * 26, 0, Math.PI * 2);
        ctx.strokeStyle = isWon ? "#10b981" : "#38bdf8";
        ctx.lineWidth = ring === 2 ? 3 : 1.5;
        ctx.stroke();
      }
      for (let i = 0; i < 4; i++) {
        const ang = (i * Math.PI) / 2 + (isWon ? 0.4 : 0);
        const nx = cx + Math.cos(ang) * 78;
        const ny = cy + Math.sin(ang) * 78;
        ctx.fillStyle = isWon ? "#10b981" : "#f59e0b";
        ctx.beginPath();
        ctx.arc(nx, ny, 14, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = "#090d16";
        ctx.font = "700 9px 'JetBrains Mono', monospace";
        ctx.fillText("N" + (i + 1), nx - 6, ny + 3);
      }
    }
  };

  // --------------------------------------------------------------------------
  // 3. SHORT 60-SECOND INTERACTIVE MICRO-VIDEO PLAYER ENGINE
  // --------------------------------------------------------------------------
  window.CQInitMicroVideo = function (containerId, rawLang, lessonTitle) {
    const root = document.getElementById(containerId);
    if (!root) return;

    const langKey = resolveLangKey(rawLang);
    const meta = LANG_META[langKey] || LANG_META.python;
    const titleText = lessonTitle || (meta.name + " — 60-Second Concept Walkthrough");

    root.innerHTML = `
      <div class="cq-micro-video-box" style="background:#090d16; border:1px solid var(--border-medium); border-radius:12px; overflow:hidden; margin-bottom:1.25rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px; padding:10px 14px; background:#0f172a; border-bottom:1px solid rgba(255,255,255,0.08); font-family:var(--font-mono); font-size:0.76rem;">
          <div style="display:flex; align-items:center; gap:8px;">
            <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#10b981;"></span>
            <strong style="color:#f8fafc;">60s SHORT VIDEO LESSON // ${meta.name.toUpperCase()}</strong>
          </div>
          <div style="display:flex; gap:6px; align-items:center;">
            <span id="${containerId}_timer" style="color:#94a3b8;">0:00 / 1:00</span>
            <button type="button" id="${containerId}_voiceBtn" class="btn btn-ghost" style="padding:2px 8px; font-size:0.72rem; color:#e2e8f0;">🔊 Voice: ON</button>
            <button type="button" id="${containerId}_speedBtn" class="btn btn-ghost" style="padding:2px 8px; font-size:0.72rem; color:#e2e8f0;">1.0x</button>
          </div>
        </div>

        <div style="position:relative;">
          <canvas id="${containerId}_canvas" height="185" style="width:100%; height:185px; display:block;"></canvas>
          <div id="${containerId}_caption" style="padding:10px 14px; background:rgba(15,23,42,0.95); border-top:1px solid rgba(255,255,255,0.07); color:#e2e8f0; font-size:0.84rem; line-height:1.5;">
            <strong>${meta.videoChapters[0].title}:</strong> ${meta.videoChapters[0].caption}
          </div>
        </div>

        <div style="padding:10px 14px; background:#0b0f17; display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:8px;">
          <div style="display:flex; gap:6px; align-items:center;">
            <button type="button" id="${containerId}_playBtn" class="btn btn-primary" style="padding:5px 14px; font-size:0.78rem; font-weight:700;">▶ Play 60s Short Video</button>
            <div style="display:flex; gap:4px;" id="${containerId}_chapters">
              ${meta.videoChapters.map((c, idx) => `<button type="button" data-ch="${idx}" class="btn btn-ghost" style="padding:4px 8px; font-size:0.72rem; font-family:var(--font-mono);">${c.t}</button>`).join("")}
            </div>
          </div>
          <input type="range" id="${containerId}_scrub" min="0" max="60" value="0" style="width:140px; accent-color:#10b981; cursor:pointer;" aria-label="Video timeline">
        </div>
      </div>
    `;

    let sec = 0;
    let playing = false;
    let voiceOn = true;
    let speed = 1;
    let timerId = null;

    const canvas = document.getElementById(containerId + "_canvas");
    const captionEl = document.getElementById(containerId + "_caption");
    const timerEl = document.getElementById(containerId + "_timer");
    const scrubEl = document.getElementById(containerId + "_scrub");
    const playBtn = document.getElementById(containerId + "_playBtn");
    const voiceBtn = document.getElementById(containerId + "_voiceBtn");
    const speedBtn = document.getElementById(containerId + "_speedBtn");

    function speakChapter(chIdx) {
      if (!voiceOn || !("speechSynthesis" in window)) return;
      try {
        window.speechSynthesis.cancel();
        const u = new SpeechSynthesisUtterance(meta.videoChapters[chIdx].caption);
        u.rate = Math.min(1.8, speed * 1.05);
        window.speechSynthesis.speak(u);
      } catch (e) {}
    }

    function drawFrame() {
      if (!canvas) return;
      const ctx = canvas.getContext("2d");
      const rect = canvas.parentElement.getBoundingClientRect();
      const w = Math.max(300, rect.width || 500);
      const h = 185;
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = w * dpr;
      canvas.height = h * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

      ctx.fillStyle = "#070b12";
      ctx.fillRect(0, 0, w, h);

      const chIdx = Math.min(3, Math.floor(sec / 15));
      const ch = meta.videoChapters[chIdx];

      // Header Pill
      ctx.fillStyle = meta.color;
      ctx.font = "700 11px 'JetBrains Mono', monospace";
      ctx.fillText("CHAPTER 0" + (chIdx + 1) + " // " + ch.title.toUpperCase(), 16, 26);

      // Lesson Title
      ctx.fillStyle = "#f8fafc";
      ctx.font = "700 14px 'Plus Jakarta Sans', sans-serif";
      ctx.fillText(titleText.slice(0, 58), 16, 50);

      // Animated Code / Architecture Visual Box
      ctx.fillStyle = "#0f172a";
      ctx.fillRect(16, 64, w - 32, 92);
      ctx.strokeStyle = meta.color;
      ctx.lineWidth = 1.5;
      ctx.strokeRect(16, 64, w - 32, 92);

      const codeLines = meta.starter.split("\n").slice(0, 4);
      ctx.font = "500 11.5px 'JetBrains Mono', monospace";
      codeLines.forEach(function (ln, idx) {
        ctx.fillStyle = idx === (chIdx % codeLines.length) ? "#34d399" : "#cbd5e1";
        ctx.fillText((idx + 1) + "  " + ln.slice(0, 68), 28, 86 + idx * 18);
      });

      // Progress Bar at bottom of canvas
      ctx.fillStyle = "#1e293b";
      ctx.fillRect(0, h - 5, w, 5);
      ctx.fillStyle = "#10b981";
      ctx.fillRect(0, h - 5, (sec / 60) * w, 5);

      captionEl.innerHTML = "<strong>" + ch.title + ":</strong> " + ch.caption;
      const sPad = sec < 10 ? "0" + sec : sec;
      timerEl.textContent = "0:" + sPad + " / 1:00";
      scrubEl.value = sec;
    }

    playBtn.addEventListener("click", function () {
      playing = !playing;
      if (playing) {
        playBtn.textContent = "⏸ Pause Video";
        speakChapter(Math.min(3, Math.floor(sec / 15)));
        timerId = setInterval(function () {
          sec += 1;
          if (sec % 15 === 0 && sec < 60) {
            speakChapter(Math.floor(sec / 15));
          }
          if (sec >= 60) {
            sec = 60;
            playing = false;
            playBtn.textContent = "↺ Replay 60s Video";
            clearInterval(timerId);
          }
          drawFrame();
        }, Math.round(1000 / speed));
      } else {
        playBtn.textContent = "▶ Resume Video";
        clearInterval(timerId);
        if ("speechSynthesis" in window) window.speechSynthesis.cancel();
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
        if (playing) speakChapter(idx);
      });
    });

    voiceBtn.addEventListener("click", function () {
      voiceOn = !voiceOn;
      this.textContent = voiceOn ? "🔊 Voice: ON" : "🔇 Voice: OFF";
      if (!voiceOn && "speechSynthesis" in window) window.speechSynthesis.cancel();
    });

    speedBtn.addEventListener("click", function () {
      speed = speed === 1 ? 1.5 : (speed === 1.5 ? 2 : 1);
      this.textContent = speed.toFixed(1) + "x";
    });

    drawFrame();
  };

  // --------------------------------------------------------------------------
  // 4. UNIVERSAL POLYGLOT TERMINAL & COMPILER CLIENT
  // --------------------------------------------------------------------------
  window.CQExecuteTerminal = function (opts) {
    const lang = opts.language || "python";
    const code = opts.code || "";
    const cliCommand = opts.cliCommand || "";
    const outputEl = typeof opts.outputEl === "string" ? document.getElementById(opts.outputEl) : opts.outputEl;
    const canvasId = opts.canvasId || null;

    if (outputEl) {
      outputEl.textContent = "Executing in polyglot sandbox...";
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
          outputEl.textContent = data.stdout || "Executed (0 errors).";
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
        if (outputEl) outputEl.textContent = "Execution Error: " + err;
      });
  };

  window.CQLangMeta = LANG_META;
  window.CQResolveLangKey = resolveLangKey;
})();
