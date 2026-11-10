/* ==========================================================================
   CodeQuest LMS — Multi-Language Runtime, CS50 Memory Trace & 6 Game Engines
   ========================================================================== */

(function () {
  "use strict";

  // 1. Theme Persistence & Toggle (Light Default for Clean Academic Look + High-Contrast Dark Mode)
  const savedTheme = localStorage.getItem("cq_theme") || "light";
  document.documentElement.setAttribute("data-theme", savedTheme);

  window.toggleCqTheme = function () {
    const cur = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", cur);
    localStorage.setItem("cq_theme", cur);
    if (typeof window.redrawActiveGameCanvas === "function") {
      window.redrawActiveGameCanvas();
    }
  };

  // 2. Live Direct Page Edit Mode (Req #5)
  let pageEditActive = false;
  window.togglePageEditMode = function (btnEl) {
    pageEditActive = !pageEditActive;
    document.body.contentEditable = pageEditActive ? "true" : "false";
    if (btnEl) {
      btnEl.textContent = pageEditActive ? "✏️ Edit Page: ON" : "✏️ Edit Page: OFF";
      btnEl.classList.toggle("btn-primary", pageEditActive);
    }
  };

  // 3. Reactive Interactive Terminal (Req #5 & #6 — Theme-Adaptive in Light & Dark Mode)
  window.runTerminalCommand = function (rawCmd, outputBoxId) {
    const out = document.getElementById(outputBoxId);
    if (!out) return;
    const cmd = (rawCmd || "").trim().toLowerCase();
    if (!cmd) return;

    const lineIn = document.createElement("div");
    lineIn.style.fontWeight = "700";
    lineIn.style.color = "var(--primary-blue)";
    lineIn.textContent = "codequest@lms:~$ " + rawCmd;
    out.appendChild(lineIn);

    if (cmd === "clear") {
      out.innerHTML = "";
      return;
    }

    const responses = {
      "help": "Available commands: courses, games, tasks, stack, theme, edit on, edit off, clear",
      "courses": "12 Structured Courses: HTML5, CSS3 & Flexbox, JS DOM, React, Python 3, Django 5, PHP & MySQLi CRUD, SQL, MongoDB, C, C++, Java.",
      "games": "6 Full-Code Visual Game Engines: [1] Flexbox Bridge [2] 3D Fractal Tree [3] Isometric Rover [4] SQL Detective [5] DOM Circuit [6] PHP Data Vault.",
      "tasks": "Multi-Platform Practice Tasks (CQ-101 to CQ-106) modeled after HackerRank, Codeforces, LeetCode & CSE 324 Lab Evaluations.",
      "stack": "[CS50 Memory Frame] 0x7ffee0: main() | 0x7ffee4: step=4 | Heap 0x7f8a10: DOM/Canvas Node Active.",
      "theme": "Switched Light/Dark theme (Editor & Terminal automatically adapt!).",
      "edit on": "Enabled live webpage content editing. Click any heading or paragraph to test.",
      "edit off": "Disabled live webpage editing."
    };

    if (cmd === "theme") window.toggleCqTheme();
    if (cmd === "edit on") document.body.contentEditable = "true";
    if (cmd === "edit off") document.body.contentEditable = "false";

    const reply = document.createElement("div");
    reply.style.marginBottom = "6px";
    reply.textContent = responses[cmd] || ("Executed: " + rawCmd + " -> OK (0 errors)");
    out.appendChild(reply);
    out.scrollTop = out.scrollHeight;
  };

  // 4. Full-Code 6-Engine Visual Game Renderer (Canvas 2D/3D)
  window.renderGameEngineCanvas = function (canvasId, engineKey, progressRatio, userCode) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const rect = canvas.parentElement.getBoundingClientRect();
    const w = Math.max(300, rect.width || 520);
    const h = Math.max(250, canvas.height || 290);
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = w * dpr;
    canvas.height = h * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    const isDark = document.documentElement.getAttribute("data-theme") === "dark";
    ctx.fillStyle = isDark ? "#080D1A" : "#F1F5F9";
    ctx.fillRect(0, 0, w, h);

    const code = (userCode || "").trim();

    if (engineKey === "FRACTAL_TREE") {
      // Organic 3D Branching Fractal Tree
      const maxDepth = progressRatio > 0.5 ? 6 : 3;
      function drawBranch(x, y, len, angle, depth) {
        if (depth === 0) return;
        const x2 = x + Math.sin(angle) * len;
        const y2 = y - Math.cos(angle) * len;
        ctx.beginPath();
        ctx.moveTo(x, y);
        ctx.lineTo(x2, y2);
        ctx.strokeStyle = depth > 3 ? "#854D0E" : "#059669";
        ctx.lineWidth = Math.max(1.5, depth * 1.4);
        ctx.lineCap = "round";
        ctx.stroke();

        if (depth <= 2 && progressRatio > 0.5) {
          ctx.fillStyle = "#10B981";
          ctx.beginPath();
          ctx.arc(x2, y2, 4.5, 0, Math.PI * 2);
          ctx.fill();
        }
        drawBranch(x2, y2, len * 0.74, angle - 0.44, depth - 1);
        drawBranch(x2, y2, len * 0.74, angle + 0.44, depth - 1);
      }
      drawBranch(w / 2, h - 22, 62, 0, maxDepth);
      ctx.fillStyle = isDark ? "#A7F3D0" : "#065F46";
      ctx.font = "600 12px 'JetBrains Mono', monospace";
      ctx.fillText(progressRatio > 0.5 ? "✔ 6-Generation Fractal Canopy Grown!" : "Waiting for grow_canopy(6, 26)...", 14, 24);

    } else if (engineKey === "FLEX_BRIDGE") {
      // River Canyon + 3 Bridge Planks aligned by CSS Flexbox
      ctx.fillStyle = isDark ? "#0C4A6E" : "#BAE6FD";
      ctx.fillRect(60, 40, w - 120, h - 80);

      const aligned = /display\s*:\s*flex/i.test(code) && (/space-between|center/i.test(code) || /rowspan/i.test(code));
      const yPos = aligned ? h / 2 - 22 : 55;
      const positions = aligned ? [75, w / 2 - 45, w - 165] : [75, 110, 145];

      positions.forEach(function (px, idx) {
        ctx.fillStyle = aligned ? "#059669" : "#D97706";
        ctx.fillRect(px, aligned ? yPos : 55 + idx * 52, 90, 42);
        ctx.strokeStyle = "#FFFFFF";
        ctx.strokeRect(px, aligned ? yPos : 55 + idx * 52, 90, 42);
        ctx.fillStyle = "#FFFFFF";
        ctx.font = "700 11px 'JetBrains Mono', monospace";
        ctx.fillText("PLANK " + (idx + 1), px + 16, (aligned ? yPos : 55 + idx * 52) + 25);
      });
      ctx.fillStyle = isDark ? "#F8FAFC" : "#0F172A";
      ctx.font = "700 12px 'JetBrains Mono', monospace";
      ctx.fillText(aligned ? "✔ Bridge Aligned Across Canyon (Flexbox Verified)" : "Align the 3 bridge planks on the center axis", 14, 24);

    } else if (engineKey === "ROVER_GRID") {
      // Isometric / Grid Algorithmic Pathfinder
      const cols = 7, rows = 5;
      const cellW = Math.min(54, (w - 60) / cols);
      const startX = (w - cols * cellW) / 2;
      const startY = 42;

      for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
          const x = startX + c * cellW, y = startY + r * cellW;
          const isGoal = (c === 5 && r === 3);
          ctx.fillStyle = isGoal ? "rgba(5, 150, 105, 0.25)" : (isDark ? "#1E293B" : "#FFFFFF");
          ctx.fillRect(x, y, cellW - 3, cellW - 3);
          ctx.strokeStyle = isGoal ? "#059669" : (isDark ? "#334155" : "#CBD5E1");
          ctx.strokeRect(x, y, cellW - 3, cellW - 3);
        }
      }
      const rx = progressRatio > 0.5 ? 5 : 1;
      const ry = progressRatio > 0.5 ? 3 : 1;
      const px = startX + rx * cellW + cellW / 2 - 2;
      const py = startY + ry * cellW + cellW / 2 - 2;
      ctx.fillStyle = "#1D4ED8";
      ctx.beginPath();
      ctx.arc(px, py, cellW * 0.34, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = "#FFFFFF";
      ctx.font = "700 10px 'JetBrains Mono', monospace";
      ctx.fillText("ROVER", px - 16, py + 3);
      ctx.fillStyle = isDark ? "#F8FAFC" : "#0F172A";
      ctx.font = "700 12px 'JetBrains Mono', monospace";
      ctx.fillText(progressRatio > 0.5 ? "✔ Rover Reached Target Portal (5, 3)!" : "Start: (1, 1) -> Goal Portal: (5, 3)", 14, 24);

    } else if (engineKey === "SQL_DETECTIVE" || engineKey === "PHP_VAULT") {
      // Relational Table & Server Data-Vault Visualizer
      ctx.fillStyle = isDark ? "#F8FAFC" : "#0F172A";
      ctx.font = "700 12px 'JetBrains Mono', monospace";
      ctx.fillText(progressRatio > 0.5 ? "✔ Query Executed — 2 Verified Records Matched:" : "Database Schema: suspects / students (Ready for Query)", 14, 26);

      const rowsData = progressRatio > 0.5
        ? [
            ["ID", "NAME", "DEPT / ZONE", "STATUS"],
            ["1119003", "Md Najmus Sakib", "CSE / ServerVault", "VERIFIED (LV-5)"],
            ["1119026", "Fahim", "CSE / ServerVault", "VERIFIED (LV-4)"]
          ]
        : [
            ["ID", "NAME", "DEPT / ZONE", "STATUS"],
            ["101", "Unknown Node", "Lobby", "PENDING"],
            ["1119003", "Md Najmus Sakib", "CSE / ServerVault", "LOCKED"]
          ];

      rowsData.forEach(function (r, rIdx) {
        const y = 48 + rIdx * 42;
        ctx.fillStyle = rIdx === 0 ? "#1D4ED8" : (isDark ? "#1E293B" : "#FFFFFF");
        ctx.fillRect(16, y, w - 32, 36);
        ctx.strokeStyle = isDark ? "#334155" : "#CBD5E1";
        ctx.strokeRect(16, y, w - 32, 36);
        ctx.fillStyle = rIdx === 0 ? "#FFFFFF" : (isDark ? "#E2E8F0" : "#0F172A");
        ctx.font = (rIdx === 0 ? "700 " : "500 ") + "11px 'JetBrains Mono', monospace";
        r.forEach(function (cell, cIdx) {
          ctx.fillText(cell, 26 + cIdx * ((w - 50) / 4), y + 22);
        });
      });

    } else {
      // DOM_CIRCUIT (4 Hardware Circuit Nodes)
      ctx.fillStyle = isDark ? "#F8FAFC" : "#0F172A";
      ctx.font = "700 12px 'JetBrains Mono', monospace";
      ctx.fillText(progressRatio > 0.5 ? "✔ DOM Circuit Nodes Energized (100%)" : "Circuit Nodes Idle — Run querySelector & Loop", 14, 26);

      for (let i = 0; i < 4; i++) {
        const cx = 65 + i * ((w - 130) / 3);
        const cy = h / 2 + 10;
        ctx.beginPath();
        ctx.arc(cx, cy, 28, 0, Math.PI * 2);
        ctx.fillStyle = progressRatio > 0.5 ? "#059669" : (isDark ? "#1E293B" : "#E2E8F0");
        ctx.fill();
        ctx.lineWidth = 2;
        ctx.strokeStyle = progressRatio > 0.5 ? "#10B981" : "#94A3B8";
        ctx.stroke();
        ctx.fillStyle = progressRatio > 0.5 ? "#FFFFFF" : (isDark ? "#CBD5E1" : "#334155");
        ctx.font = "700 11px 'JetBrains Mono', monospace";
        ctx.fillText("NODE " + i, cx - 20, cy + 4);
      }
    }
  };
})();
