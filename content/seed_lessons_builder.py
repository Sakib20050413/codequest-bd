"""
Generates the comprehensive lesson catalog for CodeQuest.
"""

def get_html_lessons():
    return [
        {
            "order": 1, "slug": "page-skeleton", "title": "01. Page Skeleton (<main> & <header>)",
            "minutes": 4, "xp": 50, "type": "IFRAME",
            "body": "Every web page begins with semantic landmarks. `<header>` contains introductory branding, while `<main>` houses the primary content unique to that page. Using semantic tags makes your layout accessible to screen readers and search engines.\n\n[Go deeper on MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/main)",
            "task": "Add a `<header>` containing an `<h1>` with text 'CodeQuest', followed by a `<main>` with a `<p>` saying 'Bite-sized learning.'",
            "starter": "<!-- Write your HTML skeleton below -->\n",
            "solution": "<header>\n  <h1>CodeQuest</h1>\n</header>\n<main>\n  <p>Bite-sized learning.</p>\n</main>",
            "tests": [
                {"id": "t1", "desc": "Has <header> element", "type": "dom_exists", "query": "header"},
                {"id": "t2", "desc": "Has <h1> inside header", "type": "dom_exists", "query": "header h1"},
                {"id": "t3", "desc": "Has <main> element", "type": "dom_exists", "query": "main"},
            ],
            "hints": ["Start by typing <header>...</header>", "Put <h1>CodeQuest</h1> inside <header>", "Below header, add <main><p>Bite-sized learning.</p></main>"]
        },
        {
            "order": 2, "slug": "headings-and-text", "title": "02. Headings & Hierarchy (h1 to h6)",
            "minutes": 4, "xp": 50, "type": "IFRAME",
            "body": "Heading tags `<h1>` through `<h6>` represent importance levels, like an outline in a book. A page should typically have exactly one `<h1>`, followed by `<h2>` for subsections, and `<p>` for paragraphs.",
            "task": "Create an `<h2>` with text 'Chapters' and a `<p>` explaining your first chapter.",
            "starter": "<h1>Book Title</h1>\n<!-- Add h2 and p below -->\n",
            "solution": "<h1>Book Title</h1>\n<h2>Chapters</h2>\n<p>Chapter 1 covers variables.</p>",
            "tests": [
                {"id": "t1", "desc": "Has <h2> element", "type": "dom_exists", "query": "h2"},
                {"id": "t2", "desc": "Has paragraph <p>", "type": "dom_exists", "query": "p"},
            ],
            "hints": ["Write <h2>Chapters</h2>", "Add a <p> tag right after."]
        },
        {
            "order": 3, "slug": "hyperlinks", "title": "03. Hyperlinks (<a href>)",
            "minutes": 3, "xp": 40, "type": "IFRAME",
            "body": "The anchor tag `<a>` connects pages. The `href` attribute specifies the destination URL. Adding `target=\"_blank\"` instructs the browser to open the destination in a new tab.",
            "task": "Create an anchor link `<a>` pointing to 'https://codequest.dev' with text 'Explore Playground'.",
            "starter": "<!-- Add your link below -->\n",
            "solution": "<a href=\"https://codequest.dev\" target=\"_blank\">Explore Playground</a>",
            "tests": [
                {"id": "t1", "desc": "Has <a> tag", "type": "dom_exists", "query": "a"},
                {"id": "t2", "desc": "href attribute is present", "type": "dom_has_attr", "query": "a", "attr": "href"},
            ],
            "hints": ["Use <a href=\"...\">Label</a>", "Set href to https://codequest.dev"]
        },
        {
            "order": 4, "slug": "images-and-alt", "title": "04. Images & Accessibility (<img> & alt)",
            "minutes": 4, "xp": 50, "type": "IFRAME",
            "body": "`<img>` is a self-closing void tag. It requires `src` for the image path and `alt` for the alternative text. Never omit `alt`—it is required for screen readers when an image cannot load.",
            "task": "Add an `<img>` tag with `src=\"/static/img/logo.svg\"` and `alt=\"CodeQuest Logo\"`.",
            "starter": "<!-- Add img with src and alt -->\n",
            "solution": "<img src=\"/static/img/logo.svg\" alt=\"CodeQuest Logo\" />",
            "tests": [
                {"id": "t1", "desc": "Has <img> tag", "type": "dom_exists", "query": "img"},
                {"id": "t2", "desc": "Has alt text attribute", "type": "dom_has_attr", "query": "img", "attr": "alt"},
            ],
            "hints": ["Write <img src=\"...\" alt=\"...\" />", "Make sure alt is non-empty."]
        },
        {
            "order": 5, "slug": "lists", "title": "05. Ordered & Unordered Lists (<ul> & <ol>)",
            "minutes": 4, "xp": 50, "type": "IFRAME",
            "body": "Use `<ul>` for bulleted collections where sequence doesn't matter, and `<ol>` for numbered sequential steps. Each entry inside must be a `<li>` item.",
            "task": "Build an unordered list `<ul>` with three `<li>` items: 'HTML', 'CSS', and 'JavaScript'.",
            "starter": "<!-- Create ul with 3 li items -->\n",
            "solution": "<ul>\n  <li>HTML</li>\n  <li>CSS</li>\n  <li>JavaScript</li>\n</ul>",
            "tests": [
                {"id": "t1", "desc": "Has <ul> list", "type": "dom_exists", "query": "ul"},
                {"id": "t2", "desc": "Contains at least 3 <li> items", "type": "dom_count_min", "query": "ul li", "min": 3},
            ],
            "hints": ["Wrap the items in <ul>...</ul>", "Inside, add <li>HTML</li>, <li>CSS</li>, <li>JavaScript</li>"]
        },
        {
            "order": 6, "slug": "tables", "title": "06. Table Foundations (<table>, <tr>, <td>)",
            "minutes": 5, "xp": 50, "type": "IFRAME",
            "body": "HTML tables organize tabular data into rows `<tr>`. Use `<th>` for column header titles and `<td>` for individual data cells.",
            "task": "Build a table with 1 header row (<tr><th>Name</th><th>XP</th></tr>) and 1 data row (<tr><td>Sakib</td><td>500</td></tr>).",
            "starter": "<table>\n  <!-- Add rows here -->\n</table>",
            "solution": "<table>\n  <tr>\n    <th>Name</th>\n    <th>XP</th>\n  </tr>\n  <tr>\n    <td>Sakib</td>\n    <td>500</td>\n  </tr>\n</table>",
            "tests": [
                {"id": "t1", "desc": "Has <table> element", "type": "dom_exists", "query": "table"},
                {"id": "t2", "desc": "Has <th> header cells", "type": "dom_exists", "query": "table th"},
                {"id": "t3", "desc": "Has <td> data cells", "type": "dom_exists", "query": "table td"},
            ],
            "hints": ["Each row uses <tr>...</tr>", "Headers use <th>, data cells use <td>"]
        },
        {
            "order": 7, "slug": "table-spanning", "title": "07. Table Cell Spanning (rowspan & colspan)",
            "minutes": 5, "xp": 60, "type": "IFRAME",
            "body": "Merge adjacent cells horizontally using `colspan=\"N\"` and vertically using `rowspan=\"N\"`. Spanning helps create summary bars and grouped headers without nested tables.",
            "task": "Create a cell with `colspan=\"2\"` containing 'Total Score'.",
            "starter": "<table>\n  <tr>\n    <!-- Add td with colspan=\"2\" -->\n  </tr>\n</table>",
            "solution": "<table>\n  <tr>\n    <td colspan=\"2\">Total Score</td>\n  </tr>\n</table>",
            "tests": [
                {"id": "t1", "desc": "Has cell with colspan=2", "type": "dom_has_attr_val", "query": "td", "attr": "colspan", "val": "2"},
            ],
            "hints": ["Add <td colspan=\"2\">Total Score</td> inside <tr>"]
        },
        {
            "order": 8, "slug": "form-inputs", "title": "08. Form Text & Email Inputs (<input>)",
            "minutes": 4, "xp": 50, "type": "IFRAME",
            "body": "User interaction begins with `<form>`. The `type` attribute on `<input>` informs the browser what keyboard and validation rules to trigger (`text`, `email`, `number`).",
            "task": "Add an `<input type=\"email\" placeholder=\"you@domain.com\" required>`.",
            "starter": "<form>\n  <!-- Add email input -->\n</form>",
            "solution": "<form>\n  <input type=\"email\" placeholder=\"you@domain.com\" required />\n</form>",
            "tests": [
                {"id": "t1", "desc": "Has email input", "type": "dom_has_attr_val", "query": "input", "attr": "type", "val": "email"},
            ],
            "hints": ["Use <input type=\"email\" ... />"]
        },
        {
            "order": 9, "slug": "form-buttons", "title": "09. Form Submit Buttons (<button type='submit'>)",
            "minutes": 3, "xp": 40, "type": "IFRAME",
            "body": "Buttons inside a form default to submit behavior. Explicitly declaring `type=\"submit\"` prevents ambiguity across browsers.",
            "task": "Add `<button type=\"submit\">Start Learning</button>` inside the form.",
            "starter": "<form>\n  <input type=\"text\" placeholder=\"Name\" />\n  <!-- Add button below -->\n</form>",
            "solution": "<form>\n  <input type=\"text\" placeholder=\"Name\" />\n  <button type=\"submit\">Start Learning</button>\n</form>",
            "tests": [
                {"id": "t1", "desc": "Has submit button", "type": "dom_exists", "query": "button[type='submit']"},
            ],
            "hints": ["Add <button type=\"submit\">Start Learning</button>"]
        },
        {
            "order": 10, "slug": "dropdowns", "title": "10. Dropdowns & Option Select (<select> & <option>)",
            "minutes": 4, "xp": 50, "type": "IFRAME",
            "body": "The `<select>` element produces a drop-down menu. Individual selectable options are defined with `<option value=\"...\">`.",
            "task": "Create a `<select>` with two options: 'Python' and 'JavaScript'.",
            "starter": "<!-- Add select and options -->\n",
            "solution": "<select name=\"language\">\n  <option value=\"py\">Python</option>\n  <option value=\"js\">JavaScript</option>\n</select>",
            "tests": [
                {"id": "t1", "desc": "Has <select> menu", "type": "dom_exists", "query": "select"},
                {"id": "t2", "desc": "Has at least 2 <option> tags", "type": "dom_count_min", "query": "select option", "min": 2},
            ],
            "hints": ["Nest <option> tags inside <select>...</select>"]
        },
        {
            "order": 11, "slug": "textareas-labels", "title": "11. Textareas & Accessible Labels (<label for>)",
            "minutes": 4, "xp": 50, "type": "IFRAME",
            "body": "Pairing `<label for=\"box-id\">` with an input or `<textarea id=\"box-id\">` ensures that clicking the label focuses the field—a critical requirement for accessible UI.",
            "task": "Create `<label for=\"bio\">Bio:</label>` and `<textarea id=\"bio\"></textarea>`.",
            "starter": "<!-- Add label and matching textarea -->\n",
            "solution": "<label for=\"bio\">Bio:</label>\n<textarea id=\"bio\"></textarea>",
            "tests": [
                {"id": "t1", "desc": "Has <label>", "type": "dom_exists", "query": "label[for='bio']"},
                {"id": "t2", "desc": "Has textarea with id='bio'", "type": "dom_exists", "query": "textarea#bio"},
            ],
            "hints": ["Make sure the label's 'for' attribute matches the textarea's 'id'."]
        },
        {
            "order": 12, "slug": "semantic-media", "title": "12. Semantic Audio & Video (<video> & <audio>)",
            "minutes": 4, "xp": 50, "type": "IFRAME",
            "body": "Modern browsers natively play media without plugins. The `controls` attribute displays playback controls (play, pause, volume).",
            "task": "Add a `<video controls width=\"320\"><source src=\"intro.mp4\" type=\"video/mp4\"></video>` tag.",
            "starter": "<!-- Add video element with controls -->\n",
            "solution": "<video controls width=\"320\">\n  <source src=\"intro.mp4\" type=\"video/mp4\" />\n</video>",
            "tests": [
                {"id": "t1", "desc": "Has <video controls>", "type": "dom_exists", "query": "video[controls]"},
            ],
            "hints": ["Include the 'controls' attribute on <video controls>."]
        },
    ]

