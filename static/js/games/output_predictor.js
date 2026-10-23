/**
 * CodeQuest Mini-Game 5: Output Predictor
 */
(function () {
  'use strict';

  const QUESTIONS = [
    {
      lang: "Python",
      code: "a = [1, 2, 3]\nb = a\nb.append(4)\nprint(len(a))",
      opts: ["3", "4", "Error", "None"],
      ans: 1, // 4 (lists are reference types)
      explanation: "Lists in Python are mutable references; mutating b also mutates a.",
    },
    {
      lang: "JavaScript",
      code: "console.log(typeof NaN);",
      opts: ["'number'", "'NaN'", "'undefined'", "'object'"],
      ans: 0,
      explanation: "In JavaScript, NaN represents 'Not-a-Number', but its type is technically 'number'.",
    },
    {
      lang: "SQL",
      code: "SELECT COUNT(*) FROM users WHERE NULL = NULL;",
      opts: ["All users", "0", "NULL", "Syntax Error"],
      ans: 1,
      explanation: "In SQL, comparisons with NULL yield UNKNOWN/FALSE. Use IS NULL instead.",
    },
    {
      lang: "C Language",
      code: "int x = 5;\nprintf(\"%d\", x++);",
      opts: ["5", "6", "4", "0"],
      ans: 0,
      explanation: "Post-increment (x++) evaluates the original value (5) before incrementing.",
    },
  ];

  let qIdx = 0;
  let score = 0;

  function initPredictor() {
    const codeEl = document.getElementById("predictorSnippet");
    const langBadge = document.getElementById("predictorLang");
    const optionsEl = document.getElementById("predictorOptions");
    const feedbackEl = document.getElementById("predictorFeedback");
    const scoreEl = document.getElementById("predictorScore");

    function loadQ() {
      if (qIdx >= QUESTIONS.length) {
        codeEl.textContent = "🏆 Prediction Marathon Complete!";
        optionsEl.innerHTML = `<button class="btn btn-primary" onclick="location.reload()">Play Again</button>`;
        feedbackEl.textContent = `Final Score: ${score} XP`;
        if (window.CodeQuest) {
          window.CodeQuest.playTone("win");
          window.CodeQuest.fireConfetti();
        }
        fetch('/api/games/output-predictor/score/', { method: 'POST', headers: { 'X-CSRFToken': getCsrf() } });
        return;
      }

      const q = QUESTIONS[qIdx];
      langBadge.textContent = q.lang;
      codeEl.textContent = q.code;
      feedbackEl.textContent = "Predict what this snippet outputs:";
      feedbackEl.style.color = "var(--text-muted)";
      optionsEl.innerHTML = "";

      q.opts.forEach(function (opt, i) {
        const btn = document.createElement("button");
        btn.className = "btn btn-ghost font-mono";
        btn.style.fontSize = "0.95rem";
        btn.style.padding = "0.75rem 1.25rem";
        btn.textContent = `${String.fromCharCode(65 + i)}) ${opt}`;
        btn.onclick = function () {
          if (i === q.ans) {
            score += 25;
            if (scoreEl) scoreEl.textContent = score;
            feedbackEl.textContent = `✔ Correct! ${q.explanation}`;
            feedbackEl.style.color = "var(--accent)";
            if (window.CodeQuest) window.CodeQuest.playTone("success");
            qIdx++;
            setTimeout(loadQ, 1200);
          } else {
            feedbackEl.textContent = `❌ Incorrect. Think about language evaluation order!`;
            feedbackEl.style.color = "var(--danger)";
            if (window.CodeQuest) window.CodeQuest.playTone("error");
          }
        };
        optionsEl.appendChild(btn);
      });
    }

    loadQ();
  }

  function getCsrf() {
    const match = document.cookie.match(/csrftoken=([^;]+)/);
    return match ? match[1] : '';
  }

  window.addEventListener("DOMContentLoaded", initPredictor);
})();
