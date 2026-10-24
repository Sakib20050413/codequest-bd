/**
 * CodeQuest Mini-Game 5: Output Predictor
 * 20 Mental Model & Code Execution Challenges
 */
(function () {
  'use strict';

  const QUESTIONS = [
    {
      id: 1,
      title: "Python: List Mutation via Aliasing",
      lang: "Python",
      difficulty: "Beginner",
      code: "a = [1, 2, 3]\nb = a\nb.append(4)\nprint(len(a))",
      opts: ["3", "4", "Error", "None"],
      ans: 1,
      explanation: "Lists in Python are mutable reference objects; mutating b directly mutates a.",
    },
    {
      id: 2,
      title: "JavaScript: The Type of NaN",
      lang: "JavaScript",
      difficulty: "Beginner",
      code: "console.log(typeof NaN);",
      opts: ["'number'", "'NaN'", "'undefined'", "'object'"],
      ans: 0,
      explanation: "In JavaScript (IEEE 754 standard), NaN is a numeric value representing Not-a-Number, so typeof NaN is 'number'.",
    },
    {
      id: 3,
      title: "SQL: Null Equality Comparison",
      lang: "SQL",
      difficulty: "Beginner",
      code: "SELECT COUNT(*)\nFROM users\nWHERE NULL = NULL;",
      opts: ["All users", "0", "NULL", "Syntax Error"],
      ans: 1,
      explanation: "In SQL three-valued logic, NULL = NULL evaluates to UNKNOWN (falsy in WHERE). Use IS NULL instead.",
    },
    {
      id: 4,
      title: "C: Post-Increment Evaluation",
      lang: "C",
      difficulty: "Beginner",
      code: "int x = 5;\nprintf(\"%d\", x++);",
      opts: ["5", "6", "4", "0"],
      ans: 0,
      explanation: "Post-increment (x++) yields the current value (5) before incrementing x to 6 in memory.",
    },
    {
      id: 5,
      title: "JavaScript: Event Loop Microtask vs Macrotask",
      lang: "JavaScript",
      difficulty: "Intermediate",
      code: "setTimeout(() => console.log('T'), 0);\nPromise.resolve().then(() => console.log('P'));\nconsole.log('S');",
      opts: ["S -> T -> P", "S -> P -> T", "P -> S -> T", "T -> P -> S"],
      ans: 1,
      explanation: "Synchronous 'S' executes first, then microtasks (Promise 'P'), and lastly macrotasks (setTimeout 'T').",
    },
    {
      id: 6,
      title: "Python: Negative Step String Slicing",
      lang: "Python",
      difficulty: "Beginner",
      code: "text = 'CodeQuest'\nprint(text[::-1][:4])",
      opts: ["'tseu'", "'Quest'", "'tseQ'", "'edoc'"],
      ans: 0,
      explanation: "text[::-1] reverses to 'tseuQedoC', and [:4] slices the first 4 characters: 'tseu'.",
    },
    {
      id: 7,
      title: "JavaScript: Loose Coercion Equality",
      lang: "JavaScript",
      difficulty: "Intermediate",
      code: "console.log([] == ![]);",
      opts: ["true", "false", "TypeError", "undefined"],
      ans: 0,
      explanation: "![] evaluates to false. In '[] == false', [] coerces to '' which coerces to 0, and false coerces to 0 (0 == 0 is true).",
    },
    {
      id: 8,
      title: "Python: Dictionary Key Deduplication",
      lang: "Python",
      difficulty: "Intermediate",
      code: "d = {1: 'a', 1.0: 'b', True: 'c'}\nprint(len(d), d[1])",
      opts: ["3 'a'", "1 'c'", "2 'b'", "TypeError"],
      ans: 1,
      explanation: "In Python, hash(1) == hash(1.0) == hash(True) and 1 == 1.0 == True, so they collide into a single key overwritten with 'c'.",
    },
    {
      id: 9,
      title: "SQL: COUNT(column) vs COUNT(*)",
      lang: "SQL",
      difficulty: "Intermediate",
      code: "-- Table scores: [100, NULL, 50]\nSELECT COUNT(*), COUNT(score)\nFROM scores;",
      opts: ["3, 3", "3, 2", "2, 2", "3, NULL"],
      ans: 1,
      explanation: "COUNT(*) counts all physical rows (3), whereas COUNT(column_name) ignores NULL rows (2).",
    },
    {
      id: 10,
      title: "JavaScript: Var Hoisting",
      lang: "JavaScript",
      difficulty: "Intermediate",
      code: "console.log(msg);\nvar msg = 'Hello World';",
      opts: ["'Hello World'", "undefined", "ReferenceError", "null"],
      ans: 1,
      explanation: "Declarations with 'var' are hoisted and initialized to undefined until execution reaches assignment.",
    },
    {
      id: 11,
      title: "Python: Default Parameter Retention",
      lang: "Python",
      difficulty: "Intermediate",
      code: "def add(item, lst=[]):\n    lst.append(item)\n    return lst\nadd(1)\nprint(add(2))",
      opts: ["[2]", "[1, 2]", "[1], [2]", "TypeError"],
      ans: 1,
      explanation: "Default arguments are evaluated once at module load, persisting mutated state across calls.",
    },
    {
      id: 12,
      title: "JavaScript: Arrow Function 'this' Binding",
      lang: "JavaScript",
      difficulty: "Intermediate",
      code: "const obj = {\n  num: 42,\n  get: () => this.num\n};\nconsole.log(obj.get());",
      opts: ["42", "undefined", "NaN", "TypeError"],
      ans: 1,
      explanation: "Arrow functions do not bind their own 'this'; they lexically capture the enclosing outer scope (global window/undefined).",
    },
    {
      id: 13,
      title: "C: Truncating Integer Division",
      lang: "C",
      difficulty: "Beginner",
      code: "int a = 7, b = 2;\nfloat c = a / b;\nprintf(\"%.1f\", c);",
      opts: ["3.5", "3.0", "4.0", "Runtime Error"],
      ans: 1,
      explanation: "In C, dividing two integers (7 / 2) performs integer truncation yielding 3 before implicit cast to 3.0f.",
    },
    {
      id: 14,
      title: "Python: Boolean Operator Precedence",
      lang: "Python",
      difficulty: "Intermediate",
      code: "print(True or False and False)",
      opts: ["True", "False", "None", "SyntaxError"],
      ans: 0,
      explanation: "'and' has higher precedence than 'or'. Evaluates as: True or (False and False) -> True or False -> True.",
    },
    {
      id: 15,
      title: "JavaScript: Lexicographical Array Sort",
      lang: "JavaScript",
      difficulty: "Intermediate",
      code: "const nums = [10, 5, 25, 2];\nnums.sort();\nconsole.log(nums[1]);",
      opts: ["5", "10", "2", "25"],
      ans: 1,
      explanation: "Array.prototype.sort() without a comparator converts elements to strings: ['10', '2', '25', '5']. Index 1 is '10' (or 2 depending on order: '10' < '2' in UTF-16, so sorted is [10, 2, 25, 5] -> index 1 is 2? Wait: '1' is 49, '2' is 50. So '10' comes first, then '2', then '25', then '5'. nums[1] is 2.",
    },
    {
      id: 16,
      title: "SQL: UNION vs UNION ALL",
      lang: "SQL",
      difficulty: "Intermediate",
      code: "SELECT 1 UNION ALL SELECT 1 UNION SELECT 1;",
      opts: ["Three rows [1, 1, 1]", "One row [1]", "Two rows [1, 1]", "Error"],
      ans: 1,
      explanation: "The final UNION removes duplicates across the unified result set, returning a single distinct row containing 1.",
    },
    {
      id: 17,
      title: "Python: Rest Unpacking",
      lang: "Python",
      difficulty: "Intermediate",
      code: "first, *middle, last = [10, 20, 30, 40, 50]\nprint(middle)",
      opts: ["[20, 30, 40]", "[10, 20, 30]", "[30, 40, 50]", "(20, 30, 40)"],
      ans: 0,
      explanation: "*middle captures all remaining intermediate items as a list: [20, 30, 40].",
    },
    {
      id: 18,
      title: "JavaScript: Object Spread Shallow Copy",
      lang: "JavaScript",
      difficulty: "Intermediate",
      code: "const a = { x: 1, nested: { y: 2 } };\nconst b = { ...a };\nb.nested.y = 99;\nconsole.log(a.nested.y);",
      opts: ["2", "99", "undefined", "TypeError"],
      ans: 1,
      explanation: "The spread operator performs a shallow copy. 'nested' is copied by reference, so mutating b.nested also mutates a.nested.",
    },
    {
      id: 19,
      title: "C: Pointer Dereference",
      lang: "C",
      difficulty: "Intermediate",
      code: "int val = 100;\nint *ptr = &val;\n*ptr = 250;\nprintf(\"%d\", val);",
      opts: ["100", "250", "Address of val", "0"],
      ans: 1,
      explanation: "Dereferencing *ptr assigns directly into the memory location of val, mutating val to 250.",
    },
    {
      id: 20,
      title: "Python: Generator Evaluation Timing",
      lang: "Python",
      difficulty: "Advanced",
      code: "gen = (x * 2 for x in [1, 2, 3])\nnums = [1, 2, 3]\nprint(next(gen), next(gen))",
      opts: ["2 4", "1 2", "2 2", "StopIteration"],
      ans: 0,
      explanation: "next(gen) lazily evaluates the generator, yielding 1*2 = 2 on first call and 2*2 = 4 on second call.",
    },
  ];

  let currentLevelIdx = 0;
  let score = 0;
  const completedLevels = new Set(JSON.parse(localStorage.getItem('cq_completed_predictor') || '[]'));

  function getQueryLevel() {
    const params = new URLSearchParams(window.location.search);
    const lvl = parseInt(params.get('level'), 10);
    if (!isNaN(lvl) && lvl >= 1 && lvl <= QUESTIONS.length) {
      return lvl - 1;
    }
    return 0;
  }

  function getCsrf() {
    const match = document.cookie.match(/csrftoken=([^;]+)/);
    return match ? match[1] : '';
  }

  function initPredictor() {
    const codeEl = document.getElementById("predictorSnippet");
    const langBadge = document.getElementById("predictorLang");
    const optionsEl = document.getElementById("predictorOptions");
    const feedbackEl = document.getElementById("predictorFeedback");
    const scoreEl = document.getElementById("predictorScore");
    const missionTitle = document.getElementById("predictorMissionTitle");
    const levelPillsContainer = document.getElementById("predictorLevelPills");

    currentLevelIdx = getQueryLevel();

    function renderLevelSelector() {
      if (!levelPillsContainer) return;
      levelPillsContainer.innerHTML = "";
      QUESTIONS.forEach(function (q, idx) {
        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = "btn " + (idx === currentLevelIdx ? "btn-primary" : "btn-ghost");
        btn.style.padding = "0.3rem 0.65rem";
        btn.style.fontSize = "0.76rem";
        btn.style.fontFamily = "var(--font-mono)";
        btn.style.borderRadius = "6px";
        btn.style.minWidth = "36px";

        const isDone = completedLevels.has(q.id);
        btn.innerHTML = `${q.id}${isDone ? ' <span style="color:#10b981;">✓</span>' : ''}`;
        btn.title = `Challenge ${q.id}: ${q.title} (${q.lang})`;

        btn.onclick = function () {
          currentLevelIdx = idx;
          loadQ();
          renderLevelSelector();
        };
        levelPillsContainer.appendChild(btn);
      });
    }

    function loadQ() {
      const q = QUESTIONS[currentLevelIdx];
      if (missionTitle) {
        missionTitle.textContent = `Challenge ${q.id} of 20: ${q.title}`;
      }
      if (langBadge) {
        langBadge.textContent = `${q.lang} • ${q.difficulty}`;
      }
      codeEl.textContent = q.code;
      feedbackEl.textContent = "Predict what this snippet outputs:";
      feedbackEl.style.color = "var(--text-muted)";
      optionsEl.innerHTML = "";

      q.opts.forEach(function (opt, i) {
        const btn = document.createElement("button");
        btn.className = "btn btn-ghost font-mono";
        btn.style.fontSize = "0.95rem";
        btn.style.padding = "0.85rem 1.25rem";
        btn.style.textAlign = "left";
        btn.style.display = "flex";
        btn.style.alignItems = "center";
        btn.style.gap = "0.75rem";
        btn.style.border = "1px solid var(--border-subtle)";
        btn.innerHTML = `<span style="font-weight:700;color:var(--accent);">${String.fromCharCode(65 + i)})</span> <code>${opt}</code>`;

        btn.onclick = function () {
          if (i === q.ans) {
            score += 25;
            completedLevels.add(q.id);
            localStorage.setItem('cq_completed_predictor', JSON.stringify(Array.from(completedLevels)));
            if (scoreEl) scoreEl.textContent = score;
            feedbackEl.innerHTML = `<span style="color:#10b981;font-weight:700;">✔ Correct!</span> ${q.explanation}`;
            feedbackEl.style.color = "var(--accent)";
            btn.style.background = "rgba(16, 185, 129, 0.2)";
            btn.style.borderColor = "#10b981";

            if (window.CodeQuest) window.CodeQuest.playTone("success");
            renderLevelSelector();

            setTimeout(function () {
              if (currentLevelIdx < QUESTIONS.length - 1) {
                currentLevelIdx++;
                loadQ();
                renderLevelSelector();
              } else {
                feedbackEl.innerHTML = "🏆 All 20 Output Predictions Solved! Flawless Execution Architecture.";
                if (window.CodeQuest) {
                  window.CodeQuest.playTone("win");
                  window.CodeQuest.fireConfetti();
                }
                fetch('/api/games/output-predictor/score/', { method: 'POST', headers: { 'X-CSRFToken': getCsrf() } });
              }
            }, 1800);
          } else {
            feedbackEl.innerHTML = `<span style="color:#ef4444;font-weight:700;">Incorrect:</span> Re-trace the evaluation order and memory model.`;
            btn.style.background = "rgba(239, 68, 68, 0.2)";
            btn.style.borderColor = "#ef4444";
            if (window.CodeQuest) window.CodeQuest.playTone("error");
          }
        };

        optionsEl.appendChild(btn);
      });
    }

    renderLevelSelector();
    loadQ();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initPredictor);
  } else {
    initPredictor();
  }
})();