def get_css_lessons():
    return [
        {
            "order": 1, "slug": "selectors-colors", "title": "01. Selectors & Color Values",
            "minutes": 4, "xp": 50, "type": "IFRAME",
            "body": "CSS targets HTML elements to apply visual rules. `color` sets text color, while `background-color` fills the element's container.",
            "task": "Style `.card` with `color: #10b981;` and `background-color: #090a0f;`.",
            "starter": "<style>\n.card {\n  /* Add color and background-color */\n}\n</style>\n<div class=\"card\">Styled Card</div>",
            "solution": "<style>\n.card {\n  color: #10b981;\n  background-color: #090a0f;\n}\n</style>\n<div class=\"card\">Styled Card</div>",
            "tests": [{"id": "t1", "desc": "Has color rule", "type": "css_rule", "sel": ".card", "prop": "color"}],
            "hints": ["Add color: #10b981; and background-color: #090a0f; inside .card { }"]
        },
        {
            "order": 2, "slug": "box-model", "title": "02. The CSS Box Model (Padding & Margin)",
            "minutes": 5, "xp": 50, "type": "IFRAME",
            "body": "Every element is a box composed of: Content $\\rightarrow$ Padding (internal buffer) $\\rightarrow$ Border $\\rightarrow$ Margin (external spacing).",
            "task": "Give `.box` a `padding: 16px;` and `margin: 20px;`.",
            "starter": "<style>\n.box {\n  background: #1e293b;\n  /* Add padding and margin */\n}\n</style>\n<div class=\"box\">Box Model</div>",
            "solution": "<style>\n.box {\n  background: #1e293b;\n  padding: 16px;\n  margin: 20px;\n}\n</style>\n<div class=\"box\">Box Model</div>",
            "tests": [{"id": "t1", "desc": "Padding is set", "type": "css_rule", "sel": ".box", "prop": "padding"}],
            "hints": ["Write padding: 16px; and margin: 20px;"]
        },
        {
            "order": 3, "slug": "flexbox-direction", "title": "03. Flexbox Container & Directions",
            "minutes": 5, "xp": 50, "type": "IFRAME",
            "body": "`display: flex;` activates flexible box layout. Child elements align in a row by default. Use `flex-direction: column;` to stack them vertically.",
            "task": "Set `.row` to `display: flex;`.",
            "starter": "<style>\n.row {\n  /* Enable flexbox */\n}\n</style>\n<div class=\"row\"><div>A</div><div>B</div></div>",
            "solution": "<style>\n.row {\n  display: flex;\n}\n</style>\n<div class=\"row\"><div>A</div><div>B</div></div>",
            "tests": [{"id": "t1", "desc": "display is flex", "type": "css_rule", "sel": ".row", "prop": "display"}],
            "hints": ["Add display: flex; inside .row"]
        },
        {
            "order": 4, "slug": "flexbox-justify", "title": "04. Flexbox Horizontal Alignment (justify-content)",
            "minutes": 5, "xp": 50, "type": "IFRAME",
            "body": "`justify-content` distributes items along the main axis. Common values: `center`, `space-between` (spreads to edges), and `flex-end`.",
            "task": "Add `justify-content: space-between;` to `.nav`.",
            "starter": "<style>\n.nav {\n  display: flex;\n  /* Add justify-content */\n}\n</style>\n<nav class=\"nav\"><span>Logo</span><span>Profile</span></nav>",
            "solution": "<style>\n.nav {\n  display: flex;\n  justify-content: space-between;\n}\n</style>\n<nav class=\"nav\"><span>Logo</span><span>Profile</span></nav>",
            "tests": [{"id": "t1", "desc": "justify-content is space-between", "type": "css_rule", "sel": ".nav", "prop": "justify-content"}],
            "hints": ["Add justify-content: space-between; inside .nav"]
        },
        {
            "order": 5, "slug": "flexbox-align", "title": "05. Flexbox Vertical Alignment (align-items)",
            "minutes": 5, "xp": 50, "type": "IFRAME",
            "body": "`align-items` aligns flex items across the cross axis. Use `align-items: center;` to vertically center badges or icons inside a navigation bar.",
            "task": "Center children vertically in `.toolbar` using `align-items: center;`.",
            "starter": "<style>\n.toolbar {\n  display: flex;\n  height: 60px;\n  /* Add align-items */\n}\n</style>\n<div class=\"toolbar\"><button>Action</button></div>",
            "solution": "<style>\n.toolbar {\n  display: flex;\n  height: 60px;\n  align-items: center;\n}\n</style>\n<div class=\"toolbar\"><button>Action</button></div>",
            "tests": [{"id": "t1", "desc": "align-items is center", "type": "css_rule", "sel": ".toolbar", "prop": "align-items"}],
            "hints": ["Write align-items: center;"]
        },
        {
            "order": 6, "slug": "css-grid-template", "title": "06. CSS Grid 2D Columns (grid-template-columns)",
            "minutes": 5, "xp": 50, "type": "IFRAME",
            "body": "CSS Grid handles two-dimensional layouts with rows and columns simultaneously. `grid-template-columns: repeat(3, 1fr);` creates 3 equal-width columns.",
            "task": "Configure `.grid` with `display: grid;` and `grid-template-columns: repeat(3, 1fr);`.",
            "starter": "<style>\n.grid {\n  /* Add grid properties */\n}\n</style>\n<div class=\"grid\"><div>1</div><div>2</div><div>3</div></div>",
            "solution": "<style>\n.grid {\n  display: grid;\n  grid-template-columns: repeat(3, 1fr);\n}\n</style>\n<div class=\"grid\"><div>1</div><div>2</div><div>3</div></div>",
            "tests": [{"id": "t1", "desc": "display is grid", "type": "css_rule", "sel": ".grid", "prop": "display"}],
            "hints": ["Add display: grid; and grid-template-columns: repeat(3, 1fr);"]
        },
        {
            "order": 7, "slug": "grid-gap", "title": "07. Grid & Flex Spacing (gap)",
            "minutes": 4, "xp": 40, "type": "IFRAME",
            "body": "The `gap` property cleanly sets gutters between rows and columns without fiddling with negative margins on child elements.",
            "task": "Add `gap: 20px;` to `.gallery`.",
            "starter": "<style>\n.gallery {\n  display: flex;\n  /* Add gap */\n}\n</style>\n<div class=\"gallery\"><div>A</div><div>B</div></div>",
            "solution": "<style>\n.gallery {\n  display: flex;\n  gap: 20px;\n}\n</style>\n<div class=\"gallery\"><div>A</div><div>B</div></div>",
            "tests": [{"id": "t1", "desc": "gap is set", "type": "css_rule", "sel": ".gallery", "prop": "gap"}],
            "hints": ["Write gap: 20px;"]
        },
        {
            "order": 8, "slug": "positioning", "title": "08. Relative & Absolute Positioning",
            "minutes": 5, "xp": 50, "type": "IFRAME",
            "body": "`position: relative;` keeps an element in the natural document flow while acting as an anchor coordinate container for child elements with `position: absolute;`.",
            "task": "Set `.parent` to `position: relative;` and `.badge` to `position: absolute; top: 0; right: 0;`.",
            "starter": "<style>\n.parent {\n  /* Anchor */\n}\n.badge {\n  /* Pin to top right */\n}\n</style>\n<div class=\"parent\"><span class=\"badge\">New</span>Card</div>",
            "solution": "<style>\n.parent {\n  position: relative;\n}\n.badge {\n  position: absolute;\n  top: 0;\n  right: 0;\n}\n</style>\n<div class=\"parent\"><span class=\"badge\">New</span>Card</div>",
            "tests": [{"id": "t1", "desc": "parent is relative", "type": "css_rule", "sel": ".parent", "prop": "position"}],
            "hints": ["parent needs position: relative; badge needs position: absolute;"]
        },
        {
            "order": 9, "slug": "hover-transitions", "title": "09. Smooth Transitions (:hover & transition)",
            "minutes": 5, "xp": 50, "type": "IFRAME",
            "body": "The `transition` property animates style changes smoothly instead of abruptly snapping. Example: `transition: opacity 180ms ease;`.",
            "task": "Add `transition: transform 160ms ease;` to `.btn` and `.btn:hover { transform: scale(1.04); }`.",
            "starter": "<style>\n.btn {\n  /* Add transition */\n}\n.btn:hover {\n  /* Add transform scale */\n}\n</style>\n<button class=\"btn\">Hover Me</button>",
            "solution": "<style>\n.btn {\n  transition: transform 160ms ease;\n}\n.btn:hover {\n  transform: scale(1.04);\n}\n</style>\n<button class=\"btn\">Hover Me</button>",
            "tests": [{"id": "t1", "desc": "transition rule exists", "type": "css_rule", "sel": ".btn", "prop": "transition"}],
            "hints": ["Define transition on .btn and transform on .btn:hover"]
        },
        {
            "order": 10, "slug": "custom-properties", "title": "10. Design Tokens (CSS Variables)",
            "minutes": 4, "xp": 50, "type": "IFRAME",
            "body": "CSS Variables (`--variable-name`) let you define design tokens once and reuse them everywhere: `color: var(--brand-emerald);`.",
            "task": "Define `--accent: #10b981;` inside `:root` and apply it to `.pill { color: var(--accent); }`.",
            "starter": "<style>\n:root {\n  /* Define --accent */\n}\n.pill {\n  /* Use var(--accent) */\n}\n</style>\n<span class=\"pill\">Token</span>",
            "solution": "<style>\n:root {\n  --accent: #10b981;\n}\n.pill {\n  color: var(--accent);\n}\n</style>\n<span class=\"pill\">Token</span>",
            "tests": [{"id": "t1", "desc": "CSS variable used", "type": "css_rule", "sel": ".pill", "prop": "color"}],
            "hints": ["Write --accent: #10b981; in :root, then color: var(--accent); in .pill"]
        },
        {
            "order": 11, "slug": "media-queries", "title": "11. Responsive Media Queries (@media)",
            "minutes": 5, "xp": 60, "type": "IFRAME",
            "body": "`@media (max-width: 768px)` adapts layout rules for mobile viewports, allowing elements to switch from a multi-column row to a single stacked column.",
            "task": "Add a media query `@media (max-width: 600px) { .row { flex-direction: column; } }`.",
            "starter": "<style>\n.row { display: flex; }\n/* Add mobile media query below */\n</style>\n<div class=\"row\"><div>1</div><div>2</div></div>",
            "solution": "<style>\n.row { display: flex; }\n@media (max-width: 600px) {\n  .row {\n    flex-direction: column;\n  }\n}\n</style>\n<div class=\"row\"><div>1</div><div>2</div></div>",
            "tests": [{"id": "t1", "desc": "Has @media rule", "type": "css_contains", "val": "@media"}],
            "hints": ["Wrap the mobile rule in @media (max-width: 600px) { ... }"]
        },
        {
            "order": 12, "slug": "accessibility-focus", "title": "12. Keyboard Accessibility (:focus-visible)",
            "minutes": 4, "xp": 50, "type": "IFRAME",
            "body": "Never remove outlines with `outline: none` without providing an alternative. Use `:focus-visible` to present clean focus rings only when navigating via keyboard.",
            "task": "Add a visible outline rule: `button:focus-visible { outline: 2px solid #10b981; outline-offset: 2px; }`.",
            "starter": "<style>\n/* Add focus-visible rule */\n</style>\n<button>Accessible Tab Focus</button>",
            "solution": "<style>\nbutton:focus-visible {\n  outline: 2px solid #10b981;\n  outline-offset: 2px;\n}\n</style>\n<button>Accessible Tab Focus</button>",
            "tests": [{"id": "t1", "desc": "Has focus-visible selector", "type": "css_contains", "val": "focus-visible"}],
            "hints": ["Use button:focus-visible { outline: ... }"]
        },
    ]

