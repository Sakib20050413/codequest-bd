/**
 * CodeQuest Web Runner & Modern Test Evaluation Engine
 * Sandboxed iframe preview + Live DOM Visualizer Tree + Assertion checks + Stepped Hint Ladder
 */
(function (global) {
  'use strict';

  function escapeHtml(str) {
    return (str || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  function formatTestDescription(rawDesc) {
    if (!rawDesc) return '';
    let safe = escapeHtml(rawDesc);
    // Transform &lt;tagname&gt; into crisp code badge pills
    safe = safe.replace(/&lt;([a-zA-Z0-9_\-\.\#]+)&gt;/g, function (match, tagName) {
      return `<code class="cq-code-pill">&lt;${tagName}&gt;</code>`;
    });
    return safe;
  }

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
    const testBadgeCount = document.getElementById('testBadgeCount');
    const domTreeContainer = document.getElementById('liveDomTreeContainer');
    const consoleLogsContainer = document.getElementById('studioConsoleLogs');

    const tests = config.tests || [];
    const hints = config.hints || [];
    const lessonId = config.lessonId;
    const initialStarterCode = editor ? editor.value : '';
    let hintIndex = 0;

    // Listen for sandboxed iframe console messages
    window.addEventListener('message', function (e) {
      if (e.data && e.data.type === 'cq_console' && consoleLogsContainer) {
        const line = document.createElement('div');
        line.style.fontSize = '0.78rem';
        line.style.fontFamily = 'var(--font-mono)';
        line.style.padding = '0.3rem 0.6rem';
        line.style.borderRadius = 'var(--radius-xs)';
        line.style.marginBottom = '0.3rem';
        line.style.display = 'flex';
        line.style.alignItems = 'center';
        line.style.gap = '0.5rem';

        if (e.data.level === 'error') {
          line.style.color = '#ef4444';
          line.style.background = 'rgba(239, 68, 68, 0.12)';
          line.style.border = '1px solid rgba(239, 68, 68, 0.25)';
          line.innerHTML = `<span>✕</span> <span>${escapeHtml(e.data.msg)}</span>`;
        } else {
          line.style.color = '#38bdf8';
          line.style.background = 'rgba(56, 189, 248, 0.08)';
          line.style.border = '1px solid rgba(56, 189, 248, 0.2)';
          line.innerHTML = `<span>ℹ</span> <span>${escapeHtml(e.data.msg)}</span>`;
        }
        consoleLogsContainer.appendChild(line);
        consoleLogsContainer.scrollTop = consoleLogsContainer.scrollHeight;
      }
    });

    // Render test list with HTML-safe pills
    function renderTestList(passedMap) {
      if (!testListEl) return;
      testListEl.innerHTML = '';
      let passCount = 0;

      tests.forEach(function (t) {
        const hasEvaluated = passedMap !== null && passedMap[t.id] !== undefined;
        const passed = hasEvaluated && passedMap[t.id];
        if (passed) passCount++;

        const row = document.createElement('div');
        row.style.display = 'flex';
        row.style.alignItems = 'center';
        row.style.gap = '0.75rem';
        row.style.padding = '0.6rem 0.85rem';
        row.style.borderRadius = 'var(--radius-sm)';
        row.style.fontSize = '0.84rem';
        row.style.fontFamily = 'var(--font-sans)';
        row.style.background = passed
          ? 'var(--success-subtle)'
          : hasEvaluated
          ? 'var(--danger-subtle)'
          : 'var(--bg-panel)';
        row.style.border =
          '1px solid ' +
          (passed
            ? 'rgba(16, 185, 129, 0.35)'
            : hasEvaluated
            ? 'rgba(239, 68, 68, 0.35)'
            : 'var(--border-subtle)');
        row.style.transition = 'all 0.2s ease';

        const icon = passed ? '✓' : hasEvaluated ? '✕' : '○';
        const iconColor = passed ? 'var(--success)' : hasEvaluated ? 'var(--danger)' : 'var(--text-muted)';
        const descHtml = formatTestDescription(t.desc);

        row.innerHTML = `<span style="font-weight:800; color:${iconColor}; font-size:1rem; flex-shrink: 0; line-height: 1;">${icon}</span>
                         <span style="color:${passed ? 'var(--text-primary)' : 'var(--text-secondary)'}; line-height:1.45; font-size:0.84rem; flex: 1;">${descHtml}</span>`;
        testListEl.appendChild(row);
      });

      if (testBadgeCount) {
        testBadgeCount.textContent = `${passCount}/${tests.length}`;
        testBadgeCount.style.color = passCount === tests.length && tests.length > 0 ? 'var(--success)' : 'var(--accent)';
      }
    }

    renderTestList(null);

    // Live Visual DOM Tree Generator (Robust Dual-Mode: Live Iframe + DOMParser Fallback)
    function updateDomTree() {
      if (!domTreeContainer) return;
      try {
        let doc = null;
        if (previewFrame) {
          try {
            doc = previewFrame.contentDocument || (previewFrame.contentWindow && previewFrame.contentWindow.document);
          } catch (e) {}
        }
        // Fallback: parse raw editor code directly via DOMParser to prevent any blank initialization state
        if (!doc || !doc.body || doc.body.children.length === 0) {
          const code = editor ? editor.value : '';
          if (code) {
            try {
              doc = new DOMParser().parseFromString(code, 'text/html');
            } catch (e) {}
          }
        }
        if (!doc || !doc.body) return;

        let totalElements = 0;
        let maxDepth = 0;

        function traverseNode(node, currentDepth) {
          if (node.nodeType !== Node.ELEMENT_NODE) return '';
          const tag = node.tagName.toLowerCase();
          if (['script', 'style', 'meta', 'link'].includes(tag)) return '';

          totalElements++;
          if (currentDepth > maxDepth) maxDepth = currentDepth;

          let textSample = '';
          for (let i = 0; i < node.childNodes.length; i++) {
            const child = node.childNodes[i];
            if (child.nodeType === Node.TEXT_NODE && child.textContent.trim()) {
              textSample = child.textContent.trim();
              if (textSample.length > 24) textSample = textSample.substring(0, 24) + '…';
              break;
            }
          }

          let childHtml = '';
          for (let i = 0; i < node.children.length; i++) {
            childHtml += traverseNode(node.children[i], currentDepth + 1);
          }

          const tagColor =
            tag === 'header'
              ? '#38bdf8'
              : tag === 'main'
              ? '#818cf8'
              : tag === 'h1' || tag === 'h2' || tag === 'h3'
              ? '#f59e0b'
              : tag === 'p'
              ? '#34d399'
              : tag === 'a'
              ? '#ec4899'
              : tag === 'article' || tag === 'section'
              ? '#a855f7'
              : '#c084fc';

          let attrHtml = '';
          if (node.id) {
            attrHtml += `<span style="font-size:0.68rem; color:#facc15; margin-left:0.35rem; font-family:var(--font-mono);">#${escapeHtml(node.id)}</span>`;
          }
          if (node.className && typeof node.className === 'string') {
            const cls = node.className.trim().split(/\s+/)[0];
            if (cls) {
              attrHtml += `<span style="font-size:0.68rem; color:#38bdf8; margin-left:0.25rem; font-family:var(--font-mono);">.${escapeHtml(cls)}</span>`;
            }
          }

          return `
            <div class="dom-tree-node">
              <span class="dom-tag" style="border-color: ${tagColor}50; color: ${tagColor};">
                &lt;${tag}&gt;
              </span>
              ${attrHtml}
              ${
                textSample
                  ? `<span style="font-size: 0.74rem; color: var(--text-muted); margin-left: 0.4rem; font-family: var(--font-mono);">&quot;${escapeHtml(
                      textSample
                    )}&quot;</span>`
                  : ''
              }
              ${childHtml}
            </div>
          `;
        }

        let fullTreeHtml = '';
        for (let i = 0; i < doc.body.children.length; i++) {
          fullTreeHtml += traverseNode(doc.body.children[i], 1);
        }

        const domStatsBadge = document.getElementById('domStatsBadge');
        if (domStatsBadge) {
          domStatsBadge.textContent = `${totalElements} Element${totalElements === 1 ? '' : 's'} • Max Depth: ${maxDepth}`;
        }

        if (!fullTreeHtml.trim()) {
          domTreeContainer.innerHTML =
            '<div style="color: var(--text-muted); font-size: 0.8rem; padding: 1rem 0; font-style: italic;">No semantic HTML landmarks detected yet. Type &lt;header&gt; or &lt;main&gt; in the editor to grow your live DOM tree!</div>';
        } else {
          domTreeContainer.innerHTML = fullTreeHtml;
        }
      } catch (err) {
        // Sandboxed security boundary catch
      }
    }

    // Render iframe live preview
    function updatePreview() {
      if (!previewFrame || !editor) return;
      const code = editor.value;
      const isDark = document.documentElement.getAttribute('data-theme') !== 'light';
      const textColor = isDark ? '#f8fafc' : '#0f172a';
      const bgColor = isDark ? '#0c0f17' : '#ffffff';

      previewFrame.style.backgroundColor = bgColor;
      previewFrame.srcdoc = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script>
    window.onerror = function(msg, url, line) {
      window.parent.postMessage({ type: 'cq_console', level: 'error', msg: msg + ' (Line ' + line + ')' }, '*');
    };
    const _origLog = console.log;
    console.log = function(...args) {
      _origLog.apply(console, args);
      window.parent.postMessage({ type: 'cq_console', level: 'log', msg: args.join(' ') }, '*');
    };
  <\/script>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      padding: 1.25rem;
      color: ${textColor};
      background: ${bgColor};
      line-height: 1.55;
      transition: background 0.2s, color 0.2s;
    }
  </style>
</head>
<body>
  ${code}
</body>
</html>`;

      setTimeout(updateDomTree, 60);
    }

    if (runBtn) {
      runBtn.onclick = function () {
        updatePreview();
        if (global.CodeQuest) global.CodeQuest.playTone('click');
        if (statusMsg) {
          statusMsg.textContent = 'Preview updated.';
          statusMsg.style.color = 'var(--text-muted)';
        }
        // Activate Preview Studio tab
        const pTab = document.querySelector('[data-studio-tab="preview"]');
        if (pTab) pTab.click();
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

    // Auto-checking tests against iframe DOM
    function runTests() {
      updatePreview();
      const code = editor ? editor.value : '';
      const passedMap = {};
      let allPass = true;

      // Ensure Test Studio tab is active so learner sees feedback
      const tTab = document.querySelector('[data-studio-tab="tests"]');
      if (tTab) tTab.click();

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
          hintBtn.textContent = hintIndex < hints.length ? `💡 Next Hint (${hintIndex + 1}/${hints.length})` : '✨ Apply Solution';
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

    // Expose runners to global instance
    global.CodeQuestLessonRunner.updateDomTree = updateDomTree;
    global.CodeQuestLessonRunner.updatePreview = updatePreview;

    // Initial preview and DOM tree render
    updatePreview();
    updateDomTree();
  }

  global.CodeQuestLessonRunner = {
    init: initLessonRunner,
    escapeHtml: escapeHtml,
    formatTestDescription: formatTestDescription,
    updateDomTree: null,
    updatePreview: null,
  };
})(typeof window !== 'undefined' ? window : this);
