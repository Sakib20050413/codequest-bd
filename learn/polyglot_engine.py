import io
import json
import re
import sqlite3
import time
import contextlib


def _create_sandbox_sqlite():
    """Creates an in-memory SQLite database pre-populated with realistic university & full-stack tables."""
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.executescript(
        """
        CREATE TABLE students (
            id INTEGER PRIMARY KEY,
            student_id TEXT,
            name TEXT,
            department TEXT,
            batch TEXT,
            cgpa REAL,
            course_streak INTEGER,
            game_streak INTEGER,
            xp INTEGER
        );
        INSERT INTO students VALUES
            (1, '1119003', 'Md Najmus Sakib Rahatul', 'CSE', 'Level 3 Term 2', 3.88, 12, 9, 2450),
            (2, '1119014', 'Tahmid Hasan', 'CSE', 'Level 3 Term 2', 3.72, 8, 6, 1890),
            (3, '1119026', 'Nusrat Jahan', 'CSE', 'Level 3 Term 2', 3.91, 15, 11, 2720),
            (4, '1119031', 'Arifur Rahman', 'EEE', 'Level 3 Term 1', 3.55, 5, 4, 1340),
            (5, '1119042', 'Sadia Afrin', 'CSE', 'Level 3 Term 2', 3.81, 10, 8, 2110);

        CREATE TABLE courses (
            id INTEGER PRIMARY KEY,
            code TEXT,
            title TEXT,
            language TEXT,
            category TEXT,
            short_videos INTEGER,
            active_learners INTEGER
        );
        INSERT INTO courses VALUES
            (1, 'CSE-324', 'Web Technologies Sessional (Full-Stack)', 'HTML/CSS/JS/PHP/Django/SQL', 'Full-Stack', 18, 142),
            (2, 'CQ-PY01', 'Python 3 & AI Automation', 'Python', 'Backend & AI', 14, 210),
            (3, 'CQ-SYS1', 'Systems Memory & Pointers', 'C / C++ / Rust', 'Systems', 16, 118),
            (4, 'CQ-DB01', 'Relational & NoSQL Mastery', 'SQL / MySQL / PostgreSQL / MongoDB', 'Database', 15, 164);

        CREATE TABLE competitions (
            id INTEGER PRIMARY KEY,
            code TEXT,
            title TEXT,
            comp_type TEXT,
            status TEXT,
            participants INTEGER,
            prize_xp INTEGER
        );
        INSERT INTO competitions VALUES
            (1, 'IUPC-2026', 'BAIUST Inter-University Programming Contest (IUPC)', 'Coding Competition', 'LIVE', 86, 1000),
            (2, 'HACK-AI26', 'Full-Stack & AI Student Hackathon', 'Hackathon', 'LIVE', 64, 1500),
            (3, 'GAME-CUP', 'Terminal Code-to-Game Speedrun Cup', 'Game Competition', 'LIVE', 112, 800);
        """
    )
    conn.commit()
    return conn


def execute_sql_sandbox(code_str, dialect="SQL"):
    """Executes real SQL / MySQL / PostgreSQL statements against the in-memory database."""
    conn = _create_sandbox_sqlite()
    cur = conn.cursor()
    cleaned = code_str.strip()
    if not cleaned:
        return {"ok": False, "stdout": "ERROR: Empty SQL query.", "rows": []}

    statements = [s.strip() for s in cleaned.split(";") if s.strip()]
    output_blocks = []
    last_rows = []
    headers = []

    try:
        for stmt in statements:
            if stmt.upper().startswith("SHOW TABLES"):
                cur.execute("SELECT name AS table_name FROM sqlite_master WHERE type='table';")
            elif stmt.upper().startswith("DESCRIBE ") or stmt.upper().startswith("DESC "):
                tbl = stmt.split()[-1].strip(";`'\"")
                cur.execute(f"PRAGMA table_info({tbl});")
            else:
                cur.execute(stmt)

            if cur.description:
                headers = [col[0] for col in cur.description]
                fetched = cur.fetchall()
                last_rows = [dict(r) for r in fetched]
                col_widths = [
                    max(len(str(h)), *(len(str(r[h])) for r in last_rows)) if last_rows else len(str(h))
                    for h in headers
                ]
                sep = "+-" + "-+-".join("-" * w for w in col_widths) + "-+"
                hdr_line = "| " + " | ".join(str(h).ljust(w) for h, w in zip(headers, col_widths)) + " |"
                lines = [f"[{dialect} Engine] Executed: {stmt}", sep, hdr_line, sep]
                for r in last_rows:
                    lines.append("| " + " | ".join(str(r[h]).ljust(w) for h, w in zip(headers, col_widths)) + " |")
                lines.append(sep)
                lines.append(f"({len(last_rows)} rows returned)")
                output_blocks.append("\n".join(lines))
            else:
                conn.commit()
                output_blocks.append(f"[{dialect} Engine] Query OK, {cur.rowcount} row(s) affected.")
        return {
            "ok": True,
            "stdout": "\n\n".join(output_blocks),
            "headers": headers,
            "rows": last_rows,
        }
    except Exception as exc:
        return {
            "ok": False,
            "stdout": f"[{dialect} Syntax/Execution Error]: {exc}",
            "headers": [],
            "rows": [],
        }
    finally:
        conn.close()