def get_js_lessons():
    return [
        {
            "order": 1, "slug": "const-let", "title": "01. Variables: const & let",
            "minutes": 3, "xp": 40, "type": "IFRAME",
            "body": "`const` declares identifiers that cannot be reassigned, while `let` allows value reassignment. Never use legacy `var` in modern JavaScript.",
            "task": "Declare `const platform = 'CodeQuest';` and `let score = 100;`.",
            "starter": "// Declare platform and score\n",
            "solution": "const platform = 'CodeQuest';\nlet score = 100;",
            "tests": [{"id": "t1", "desc": "platform is declared with const", "type": "js_var", "name": "platform", "val": "CodeQuest"}],
            "hints": ["Use const for platform and let for score."]
        },
        {
            "order": 2, "slug": "template-literals", "title": "02. String Interpolation (`${var}`)",
            "minutes": 4, "xp": 45, "type": "IFRAME",
            "body": "Template literals enclosed in backticks (`` ` ``) allow embedding variables and expressions directly with `${expression}` without clunky string concatenation.",
            "task": "Create `const greeting = `Hello, ${user}!`;` where user is 'Sakib'.",
            "starter": "const user = 'Sakib';\n// Create greeting using template literal\n",
            "solution": "const user = 'Sakib';\nconst greeting = `Hello, ${user}!`;",
            "tests": [{"id": "t1", "desc": "greeting equals 'Hello, Sakib!'", "type": "js_var", "name": "greeting", "val": "Hello, Sakib!"}],
            "hints": ["Use backticks `` `Hello, ${user}!` ``"]
        },
        {
            "order": 3, "slug": "arrow-functions", "title": "03. Arrow Functions (() => {})",
            "minutes": 4, "xp": 50, "type": "IFRAME",
            "body": "Arrow functions provide concise syntax: `const add = (a, b) => a + b;` implicitly returns the sum if written on one line without braces.",
            "task": "Write an arrow function `const double = (n) => n * 2;`.",
            "starter": "// Define double arrow function\n",
            "solution": "const double = (n) => n * 2;",
            "tests": [{"id": "t1", "desc": "double(5) returns 10", "type": "js_fn_eval", "expr": "double(5)", "expected": 10}],
            "hints": ["Write const double = (n) => n * 2;"]
        },
        {
            "order": 4, "slug": "dom-query-selector", "title": "04. DOM Selection (document.querySelector)",
            "minutes": 4, "xp": 50, "type": "IFRAME",
            "body": "`document.querySelector('#target')` selects the first element matching a standard CSS selector so you can inspect or mutate it.",
            "task": "Grab `#hero` using `document.querySelector('#hero')` and store in `const el`.",
            "starter": "<h1 id=\"hero\">CodeQuest</h1>\n<script>\n// Select #hero\n</script>",
            "solution": "<h1 id=\"hero\">CodeQuest</h1>\n<script>\nconst el = document.querySelector('#hero');\n</script>",
            "tests": [{"id": "t1", "desc": "el points to #hero element", "type": "js_eval", "expr": "el && el.id === 'hero'"}],
            "hints": ["Write const el = document.querySelector('#hero');"]
        },
        {
            "order": 5, "slug": "dom-text-content", "title": "05. DOM Text Mutation (textContent)",
            "minutes": 4, "xp": 50, "type": "IFRAME",
            "body": "`element.textContent` sets or retrieves text content safely without interpreting HTML tags, protecting against XSS vulnerabilities.",
            "task": "Select `#status` and change its `textContent` to 'Ready to Code'.",
            "starter": "<span id=\"status\">Loading...</span>\n<script>\n// Update textContent\n</script>",
            "solution": "<span id=\"status\">Loading...</span>\n<script>\ndocument.querySelector('#status').textContent = 'Ready to Code';\n</script>",
            "tests": [{"id": "t1", "desc": "#status contains 'Ready to Code'", "type": "dom_text", "query": "#status", "val": "Ready to Code"}],
            "hints": ["Use document.querySelector('#status').textContent = 'Ready to Code';"]
        },
    ]

