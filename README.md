# CodeQuest — Minimal Bite-Sized Coding Learning Platform

CodeQuest is a modern, distraction-free web platform where beginners learn programming through short, interactive lessons (3–7 minutes) instead of long video tutorials. Each lesson pairs a concise mental model with a live browser editor, auto-checking tests, and focused mini-games.

---

## 1. Core Architecture & Tech Stack

- **Backend Framework:** Django 5 (Python 3.11+)
- **Database:** PostgreSQL on Neon (production) / SQLite (local development)
- **Frontend:** Server-rendered Django templates, Vanilla JS islands, CSS Custom Properties (zero CSS framework lock-in)
- **Code Execution:** 100% Client-Side Sandboxed (Zero server-side code execution):
  - **HTML/CSS/JS:** Sandboxed `<iframe sandbox="allow-scripts">` live preview
  - **Python:** Pyodide (WebAssembly)
  - **SQL:** `sql.js` (SQLite in browser WASM)
  - **C / Java / PHP / Bash:** Predictive multiple-choice & fill-the-blank sandboxes
- **Gamification:** XP points, streak tracking (SVG flame icon), progress rings, level badges, and 5 interactive mini-games

---

## 2. 5 Practice Mini-Games (1–2 Minutes Each)

1. **Tag Match:** Drag the correct HTML semantic tag onto its real-world description.
2. **Flexbox Pond:** Align floating elements to target pads using CSS Flexbox properties (`justify-content`, `align-items`).
3. **Bug Hunt:** Spot and click the buggy line in short code snippets.
4. **Code Typer:** Build typing muscle memory with real programming syntax, scored on accuracy and WPM.
5. **Output Predictor:** Read concise logic snippets and predict the exact console output.

---

## 3. How to Add a Lesson from Admin

1. Log into the hidden Django admin route defined by the `ADMIN_URL` environment variable (e.g. `/dashboard-cms/` or `/manage-core/`).
2. Navigate to **Learn > Lessons** and click **Add Lesson**.
3. Fill in:
   - **Course / Language:** Select the target language track (HTML, CSS, JavaScript, Python, SQL, etc.).
   - **Title & Slug:** e.g. `01. Semantic Tags` (`semantic-tags`).
   - **Order:** Integer defining sequence inside the course path.
   - **Estimated Minutes:** e.g. `4`.
   - **Body (Markdown):** Concise explanation (under 150 words) with one clear diagram or mental model.
   - **Starter Code:** Initial code presented in the editor.
   - **Solution Code:** Reference passing solution.
   - **Test Cases (JSON):** Assertions or DOM queries used by the auto-checker.
   - **Hints (JSON):** Stepped ladder (Hint 1 → Hint 2 → Full Solution).
4. Save the lesson. It immediately appears on the course roadmap and public catalogue.

---

## 4. Local Development Setup

```bash
# 1. Clone repository & enter workspace
git clone https://github.com/Sakib20050413/codequest-bd.git
cd codequest-bd

# 2. Set up virtual environment
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env

# 5. Run database migrations
python manage.py migrate

# 6. Seed initial curriculum
python seed_codequest.py

# 7. Start local live server
python manage.py runserver 127.0.0.1:8000
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## 5. Deployment Guide (Render + Neon)

- **Database:** Provision a serverless Postgres database on **Neon** (Singapore region `ap-southeast-1` for South Asia/global low latency).
- **Web Service:** Deploy on **Render** (Singapore region):
  - **Build Command:** `./build_files.sh`
  - **Start Command:** `gunicorn codequest_project.wsgi:application`
  - **Environment Variables:** `SECRET_KEY`, `DEBUG=False`, `DATABASE_URL`, `ADMIN_URL`, `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`.