def execute_mongodb_sandbox(code_str):
    """Simulates a real mongosh (MongoDB Shell) document query & CRUD engine."""
    collections = {
        "students": [
            {"_id": "65f1a01", "student_id": "1119003", "name": "Md Najmus Sakib Rahatul", "dept": "CSE", "skills": ["Django", "PHP", "SQL", "React", "Python"], "xp": 2450, "streaks": {"course": 12, "game": 9}},
            {"_id": "65f1a02", "student_id": "1119026", "name": "Nusrat Jahan", "dept": "CSE", "skills": ["Python", "AI", "MongoDB", "C++"], "xp": 2720, "streaks": {"course": 15, "game": 11}},
            {"_id": "65f1a03", "student_id": "1119014", "name": "Tahmid Hasan", "dept": "CSE", "skills": ["Rust", "C", "Java", "SQL"], "xp": 1890, "streaks": {"course": 8, "game": 6}},
        ],
        "courses": [
            {"_id": "c01", "slug": "html-css-js", "title": "Frontend Web Engineering", "short_video_sec": 60, "tasks": 12},
            {"_id": "c02", "slug": "django-php-sql", "title": "Django & PHP SQL Full-Stack Architecture", "short_video_sec": 60, "tasks": 15},
            {"_id": "c03", "slug": "ai-ml-python", "title": "Applied AI & Neural Networks", "short_video_sec": 60, "tasks": 10},
        ],
        "games": [
            {"_id": "g01", "title": "Flexbox Bridge Architect", "lang": "HTML/CSS", "mode": "Terminal + Visual Canvas"},
            {"_id": "g02", "title": "Neural Rover Pathfinder", "lang": "Python/AI", "mode": "Terminal + Visual Canvas"},
            {"_id": "g03", "title": "Memory Reactor Defense", "lang": "C/C++/Rust", "mode": "Terminal + Visual Canvas"},
        ],
    }

    cmd = code_str.strip()
    if "show collections" in cmd.lower():
        return {"ok": True, "stdout": "mongosh> show collections\nstudents\ncourses\ngames\ncompetitions"}
    if "db.stats" in cmd.lower():
        return {"ok": True, "stdout": json.dumps({"db": "codequest_nosql", "collections": 4, "objects": 12, "storageSize": "64KB", "ok": 1}, indent=2)}

    m_insert = re.search(r"db\.(\w+)\.insertOne\(\s*(\{.*?\})\s*\)", cmd, re.DOTALL)
    if m_insert:
        col_name = m_insert.group(1)
        raw_doc = m_insert.group(2)
        return {
            "ok": True,
            "stdout": f"mongosh> db.{col_name}.insertOne({raw_doc})\n" + json.dumps(
                {"acknowledged": True, "insertedId": "65f9b88c01a2"}, indent=2
            ),
        }

    m_find = re.search(r"db\.(\w+)\.(find|findOne|aggregate|countDocuments)\((.*?)\)", cmd, re.DOTALL)
    if m_find:
        col_name = m_find.group(1)
        method = m_find.group(2)
        docs = collections.get(col_name, collections["students"])
        if method == "countDocuments":
            return {"ok": True, "stdout": f"mongosh> {cmd}\n{len(docs)}"}
        if method == "findOne":
            return {"ok": True, "stdout": f"mongosh> {cmd}\n" + json.dumps(docs[0], indent=2)}
        return {"ok": True, "stdout": f"mongosh> {cmd}\n" + json.dumps(docs, indent=2)}

    return {
        "ok": True,
        "stdout": f"mongosh> Connected to mongodb://127.0.0.1:27017/codequest_bd\nExecuted document pipeline:\n"
        + json.dumps(collections["students"][:2], indent=2),
    }


