/**
 * CodeQuest Mini-Game 3: Bug Hunt
 */
(function () {
  'use strict';

  const BUGS = [
    {
      lang: "Python",
      lines: [
        "def calculate_total(prices):",
        "    total = 0",
        "    for p in prices",
        "        total += p",
        "    return total",
      ],
      bugLine: 2, // 0-indexed: missing colon
      reason: "Missing colon ':' at the end of the for statement.",
    },
    {
      lang: "JavaScript",
      lines: [
        "const user = 'Sakib';",
        "let xp = 200;",
        "if (user = 'Sakib') {",
        "    console.log(xp);",
        "}",
      ],
      bugLine: 2, // assignment instead of comparison ===
      reason: "Assignment '=' used inside condition instead of comparison '==='.",
    },
    {
      lang: "HTML",
      lines: [
        "<header>",
        "  <h1>Welcome</h1>",
        "  <img src='logo.png'>",
        "  <p>Overview",
        "</header>",
      ],
      bugLine: 3, // unclosed <p>
      reason: "Unclosed <p> tag before closing </header>.",
    },
  ];

  let bIdx = 0;
  let score = 0;

  function initBugHunt() {
    const codeArea = document.getElementById("bugCodeSnippet");
    const langBadge = document.getElementById("bugLangBadge");
    const feedback = document.getElementById("bugFeedback");
    const scoreDisplay = document.getElementById("bugScore");

    function loadBug() {
      if (bIdx >= BUGS.length) {
        codeArea.innerHTML = "<div style='padding:2rem;text-align:center;'>🎉 All bugs found! Superb code reviewing skills.</div>";
        feedback.textContent = `Final Score: ${score} XP`;
        if (window.CodeQuest) {
          window.CodeQuest.playTone("win");
          window.CodeQuest.fireConfetti();
        }
        fetch('/api/games/bug-hunt/score/', { method: 'POST', headers: { 'X-CSRFToken': getCsrf() } });
        return;
      }

      const item = BUGS[bIdx];
      langBadge.textContent = item.lang;
      feedback.textContent = "Click the line containing the bug:";
      feedback.style.color = "var(--text-muted)";
      codeArea.innerHTML = "";

      item.lines.forEach(function (line, idx) {
        const row = document.createElement("div");
        row.style.display = "flex";
        row.style.gap = "1rem";
        row.style.padding = "0.35rem 0.75rem";
        row.style.borderRadius = "6px";
        row.style.cursor = "pointer";
        row.style.fontFamily = "var(--font-mono)";
        row.style.fontSize = "0.85rem";
        row.className = "bug-line-row";

        const num = document.createElement("span");
        num.style.opacity = "0.4";
        num.style.userSelect = "none";
        num.textContent = (idx + 1).toString();

        const txt = document.createElement("span");
        txt.textContent = line;

        row.appendChild(num);
        row.appendChild(txt);

        row.onclick = function () {
          if (idx === item.bugLine) {
            score += 25;
            if (scoreDisplay) scoreDisplay.textContent = score;
            row.style.background = "rgba(16, 185, 129, 0.2)";
            feedback.textContent = `✔ Bug found on line ${idx + 1}! ${item.reason}`;
            feedback.style.color = "var(--accent)";
            if (window.CodeQuest) window.CodeQuest.playTone("success");
            bIdx++;
            setTimeout(loadBug, 1200);
          } else {
            row.style.background = "rgba(244, 63, 94, 0.2)";
            feedback.textContent = `❌ Line ${idx + 1} is clean. Look closer!`;
            feedback.style.color = "var(--danger)";
            if (window.CodeQuest) window.CodeQuest.playTone("error");
          }
        };

        codeArea.appendChild(row);
      });
    }

    loadBug();
  }

  function getCsrf() {
    const match = document.cookie.match(/csrftoken=([^;]+)/);
    return match ? match[1] : '';
  }

  window.addEventListener("DOMContentLoaded", initBugHunt);
})();
