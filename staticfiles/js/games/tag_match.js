/**
 * CodeQuest Mini-Game 1: Tag & Syntax Matcher
 * 20 Timed Speed Drills across HTML5, CSS Selectors, HTTP & Git
 */
(function () {
  'use strict';

  const DRILLS = [
    {
      id: 1,
      category: "HTML5 Semantic",
      desc: "Top-level container for primary document content unique to this page",
      tag: "<main>",
      decoys: ["<header>", "<section>", "<div>"],
      hint: "Excluded from site-wide headers, footers, or repetitive sidebars."
    },
    {
      id: 2,
      category: "HTML5 Semantic",
      desc: "Introductory content, site branding/logo, or primary navigation banner",
      tag: "<header>",
      decoys: ["<nav>", "<top>", "<banner>"],
      hint: "Can appear at document root or inside <article>/<section>."
    },
    {
      id: 3,
      category: "HTML5 Semantic",
      desc: "Footer containing author bio, copyright notice, legal links, or back-to-top",
      tag: "<footer>",
      decoys: ["<bottom>", "<aside>", "<meta>"],
      hint: "Standard closing landmark across pages and articles."
    },
    {
      id: 4,
      category: "HTML5 Semantic",
      desc: "Self-contained, independently distributable composition (blog post, news story)",
      tag: "<article>",
      decoys: ["<section>", "<aside>", "<div>"],
      hint: "Should make sense on its own if syndicated via RSS."
    },
    {
      id: 5,
      category: "HTML5 Semantic",
      desc: "Content indirectly or tangentially related to main content (sidebar, callout, glossary)",
      tag: "<aside>",
      decoys: ["<sidebar>", "<nav>", "<callout>"],
      hint: "Often positioned as a secondary side column."
    },
    {
      id: 6,
      category: "HTML5 Semantic",
      desc: "Major grouping of navigation links (site menu, table of contents, pagination)",
      tag: "<nav>",
      decoys: ["<menu>", "<header>", "<links>"],
      hint: "Not all link groups belong here, only primary navigation."
    },
    {
      id: 7,
      category: "HTML5 Semantic",
      desc: "Self-contained illustration, code snippet, diagram with an optional caption",
      tag: "<figure>",
      decoys: ["<picture>", "<img>", "<canvas>"],
      hint: "Paired with <figcaption> for accessible captions."
    },
    {
      id: 8,
      category: "HTML5 Semantic",
      desc: "Native dialog, alert modal, or subwindow with built-in backdrop support",
      tag: "<dialog>",
      decoys: ["<modal>", "<popup>", "<window>"],
      hint: "Opened via JavaScript dialog.showModal()."
    },
    {
      id: 9,
      category: "HTML5 Semantic",
      desc: "Client-side template HTML held inert in DOM until cloned via JavaScript",
      tag: "<template>",
      decoys: ["<slot>", "<script>", "<hidden>"],
      hint: "Contents are parsed but not rendered until stamped into DOM."
    },
    {
      id: 10,
      category: "HTML5 Semantic",
      desc: "Marked or highlighted text for visual reference in a search or quote",
      tag: "<mark>",
      decoys: ["<highlight>", "<em>", "<strong>"],
      hint: "Default yellow background highlight in most browsers."
    },
    {
      id: 11,
      category: "CSS Pseudo-Class",
      desc: "Selects alternating even-numbered sibling elements inside a list",
      tag: ":nth-child(even)",
      decoys: [":nth-of-type(odd)", ":even", ":nth(2n+1)"],
      hint: "Commonly used for zebra-striped tables."
    },
    {
      id: 12,
      category: "CSS Relational",
      desc: "Parent selector matching an element if any nested descendants match the condition",
      tag: ":has()",
      decoys: [":is()", ":where()", ":parent()"],
      hint: "Modern relational selector (e.g. h1:has(+ p))."
    },
    {
      id: 13,
      category: "CSS Attribute",
      desc: "Attribute selector matching elements whose attribute value begins with a prefix",
      tag: "[attr^='val']",
      decoys: ["[attr$='val']", "[attr*='val']", "[attr~='val']"],
      hint: "Caret (^) denotes start of string in regex and CSS."
    },
    {
      id: 14,
      category: "HTTP Status",
      desc: "HTTP response code indicating successful request and creation of a new resource",
      tag: "201 Created",
      decoys: ["200 OK", "204 No Content", "202 Accepted"],
      hint: "Standard response for POST API endpoints."
    },
    {
      id: 15,
      category: "HTTP Status",
      desc: "HTTP response code indicating cached client resource is fresh and unchanged",
      tag: "304 Not Modified",
      decoys: ["301 Moved", "302 Found", "204 No Content"],
      hint: "Transfers zero body payload; relies on HTTP ETag validation."
    },
    {
      id: 16,
      category: "HTTP Status",
      desc: "HTTP status code indicating client sent too many requests in given timeframe",
      tag: "429 Too Many Requests",
      decoys: ["403 Forbidden", "400 Bad Request", "503 Service Unavailable"],
      hint: "Triggers rate limiter backoff protocols."
    },
    {
      id: 17,
      category: "Git CLI",
      desc: "Command to apply changes introduced by a specific existing commit to current branch",
      tag: "git cherry-pick",
      decoys: ["git merge", "git rebase", "git checkout"],
      hint: "Port bug fixes across branches without merging entire history."
    },
    {
      id: 18,
      category: "Git CLI",
      desc: "Command to temporarily stash modified tracked files to get a clean working tree",
      tag: "git stash",
      decoys: ["git clean", "git reset", "git pause"],
      hint: "Reapplied later via git stash pop."
    },
    {
      id: 19,
      category: "SQL Clauses",
      desc: "SQL clause used to filter aggregated group records after a GROUP BY statement",
      tag: "HAVING",
      decoys: ["WHERE", "FILTER", "LIMIT"],
      hint: "Used when filtering on aggregate functions like COUNT() or AVG()."
    },
    {
      id: 20,
      category: "SQL Functions",
      desc: "SQL function returning the first non-null expression from a list of arguments",
      tag: "COALESCE()",
      decoys: ["IFNULL()", "NULLIF()", "NVL()"],
      hint: "Standard ANSI SQL function for handling fallback defaults."
    },
  ];

  let currentDrillIdx = 0;
  let score = 0;
  const completedDrills = new Set(JSON.parse(localStorage.getItem('cq_completed_tagmatch') || '[]'));

  function getQueryLevel() {
    const params = new URLSearchParams(window.location.search);
    const lvl = parseInt(params.get('level'), 10);
    if (!isNaN(lvl) && lvl >= 1 && lvl <= DRILLS.length) {
      return lvl - 1;
    }
    return 0;
  }

  function getCsrf() {
    const match = document.cookie.match(/csrftoken=([^;]+)/);
    return match ? match[1] : '';
  }

  function initGame() {
    const promptEl = document.getElementById("gamePrompt");
    const optionsEl = document.getElementById("gameOptions");
    const scoreEl = document.getElementById("gameScore");
    const feedbackEl = document.getElementById("gameFeedback");
    const drillTitle = document.getElementById("tagMissionTitle");
    const categoryBadge = document.getElementById("tagCategoryBadge");
    const levelPillsContainer = document.getElementById("tagLevelPills");

    currentDrillIdx = getQueryLevel();

    function renderLevelSelector() {
      if (!levelPillsContainer) return;
      levelPillsContainer.innerHTML = "";
      DRILLS.forEach(function (d, idx) {
        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = "btn " + (idx === currentDrillIdx ? "btn-primary" : "btn-ghost");
        btn.style.padding = "0.3rem 0.65rem";
        btn.style.fontSize = "0.76rem";
        btn.style.fontFamily = "var(--font-mono)";
        btn.style.borderRadius = "6px";
        btn.style.minWidth = "36px";

        const isDone = completedDrills.has(d.id);
        btn.innerHTML = `${d.id}${isDone ? ' <span style="color:#10b981;">✓</span>' : ''}`;
        btn.title = `Drill ${d.id}: ${d.category} — ${d.tag}`;

        btn.onclick = function () {
          currentDrillIdx = idx;
          renderRound();
          renderLevelSelector();
        };
        levelPillsContainer.appendChild(btn);
      });
    }

    function renderRound() {
      const q = DRILLS[currentDrillIdx];
      if (drillTitle) {
        drillTitle.textContent = `Drill ${q.id} of 20: ${q.category}`;
      }
      if (categoryBadge) {
        categoryBadge.textContent = q.category;
      }
      promptEl.textContent = q.desc;
      feedbackEl.textContent = "";

      const pool = [q.tag].concat(q.decoys);
      pool.sort(() => Math.random() - 0.5);

      optionsEl.innerHTML = "";
      pool.forEach(function (tag) {
        const btn = document.createElement("button");
        btn.className = "btn btn-ghost font-mono";
        btn.style.fontSize = "1.05rem";
        btn.style.padding = "1rem 1.25rem";
        btn.style.fontWeight = "700";
        btn.style.border = "1px solid var(--border-subtle)";
        btn.textContent = tag;

        btn.onclick = function () {
          if (tag === q.tag) {
            score += 25;
            completedDrills.add(q.id);
            localStorage.setItem('cq_completed_tagmatch', JSON.stringify(Array.from(completedDrills)));
            if (scoreEl) scoreEl.textContent = score;
            feedbackEl.innerHTML = `<span style="color:#10b981;font-weight:700;">✔ Correct! ${q.tag}</span> — ${q.hint}`;
            feedbackEl.style.color = "var(--accent)";
            btn.style.background = "rgba(16, 185, 129, 0.25)";
            btn.style.borderColor = "#10b981";

            if (window.CodeQuest) window.CodeQuest.playTone("success");
            renderLevelSelector();

            setTimeout(function () {
              if (currentDrillIdx < DRILLS.length - 1) {
                currentDrillIdx++;
                renderRound();
                renderLevelSelector();
              } else {
                feedbackEl.innerHTML = "🎉 All 20 Tag & Syntax Drills Mastered! Semantic Mastery Unlocked.";
                if (window.CodeQuest) {
                  window.CodeQuest.playTone("win");
                  window.CodeQuest.fireConfetti();
                }
                fetch('/api/games/tag-match/score/', { method: 'POST', headers: { 'X-CSRFToken': getCsrf() } });
              }
            }, 1800);
          } else {
            feedbackEl.innerHTML = `<span style="color:#ef4444;font-weight:700;">Incorrect match.</span> Hint: ${q.hint}`;
            feedbackEl.style.color = "#ef4444";
            btn.style.background = "rgba(239, 68, 68, 0.2)";
            btn.style.borderColor = "#ef4444";
            if (window.CodeQuest) window.CodeQuest.playTone("error");
          }
        };

        optionsEl.appendChild(btn);
      });
    }

    renderLevelSelector();
    renderRound();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initGame);
  } else {
    initGame();
  }
})();