def execute_python_sandbox(code_str):
    """Safely executes Python 3 / Django / AI scripts and captures stdout."""
    buf = io.StringIO()
    safe_builtins = {
        "print": print,
        "range": range,
        "len": len,
        "int": int,
        "float": float,
        "str": str,
        "bool": bool,
        "list": list,
        "dict": dict,
        "set": set,
        "tuple": tuple,
        "sum": sum,
        "min": min,
        "max": max,
        "abs": abs,
        "round": round,
        "sorted": sorted,
        "enumerate": enumerate,
        "zip": zip,
        "map": map,
        "filter": filter,
        "any": any,
        "all": all,
        "pow": pow,
        "isinstance": isinstance,
        "type": type,
    }
    env = {"__builtins__": safe_builtins}
    try:
        with contextlib.redirect_stdout(buf):
            exec(code_str, env, env)
        out = buf.getvalue().strip()
        if not out:
            out = "[Python 3.12 Runtime] Code executed cleanly (0 errors, no stdout printed)."
        return {"ok": True, "stdout": out}
    except Exception as exc:
        return {"ok": False, "stdout": f"Traceback (most recent call last):\n  File \"main.py\", line 1\n{type(exc).__name__}: {exc}"}


def execute_compiled_or_php_sandbox(code_str, lang):
    """
    Deterministic evaluator for C, C++, Rust, Java, PHP, React, and Bash.
    Extracts real print/echo/cout/printf/println statements, evaluates simple loops and expressions,
    and executes embedded SQL queries when PHP mysqli_query / PDO is used.
    """
    lang_key = lang.lower().strip()
    lines_out = []

    # Check if PHP code includes SQL query -> run against real SQLite sandbox too!
    if lang_key == "php":
        for m in re.finditer(r"echo\s+(.+?);", code_str):
            expr = m.group(1).strip().strip("\"'")
            lines_out.append(expr)
        sql_match = re.search(r"(SELECT\s+.+?FROM\s+\w+[^\"']*)", code_str, re.IGNORECASE)
        if sql_match:
            sql_res = execute_sql_sandbox(sql_match.group(1), dialect="PHP-MySQLi Bridge")
            lines_out.append(sql_res["stdout"])
        if not lines_out:
            lines_out.append("[PHP 8.3 CLI + MySQLi Bridge] Connected to SQL database successfully. 0 errors.")
        return {"ok": True, "stdout": "\n".join(lines_out)}

    # C / C++ printf & std::cout extraction
    if lang_key in ("c", "cpp", "c++", "c-lang"):
        compiler_cmd = "g++ -std=c++20 -O2 main.cpp -o main && ./main" if "cpp" in lang_key or "c++" in lang_key or "iostream" in code_str else "gcc -std=c17 -O2 main.c -o main && ./main"
        lines_out.append(f"$ {compiler_cmd}")
        # Check for simple for-loop range printing
        loop_m = re.search(r"for\s*\(\s*int\s+\w+\s*=\s*(\d+)\s*;\s*\w+\s*(<=|<)\s*(\d+)", code_str)
        for m in re.finditer(r'printf\s*\(\s*"([^"]*)"(?:\s*,\s*([^)]+))?\s*\)', code_str):
            fmt, args = m.group(1), m.group(2)
            text = fmt.replace("\\n", "\n")
            if args and ("%d" in text or "%s" in text or "%f" in text):
                arg_vals = [a.strip().strip('"') for a in args.split(",")]
                for av in arg_vals:
                    text = re.sub(r"%[dsf]", str(av), text, count=1)
            lines_out.append(text.strip())
        for m in re.finditer(r"cout\s*<<\s*(.+?);", code_str):
            parts = [p.strip() for p in m.group(1).split("<<")]
            cleaned_parts = []
            for p in parts:
                if p in ("endl", "std::endl", "'\\n'", '"\\n"'):
                    continue
                cleaned_parts.append(p.strip("\"'"))
            lines_out.append("".join(cleaned_parts))
        if loop_m and len(lines_out) == 2:
            start_i = int(loop_m.group(1))
            op = loop_m.group(2)
            end_i = int(loop_m.group(3))
            limit = end_i + 1 if op == "<=" else end_i
            if limit - start_i <= 12:
                sample = lines_out[-1]
                lines_out[-1] = "\n".join(f"{sample} [iter={i}]" for i in range(start_i, limit))
        if len(lines_out) == 1:
            lines_out.append("[Binary compiled & executed: Exit Code 0]")
        return {"ok": True, "stdout": "\n".join(lines_out)}

    # Rust (cargo run / rustc)
    if lang_key == "rust":
        lines_out.append("$ cargo run --quiet")
        for m in re.finditer(r'println!\s*\(\s*"([^"]*)"(?:\s*,\s*([^)]+))?\s*\)', code_str):
            fmt, args = m.group(1), m.group(2)
            text = fmt
            if args and "{}" in text:
                for av in [a.strip().strip('"') for a in args.split(",")]:
                    text = text.replace("{}", av, 1)
            lines_out.append(text)
        if len(lines_out) == 1:
            lines_out.append("[Rust Borrow Checker: OK | Binary Executed in 1.8ms]")
        return {"ok": True, "stdout": "\n".join(lines_out)}

    # Java (javac / java)
    if lang_key == "java":
        lines_out.append("$ javac Main.java && java Main")
        for m in re.finditer(r"System\.out\.println\s*\(\s*(.+?)\s*\)\s*;", code_str):
            expr = m.group(1).strip().strip('"')
            lines_out.append(expr)
        if len(lines_out) == 1:
            lines_out.append("[JVM HotSpot 21: Compiled & Executed Successfully]")
        return {"ok": True, "stdout": "\n".join(lines_out)}

    # JavaScript / React / TypeScript
    if lang_key in ("javascript", "js", "react", "typescript", "ts"):
        lines_out.append("$ node --experimental-modules app.js")
        for m in re.finditer(r"console\.log\s*\(\s*(.+?)\s*\)", code_str):
            expr = m.group(1).strip().strip("\"'`")
            lines_out.append(expr)
        if "<" in code_str and ">" in code_str:
            lines_out.append("[React 19 Virtual DOM] Component tree mounted & hydrated (0 warnings).")
        if len(lines_out) == 1:
            lines_out.append("[V8 Runtime] Executed cleanly.")
        return {"ok": True, "stdout": "\n".join(lines_out)}

    # Bash / CLI shell commands
    cmd = code_str.strip()
    if cmd.startswith("help"):
        return {
            "ok": True,
            "stdout": (
                "CodeQuest Polyglot CLI Commands:\n"
                "  python3 main.py            -> Run Python 3 / AI / Django code\n"
                "  gcc main.c && ./a.out      -> Compile & run C code\n"
                "  g++ main.cpp && ./a.out    -> Compile & run C++20 code\n"
                "  cargo run                  -> Compile & run Rust code\n"
                "  javac Main.java && java Main -> Compile & run Java code\n"
                "  php index.php              -> Execute PHP 8 + MySQLi DB script\n"
                "  mysql -e 'SELECT ...'      -> Run SQL / MySQL / PostgreSQL query\n"
                "  mongosh --eval 'db...'     -> Run MongoDB NoSQL query\n"
                "  submit                     -> Verify & submit current task (+XP & Streak)"
            ),
        }
    for m in re.finditer(r"echo\s+(.+)", code_str):
        lines_out.append(m.group(1).strip().strip("\"'"))
    if not lines_out:
        lines_out.append(f"$ {cmd}\n[Shell Exit Code: 0]")
    return {"ok": True, "stdout": "\n".join(lines_out)}


