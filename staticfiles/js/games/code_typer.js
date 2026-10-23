/**
 * CodeQuest Mini-Game 4: Code Typer
 */
(function () {
  'use strict';

  const SNIPPETS = [
    "const result = items.map(x => x * 2);",
    "for i in range(len(records)):",
    "SELECT name, email FROM users WHERE id = 1;",
    "display: flex; justify-content: space-between;",
    "public static void main(String[] args) {",
  ];

  let currentTarget = "";
  let startTime = null;

  function initTyper() {
    const targetEl = document.getElementById("targetCodeSnippet");
    const inputEl = document.getElementById("typeInputBox");
    const wpmEl = document.getElementById("wpmScore");
    const accEl = document.getElementById("accuracyScore");
    const feedbackEl = document.getElementById("typeFeedback");
    const newBtn = document.getElementById("newSnippetBtn");

    function pickSnippet() {
      currentTarget = SNIPPETS[Math.floor(Math.random() * SNIPPETS.length)];
      targetEl.textContent = currentTarget;
      inputEl.value = "";
      inputEl.disabled = false;
      inputEl.focus();
      startTime = null;
      feedbackEl.textContent = "Start typing to begin timing...";
      feedbackEl.style.color = "var(--text-muted)";
    }

    inputEl.addEventListener("input", function () {
      if (!startTime) startTime = Date.now();
      const val = inputEl.value;

      // Calculate accuracy
      let correctChars = 0;
      for (let i = 0; i < val.length; i++) {
        if (val[i] === currentTarget[i]) correctChars++;
      }
      const acc = val.length > 0 ? Math.round((correctChars / val.length) * 100) : 100;
      if (accEl) accEl.textContent = acc + "%";

      // Calculate WPM
      const elapsedSec = (Date.now() - startTime) / 1000;
      const words = val.length / 5;
      const wpm = elapsedSec > 0 ? Math.round((words / elapsedSec) * 60) : 0;
      if (wpmEl) wpmEl.textContent = wpm.toString();

      if (val === currentTarget) {
        feedbackEl.textContent = `🎉 Flawless! Speed: ${wpm} WPM | Accuracy: ${acc}%`;
        feedbackEl.style.color = "var(--accent)";
        inputEl.disabled = true;
        if (window.CodeQuest) {
          window.CodeQuest.playTone("win");
          window.CodeQuest.fireConfetti();
        }
        fetch('/api/games/code-typer/score/', { method: 'POST', headers: { 'X-CSRFToken': getCsrf() } });
      }
    });

    if (newBtn) newBtn.onclick = pickSnippet;
    pickSnippet();
  }

  function getCsrf() {
    const match = document.cookie.match(/csrftoken=([^;]+)/);
    return match ? match[1] : '';
  }

  window.addEventListener("DOMContentLoaded", initTyper);
})();
