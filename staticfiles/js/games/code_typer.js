/**
 * CodeQuest BD — Code TypeRacer 3D Simulation
 * Real-time multiplayer-style race track against AI competitors
 */
(function () {
  'use strict';

  const SNIPPETS = [
    "const result = items.filter(x => x.active).map(x => x.score * 2);",
    "for (let i = 0; i < records.length; i++) { renderCard(records[i]); }",
    "SELECT id, username, email FROM auth_users WHERE is_active = true;",
    "display: flex; align-items: center; justify-content: space-between;",
    "def calculate_total(prices, tax_rate=0.08): return sum(prices) * (1 + tax_rate)",
    "const [state, setState] = useState({ count: 0, loading: false });",
    "fetch('/api/v1/telemetry').then(r => r.json()).then(data => update(data));",
  ];

  let currentTarget = "";
  let raceActive = false;
  let raceFinished = false;
  let startTime = null;
  let botTimer = null;
  let bot1Progress = 0;
  let bot2Progress = 0;
  let playerFinishTime = null;
  let bot1FinishTime = null;
  let bot2FinishTime = null;

  function initTypeRacer() {
    const inputEl = document.getElementById("typeInputBox");
    const targetRenderEl = document.getElementById("targetSnippetRender");
    const wpmEl = document.getElementById("wpmScore");
    const accEl = document.getElementById("accuracyScore");
    const rankEl = document.getElementById("racerRank");
    const statusTextEl = document.getElementById("raceStatusText");
    const restartBtn = document.getElementById("restartRaceBtn");
    const modalRestartBtn = document.getElementById("modalRestartBtn");

    const playerCar = document.getElementById("playerCar");
    const bot1Car = document.getElementById("bot1Car");
    const bot2Car = document.getElementById("bot2Car");
    const playerPctEl = document.getElementById("playerProgressPct");
    const bot1PctEl = document.getElementById("bot1ProgressPct");
    const bot2PctEl = document.getElementById("bot2ProgressPct");

    const podiumModal = document.getElementById("racePodiumModal");
    const podiumIcon = document.getElementById("podiumIcon");
    const podiumTitle = document.getElementById("podiumTitle");
    const podiumStats = document.getElementById("podiumStats");

    function renderHighlightedSnippet(typedText) {
      if (!targetRenderEl) return;
      let html = "";
      for (let i = 0; i < currentTarget.length; i++) {
        const char = currentTarget[i];
        const displayChar = char === ' ' ? '&nbsp;' : (char === '<' ? '&lt;' : (char === '>' ? '&gt;' : char));

        if (i < typedText.length) {
          if (typedText[i] === char) {
            html += `<span style="color: #10b981; font-weight: 700;">${displayChar}</span>`;
          } else {
            html += `<span style="background: rgba(239, 68, 68, 0.4); color: #f87171; border-radius: 2px;">${displayChar}</span>`;
          }
        } else if (i === typedText.length) {
          html += `<span style="background: rgba(56, 189, 248, 0.3); border-bottom: 2px solid #38bdf8; color: #ffffff;">${displayChar}</span>`;
        } else {
          html += `<span style="color: var(--text-muted);">${displayChar}</span>`;
        }
      }
      targetRenderEl.innerHTML = html;
    }

    function resetRace() {
      clearInterval(botTimer);
      currentTarget = SNIPPETS[Math.floor(Math.random() * SNIPPETS.length)];
      raceActive = false;
      raceFinished = false;
      startTime = null;
      bot1Progress = 0;
      bot2Progress = 0;
      playerFinishTime = null;
      bot1FinishTime = null;
      bot2FinishTime = null;

      if (inputEl) {
        inputEl.value = "";
        inputEl.disabled = false;
        inputEl.focus();
      }

      if (wpmEl) wpmEl.textContent = "0";
      if (accEl) accEl.textContent = "100%";
      if (rankEl) {
        rankEl.textContent = "1st";
        rankEl.style.color = "#fbbf24";
      }
      if (statusTextEl) {
        statusTextEl.textContent = "Ready to race. Type below to launch!";
        statusTextEl.style.color = "var(--accent-secondary)";
      }

      if (playerCar) playerCar.style.left = "0%";
      if (bot1Car) bot1Car.style.left = "0%";
      if (bot2Car) bot2Car.style.left = "0%";
      if (playerPctEl) playerPctEl.textContent = "0%";
      if (bot1PctEl) bot1PctEl.textContent = "0%";
      if (bot2PctEl) bot2PctEl.textContent = "0%";

      if (podiumModal) podiumModal.style.display = "none";
      renderHighlightedSnippet("");
    }

    function startBotRacers() {
      // Bot 1 speeds at ~50 WPM (~4.2 chars/sec)
      // Bot 2 speeds at ~38 WPM (~3.2 chars/sec)
      const bot1CharSpeed = (48 * 5) / 60; // chars/sec
      const bot2CharSpeed = (38 * 5) / 60; // chars/sec

      botTimer = setInterval(function () {
        if (!raceActive) return;
        const elapsed = (Date.now() - startTime) / 1000;

        // Bot 1 (Turing)
        if (!bot1FinishTime) {
          const charsTyped = Math.min(currentTarget.length, Math.floor(elapsed * bot1CharSpeed + (Math.sin(elapsed) * 2)));
          bot1Progress = (charsTyped / currentTarget.length) * 100;
          if (bot1Car) bot1Car.style.left = `calc(${Math.min(92, bot1Progress * 0.92)}%)`;
          if (bot1PctEl) bot1PctEl.textContent = Math.round(bot1Progress) + "%";
          if (bot1Progress >= 100) {
            bot1FinishTime = Date.now();
          }
        }

        // Bot 2 (Ada)
        if (!bot2FinishTime) {
          const charsTyped = Math.min(currentTarget.length, Math.floor(elapsed * bot2CharSpeed));
          bot2Progress = (charsTyped / currentTarget.length) * 100;
          if (bot2Car) bot2Car.style.left = `calc(${Math.min(92, bot2Progress * 0.92)}%)`;
          if (bot2PctEl) bot2PctEl.textContent = Math.round(bot2Progress) + "%";
          if (bot2Progress >= 100) {
            bot2FinishTime = Date.now();
          }
        }

        updateRankings();
      }, 100);
    }

    function updateRankings() {
      const playerVal = inputEl ? inputEl.value : "";
      const playerProg = (playerVal.length / currentTarget.length) * 100;

      let rank = 1;
      if (bot1Progress > playerProg) rank++;
      if (bot2Progress > playerProg) rank++;

      if (rankEl) {
        if (rank === 1) {
          rankEl.textContent = "1st 🥇";
          rankEl.style.color = "#fbbf24";
        } else if (rank === 2) {
          rankEl.textContent = "2nd 🥈";
          rankEl.style.color = "#94a3b8";
        } else {
          rankEl.textContent = "3rd 🥉";
          rankEl.style.color = "#b45309";
        }
      }
    }

    if (inputEl) {
      inputEl.addEventListener("input", function () {
        if (!raceActive && !raceFinished) {
          raceActive = true;
          startTime = Date.now();
          startBotRacers();
          if (statusTextEl) {
            statusTextEl.textContent = "⚡ Race in progress! Full throttle!";
            statusTextEl.style.color = "#10b981";
          }
        }

        const val = inputEl.value;
        renderHighlightedSnippet(val);

        // Sound effect
        if (window.CodeQuest) window.CodeQuest.playTone("click");

        // Accuracy
        let correctChars = 0;
        for (let i = 0; i < val.length; i++) {
          if (val[i] === currentTarget[i]) correctChars++;
        }
        const acc = val.length > 0 ? Math.round((correctChars / val.length) * 100) : 100;
        if (accEl) {
          accEl.textContent = acc + "%";
          accEl.style.color = acc >= 95 ? "#10b981" : (acc >= 80 ? "#f59e0b" : "#ef4444");
        }

        // Speed WPM
        const elapsedSec = (Date.now() - startTime) / 1000;
        const words = val.length / 5;
        const wpm = elapsedSec > 0.5 ? Math.round((words / elapsedSec) * 60) : 0;
        if (wpmEl) wpmEl.textContent = wpm.toString();

        // Player car progression
        const playerProg = Math.min(100, (val.length / currentTarget.length) * 100);
        if (playerCar) {
          playerCar.style.left = `calc(${Math.min(92, playerProg * 0.92)}%)`;
        }
        if (playerPctEl) playerPctEl.textContent = Math.round(playerProg) + "%";

        updateRankings();

        // Check if finished
        if (val === currentTarget) {
          raceActive = false;
          raceFinished = true;
          playerFinishTime = Date.now();
          clearInterval(botTimer);
          inputEl.disabled = true;

          // Determine final rank
          let finalRank = "1st Place Champion! 🥇";
          let icon = "🏆";
          if (bot1FinishTime && bot1FinishTime < playerFinishTime) {
            finalRank = "2nd Place! 🥈";
            icon = "🥈";
          }
          if (bot2FinishTime && bot2FinishTime < playerFinishTime) {
            finalRank = "3rd Place! 🥉";
            icon = "🥉";
          }

          if (podiumModal && podiumTitle && podiumStats && podiumIcon) {
            podiumIcon.textContent = icon;
            podiumTitle.textContent = finalRank;
            podiumStats.textContent = `Finish Speed: ${wpm} WPM • Accuracy: ${acc}% • Reward: +25 XP`;
            podiumModal.style.display = "block";
          }

          if (window.CodeQuest) {
            window.CodeQuest.playTone("win");
            window.CodeQuest.fireConfetti();
          }

          fetch('/api/games/code-typer/score/', {
            method: 'POST',
            headers: { 'X-CSRFToken': getCsrf() }
          });
        }
      });
    }

    if (restartBtn) restartBtn.onclick = resetRace;
    if (modalRestartBtn) modalRestartBtn.onclick = resetRace;

    resetRace();
  }

  function getCsrf() {
    const match = document.cookie.match(/csrftoken=([^;]+)/);
    return match ? match[1] : '';
  }

  window.addEventListener("DOMContentLoaded", initTypeRacer);
})();
