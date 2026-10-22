# CodeQuest BD — Gamified Multi-Language Programming & Problem-Solving Platform
**Course:** CSE 324 — Web Technologies Sessional Lab Final Project  
**Author / Student:** Md Najmus Sakib Rahatul (Student ID: `1119003`)  
**Academic Tier:** Level 3, Term 2, Section A  
**Department:** Computer Science & Engineering, Bangladesh Army International University of Science & Technology (BAIUST), Cumilla  

---

## 1. Project Overview & Pedagogical Objective
**CodeQuest BD** is an interactive, full-stack educational web application designed to eliminate the friction university students face when bridging foundational syntax with spatial computational logic and server-side database CRUD.

### 4 Core Interactive Engines
1. **Mode 1: Grid Rover Maze (`ROVER_MAZE`):** 2D tile canvas (`8x8`) where students write loops and conditionals in C, C++, Python, or JavaScript to guide the Cyber Rover `[R]` past laser barriers `[⚡]` and collect energy gems `[💎]` to reach the extraction portal `[🏁]`. Includes Web Audio API step-by-step sound synthesis and trail animations.
2. **Mode 2: Visual CSS & DOM Builder (`DOM_BUILDER`):** Inspired by *Flexbox Froggy* & *CSS Diner*. Interactive split-screen stage where students write Flexbox/Grid CSS properties or DOM manipulation scripts to align cyber drones onto landing pads in real-time.
3. **Mode 3: Multi-Language Code Judge (`CODE_JUDGE`):** Multi-language sandbox supporting C, C++, Python, JavaScript, and PHP. Powered by the public Piston Cloud API (`https://emkc.org/api/v2/piston/execute`) with a **guaranteed offline/viva fallback engine** that ensures test cases validate even without lab internet.
4. **Mode 4: Bug-Hunter & Output Blitz (`BUG_HUNTER`):** 60-second arcade quiz trainer with combo multipliers (`2x`, `3x`, `5x`), streak fire animations, and instant pedagogical explanations for the 20-Mark Handwritten Lab Code Quiz.

---

## 2. Technology Stack & Sessional Rubric Alignment
- **Frontend:** Semantic HTML5, CSS3, Tailwind CSS (Dark Gamified Theme), FontAwesome 6, Google Fonts (Inter & JetBrains Mono).
- **Client Scripting & DOM:** Pure JavaScript ES6+ (`querySelector`, `addEventListener`, `classList`, `localStorage`, `fetch()` AJAX, Web Audio API sound synthesis).
- **Backend Framework:** Python Django 5.x (`codequest_cms` with `arena`, `accounts`, and `instructor_panel` apps).
- **Persistence Tier:** SQLite (`db.sqlite3`) for local development; automatic `dj-database-url` switching to PostgreSQL on cloud hosts.
- **Continuous Evaluation iv (PHP CRUD):** Dedicated `/php_sessional_crud/` folder containing standalone Procedural PHP + MySQLi CRUD scripts (`db.php`, `index.php`, `create_challenge.php`, `edit_challenge.php`, `delete_challenge.php`, `schema.sql`).
- **Academic Proposal:** Printable formal academic proposal route at `/proposal/` equipped with `@media print` styling and a one-click PDF print trigger.
- **Custom Instructor CMS:** Dedicated frontend `/instructor-panel/` with 100% modal CRUD over tracks, levels, quizzes, student submissions, and announcements.

---

## 3. How to Run Locally

### Step 1: Install Dependencies & Migrate
```bash
# In the root directory (codequest-bd)
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

### Step 2: Seed All Initial Data
```bash
python seed_codequest.py
```
This populates:
- **Admin & Lead Student:** `sakib_admin` / `baiust1119003` (ID: `1119003`, Level 5 Grandmaster, 1850 XP)
- **6 Language Tracks**
- **18 Playable Levels (3 per track)**
- **15 Bug Blitz Quiz Questions**
- **BAIUST Leaderboard Classmates**

### Step 3: Start the Development Server
```bash
python manage.py runserver
```
Then visit:
- **Landing Hub:** `http://127.0.0.1:8000/`
- **6 Tracks Arena:** `http://127.0.0.1:8000/tracks/`
- **60-Second Bug Blitz:** `http://127.0.0.1:8000/blitz/`
- **Campus Leaderboard:** `http://127.0.0.1:8000/leaderboard/`
- **Formal Project Proposal:** `http://127.0.0.1:8000/proposal/`
- **Custom Instructor Panel:** `http://127.0.0.1:8000/instructor-panel/` (Login: `sakib_admin` / `baiust1119003`)
- **Standalone PHP CRUD Module:** `http://127.0.0.1:8080/` (Run via `cd php_sessional_crud && php -S localhost:8080`)

---

## 4. Default Credentials Summary
| Role | Identifier / Username | Password | Access Area |
| :--- | :--- | :--- | :--- |
| **Lead Student / Architect** | `1119003` or `sakib_admin` | `baiust1119003` | Full Access + `/instructor-panel/` |
| **Classmate Student** | `tanvir_cse` | `baiust1234` | Student Game Arena & Blitz |
