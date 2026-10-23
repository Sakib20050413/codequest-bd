/**
 * CodeQuest Mini-Game 2: Flexbox Pond
 */
(function () {
  'use strict';

  const LEVELS = [
    {
      instructions: "Move the frog to the right using justify-content.",
      targetClass: "justify-end",
      cssSolution: "justify-content: flex-end;",
      targetX: "flex-end",
      targetY: "flex-start",
    },
    {
      instructions: "Center the frog horizontally using justify-content.",
      targetClass: "justify-center",
      cssSolution: "justify-content: center;",
      targetX: "center",
      targetY: "flex-start",
    },
    {
      instructions: "Move the frog to the bottom using align-items.",
      targetClass: "align-end",
      cssSolution: "align-items: flex-end;",
      targetX: "flex-start",
      targetY: "flex-end",
    },
    {
      instructions: "Center the frog both horizontally and vertically.",
      targetClass: "center-both",
      cssSolution: "justify-content: center;\nalign-items: center;",
      targetX: "center",
      targetY: "center",
    },
  ];

  let levelIdx = 0;

  function initPond() {
    const pond = document.getElementById("pondArea");
    const frog = document.getElementById("pondFrog");
    const pad = document.getElementById("pondPad");
    const input = document.getElementById("cssInput");
    const checkBtn = document.getElementById("checkPondBtn");
    const feedback = document.getElementById("pondFeedback");
    const promptText = document.getElementById("pondPrompt");

    function loadLevel() {
      if (levelIdx >= LEVELS.length) {
        promptText.textContent = "🏆 All Flexbox Pond levels completed! You earned the Pond Champion badge.";
        input.disabled = true;
        checkBtn.disabled = true;
        if (window.CodeQuest) {
          window.CodeQuest.playTone("win");
          window.CodeQuest.fireConfetti();
        }
        fetch('/api/games/flexbox-pond/score/', { method: 'POST', headers: { 'X-CSRFToken': getCsrf() } });
        return;
      }

      const lvl = LEVELS[levelIdx];
      promptText.textContent = `Level ${levelIdx + 1} of ${LEVELS.length}: ${lvl.instructions}`;
      input.value = "";
      feedback.textContent = "";

      // Position target pad
      pad.style.justifyContent = lvl.targetX;
      pad.style.alignItems = lvl.targetY;
      pond.style.justifyContent = "flex-start";
      pond.style.alignItems = "flex-start";
    }

    input.addEventListener("input", function () {
      const val = input.value;
      const lines = val.split(";");
      lines.forEach((line) => {
        const parts = line.split(":");
        if (parts.length === 2) {
          const prop = parts[0].trim();
          const pval = parts[1].trim();
          if (prop === "justify-content" || prop === "align-items" || prop === "flex-direction") {
            pond.style[prop] = pval;
          }
        }
      });
    });

    checkBtn.onclick = function () {
      const lvl = LEVELS[levelIdx];
      const matchX = pond.style.justifyContent === lvl.targetX;
      const matchY = pond.style.alignItems === lvl.targetY;

      if (matchX && matchY) {
        feedback.textContent = "✔ Lily pad reached! Next level...";
        feedback.style.color = "var(--accent)";
        if (window.CodeQuest) window.CodeQuest.playTone("success");
        levelIdx++;
        setTimeout(loadLevel, 800);
      } else {
        feedback.textContent = "❌ The frog missed the pad. Check your properties.";
        feedback.style.color = "var(--danger)";
        if (window.CodeQuest) window.CodeQuest.playTone("error");
      }
    };

    loadLevel();
  }

  function getCsrf() {
    const match = document.cookie.match(/csrftoken=([^;]+)/);
    return match ? match[1] : '';
  }

  window.addEventListener("DOMContentLoaded", initPond);
})();