def get_python_lessons():
    return [
        {
            "order": 1, "slug": "print-syntax", "title": "01. Print & Standard Output",
            "minutes": 3, "xp": 40, "type": "PYODIDE",
            "body": "Python uses `print()` to send output to the console. Strings can be enclosed in single or double quotes.\n\n```python\nprint('Hello, CodeQuest!')\n```",
            "task": "Write a `print()` call outputting 'Hello, World!'.",
            "starter": "# Output Hello, World!\n",
            "solution": "print('Hello, World!')",
            "tests": [{"id": "t1", "desc": "Outputs 'Hello, World!'", "type": "stdout_match", "val": "Hello, World!"}],
            "hints": ["Write print('Hello, World!')"]
        },
        {
            "order": 2, "slug": "variables-math", "title": "02. Variables & Arithmetic",
            "minutes": 4, "xp": 45, "type": "PYODIDE",
            "body": "Variables are declared by assignment without explicit type declarations: `score = 100`. Python supports arithmetic operators: `+`, `-`, `*`, `/`, and integer division `//`.",
            "task": "Create `points = 50 * 2` and print `points`.",
            "starter": "# Calculate and print points\n",
            "solution": "points = 50 * 2\nprint(points)",
            "tests": [{"id": "t1", "desc": "Prints 100", "type": "stdout_match", "val": "100"}],
            "hints": ["Assign points = 50 * 2, then print(points)."]
        },
        {
            "order": 3, "slug": "range-loops", "title": "03. The range() Loop",
            "minutes": 4, "xp": 50, "type": "PYODIDE",
            "body": "Python's `for i in range(N):` iterates $0, 1, ..., N-1$. Code blocks are defined with a 4-space indentation rather than braces.",
            "task": "Write a `for i in range(4):` loop that prints `i`.",
            "starter": "# Loop 4 times\n",
            "solution": "for i in range(4):\n    print(i)",
            "tests": [{"id": "t1", "desc": "Outputs numbers 0, 1, 2, 3", "type": "stdout_contains", "val": "0\n1\n2\n3"}],
            "hints": ["Indent print(i) inside for i in range(4):"]
        },
        {
            "order": 4, "slug": "list-comprehensions", "title": "04. List Comprehensions",
            "minutes": 5, "xp": 60, "type": "PYODIDE",
            "body": "List comprehensions offer concise syntax to generate lists: `[x * 2 for x in numbers]` creates a new list without an explicit `.append()` loop.",
            "task": "Create `squares = [x**2 for x in range(5)]` and print it.",
            "starter": "# Generate squares of 0..4\n",
            "solution": "squares = [x**2 for x in range(5)]\nprint(squares)",
            "tests": [{"id": "t1", "desc": "Prints [0, 1, 4, 9, 16]", "type": "stdout_match", "val": "[0, 1, 4, 9, 16]"}],
            "hints": ["Use [x**2 for x in range(5)]"]
        },
    ]

