/**
 * CodeQuest BD — Software Architecture & Models Studio
 * Interactive living representations of foundational software engineering models:
 * 1. DOM Tree Model (Document Object Model)
 * 2. CSS Box Model (Layout & Geometry Model)
 * 3. AST & State Flow Model (Abstract Syntax Tree & Call Stack)
 * 4. Relational Schema Model (Database & Entity-Relationship Model)
 * 5. 3-Tier Clean Software Architecture (Presentation -> Logic -> Persistence)
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

  function initSoftwareModels(options) {
    const langSlug = (options && options.langSlug) || 'html';
    const editor = document.getElementById('codeEditor');

    // Model Pill Buttons
    const modelPills = document.querySelectorAll('.model-pill-btn');
    const modelPanes = {
      dom: document.getElementById('modelPaneDom'),
      box: document.getElementById('modelPaneBox'),
      ast: document.getElementById('modelPaneAst'),
      schema: document.getElementById('modelPaneSchema'),
      arch: document.getElementById('modelPaneArch')
    };

    function switchModel(modelKey) {
      modelPills.forEach(p => {
        p.classList.toggle('active', p.getAttribute('data-model') === modelKey);
      });
      Object.keys(modelPanes).forEach(k => {
        if (modelPanes[k]) {
          modelPanes[k].style.display = (k === modelKey) ? 'block' : 'none';
        }
      });

      // Trigger specific model refresh
      if (modelKey === 'box') updateBoxModel();
      if (modelKey === 'ast') updateAstModel();
      if (modelKey === 'schema') updateSchemaModel();
      if (modelKey === 'arch') updateArchModel();
      if (modelKey === 'dom' && global.CodeQuestLessonRunner && global.CodeQuestLessonRunner.updateDomTree) {
        global.CodeQuestLessonRunner.updateDomTree();
      }
    }

    modelPills.forEach(pill => {
      pill.addEventListener('click', function () {
        const target = pill.getAttribute('data-model');
        switchModel(target);
      });
    });

    // -------------------------------------------------------------
    // MODEL 2: CSS Box Model Logic
    // -------------------------------------------------------------
    const inM = document.getElementById('inlineInputMargin');
    const inB = document.getElementById('inlineInputBorder');
    const inP = document.getElementById('inlineInputPadding');
    const inR = document.getElementById('inlineInputRadius');
    const boxSizingRadios = document.querySelectorAll('input[name="boxSizingMode"]');
    const boxOutput = document.getElementById('inlineBoxModelCssOutput');
    const copyBtn = document.getElementById('inlineCopyBoxCssBtn');

    let isBorderBox = true;

    boxSizingRadios.forEach(radio => {
      radio.addEventListener('change', function () {
        isBorderBox = this.value === 'border-box';
        updateBoxModel();
      });
    });

    function updateBoxModel() {
      if (!inM || !inB || !inP || !inR) return;
      const m = parseInt(inM.value, 10) || 0;
      const b = parseInt(inB.value, 10) || 0;
      const p = parseInt(inP.value, 10) || 0;
      const r = parseInt(inR.value, 10) || 0;

      // Update Labels
      const lblM = document.getElementById('inlineLabelMargin');
      const lblB = document.getElementById('inlineLabelBorder');
      const lblP = document.getElementById('inlineLabelPadding');
      const lblR = document.getElementById('inlineLabelRadius');
      if (lblM) lblM.textContent = m + 'px';
      if (lblB) lblB.textContent = b + 'px';
      if (lblP) lblP.textContent = p + 'px';
      if (lblR) lblR.textContent = r + 'px';

      // Update concentric layers
      const elMargin = document.getElementById('inBmMarginLayer');
      const elBorder = document.getElementById('inBmBorderLayer');
      const elPadding = document.getElementById('inBmPaddingLayer');
      const elContent = document.getElementById('inBmContentLayer');

      if (elMargin) {
        elMargin.style.padding = `${m}px`;
        elMargin.style.borderRadius = `${r}px`;
      }
      if (elBorder) {
        elBorder.style.borderWidth = `${b}px`;
        elBorder.style.borderRadius = `${Math.max(0, r - 2)}px`;
      }
      if (elPadding) {
        elPadding.style.padding = `${p}px`;
        elPadding.style.borderRadius = `${Math.max(0, r - 4)}px`;
      }

      // Mathematical computation readout
      const nominalWidth = 240;
      const nominalHeight = 56;
      let renderedWidth, renderedHeight, actualContentW;

      if (isBorderBox) {
        // In border-box, padding + border are inside the 240px width
        renderedWidth = nominalWidth;
        renderedHeight = nominalHeight;
        actualContentW = Math.max(20, nominalWidth - (2 * (p + b)));
      } else {
        // In content-box, padding + border add onto width
        renderedWidth = nominalWidth + 2 * (p + b);
        renderedHeight = nominalHeight + 2 * (p + b);
        actualContentW = nominalWidth;
      }

      const outerFootprintW = renderedWidth + (2 * m);
      const mathDisplay = document.getElementById('boxModelMathDisplay');
      if (mathDisplay) {
        mathDisplay.innerHTML = `
          <div style="display:flex; justify-content:space-between; margin-bottom:0.25rem;">
            <span>Specified Width: <strong>${nominalWidth}px</strong></span>
            <span>Box-Sizing: <strong style="color:var(--accent);">${isBorderBox ? 'border-box' : 'content-box'}</strong></span>
          </div>
          <div style="font-size:0.75rem; color:var(--text-muted);">
            Rendered Element: <strong>${renderedWidth} &times; ${renderedHeight}px</strong> &bull; Total Screen Footprint: <strong>${outerFootprintW}px</strong>
          </div>
        `;
      }

      if (elContent) {
        elContent.querySelector('span').textContent = `Content (${actualContentW} × ${nominalHeight}px)`;
      }

      // Generate CSS
      const cssString = `box-sizing: ${isBorderBox ? 'border-box' : 'content-box'};\nmargin: ${m}px;\nborder: ${b}px solid #06b6d4;\npadding: ${p}px;\nborder-radius: ${r}px;`;
      if (boxOutput) boxOutput.textContent = cssString;
    }

    [inM, inB, inP, inR].forEach(slider => {
      if (slider) slider.addEventListener('input', updateBoxModel);
    });

    if (copyBtn && boxOutput) {
      copyBtn.onclick = function () {
        navigator.clipboard.writeText(boxOutput.textContent.trim());
        copyBtn.textContent = '✓ Copied';
        setTimeout(() => { copyBtn.textContent = 'Copy CSS'; }, 1400);
      };
    }

    // -------------------------------------------------------------
    // MODEL 3: AST & State Flow Model Logic
    // -------------------------------------------------------------
    function updateAstModel() {
      const astContainer = document.getElementById('astNodesContainer');
      const stackContainer = document.getElementById('callStackContainer');
      const scopeContainer = document.getElementById('scopeChainContainer');
      if (!astContainer || !editor) return;

      const code = editor.value || '';
      const lines = code.split('\n').filter(l => l.trim().length > 0);

      // Generate AST Node hierarchy
      let astHtml = `
        <div style="font-family:var(--font-mono); font-size:0.75rem; line-height:1.6;">
          <div style="display:flex; align-items:center; gap:0.5rem; color:var(--accent); font-weight:700;">
            <span>📦 Program</span>
            <span style="font-size:0.68rem; color:var(--text-muted); font-weight:normal;">(Root Module Body &bull; ${lines.length} lines)</span>
          </div>
          <div style="margin-left:1rem; border-left:2px solid rgba(99,102,241,0.25); padding-left:0.75rem; margin-top:0.4rem;">
      `;

      if (lines.length === 0) {
        astHtml += `<div style="color:var(--text-muted); font-style:italic;">Editor is empty. Write code to generate AST syntax tokens.</div>`;
      } else {
        lines.slice(0, 8).forEach((line, idx) => {
          const trimmed = line.trim();
          let nodeType = 'Statement';
          let nodeColor = '#38bdf8';

          if (/^(const|let|var)\s/.test(trimmed)) {
            nodeType = 'VariableDeclaration';
            nodeColor = '#facc15';
          } else if (/^(function|def)\s/.test(trimmed)) {
            nodeType = 'FunctionDeclaration';
            nodeColor = '#a855f7';
          } else if (/^(if|elif|else)\b/.test(trimmed)) {
            nodeType = 'ConditionalStatement';
            nodeColor = '#f97316';
          } else if (/^(for|while)\b/.test(trimmed)) {
            nodeType = 'IterationStatement';
            nodeColor = '#34d399';
          } else if (/^(select|insert|update|delete)\b/i.test(trimmed)) {
            nodeType = 'SqlDmlQuery';
            nodeColor = '#ec4899';
          } else if (/^<[a-zA-Z]/.test(trimmed)) {
            nodeType = 'JsxOrHtmlElement';
            nodeColor = '#06b6d4';
          } else if (/console\.|print\(|return\b/.test(trimmed)) {
            nodeType = 'CallOrReturnExpression';
            nodeColor = '#818cf8';
          }

          astHtml += `
            <div style="margin-bottom:0.4rem; background:rgba(255,255,255,0.03); padding:0.35rem 0.55rem; border-radius:6px; border:1px solid var(--border-subtle);">
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="color:${nodeColor}; font-weight:700;">${nodeType}</span>
                <span style="font-size:0.68rem; color:var(--text-muted);">Line ${idx + 1}</span>
              </div>
              <div style="color:var(--text-secondary); font-size:0.72rem; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; margin-top:0.15rem;">
                ${escapeHtml(trimmed.length > 45 ? trimmed.substring(0, 45) + '…' : trimmed)}
              </div>
            </div>
          `;
        });
      }

      astHtml += `</div></div>`;
      astContainer.innerHTML = astHtml;

      // Update Call Stack Context
      if (stackContainer) {
        stackContainer.innerHTML = `
          <div style="display:flex; flex-direction:column; gap:0.4rem; font-family:var(--font-mono); font-size:0.72rem;">
            <div style="background:rgba(16,185,129,0.12); border:1px solid rgba(16,185,129,0.3); color:#10b981; padding:0.35rem 0.6rem; border-radius:6px; display:flex; justify-content:space-between;">
              <span>[TOP] Active Execution Frame</span>
              <span>Evaluating</span>
            </div>
            <div style="background:rgba(99,102,241,0.1); border:1px solid rgba(99,102,241,0.25); color:var(--text-primary); padding:0.35rem 0.6rem; border-radius:6px; display:flex; justify-content:space-between;">
              <span>[STACK 0] Global Script Context</span>
              <span style="color:var(--text-muted);">Loaded</span>
            </div>
          </div>
        `;
      }

      // Update Scope Chain
      if (scopeContainer) {
        scopeContainer.innerHTML = `
          <div style="font-family:var(--font-mono); font-size:0.72rem; color:var(--text-secondary);">
            <div style="display:flex; justify-content:space-between; padding:0.25rem 0; border-bottom:1px dashed var(--border-subtle);">
              <span>Scope Type:</span>
              <span style="color:var(--accent); font-weight:700;">Module Lexical Scope</span>
            </div>
            <div style="display:flex; justify-content:space-between; padding:0.25rem 0; border-bottom:1px dashed var(--border-subtle);">
              <span>Closure Resolution:</span>
              <span style="color:#10b981;">Clean (0 Memory Leaks)</span>
            </div>
            <div style="display:flex; justify-content:space-between; padding:0.25rem 0;">
              <span>Garbage Collection:</span>
              <span style="color:var(--text-muted);">V8 / Pyodide WASM Ready</span>
            </div>
          </div>
        `;
      }
    }

    // -------------------------------------------------------------
    // MODEL 4: Relational Schema Model Logic
    // -------------------------------------------------------------
    const TABLES_META = [
      {
        name: 'auth_user',
        desc: 'Core Identity & Authentication',
        color: '#6366f1',
        fields: [
          { name: 'id', type: 'INT', tag: 'PK' },
          { name: 'username', type: 'VARCHAR(150)', tag: 'UNIQUE' },
          { name: 'email', type: 'VARCHAR(254)', tag: '' },
          { name: 'date_joined', type: 'TIMESTAMP', tag: '' }
        ]
      },
      {
        name: 'learn_course',
        desc: 'Curriculum Learning Tracks',
        color: '#06b6d4',
        fields: [
          { name: 'id', type: 'INT', tag: 'PK' },
          { name: 'title', type: 'VARCHAR(200)', tag: '' },
          { name: 'slug', type: 'VARCHAR(100)', tag: 'INDEX' },
          { name: 'language_id', type: 'INT', tag: 'FK' }
        ]
      },
      {
        name: 'learn_lesson',
        desc: 'Interactive In-Browser Challenges',
        color: '#10b981',
        fields: [
          { name: 'id', type: 'INT', tag: 'PK' },
          { name: 'course_id', type: 'INT', tag: 'FK' },
          { name: 'title', type: 'VARCHAR(200)', tag: '' },
          { name: 'order', type: 'INT', tag: '' },
          { name: 'xp', type: 'INT', tag: 'DEF 50' }
        ]
      },
      {
        name: 'learn_userprogress',
        desc: 'Relational Completion & Attempt Ledger',
        color: '#f59e0b',
        fields: [
          { name: 'id', type: 'INT', tag: 'PK' },
          { name: 'user_id', type: 'INT', tag: 'FK' },
          { name: 'lesson_id', type: 'INT', tag: 'FK' },
          { name: 'status', type: 'VARCHAR(20)', tag: '' },
          { name: 'attempts', type: 'INT', tag: '' }
        ]
      }
    ];

    function updateSchemaModel() {
      const container = document.getElementById('relationalTablesList');
      if (!container) return;

      let html = '';
      TABLES_META.forEach(t => {
        html += `
          <div style="background:var(--bg-surface); border:1px solid var(--border-subtle); border-radius:var(--radius-sm); padding:0.75rem 0.85rem; margin-bottom:0.75rem;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem; border-bottom:1px solid var(--border-subtle); padding-bottom:0.35rem;">
              <span style="font-family:var(--font-mono); font-size:0.82rem; font-weight:700; color:${t.color};">
                📋 ${t.name}
              </span>
              <span style="font-size:0.68rem; color:var(--text-muted);">${t.desc}</span>
            </div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.35rem; font-family:var(--font-mono); font-size:0.72rem;">
        `;
        t.fields.forEach(f => {
          let tagBadge = '';
          if (f.tag === 'PK') tagBadge = `<span style="background:rgba(239,68,68,0.15); color:#ef4444; padding:0 4px; border-radius:3px; font-weight:700;">PK</span>`;
          else if (f.tag === 'FK') tagBadge = `<span style="background:rgba(99,102,241,0.15); color:#818cf8; padding:0 4px; border-radius:3px; font-weight:700;">FK</span>`;
          else if (f.tag) tagBadge = `<span style="background:rgba(255,255,255,0.06); color:var(--text-muted); padding:0 4px; border-radius:3px;">${f.tag}</span>`;

          html += `
            <div style="display:flex; justify-content:space-between; align-items:center; padding:0.2rem 0.4rem; background:rgba(255,255,255,0.02); border-radius:4px;">
              <span>${f.name}</span>
              <span style="color:var(--text-muted);">${f.type} ${tagBadge}</span>
            </div>
          `;
        });
        html += `</div></div>`;
      });

      container.innerHTML = html;
    }

    // -------------------------------------------------------------
    // MODEL 5: 3-Tier Architecture Model Logic
    // -------------------------------------------------------------
    function updateArchModel() {
      const archContainer = document.getElementById('architectureTiersContainer');
      if (!archContainer) return;

      const isPresentation = ['html', 'css'].some(s => langSlug.includes(s));
      const isLogic = ['js', 'javascript', 'py', 'python', 'rust', 'go'].some(s => langSlug.includes(s));
      const isData = ['sql', 'database'].some(s => langSlug.includes(s));

      archContainer.innerHTML = `
        <div style="display:flex; flex-direction:column; gap:0.75rem; font-family:var(--font-sans);">
          <!-- Tier 1: Client / Presentation -->
          <div style="padding:0.85rem 1rem; border-radius:var(--radius-sm); border:1px solid ${isPresentation ? 'var(--accent)' : 'var(--border-subtle)'}; background:${isPresentation ? 'var(--accent-subtle)' : 'var(--bg-surface)'};">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.35rem;">
              <span style="font-weight:700; font-size:0.85rem; color:${isPresentation ? 'var(--accent)' : 'var(--text-primary)'};">
                1. Presentation Tier (Client UI &amp; DOM)
              </span>
              ${isPresentation ? '<span style="font-size:0.68rem; font-weight:700; background:var(--accent); color:#ffffff; padding:0.15rem 0.5rem; border-radius:999px;">📍 ACTIVE LESSON</span>' : '<span style="font-size:0.7rem; color:var(--text-muted);">Browser Engine</span>'}
            </div>
            <div style="font-size:0.78rem; color:var(--text-secondary); line-height:1.45;">
              Parses HTML DOM landmarks, evaluates CSS visual styles, handles keyboard inputs, and paints real-time pixels in the viewport.
            </div>
          </div>

          <div style="text-align:center; color:var(--text-muted); font-size:0.9rem; margin:-0.35rem 0;">⬇ JSON RPC / REST API (HTTP &bull; 0ms latency) ⬇</div>

          <!-- Tier 2: Logic & Controller Engine -->
          <div style="padding:0.85rem 1rem; border-radius:var(--radius-sm); border:1px solid ${isLogic ? '#a855f7' : 'var(--border-subtle)'}; background:${isLogic ? 'rgba(168,85,247,0.1)' : 'var(--bg-surface)'};">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.35rem;">
              <span style="font-weight:700; font-size:0.85rem; color:${isLogic ? '#c084fc' : 'var(--text-primary)'};">
                2. Application Logic Tier (Controller &amp; AST Engine)
              </span>
              ${isLogic ? '<span style="font-size:0.68rem; font-weight:700; background:#a855f7; color:#ffffff; padding:0.15rem 0.5rem; border-radius:999px;">📍 ACTIVE LESSON</span>' : '<span style="font-size:0.7rem; color:var(--text-muted);">WASM / Node / Django</span>'}
            </div>
            <div style="font-size:0.78rem; color:var(--text-secondary); line-height:1.45;">
              Parses source code into AST trees, enforces automated verification assertions, executes algorithms, and calculates XP streaks.
            </div>
          </div>

          <div style="text-align:center; color:var(--text-muted); font-size:0.9rem; margin:-0.35rem 0;">⬇ SQL ORM / PostgreSQL Connections (ACID Safe) ⬇</div>

          <!-- Tier 3: Data Persistence Tier -->
          <div style="padding:0.85rem 1rem; border-radius:var(--radius-sm); border:1px solid ${isData ? '#f59e0b' : 'var(--border-subtle)'}; background:${isData ? 'rgba(245,158,11,0.1)' : 'var(--bg-surface)'};">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.35rem;">
              <span style="font-weight:700; font-size:0.85rem; color:${isData ? '#f59e0b' : 'var(--text-primary)'};">
                3. Data Persistence Tier (Relational Storage &amp; Schemas)
              </span>
              ${isData ? '<span style="font-size:0.68rem; font-weight:700; background:#f59e0b; color:#ffffff; padding:0.15rem 0.5rem; border-radius:999px;">📍 ACTIVE LESSON</span>' : '<span style="font-size:0.7rem; color:var(--text-muted);">Cloud PostgreSQL / SQLite</span>'}
            </div>
            <div style="font-size:0.78rem; color:var(--text-secondary); line-height:1.45;">
              Saves permanent user achievements, badge unlocks, session tokens, and relational progress records with indexed durability.
            </div>
          </div>
        </div>
      `;
    }

    // Default active model based on language
    let defaultModel = 'dom';
    if (langSlug.includes('css')) defaultModel = 'box';
    else if (langSlug.includes('js') || langSlug.includes('py') || langSlug.includes('rust') || langSlug.includes('go')) defaultModel = 'ast';
    else if (langSlug.includes('sql')) defaultModel = 'schema';

    switchModel(defaultModel);

    // Global debounce hook for code editor updates
    let debounceTimer = null;
    global.updateAllSoftwareModels = function () {
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(function () {
        if (global.CodeQuestLessonRunner && global.CodeQuestLessonRunner.updateDomTree) {
          global.CodeQuestLessonRunner.updateDomTree();
        }
        updateAstModel();
      }, 150);
    };
  }

  global.CodeQuestSoftwareModels = {
    init: initSoftwareModels
  };
})(typeof window !== 'undefined' ? window : this);
