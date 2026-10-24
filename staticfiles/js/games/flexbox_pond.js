/**
 * CodeQuest Mini-Game 2: Flexbox & CSS Grid Alignment Pond
 * 20 Interactive Layout Levels (10 Flexbox + 10 CSS Grid)
 */
(function () {
  'use strict';

  const LEVELS = [
    // --- Levels 1 to 10: CSS Flexbox Fundamentals ---
    {
      id: 1,
      title: "Flexbox: Align Right (justify-content)",
      mode: "flex",
      instructions: "Move the frog to the right lilypad using justify-content.",
      hint: "justify-content: flex-end;",
      padStyle: { justifyContent: "flex-end", alignItems: "flex-start" },
      test: function (css) {
        return /justify-content\s*:\s*(flex-end|end)/i.test(css);
      }
    },
    {
      id: 2,
      title: "Flexbox: Center Horizontally (justify-content)",
      mode: "flex",
      instructions: "Center the frog horizontally using justify-content.",
      hint: "justify-content: center;",
      padStyle: { justifyContent: "center", alignItems: "flex-start" },
      test: function (css) {
        return /justify-content\s*:\s*center/i.test(css);
      }
    },
    {
      id: 3,
      title: "Flexbox: Move to Bottom (align-items)",
      mode: "flex",
      instructions: "Move the frog to the bottom lilypad using align-items.",
      hint: "align-items: flex-end;",
      padStyle: { justifyContent: "flex-start", alignItems: "flex-end" },
      test: function (css) {
        return /align-items\s*:\s*(flex-end|end)/i.test(css);
      }
    },
    {
      id: 4,
      title: "Flexbox: Dead Center (2D Alignment)",
      mode: "flex",
      instructions: "Center the frog both horizontally and vertically in the pond.",
      hint: "justify-content: center; align-items: center;",
      padStyle: { justifyContent: "center", alignItems: "center" },
      test: function (css) {
        return /justify-content\s*:\s*center/i.test(css) && /align-items\s*:\s*center/i.test(css);
      }
    },
    {
      id: 5,
      title: "Flexbox: Bottom Right Corner",
      mode: "flex",
      instructions: "Move the frog to the bottom-right corner using both axes.",
      hint: "justify-content: flex-end; align-items: flex-end;",
      padStyle: { justifyContent: "flex-end", alignItems: "flex-end" },
      test: function (css) {
        return /justify-content\s*:\s*(flex-end|end)/i.test(css) && /align-items\s*:\s*(flex-end|end)/i.test(css);
      }
    },
    {
      id: 6,
      title: "Flexbox: Space Around Elements",
      mode: "flex",
      instructions: "Distribute elements with equal space around them along main axis.",
      hint: "justify-content: space-around;",
      padStyle: { justifyContent: "space-around", alignItems: "flex-start" },
      test: function (css) {
        return /justify-content\s*:\s*space-around/i.test(css);
      }
    },
    {
      id: 7,
      title: "Flexbox: Space Evenly Distribution",
      mode: "flex",
      instructions: "Distribute elements so spacing between any two edges is completely identical.",
      hint: "justify-content: space-evenly;",
      padStyle: { justifyContent: "space-evenly", alignItems: "flex-start" },
      test: function (css) {
        return /justify-content\s*:\s*space-evenly/i.test(css);
      }
    },
    {
      id: 8,
      title: "Flexbox: Vertical Column Stacking",
      mode: "flex",
      instructions: "Stack elements in a vertical column using flex-direction.",
      hint: "flex-direction: column;",
      padStyle: { flexDirection: "column", justifyContent: "flex-start", alignItems: "flex-start" },
      test: function (css) {
        return /flex-direction\s*:\s*column/i.test(css);
      }
    },
    {
      id: 9,
      title: "Flexbox: Reversed Row Layout",
      mode: "flex",
      instructions: "Reverse the direction of the row so elements flow right to left.",
      hint: "flex-direction: row-reverse;",
      padStyle: { flexDirection: "row-reverse", justifyContent: "flex-start", alignItems: "flex-start" },
      test: function (css) {
        return /flex-direction\s*:\s*row-reverse/i.test(css);
      }
    },
    {
      id: 10,
      title: "Flexbox: Column Centered Vertical",
      mode: "flex",
      instructions: "Stack vertically and center elements along cross-axis.",
      hint: "flex-direction: column; align-items: center;",
      padStyle: { flexDirection: "column", justifyContent: "flex-start", alignItems: "center" },
      test: function (css) {
        return /flex-direction\s*:\s*column/i.test(css) && /align-items\s*:\s*center/i.test(css);
      }
    },

    // --- Levels 11 to 20: CSS Grid Layouts ---
    {
      id: 11,
      title: "CSS Grid: Shorthand Center (place-items)",
      mode: "grid",
      instructions: "Use modern CSS Grid shorthand place-items to dead center the frog.",
      hint: "place-items: center;",
      padStyle: { display: "grid", placeItems: "center" },
      test: function (css) {
        return /place-items\s*:\s*center/i.test(css) || (/justify-items\s*:\s*center/i.test(css) && /align-items\s*:\s*center/i.test(css));
      }
    },
    {
      id: 12,
      title: "CSS Grid: Align Items to End",
      mode: "grid",
      instructions: "Align the grid item to the end of its column track using justify-items.",
      hint: "justify-items: end;",
      padStyle: { display: "grid", justifyItems: "end", alignItems: "start" },
      test: function (css) {
        return /justify-items\s*:\s*(end|flex-end)/i.test(css);
      }
    },
    {
      id: 13,
      title: "CSS Grid: Align Items to Bottom (align-items)",
      mode: "grid",
      instructions: "Align the grid item to the bottom row edge using align-items.",
      hint: "align-items: end;",
      padStyle: { display: "grid", justifyItems: "start", alignItems: "end" },
      test: function (css) {
        return /align-items\s*:\s*(end|flex-end)/i.test(css);
      }
    },
    {
      id: 14,
      title: "CSS Grid: Bottom-Right Shorthand (place-items)",
      mode: "grid",
      instructions: "Move the frog to the bottom right using place-items: end end.",
      hint: "place-items: end end;",
      padStyle: { display: "grid", placeItems: "end end" },
      test: function (css) {
        return /place-items\s*:\s*(end|flex-end)\s+(end|flex-end)/i.test(css) || (/justify-items\s*:\s*end/i.test(css) && /align-items\s*:\s*end/i.test(css));
      }
    },
    {
      id: 15,
      title: "CSS Grid: 3-Column Equal Grid Template",
      mode: "grid",
      instructions: "Define three equal flexible columns using repeat() and fr units.",
      hint: "grid-template-columns: repeat(3, 1fr);",
      padStyle: { display: "grid", gridTemplateColumns: "repeat(3, 1fr)" },
      test: function (css) {
        return /grid-template-columns\s*:\s*(repeat\(3,\s*1fr\)|1fr\s+1fr\s+1fr)/i.test(css);
      }
    },
    {
      id: 16,
      title: "CSS Grid: Proportional 1fr 2fr Columns",
      mode: "grid",
      instructions: "Create a 2-column grid where the second column is twice as wide as the first.",
      hint: "grid-template-columns: 1fr 2fr;",
      padStyle: { display: "grid", gridTemplateColumns: "1fr 2fr" },
      test: function (css) {
        return /grid-template-columns\s*:\s*1fr\s+2fr/i.test(css);
      }
    },
    {
      id: 17,
      title: "CSS Grid: Grid Gap Spacing",
      mode: "grid",
      instructions: "Set a 1.5rem gutter between grid cells using the gap property.",
      hint: "gap: 1.5rem;",
      padStyle: { display: "grid", gap: "1.5rem" },
      test: function (css) {
        return /gap\s*:\s*(1\.5rem|24px)/i.test(css);
      }
    },
    {
      id: 18,
      title: "CSS Grid: Align Full Grid Content to Center",
      mode: "grid",
      instructions: "Align the entire grid track block to the horizontal center of the container.",
      hint: "justify-content: center;",
      padStyle: { display: "grid", justifyContent: "center" },
      test: function (css) {
        return /justify-content\s*:\s*center/i.test(css);
      }
    },
    {
      id: 19,
      title: "CSS Grid: Auto-Flow Columns",
      mode: "grid",
      instructions: "Cause auto-placed grid items to fill columns instead of rows.",
      hint: "grid-auto-flow: column;",
      padStyle: { display: "grid", gridAutoFlow: "column" },
      test: function (css) {
        return /grid-auto-flow\s*:\s*column/i.test(css);
      }
    },
    {
      id: 20,
      title: "CSS Layout Master: Shorthand place-content",
      mode: "grid",
      instructions: "Center the entire grid and its items completely using place-content: center.",
      hint: "place-content: center;",
      padStyle: { display: "grid", placeContent: "center" },
      test: function (css) {
        return /place-content\s*:\s*center/i.test(css);
      }
    },
  ];

  let currentLevelIdx = 0;
  let score = 0;
  const completedLevels = new Set(JSON.parse(localStorage.getItem('cq_completed_flexpond') || '[]'));

  function getQueryLevel() {
    const params = new URLSearchParams(window.location.search);
    const lvl = parseInt(params.get('level'), 10);
    if (!isNaN(lvl) && lvl >= 1 && lvl <= LEVELS.length) {
      return lvl - 1;
    }
    return 0;
  }

  function getCsrf() {
    const match = document.cookie.match(/csrftoken=([^;]+)/);
    return match ? match[1] : '';
  }

  function initPond() {
    const pond = document.getElementById("pondArea");
    const frog = document.getElementById("pondFrog");
    const pad = document.getElementById("pondPad");
    const input = document.getElementById("cssInput");
    const checkBtn = document.getElementById("checkPondBtn");
    const feedback = document.getElementById("pondFeedback");
    const promptText = document.getElementById("pondPrompt");
    const missionTitle = document.getElementById("pondMissionTitle");
    const levelPillsContainer = document.getElementById("pondLevelPills");
    const containerModeBadge = document.getElementById("pondModeBadge");
    const containerCssPrefix = document.getElementById("pondCssPrefix");

    currentLevelIdx = getQueryLevel();

    function renderLevelSelector() {
      if (!levelPillsContainer) return;
      levelPillsContainer.innerHTML = "";
      LEVELS.forEach(function (lvl, idx) {
        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = "btn " + (idx === currentLevelIdx ? "btn-primary" : "btn-ghost");
        btn.style.padding = "0.3rem 0.65rem";
        btn.style.fontSize = "0.76rem";
        btn.style.fontFamily = "var(--font-mono)";
        btn.style.borderRadius = "6px";
        btn.style.minWidth = "36px";

        const isDone = completedLevels.has(lvl.id);
        btn.innerHTML = `${lvl.id}${isDone ? ' <span style="color:#10b981;">✓</span>' : ''}`;
        btn.title = `Level ${lvl.id}: ${lvl.title}`;

        btn.onclick = function () {
          currentLevelIdx = idx;
          loadLevel();
          renderLevelSelector();
        };
        levelPillsContainer.appendChild(btn);
      });
    }

    function applyStyles(element, styleObj) {
      // Reset layout styles
      element.style.display = styleObj.display || (LEVELS[currentLevelIdx].mode === "grid" ? "grid" : "flex");
      element.style.justifyContent = styleObj.justifyContent || "";
      element.style.alignItems = styleObj.alignItems || "";
      element.style.flexDirection = styleObj.flexDirection || "";
      element.style.justifyItems = styleObj.justifyItems || "";
      element.style.placeItems = styleObj.placeItems || "";
      element.style.placeContent = styleObj.placeContent || "";
      element.style.gridTemplateColumns = styleObj.gridTemplateColumns || "";
      element.style.gridAutoFlow = styleObj.gridAutoFlow || "";
      element.style.gap = styleObj.gap || "";
    }

    function loadLevel() {
      const lvl = LEVELS[currentLevelIdx];
      if (missionTitle) {
        missionTitle.textContent = `Level ${lvl.id} of 20: ${lvl.title}`;
      }
      if (containerModeBadge) {
        containerModeBadge.textContent = lvl.mode === "grid" ? "CSS Grid Mode" : "CSS Flexbox Mode";
      }
      if (containerCssPrefix) {
        containerCssPrefix.textContent = lvl.mode === "grid" ? "#pond { display: grid;" : "#pond { display: flex;";
      }

      promptText.textContent = lvl.instructions;
      input.value = "";
      input.placeholder = lvl.hint;
      feedback.textContent = "";

      // Apply target styles to the Lilypad layer
      applyStyles(pad, lvl.padStyle);

      // Reset frog layer to default
      applyStyles(pond, { display: lvl.mode === "grid" ? "grid" : "flex" });
    }

    // Real-time CSS live typing reaction
    input.addEventListener("input", function () {
      const userCss = input.value.trim();
      const tempDiv = document.createElement("div");
      tempDiv.style.cssText = userCss;

      // Extract inline properties and apply dynamically to pond
      if (tempDiv.style.justifyContent) pond.style.justifyContent = tempDiv.style.justifyContent;
      if (tempDiv.style.alignItems) pond.style.alignItems = tempDiv.style.alignItems;
      if (tempDiv.style.flexDirection) pond.style.flexDirection = tempDiv.style.flexDirection;
      if (tempDiv.style.justifyItems) pond.style.justifyItems = tempDiv.style.justifyItems;
      if (tempDiv.style.placeItems) pond.style.placeItems = tempDiv.style.placeItems;
      if (tempDiv.style.placeContent) pond.style.placeContent = tempDiv.style.placeContent;
      if (tempDiv.style.gridTemplateColumns) pond.style.gridTemplateColumns = tempDiv.style.gridTemplateColumns;
      if (tempDiv.style.gridAutoFlow) pond.style.gridAutoFlow = tempDiv.style.gridAutoFlow;
      if (tempDiv.style.gap) pond.style.gap = tempDiv.style.gap;
    });

    checkBtn.addEventListener("click", function () {
      const lvl = LEVELS[currentLevelIdx];
      const userVal = input.value.trim();

      if (lvl.test(userVal)) {
        score += 25;
        completedLevels.add(lvl.id);
        localStorage.setItem('cq_completed_flexpond', JSON.stringify(Array.from(completedLevels)));

        feedback.innerHTML = `<span style="color: #10b981; font-weight: 700;">✔ Perfect alignment! The frog reached its pad.</span>`;
        if (window.CodeQuest) window.CodeQuest.playTone("success");
        renderLevelSelector();

        setTimeout(function () {
          if (currentLevelIdx < LEVELS.length - 1) {
            currentLevelIdx++;
            loadLevel();
            renderLevelSelector();
          } else {
            feedback.innerHTML = "🏆 All 20 Flexbox & CSS Grid Levels Solved! Master of Web Layouts.";
            if (window.CodeQuest) {
              window.CodeQuest.playTone("win");
              window.CodeQuest.fireConfetti();
            }
            fetch('/api/games/flexbox-pond/score/', { method: 'POST', headers: { 'X-CSRFToken': getCsrf() } });
          }
        }, 1800);
      } else {
        feedback.innerHTML = `<span style="color: #ef4444; font-weight: 700;">Not quite aligned.</span> Hint: <code>${lvl.hint}</code>`;
        if (window.CodeQuest) window.CodeQuest.playTone("error");
      }
    });

    renderLevelSelector();
    loadLevel();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initPond);
  } else {
    initPond();
  }
})();
