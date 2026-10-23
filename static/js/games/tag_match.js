/**
 * CodeQuest Mini-Game 1: Tag Match
 */
(function () {
  'use strict';

  const QUESTIONS = [
    { desc: "Main content of the document unique to this page", tag: "<main>" },
    { desc: "Introductory content, logo or primary navigation", tag: "<header>" },
    { desc: "Footer containing copyright, links, or contact info", tag: "<footer>" },
    { desc: "Self-contained composition (blog post, news story)", tag: "<article>" },
    { desc: "Content indirectly related to the main content (sidebar)", tag: "<aside>" },
    { desc: "Section of navigation links", tag: "<nav>" },
  ];

  let current = 0;
  let score = 0;

  function initGame() {
    const promptEl = document.getElementById("gamePrompt");
    const optionsEl = document.getElementById("gameOptions");
    const scoreEl = document.getElementById("gameScore");
    const feedbackEl = document.getElementById("gameFeedback");

    function renderRound() {
      if (current >= QUESTIONS.length) {
        promptEl.textContent = "🎉 Round Complete! You mastered HTML semantic tags.";
        optionsEl.innerHTML = `<button class="btn btn-primary" onclick="location.reload()">Play Again</button>`;
        if (window.CodeQuest) {
          window.CodeQuest.playTone("win");
          window.CodeQuest.fireConfetti();
        }
        fetch('/api/games/tag-match/score/', { method: 'POST', headers: { 'X-CSRFToken': getCsrf() } });
        return;
      }

      const q = QUESTIONS[current];
      promptEl.textContent = q.desc;
      feedbackEl.textContent = "";

      // Shuffle options with 3 decoys
      const pool = [q.tag];
      while (pool.length < 4) {
        const rand = QUESTIONS[Math.floor(Math.random() * QUESTIONS.length)].tag;
        if (pool.indexOf(rand) === -1) pool.push(rand);
      }
      pool.sort(() => Math.random() - 0.5);

      optionsEl.innerHTML = "";
      pool.forEach(function (tag) {
        const btn = document.createElement("button");
        btn.className = "btn btn-ghost font-mono";
        btn.style.fontSize = "1rem";
        btn.style.padding = "0.75rem 1.25rem";
        btn.textContent = tag;
        btn.onclick = function () {
          if (tag === q.tag) {
            score += 20;
            if (scoreEl) scoreEl.textContent = score;
            if (window.CodeQuest) window.CodeQuest.playTone("success");
            feedbackEl.textContent = "✔ Correct!";
            feedbackEl.style.color = "var(--accent)";
            current++;
            setTimeout(renderRound, 400);
          } else {
            if (window.CodeQuest) window.CodeQuest.playTone("error");
            feedbackEl.textContent = "❌ Try again!";
            feedbackEl.style.color = "var(--danger)";
          }
        };
        optionsEl.appendChild(btn);
      });
    }

    renderRound();
  }

  function getCsrf() {
    const match = document.cookie.match(/csrftoken=([^;]+)/);
    return match ? match[1] : '';
  }

  window.addEventListener("DOMContentLoaded", initGame);
})();
