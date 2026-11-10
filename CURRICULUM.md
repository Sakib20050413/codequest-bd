# CodeQuest — Curriculum Structure (CURRICULUM.md)

Each lesson follows the **3–7 minute rule**:
1. **Explanation:** Under 150 words + 1 concrete diagram or mental model.
2. **Editor:** Lightweight CodeMirror 6 or sandboxed live editor.
3. **Auto-Checked Task:** 1–3 specific assertions that must pass.

---

## 1. Initial Launch Tracks (5 Full Tracks)

### Track 1: HTML5 (12 Lessons)
1. Semantic Page Skeleton (`<header>`, `<main>`, `<footer>`)
2. Headings and Text Hierarchy (`<h1>` to `<h6>`, `<p>`)
3. Hyperlinks and Target Attributes (`<a>`, `href`, `target="_blank"`)
4. Images and Accessibility (`<img>`, `src`, `alt`)
5. Unordered and Ordered Lists (`<ul>`, `<ol>`, `<li>`)
6. Table Foundations (`<table>`, `<tr>`, `<td>`, `<th>`)
7. Table Spanning (`colspan` & `rowspan`)
8. Form Inputs (`<input type="text|email|number">`)
9. Form Submission & Buttons (`<form>`, `<button type="submit">`)
10. Dropdowns & Selections (`<select>`, `<option>`)
11. Textarea and Labels (`<textarea>`, `<label for="...">`)
12. Semantic Audio & Video (`<audio>`, `<video>`)

### Track 2: CSS3 (12 Lessons)
1. CSS Selectors & Color Values (`color`, `background-color`)
2. The Box Model (`content`, `padding`, `border`, `margin`)
3. Typography & Google Fonts (`font-family`, `line-height`, `font-size`)
4. Display Types (`block`, `inline`, `inline-block`, `none`)
5. Flexbox 1: Container & Directions (`display: flex`, `flex-direction`)
6. Flexbox 2: Horizontal Justification (`justify-content`)
7. Flexbox 3: Vertical Alignment (`align-items`)
8. CSS Grid 1: Template Columns (`grid-template-columns: repeat(...)`)
9. CSS Grid 2: Gap & Alignment (`gap`, `place-items`)
10. Positioning: Relative & Absolute (`position: relative|absolute`, `top`, `left`)
11. Transitions & Pseudo-Classes (`:hover`, `:focus`, `transition`)
12. Responsive Design (`@media (max-width: 768px)`)

### Track 3: JavaScript ES6+ (15 Lessons)
1. Variables: `const` and `let`
2. Data Types: Strings, Numbers, Booleans
3. Template Literals (`${variable}`)
4. Conditional Statements (`if`, `else if`, `else`)
5. Array Basics (`push`, `pop`, index lookup)
6. Array Methods (`map`, `filter`, `forEach`)
7. Object Literals & Property Access
8. Functions & Arrow Syntax (`() => {}`)
9. DOM Selection (`document.querySelector`)
10. DOM Text & HTML Mutation (`textContent`, `innerHTML`)
11. Class Manipulation (`classList.add`, `classList.toggle`)
12. Event Listeners (`addEventListener('click', ...)`)
13. Form Input Handling (`input.value`)
14. JSON Parsing & Stringifying (`JSON.parse`, `JSON.stringify`)
15. Fetch API & Promises (`async/await`)

### Track 4: Python 3 (12 Lessons)
1. Printing & Basic Syntax (`print()`)
2. Variables & Type Casting (`int`, `str`, `float`)
3. Arithmetic & Modulo Operations
4. Conditionals & Logical Operators (`and`, `or`, `not`)
5. Lists & Indexing
6. The `range()` Loop (`for i in range(N):`)
7. `while` Loops & Break Guards
8. Functions & Return Values (`def`)
9. Dictionaries & Key-Value Pairs
10. String Methods (`strip`, `split`, `join`)
11. List Comprehensions (`[x for x in list]`)
12. File Operations (`with open(...) as f:`)

### Track 5: SQL & Relational Databases (8 Lessons)
1. Basic Querying (`SELECT * FROM table;`)
2. Column Selection & Renaming (`SELECT col AS alias`)
3. Row Filtering (`WHERE condition = 'value'`)
4. Sorting Results (`ORDER BY col DESC`)
5. Limiting Rows (`LIMIT N`)
6. Inserting Data (`INSERT INTO table VALUES (...)`)
7. Updating Records (`UPDATE table SET col = val WHERE ...`)
8. Deleting Rows (`DELETE FROM table WHERE ...`)

---

## 2. Advanced Language Stubs (Read & Predict Mode)
- **C:** Data types, pointers, loops, structs.
- **Java:** Class structure, methods, arrays, OOP.
- **PHP:** Server variables, basic arrays, `mysqli_connect`.
- **Bash:** Navigating directories (`cd`, `ls`), pipes (`|`), redirects (`>`).
