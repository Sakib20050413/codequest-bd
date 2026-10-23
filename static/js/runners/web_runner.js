/**
 * CodeQuest Web Runner & Test Evaluation Engine
 * Sandboxed iframe preview + Client-side DOM & Assertion checks + Stepped Hint Ladder
 */
(function (global) {
  'use strict';

  function initLessonRunner(config) {
    const editor = document.getElementById('codeEditor');
    const previewFrame = document.getElementById('previewIframe');
    const testListEl = document.getElementById('testChecklist');
    const runBtn = document.getElementById('runCodeBtn');
    const checkBtn = document.getElementById('checkSolutionBtn');
    const resetBtn = document.getElementById('resetCodeBtn');
    const hintBtn = document.getElementById('revealHintBtn');
    const hintBox = document.getElementById('hintDisplayBox');
    const statusMsg = document.getElementById('runnerStatusMessage');
    const completionBanner = document.getElementById('lessonCompletionBanner');

    const tests = config.tests || [];
    const hints = config.hints || [];
    const lessonId = config.lessonId;
    const initialStarterCode = editor ? editor.value : '';
    let hintIndex = 0;

    // Render test list
    function renderTestList(passedMap) {
      if (!testListEl) return;
      testListEl.innerHTML = '';
      tests.forEach(function (t) {
        const hasEvaluated = passedMap !== null && passedMap[t.id] !== undefined;
        const passed = hasEvaluated && passedMap[t.id];

        const row = document.createElement('div');
        row.style.display = 'flex';
        row.style.alignItems = 'flex-start';
        row.style.gap = '0.65rem';
        row.style.padding = '0.45rem 0.65rem';
        row.style.borderRadius = 'var(--radius-sm)';
        row.style.fontSize = '0.84rem';
        row.style.fontFamily = 'var(--font-mono)';
        row.style.background = passed ? 'var(--success-subtle)' : hasEvaluated ? 'var(--danger-subtle)' : 'var(--bg-panel)';
        row.style.border = '1px solid ' + (passed ? 'rgba(16, 185, 129, 0.3)' : hasEvaluated ? 'rgba(244, 63, 94, 0.3)' : 'var(--border-subtle)');

        const icon = passed ? '✓' : hasEvaluated ? '✕' : '○';
        const color = passed ? 'var(--success)' : hasEvaluated ? 'var(--danger)' : 'var(--text-muted)';

        row.innerHTML = `<span style="font-weight:700; color:${color}; font-size:0.95rem;">${icon}</span>
                         <span style="color:${passed ? 'var(--text-primary)' : 'var(--text-secondary)'}; line-height:1.4;">${t.desc}</span>`;
        testListEl.appendChild(row);
      });
    }

    renderTestList(null);

    // Render iframe live preview
    function updatePreview() {
      if (!previewFrame || !editor) return;
      const code = editor.value;
      previewFrame.srcdoc = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      padding: 1.25rem;
      color: #0f172a;
      background: #ffffff;
      line-height: 1.5;
    }
  </style>
</head>
<body>
  ${code}
</body>
</html>`;
    }

    if (runBtn) {
      runBtn.onclick = function () {
        updatePreview();
        if (global.CodeQuest) global.CodeQuest.playTone('click');
        if (statusMsg) {
          statusMsg.textContent = 'Preview updated.';
          statusMsg.style.color = 'var(--text-muted)';
        }
      };
    }

    // Reset starter code
    if (resetBtn) {
      resetBtn.onclick = function () {
        if (confirm('Reset editor to original starter code?')) {
          editor.value = initialStarterCode;
          updatePreview();
          renderTestList(null);
          if (statusMsg) statusMsg.textContent = '';
        }
      };
    }

    // Tab key indentation support inside textarea
    if (editor) {
      editor.addEventListener('keydown', function (e) {
        if (e.key === 'Tab') {
          e.preventDefault();
          const start = this.selectionStart;
          const end = this.selectionEnd;
          this.value = this.value.substring(0, start) + '  ' + this.value.substring(end);
          this.selectionStart = this.selectionEnd = start + 2;
        } else if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
          e.preventDefault();
          runTests();
        }
      });
    }

    // Auto-checking tests against iframe DOM
    function runTests() {
      updatePreview();
      const code = editor ? editor.value : '';
      const passedMap = {};
      let allPass = true;

      // Allow iframe DOM to parse
      setTimeout(function () {
        const doc = previewFrame.contentDocument || (previewFrame.contentWindow && previewFrame.contentWindow.document);
        if (!doc) return;

        tests.forEach(function (t) {
          let pass = false;
          try {
            if (t.type === 'dom_exists') {
              pass = !!doc.querySelector(t.query);
            } else if (t.type === 'dom_has_attr') {
              const el = doc.querySelector(t.query);
              pass = !!(el && el.hasAttribute(t.attr));
            } else if (t.type === 'dom_has_attr_val') {
              const el = doc.querySelector(t.query);
              pass = !!(el && el.getAttribute(t.attr) === t.val);
            } else if (t.type === 'dom_text') {
              const el = doc.querySelector(t.query);
              pass = !!(el && el.textContent.trim().toLowerCase().includes((t.val || '').toLowerCase()));
            } else if (t.type === 'dom_count_min') {
              pass = doc.querySelectorAll(t.query).length >= t.min;
            } else if (t.type === 'css_rule') {
              pass = code.includes(t.sel) && code.includes(t.prop);
            } else if (t.type === 'css_contains') {
              pass = code.includes(t.val);
            } else if (t.type === 'exact_match') {
              pass = code.trim().includes(t.val);
            } else {
              pass = code.length > 5;
            }
          } catch (e) {
            pass = false;
          }

          passedMap[t.id] = pass;
          if (!pass) allPass = false;
        });

        renderTestList(passedMap);

        if (allPass && tests.length > 0) {
          if (global.CodeQuest) {
            global.CodeQuest.playTone('success');
            global.CodeQuest.fireConfetti();
            global.CodeQuest.recordGuestCompleted(lessonId, config.xpReward || 50);
          }
          if (statusMsg) {
            statusMsg.textContent = `All checks passed! +${config.xpReward || 50} XP awarded.`;
            statusMsg.style.color = 'var(--success)';
          }

          if (completionBanner) {
            completionBanner.style.display = 'flex';
          }

          // Report pass to backend
          fetch(`/api/lesson/${lessonId}/check/`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': getCsrfToken(),
            },
            body: JSON.stringify({ passed: true }),
          })
            .then((r) => r.json())
            .then((res) => {
              if (res.new_badge) {
                alert(`New Badge Unlocked: ${res.new_badge}!`);
              }
            })
            .catch(() => {});
        } else {
          if (global.CodeQuest) global.CodeQuest.playTone('error');
          if (statusMsg) {
            statusMsg.textContent = 'Some checks failed. Inspect the requirements and try again.';
            statusMsg.style.color = 'var(--danger)';
          }
        }
      }, 180);
    }

    if (checkBtn) {
      checkBtn.onclick = runTests;
    }

    // Hint Ladder
    if (hintBtn && hintBox) {
      hintBtn.onclick = function () {
        if (hints.length === 0) {
          hintBox.textContent = 'Carefully review the conceptual explanation and example on the left.';
          hintBox.style.display = 'block';
          return;
        }
        if (hintIndex < hints.length) {
          hintBox.textContent = hints[hintIndex];
          hintBox.style.display = 'block';
          hintIndex++;
          hintBtn.textContent = hintIndex < hints.length ? `💡 Hint ${hintIndex + 1}` : '✨ Show Solution';
        } else {
          if (editor) {
            editor.value = config.solution || '';
            updatePreview();
          }
          hintBox.textContent = 'Working reference solution applied to editor. Click "Check Solution" to verify!';
        }
      };
    }

    function getCsrfToken() {
      const match = document.cookie.match(/csrftoken=([^;]+)/);
      return match ? match[1] : '';
    }

    // Initial preview render
    updatePreview();
  }

  global.CodeQuestLessonRunner = {
    init: initLessonRunner,
  };
})(typeof window !== 'undefined' ? window : this);