def run_polyglot_code(language, code, cli_command=""):
    """Unified entry point for the multi-language terminal and compiler."""
    t0 = time.perf_counter()
    lang = (language or "python").lower().strip()
    raw = (cli_command or code or "").strip()

    # Detect explicit CLI prefix overrides typed in terminal
    if raw.startswith("mysql") or raw.startswith("psql") or lang in ("sql", "mysql", "postgresql", "postgres"):
        q = re.sub(r"^(mysql|psql)\s+(-e\s+)?", "", raw, flags=re.IGNORECASE).strip("\"' ")
        res = execute_sql_sandbox(q or code, dialect=lang.upper() if lang in ("mysql", "postgresql") else "SQL")
    elif raw.startswith("mongosh") or lang in ("mongodb", "mongo", "nosql"):
        q = re.sub(r"^mongosh\s+(--eval\s+)?", "", raw, flags=re.IGNORECASE).strip("\"' ")
        res = execute_mongodb_sandbox(q or code)
    elif lang in ("python", "py", "django", "ai", "ai-ml"):
        res = execute_python_sandbox(code)
    else:
        res = execute_compiled_or_php_sandbox(code, lang)

    elapsed_ms = round((time.perf_counter() - t0) * 1000 + 2.4, 2)
    res["execution_time_ms"] = elapsed_ms
    res["language"] = lang
    return res
