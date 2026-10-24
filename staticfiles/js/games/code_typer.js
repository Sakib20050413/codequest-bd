/**
 * CodeQuest BD — Code TypeRacer 3D Simulation
 * 20 High-Speed Keystroke Racing Tracks across 10 Programming Languages
 */
(function () {
  'use strict';

  const TRACKS = [
    {
      id: 1,
      title: "JavaScript: Array Transformations",
      lang: "JavaScript",
      snippet: "const result = items.filter(x => x.active).map(x => x.score * 2);",
      bot1Wpm: 52,
      bot2Wpm: 38
    },
    {
      id: 2,
      title: "Python: Data Pipeline & Sum",
      lang: "Python",
      snippet: "def calculate_total(prices, tax_rate=0.08): return sum(prices) * (1 + tax_rate)",
      bot1Wpm: 48,
      bot2Wpm: 36
    },
    {
      id: 3,
      title: "SQL: Modern User Query",
      lang: "SQL",
      snippet: "SELECT id, username, email FROM auth_users WHERE is_active = true ORDER BY id DESC;",
      bot1Wpm: 55,
      bot2Wpm: 40
    },
    {
      id: 4,
      title: "CSS: Responsive Flex Container",
      lang: "CSS",
      snippet: "display: flex; align-items: center; justify-content: space-between; gap: 1rem;",
      bot1Wpm: 50,
      bot2Wpm: 35
    },
    {
      id: 5,
      title: "React: State & Loading Hook",
      lang: "React / JS",
      snippet: "const [state, setState] = useState({ count: 0, loading: false });",
      bot1Wpm: 54,
      bot2Wpm: 42
    },
    {
      id: 6,
      title: "JavaScript: Fetch & Promise Stream",
      lang: "JavaScript",
      snippet: "fetch('/api/v1/telemetry').then(r => r.json()).then(data => update(data));",
      bot1Wpm: 56,
      bot2Wpm: 41
    },
    {
      id: 7,
      title: "Rust: Safe Memory Allocation",
      lang: "Rust",
      snippet: "let mut buffer: Vec<u8> = Vec::with_capacity(1024); buffer.push(42);",
      bot1Wpm: 50,
      bot2Wpm: 37
    },
    {
      id: 8,
      title: "TypeScript: Generic Response Interface",
      lang: "TypeScript",
      snippet: "interface ApiResponse<T> { status: number; data: T; timestamp: string; }",
      bot1Wpm: 52,
      bot2Wpm: 39
    },
    {
      id: 9,
      title: "C++: Vector Sorting Algorithm",
      lang: "C++",
      snippet: "std::vector<int> nums = {5, 2, 8, 1}; std::sort(nums.begin(), nums.end());",
      bot1Wpm: 53,
      bot2Wpm: 38
    },
    {
      id: 10,
      title: "Go: Goroutines & Channel Concurrency",
      lang: "Go",
      snippet: "ch := make(chan int, 5); go func() { ch <- computeResult() }();",
      bot1Wpm: 55,
      bot2Wpm: 43
    },
    {
      id: 11,
      title: "Java: Stream Filter Collection",
      lang: "Java",
      snippet: "List<String> valid = list.stream().filter(s -> !s.isEmpty()).collect(Collectors.toList());",
      bot1Wpm: 58,
      bot2Wpm: 44
    },
    {
      id: 12,
      title: "Python: List Comprehension Filter",
      lang: "Python",
      snippet: "squares = [x**2 for x in range(10) if x % 2 == 0]",
      bot1Wpm: 47,
      bot2Wpm: 34
    },
    {
      id: 13,
      title: "HTML5: Semantic Container",
      lang: "HTML5",
      snippet: "<main class=\"container\"><section class=\"hero\"><h1 class=\"title\">CodeQuest</h1></section></main>",
      bot1Wpm: 60,
      bot2Wpm: 45
    },
    {
      id: 14,
      title: "Docker: Production Buildfile",
      lang: "Docker",
      snippet: "FROM node:20-alpine WORKDIR /app COPY package*.json ./ RUN npm ci",
      bot1Wpm: 51,
      bot2Wpm: 36
    },
    {
      id: 15,
      title: "Bash: Log Rotation & Archival",
      lang: "Bash",
      snippet: "find /var/log -type f -name \"*.log\" -mtime +30 -exec gzip {} \\;",
      bot1Wpm: 49,
      bot2Wpm: 35
    },
    {
      id: 16,
      title: "CSS: Container Query Responsive",
      lang: "CSS",
      snippet: "@container (min-width: 400px) { .card { grid-template-columns: 1fr 2fr; } }",
      bot1Wpm: 54,
      bot2Wpm: 40
    },
    {
      id: 17,
      title: "SQL: Window Function Dense Rank",
      lang: "SQL",
      snippet: "SELECT name, salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rank FROM staff;",
      bot1Wpm: 56,
      bot2Wpm: 41
    },
    {
      id: 18,
      title: "Python: Context Manager Safe IO",
      lang: "Python",
      snippet: "with open('config.json', 'r', encoding='utf-8') as f: data = json.load(f)",
      bot1Wpm: 50,
      bot2Wpm: 38
    },
    {
      id: 19,
      title: "JavaScript: Nullish Coalescing & Optional Chaining",
      lang: "JavaScript",
      snippet: "const street = user?.profile?.address?.street ?? 'Default Avenue';",
      bot1Wpm: 53,
      bot2Wpm: 39
    },
    {
      id: 20,
      title: "Rust: Pattern Matching Result Handling",
      lang: "Rust",
      snippet: "match result { Ok(val) => println!(\"OK: {}\", val), Err(e) => eprintln!(\"Err: {}\", e) };",
      bot1Wpm: 57,
      bot2Wpm: 42
    },
  ];

  let currentTrackIdx = 0;
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

  const completedTracks = new Set(JSON.parse(localStorage.getItem('cq_completed_typeracer') || '[]'));

  function getQueryLevel() {
    const params = new URLSearchParams(window.location.search);
    const lvl = parseInt(params.get('level'), 10);
    if (!isNaN(lvl) && lvl >= 1 && lvl <= TRACKS.length) {
      return lvl - 1;
    }
    return 0;
  }

  function getCsrf() {
    const match = document.cookie.match(/csrftoken=([^;]+)/);
    return match ? match[1] : '';
  }

  function initTypeRacer() {
    const inputEl = document.getElementById("typeInputBox");
    const targetRenderEl = document.getElementById("targetSnippetRender");
    const wpmEl = document.getElementById("wpmScore");
    const accEl = document.getElementById("accuracyScore");
    const rankEl = document.getElementById("racerRank");
    const statusTextEl = document.getElementById("raceStatusText");
    const restartBtn = document.getElementById("restartRaceBtn");
    const modalRestartBtn = document.getElementById("modalRestartBtn");
    const trackPillsContainer = document.getElementById("trackPillsContainer");
    const trackMissionTitle = document.getElementById("trackMissionTitle");

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

    currentTrackIdx = getQueryLevel();

    function renderTrackSelector() {
      if (!trackPillsContainer) return;
      trackPillsContainer.innerHTML = "";
      TRACKS.forEach(function (tr, idx) {
        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = "btn " + (idx === currentTrackIdx ? "btn-primary" : "btn-ghost");
        btn.style.padding = "0.3rem 0.65rem";
        btn.style.fontSize = "0.76rem";
        btn.style.fontFamily = "var(--font-mono)";
        btn.style.borderRadius = "6px";
        btn.style.minWidth = "36px";

        const isDone = completedTracks.has(tr.id);
        btn.innerHTML = `${tr.id}${isDone ? ' <span style="color:#10b981;">✓</span>' : ''}`;
        btn.title = `Track ${tr.id}: ${tr.title} (${tr.lang})`;

        btn.onclick = function () {
          currentTrackIdx = idx;
          resetRace();
          renderTrackSelector();
        };
        trackPillsContainer.appendChild(btn);
      });
    }

    function renderHighlightedSnippet(typedText) {
      if (!targetRenderEl) return;
      let html = "";
      for (let i = 0; i < currentTarget.length; i++) {
        const char = currentTarget[i];
        const displayChar = char === ' ' ? '&nbsp;' : (char === '<' ? '&lt;' : (char === '>' ? '&gt;' : (char === '&' ? '&amp;' : char)));

        if (i < typedText.length) {
          if (typedText[i] === char) {
            html += `<span style="color: #10b981; font-weight: 700;">${displayChar}</span>`;
          } else {
            html += `<span style="color: #ef4444; background: rgba(239, 68, 68, 0.25); border-bottom: 2px solid #ef4444;">${displayChar}</span>`;
          }
        } else if (i === typedText.length) {
          html += `<span style="background: var(--accent); color: #040812; font-weight: 800; border-radius: 2px;">${displayChar}</span>`;
        } else {
          html += `<span style="color: var(--text-muted);">${displayChar}</span>`;
        }
      }
      targetRenderEl.innerHTML = html;
    }

    function resetRace() {
      if (botTimer) clearInterval(botTimer);

      const track = TRACKS[currentTrackIdx];
      currentTarget = track.snippet;
      if (trackMissionTitle) {
        trackMissionTitle.textContent = `Circuit Track ${track.id} of 20: ${track.title}`;
      }

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
        inputEl.placeholder = "Click here and start typing to race...";
        inputEl.focus();
      }

      if (wpmEl) wpmEl.textContent = "0";
      if (accEl) accEl.textContent = "100%";
      if (rankEl) {
        rankEl.textContent = "1st";
        rankEl.style.color = "#fbbf24";
      }
      if (statusTextEl) statusTextEl.textContent = "Waiting for your first keystroke...";

      updateCarPosition(playerCar, playerPctEl, 0);
      updateCarPosition(bot1Car, bot1PctEl, 0);
      updateCarPosition(bot2Car, bot2PctEl, 0);

      renderHighlightedSnippet("");
      if (podiumModal) podiumModal.style.display = "none";
    }

    function updateCarPosition(carEl, pctEl, percentage) {
      const clamped = Math.min(100, Math.max(0, percentage));
      if (carEl) {
        carEl.style.left = `calc(${clamped}% - ${clamped > 90 ? '36px' : '0px'})`;
      }
      if (pctEl) {
        pctEl.textContent = `${Math.round(clamped)}%`;
      }
    }

    function startBots() {
      const track = TRACKS[currentTrackIdx];
      const bot1CharsPerSec = (track.bot1Wpm * 5) / 60;
      const bot2CharsPerSec = (track.bot2Wpm * 5) / 60;

      botTimer = setInterval(function () {
        if (!raceActive) return;

        // Add some jitter
        const jitter1 = (Math.random() - 0.5) * 0.4;
        const jitter2 = (Math.random() - 0.5) * 0.4;

        if (bot1Progress < 100) {
          bot1Progress += ((bot1CharsPerSec + jitter1) / currentTarget.length) * 100 * 0.1;
          if (bot1Progress >= 100) {
            bot1Progress = 100;
            if (!bot1FinishTime) bot1FinishTime = Date.now();
          }
          updateCarPosition(bot1Car, bot1PctEl, bot1Progress);
        }

        if (bot2Progress < 100) {
          bot2Progress += ((bot2CharsPerSec + jitter2) / currentTarget.length) * 100 * 0.1;
          if (bot2Progress >= 100) {
            bot2Progress = 100;
            if (!bot2FinishTime) bot2FinishTime = Date.now();
          }
          updateCarPosition(bot2Car, bot2PctEl, bot2Progress);
        }

        // Update live rank
        if (!raceFinished) {
          let rank = 1;
          if (bot1Progress > (inputEl.value.length / currentTarget.length) * 100) rank++;
          if (bot2Progress > (inputEl.value.length / currentTarget.length) * 100) rank++;

          if (rankEl) {
            if (rank === 1) {
              rankEl.textContent = "1st";
              rankEl.style.color = "#fbbf24";
            } else if (rank === 2) {
              rankEl.textContent = "2nd";
              rankEl.style.color = "#94a3b8";
            } else {
              rankEl.textContent = "3rd";
              rankEl.style.color = "#f97316";
            }
          }
        }
      }, 100);
    }

    function finishRace(finalWpm, finalAccuracy) {
      raceFinished = true;
      raceActive = false;
      playerFinishTime = Date.now();
      if (botTimer) clearInterval(botTimer);

      if (inputEl) inputEl.disabled = true;

      let position = 1;
      if (bot1FinishTime && bot1FinishTime < playerFinishTime) position++;
      if (bot2FinishTime && bot2FinishTime < playerFinishTime) position++;

      completedTracks.add(TRACKS[currentTrackIdx].id);
      localStorage.setItem('cq_completed_typeracer', JSON.stringify(Array.from(completedTracks)));
      renderTrackSelector();

      if (statusTextEl) {
        statusTextEl.textContent = `Race finished! You placed #${position} with ${finalWpm} WPM.`;
      }

      if (position === 1) {
        if (podiumIcon) podiumIcon.textContent = "🥇";
        if (podiumTitle) podiumTitle.textContent = "VICTORY! 1st Place Podium!";
        if (window.CodeQuest) {
          window.CodeQuest.playTone("win");
          window.CodeQuest.fireConfetti();
        }
      } else if (position === 2) {
        if (podiumIcon) podiumIcon.textContent = "🥈";
        if (podiumTitle) podiumTitle.textContent = "2nd Place! Superb Keystroke Pace!";
        if (window.CodeQuest) window.CodeQuest.playTone("success");
      } else {
        if (podiumIcon) podiumIcon.textContent = "🥉";
        if (podiumTitle) podiumTitle.textContent = "3rd Place Finish! Keep Honing Muscle Memory!";
        if (window.CodeQuest) window.CodeQuest.playTone("success");
      }

      if (podiumStats) {
        podiumStats.innerHTML = `
          <div style="display:flex; justify-content:space-around; gap:1rem;">
            <div><div style="font-size:0.75rem;color:var(--text-muted);">SPEED</div><div style="font-size:1.5rem;font-weight:800;color:var(--accent);">${finalWpm} WPM</div></div>
            <div><div style="font-size:0.75rem;color:var(--text-muted);">ACCURACY</div><div style="font-size:1.5rem;font-weight:800;color:#10b981;">${finalAccuracy}%</div></div>
            <div><div style="font-size:0.75rem;color:var(--text-muted);">CIRCUIT XP</div><div style="font-size:1.5rem;font-weight:800;color:#fbbf24;">+30 XP</div></div>
          </div>
        `;
      }

      if (podiumModal) podiumModal.style.display = "flex";

      fetch('/api/games/code-typer/score/', {
        method: 'POST',
        headers: { 'X-CSRFToken': getCsrf() }
      });
    }

    if (inputEl) {
      inputEl.addEventListener("input", function () {
        const val = inputEl.value;

        if (!raceActive && !raceFinished && val.length > 0) {
          raceActive = true;
          startTime = Date.now();
          startBots();
          if (statusTextEl) statusTextEl.textContent = "🏁 GREEN LIGHT! Racing to the finish line...";
        }

        renderHighlightedSnippet(val);

        const currentPct = (val.length / currentTarget.length) * 100;
        updateCarPosition(playerCar, playerPctEl, currentPct);

        let correctChars = 0;
        for (let i = 0; i < val.length; i++) {
          if (val[i] === currentTarget[i]) correctChars++;
        }
        const acc = val.length > 0 ? Math.round((correctChars / val.length) * 100) : 100;
        if (accEl) accEl.textContent = `${acc}%`;

        if (startTime) {
          const elapsedMinutes = (Date.now() - startTime) / 60000;
          const wordsTyped = correctChars / 5;
          const currentWpm = elapsedMinutes > 0 ? Math.round(wordsTyped / elapsedMinutes) : 0;
          if (wpmEl) wpmEl.textContent = currentWpm;

          if (val === currentTarget) {
            finishRace(currentWpm, acc);
          }
        }
      });
    }

    if (restartBtn) restartBtn.addEventListener("click", resetRace);
    if (modalRestartBtn) modalRestartBtn.addEventListener("click", resetRace);

    renderTrackSelector();
    resetRace();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initTypeRacer);
  } else {
    initTypeRacer();
  }
})();
