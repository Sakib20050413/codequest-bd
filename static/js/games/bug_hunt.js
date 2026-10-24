/**
 * CodeQuest Mini-Game 3: Bug Hunt
 * 20 Real-World Debugging Missions across 8 Languages
 */
(function () {
  'use strict';

  const BUGS = [
    {
      id: 1,
      title: "Python: Missing Loop Colon",
      lang: "Python",
      difficulty: "Beginner",
      lines: [
        "def calculate_total(prices):",
        "    total = 0",
        "    for p in prices",
        "        total += p",
        "    return total",
      ],
      bugLine: 2,
      reason: "Missing colon ':' at the end of the for statement.",
    },
    {
      id: 2,
      title: "JavaScript: Assignment in Condition",
      lang: "JavaScript",
      difficulty: "Beginner",
      lines: [
        "const user = 'Sakib';",
        "let xp = 200;",
        "if (user = 'Sakib') {",
        "    console.log(xp);",
        "}",
      ],
      bugLine: 2,
      reason: "Assignment '=' used inside condition instead of comparison '==='.",
    },
    {
      id: 3,
      title: "HTML: Unclosed Element",
      lang: "HTML",
      difficulty: "Beginner",
      lines: [
        "<header>",
        "  <h1>Welcome</h1>",
        "  <img src='logo.png'>",
        "  <p>Overview",
        "</header>",
      ],
      bugLine: 3,
      reason: "Unclosed <p> tag before closing </header>.",
    },
    {
      id: 4,
      title: "CSS: Missing Unit on Length",
      lang: "CSS",
      difficulty: "Beginner",
      lines: [
        ".card {",
        "  display: flex;",
        "  margin: 20;",
        "  border-radius: 8px;",
        "}",
      ],
      bugLine: 2,
      reason: "In CSS, non-zero lengths require units like 'px', 'rem', or '%'.",
    },
    {
      id: 5,
      title: "SQL: Null Comparison with Equals",
      lang: "SQL",
      difficulty: "Beginner",
      lines: [
        "SELECT id, username, status",
        "FROM auth_users",
        "WHERE status = NULL",
        "ORDER BY id DESC;",
      ],
      bugLine: 2,
      reason: "In SQL, comparing '= NULL' always yields false/unknown. Use 'IS NULL' instead.",
    },
    {
      id: 6,
      title: "Python: Modifying List During Iteration",
      lang: "Python",
      difficulty: "Intermediate",
      lines: [
        "scores = [10, 25, 40, 55, 70]",
        "for s in scores:",
        "    if s < 30:",
        "        scores.remove(s)",
        "print(len(scores))",
      ],
      bugLine: 3,
      reason: "Mutating a list while iterating over it causes skipped elements.",
    },
    {
      id: 7,
      title: "JavaScript: Unchecked Property Access",
      lang: "JavaScript",
      difficulty: "Intermediate",
      lines: [
        "function getStreet(user) {",
        "  const hasAddress = user && user.address;",
        "  return user.location.street.toUpperCase();",
        "}",
      ],
      bugLine: 2,
      reason: "Accessing 'user.location.street' without checking if 'location' is defined throws TypeError.",
    },
    {
      id: 8,
      title: "C: Missing Semicolon",
      lang: "C",
      difficulty: "Beginner",
      lines: [
        "#include <stdio.h>",
        "int main() {",
        "    int counter = 42",
        "    printf(\"%d\\n\", counter);",
        "    return 0;",
        "}",
      ],
      bugLine: 2,
      reason: "Missing terminating semicolon ';' after variable declaration.",
    },
    {
      id: 9,
      title: "Python: Mutable Default Argument",
      lang: "Python",
      difficulty: "Intermediate",
      lines: [
        "def enroll_student(student_id, roster=[]):",
        "    roster.append(student_id)",
        "    return roster",
      ],
      bugLine: 0,
      reason: "Default list 'roster=[]' is evaluated once at definition time and shared across calls.",
    },
    {
      id: 10,
      title: "JavaScript: Const Reassignment",
      lang: "JavaScript",
      difficulty: "Beginner",
      lines: [
        "const maxRetries = 3;",
        "let attempts = 0;",
        "maxRetries = maxRetries + 1;",
        "console.log(attempts);",
      ],
      bugLine: 2,
      reason: "Attempting to reassign a 'const' variable throws TypeError: Assignment to constant variable.",
    },
    {
      id: 11,
      title: "Java: String Identity vs Equality",
      lang: "Java",
      difficulty: "Intermediate",
      lines: [
        "public boolean checkRole(String role) {",
        "    String admin = new String(\"ADMIN\");",
        "    if (role == admin) {",
        "        return true;",
        "    }",
        "    return false;",
        "}",
      ],
      bugLine: 2,
      reason: "In Java, '==' compares object references. Use role.equals(admin) for content comparison.",
    },
    {
      id: 12,
      title: "SQL: Missing Column in Group By",
      lang: "SQL",
      difficulty: "Intermediate",
      lines: [
        "SELECT department, role, COUNT(*)",
        "FROM employees",
        "GROUP BY department",
        "HAVING COUNT(*) > 5;",
      ],
      bugLine: 2,
      reason: "All non-aggregated columns in SELECT ('role') must be included in the GROUP BY clause.",
    },
    {
      id: 13,
      title: "Python: Unbound Local Variable",
      lang: "Python",
      difficulty: "Intermediate",
      lines: [
        "total = 100",
        "def adjust():",
        "    print(total)",
        "    total = total + 10",
        "adjust()",
      ],
      bugLine: 2,
      reason: "Local 'total' is assigned on line 4, making it local; line 3 accesses it before assignment.",
    },
    {
      id: 14,
      title: "JavaScript: Off-by-One Loop Condition",
      lang: "JavaScript",
      difficulty: "Beginner",
      lines: [
        "const items = ['a', 'b', 'c'];",
        "for (let i = 0; i <= items.length; i++) {",
        "  console.log(items[i].toUpperCase());",
        "}",
      ],
      bugLine: 1,
      reason: "Loop condition '<= items.length' attempts to access items[3], which is undefined.",
    },
    {
      id: 15,
      title: "CSS: Malformed Hex Color",
      lang: "CSS",
      difficulty: "Beginner",
      lines: [
        ".button-glow {",
        "  background: #3b82f6;",
        "  border: 1px solid #60a5fa7;",
        "  color: #ffffff;",
        "}",
      ],
      bugLine: 2,
      reason: "Hex colors must be 3, 4, 6, or 8 hexadecimal digits; 7 digits is invalid.",
    },
    {
      id: 16,
      title: "Python: Unhandled ZeroDivisionError",
      lang: "Python",
      difficulty: "Beginner",
      lines: [
        "def calculate_average(grades):",
        "    avg = sum(grades) / len(grades)",
        "    return round(avg, 2)",
      ],
      bugLine: 1,
      reason: "If grades is an empty list, len(grades) is 0, causing a ZeroDivisionError.",
    },
    {
      id: 17,
      title: "JavaScript: Missing Await in Async Workflow",
      lang: "JavaScript",
      difficulty: "Intermediate",
      lines: [
        "async function fetchUserData(userId) {",
        "  const res = fetch('/api/user/' + userId);",
        "  const data = await res.json();",
        "  return data;",
        "}",
      ],
      bugLine: 1,
      reason: "fetch() returns a Promise; missing 'await' means 'res' is a Promise without a '.json()' method.",
    },
    {
      id: 18,
      title: "SQL: Missing Join ON Condition",
      lang: "SQL",
      difficulty: "Intermediate",
      lines: [
        "SELECT o.id, c.name, o.total",
        "FROM orders o",
        "INNER JOIN customers c",
        "WHERE o.created_at >= '2026-01-01';",
      ],
      bugLine: 2,
      reason: "INNER JOIN requires an 'ON' predicate specifying the join condition (e.g., ON o.cust_id = c.id).",
    },
    {
      id: 19,
      title: "C: Array Out-of-Bounds Write",
      lang: "C",
      difficulty: "Advanced",
      lines: [
        "int buffer[4] = {1, 2, 3, 4};",
        "for (int i = 0; i < 4; i++) {",
        "    buffer[i + 1] = buffer[i] * 2;",
        "}",
      ],
      bugLine: 2,
      reason: "When i = 3, buffer[4] writes beyond the 4-element allocated buffer.",
    },
    {
      id: 20,
      title: "PHP: Strict Type Mismatch & Unset Key",
      lang: "PHP",
      difficulty: "Intermediate",
      lines: [
        "function formatPrice(float $amount): string {",
        "    return '$' . number_format($amount, 2);",
        "}",
        "$raw = $_POST['total_cost'];",
        "echo formatPrice($raw);",
      ],
      bugLine: 3,
      reason: "Accessing $_POST['total_cost'] directly without isset() triggers an Undefined array key warning.",
    },
  ];

  let currentLevelIdx = 0;
  let score = 0;
  const completedMissions = new Set(JSON.parse(localStorage.getItem('cq_completed_bughunt') || '[]'));

  function getQueryLevel() {
    const params = new URLSearchParams(window.location.search);
    const lvl = parseInt(params.get('level'), 10);
    if (!isNaN(lvl) && lvl >= 1 && lvl <= BUGS.length) {
      return lvl - 1;
    }
    return 0;
  }

  function getCsrf() {
    const match = document.cookie.match(/csrftoken=([^;]+)/);
    return match ? match[1] : '';
  }

  function initBugHunt() {
    const codeArea = document.getElementById("bugCodeSnippet");
    const langBadge = document.getElementById("bugLangBadge");
    const feedback = document.getElementById("bugFeedback");
    const scoreDisplay = document.getElementById("bugScore");
    const levelTitle = document.getElementById("bugMissionTitle");
    const levelPillsContainer = document.getElementById("bugLevelPills");

    currentLevelIdx = getQueryLevel();

    function renderLevelSelector() {
      if (!levelPillsContainer) return;
      levelPillsContainer.innerHTML = "";
      BUGS.forEach(function (b, idx) {
        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = "btn " + (idx === currentLevelIdx ? "btn-primary" : "btn-ghost");
        btn.style.padding = "0.3rem 0.65rem";
        btn.style.fontSize = "0.76rem";
        btn.style.fontFamily = "var(--font-mono)";
        btn.style.borderRadius = "6px";
        btn.style.minWidth = "36px";

        const isDone = completedMissions.has(b.id);
        btn.innerHTML = `${b.id}${isDone ? ' <span style="color:#10b981;">✓</span>' : ''}`;
        btn.title = `Level ${b.id}: ${b.title} (${b.lang})`;

        btn.onclick = function () {
          currentLevelIdx = idx;
          loadBug();
          renderLevelSelector();
        };
        levelPillsContainer.appendChild(btn);
      });
    }

    function loadBug() {
      const item = BUGS[currentLevelIdx];
      if (levelTitle) {
        levelTitle.textContent = `Mission ${item.id} of 20: ${item.title}`;
      }
      if (langBadge) {
        langBadge.textContent = `${item.lang} • ${item.difficulty}`;
      }
      feedback.textContent = "Click the specific line containing the bug:";
      feedback.style.color = "var(--text-muted)";
      codeArea.innerHTML = "";

      item.lines.forEach(function (line, idx) {
        const row = document.createElement("div");
        row.style.display = "flex";
        row.style.gap = "1rem";
        row.style.padding = "0.45rem 0.85rem";
        row.style.borderRadius = "6px";
        row.style.cursor = "pointer";
        row.style.fontFamily = "var(--font-mono)";
        row.style.fontSize = "0.88rem";
        row.style.transition = "background 0.15s ease";
        row.className = "bug-line-row";

        const num = document.createElement("span");
        num.style.opacity = "0.4";
        num.style.userSelect = "none";
        num.style.minWidth = "20px";
        num.textContent = (idx + 1).toString();

        const txt = document.createElement("span");
        txt.textContent = line;

        row.appendChild(num);
        row.appendChild(txt);

        row.onmouseover = function () {
          if (!row.dataset.inspected) {
            row.style.background = "rgba(255, 255, 255, 0.04)";
          }
        };
        row.onmouseout = function () {
          if (!row.dataset.inspected) {
            row.style.background = "transparent";
          }
        };

        row.onclick = function () {
          row.dataset.inspected = "true";
          if (idx === item.bugLine) {
            score += 25;
            completedMissions.add(item.id);
            localStorage.setItem('cq_completed_bughunt', JSON.stringify(Array.from(completedMissions)));
            if (scoreDisplay) scoreDisplay.textContent = score;
            row.style.background = "rgba(16, 185, 129, 0.25)";
            row.style.border = "1px solid #10b981";
            feedback.innerHTML = `<span style="color:#10b981;font-weight:700;">✔ Correct! Line ${idx + 1}:</span> ${item.reason}`;

            if (window.CodeQuest) {
              window.CodeQuest.playTone("success");
            }
            renderLevelSelector();

            // Next mission auto-advance after 1.8s
            setTimeout(function () {
              if (currentLevelIdx < BUGS.length - 1) {
                currentLevelIdx++;
                loadBug();
                renderLevelSelector();
              } else {
                feedback.innerHTML = "🎉 All 20 Bug Hunt Missions Solved! Elite Code Reviewer Status Achieved.";
                if (window.CodeQuest) {
                  window.CodeQuest.playTone("win");
                  window.CodeQuest.fireConfetti();
                }
                fetch('/api/games/bug-hunt/score/', { method: 'POST', headers: { 'X-CSRFToken': getCsrf() } });
              }
            }, 1800);
          } else {
            row.style.background = "rgba(239, 68, 68, 0.2)";
            row.style.border = "1px solid #ef4444";
            feedback.innerHTML = `<span style="color:#ef4444;font-weight:700;">Line ${idx + 1} is clean:</span> Keep looking for the syntax or logic flaw.`;
            if (window.CodeQuest) {
              window.CodeQuest.playTone("error");
            }
          }
        };

        codeArea.appendChild(row);
      });
    }

    renderLevelSelector();
    loadBug();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initBugHunt);
  } else {
    initBugHunt();
  }
})();
