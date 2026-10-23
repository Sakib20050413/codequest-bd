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
    const hintBtn = document.getElementById('revealHintBtn');
    const hintBox = document.getElementById('hintDisplayBox');
    const statusMsg = document.getElementById('runnerStatusMessage');

    const tests = config.tests || [];
    const hints = config.hints || [];
    const lessonId = config.lessonId;
    let hintIndex = 0;

    // Render initial test list
    function renderTestList(passedMap) {
      if (!testListEl) return;
      testListEl.innerHTML = '';
      tests.forEach(function (t, i) {
        const passed = passedMap && passedMap[t.id];
        const li = document.createElement('div');
        li.style.display = 'flex';
        li.style.alignItems = 'center';
        li.style.gap = '0.5rem';
        li.style.padding = '0.4rem 0';
        li.style.fontSize = '0.82rem';
        li.style.fontFamily = 'var(--font-mono)';
        li.style.color = passed ? 'var(--accent)' : 'var(--text-muted)';

        const icon = passed ? '✔' : '○';
        li.innerHTML = `<span style="font-weight:700;color:${passed ? 'var(--accent)' : 'var(--text-muted)'}">${icon}</span> <span>${t.desc}</span>`;
        testListEl.appendChild(li);
      });
    }
    renderTestList({});

    // Render iframe live preview
    function updatePreview() {
      if (!previewFrame) return;
      const code = editor.value;
      previewFrame.srcdoc = `<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body { font-family: -apple-system, sans-serif; padding: 1rem; color: #1e293b; line-height: 1.5; }
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
          statusMsg.style.color = 'var(--text-secondary)';
        }
      };
    }

    // Auto-checking tests against iframe DOM
    function runTests() {
      updatePreview();
      const code = editor.value;
      const passedMap = {};
      let allPass = true;

      // Allow iframe DOM to parse
      setTimeout(function () {
        const doc = previewFrame.contentDocument || previewFrame.contentWindow.document;

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
              pass = !!(el && el.textContent.trim().includes(t.val));
            } else if (t.type === 'dom_count_min') {
              pass = doc.querySelectorAll(t.query).length >= t.min;
            } else if (t.type === 'css_rule') {
              pass = code.includes(t.sel) && code.includes(t.prop);
            } else if (t.type === 'css_contains') {
              pass = code.includes(t.val);
            } else if (t.type === 'js_var' || t.type === 'stdout_match') {
              pass = code.includes(t.val);
            } else {
              pass = code.length > 10;
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
            statusMsg.textContent = `🎉 All checks passed! +${config.xpReward || 50} XP earned.`;
            statusMsg.style.color = 'var(--accent)';
          }

          // Report pass to server
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
                alert(`🏆 New Badge Unlocked: ${res.new_badge}!`);
              }
            })
            .catch(() => {});
        } else {
          if (global.CodeQuest) global.CodeQuest.playTone('error');
          if (statusMsg) {
            statusMsg.textContent = 'Some checks failed. Review the list or check a hint.';
            statusMsg.style.color = 'var(--danger)';
          }
        }
      }, 150);
    }

    if (checkBtn) {
      checkBtn.onclick = runTests;
    }

    // Hint Ladder
    if (hintBtn && hintBox) {
      hintBtn.onclick = function () {
        if (hints.length === 0) {
          hintBox.textContent = '💡 Review the explanation on the left carefully.';
          hintBox.style.display = 'block';
          return;
        }
        if (hintIndex < hints.length) {
          hintBox.textContent = hints[hintIndex];
          hintBox.style.display = 'block';
          hintIndex++;
          hintBtn.textContent = hintIndex < hints.length ? `💡 Hint ${hintIndex + 1}` : '✨ Show Solution';
        } else {
          editor.value = config.solution || '';
          updatePreview();
          hintBox.textContent = 'Solution applied to editor. Click Check to verify!';
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
