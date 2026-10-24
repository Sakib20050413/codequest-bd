# CodeQuest BD Project Memory

This file serves as persistent project context for any AI agent working on this repository.

## Quick Reference
- **Read the full project memory**: `C:\Users\mdnaj\.gemini\CODEQUEST_BD_PROJECT_MEMORY.md`
- **Live URL**: https://codequest-bd.vercel.app
- **Django Settings**: `config.settings` (NOT `codequest.settings`)
- **Database**: SQLite (read-only on Vercel; mutations must be local + git committed)

## Critical Rules
1. Line endings: CRLF (`\r\n`) on Windows
2. Game templates: filenames use underscores, URLs use hyphens
3. Guard `THREE.OrbitControls` against CDN failures
4. PowerShell: use `;` not `&&`
5. All user-facing responses in Bengali script (bangla), technical terms in English
6. Course pages: `/courses/<slug>/` — Lesson pages: `/learn/<course>/<lesson>/`

## Content Stats
- 9 languages, 9 courses, 88 lessons, 108 games (1,080 levels), 28 coding tasks, 6 badges
- 0 quality issues remaining (all lessons have body, task, starter code, and tests)

## When Making Changes
- Always update `CODEQUEST_BD_PROJECT_MEMORY.md` after significant changes
- Run `python manage.py test learn` (14 tests) to verify
- Run `python manage.py check` for Django system check
- Commit with conventional commit messages (`feat:`, `fix:`, `docs:`)