def get_sql_lessons():
    return [
        {
            "order": 1, "slug": "select-all", "title": "01. Basic SELECT Query",
            "minutes": 4, "xp": 45, "type": "SQL",
            "body": "`SELECT * FROM table;` retrieves all columns and all rows from a relational table.",
            "task": "Write a query to read all columns from `users` table.",
            "starter": "-- Query all users\n",
            "solution": "SELECT * FROM users;",
            "tests": [{"id": "t1", "desc": "Query starts with SELECT * FROM users", "type": "sql_query_match", "val": "SELECT * FROM users"}],
            "hints": ["Type SELECT * FROM users;"]
        },
        {
            "order": 2, "slug": "where-filter", "title": "02. Row Filtering (WHERE)",
            "minutes": 4, "xp": 50, "type": "SQL",
            "body": "The `WHERE` clause filters rows based on a boolean condition: `WHERE status = 'ACTIVE'`.",
            "task": "Select all columns from `users` where `role = 'admin'`.",
            "starter": "-- Select admin users\n",
            "solution": "SELECT * FROM users WHERE role = 'admin';",
            "tests": [{"id": "t1", "desc": "Has WHERE role = 'admin'", "type": "sql_query_contains", "val": "WHERE role = 'admin'"}],
            "hints": ["Add WHERE role = 'admin';"]
        },
    ]
