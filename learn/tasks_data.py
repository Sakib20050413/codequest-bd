# CodeQuest BD — Curated Practical Coding Tasks & Problem Sets (28 Real-World Industry Specifications)

CODING_TASKS = [
  {
    "id": "task-01",
    "cat": "frontend",
    "cat_label": "Frontend Web",
    "diff": "easy",
    "diff_label": "Easy",
    "xp": 60,
    "time": "10m",
    "title": "Accessible Navbar with Mobile Off-Canvas Drawer",
    "desc": "Build a responsive semantic navigation header that collapses into an off-canvas drawer on mobile screens with ARIA landmarks and focus management.",
    "criteria": [
      "Semantic <header> and <nav> with aria-label",
      "CSS media query breakpoint at 768px",
      "JavaScript click listener toggling aria-expanded state"
    ],
    "tags": [
      "SemanticHTML",
      "CSSFlexbox",
      "A11y",
      "VanillaJS"
    ],
    "starter": "<!-- HTML Structure -->\\n<header class=\\\"site-header\\\">\\n  <nav class=\\\"main-nav\\\" aria-label=\\\"Primary Navigation\\\">\\n    <a href=\\\"#\\\" class=\\\"brand\\\">Logo</a>\\n    <button id=\\\"mobileToggle\\\" aria-expanded=\\\"false\\\">Menu</button>\\n    <ul id=\\\"navMenu\\\" class=\\\"nav-links\\\">\\n      <li><a href=\\\"#home\\\">Home</a></li>\\n      <li><a href=\\\"#courses\\\">Courses</a></li>\\n    </ul>\\n  </nav>\\n</header>",
    "tests": "Assert <header> exists\\nAssert #mobileToggle has aria-expanded='false'\\nAssert clicking #mobileToggle updates aria-expanded to 'true'"
  },
  {
    "id": "task-02",
    "cat": "frontend",
    "cat_label": "Frontend Web",
    "diff": "easy",
    "diff_label": "Easy",
    "xp": 50,
    "time": "10m",
    "title": "Responsive 3-Tier SaaS Pricing Matrix",
    "desc": "Construct a responsive 3-column pricing grid featuring distinct plan tiers, visual hierarchy on the popular tier, and interactive plan selection.",
    "criteria": [
      "CSS Grid repeat(auto-fit, minmax(280px, 1fr))",
      "Highlighted 'Popular' tier with accent border & badge",
      "Focus-visible keyboard accessible CTA buttons"
    ],
    "tags": [
      "CSSGrid",
      "ResponsiveDesign",
      "SaaSUX"
    ],
    "starter": "<div class=\\\"pricing-grid\\\">\\n  <div class=\\\"plan-card\\\">Starter - $9</div>\\n  <div class=\\\"plan-card featured\\\">Pro - $29 (Popular)</div>\\n  <div class=\\\"plan-card\\\">Enterprise - $99</div>\\n</div>",
    "tests": "Assert 3 plan cards present\\nAssert .featured has distinct border or badge\\nAssert responsive scaling on mobile viewport"
  },
  {
    "id": "task-03",
    "cat": "frontend",
    "cat_label": "Frontend Web",
    "diff": "medium",
    "diff_label": "Medium",
    "xp": 80,
    "time": "15m",
    "title": "Stateful Todo App with LocalStorage & Filters",
    "desc": "Create a task manager component in vanilla JavaScript that saves items to window.localStorage, supports completion toggles, and filters by Active/Completed.",
    "criteria": [
      "Serializes tasks to window.localStorage as JSON",
      "Event delegation on parent <ul> for click & delete",
      "Tab filter state updates DOM without page refresh"
    ],
    "tags": [
      "DOMState",
      "LocalStorage",
      "EventDelegation"
    ],
    "starter": "function saveTodos(todos) {\\n  localStorage.setItem('cq_todos', JSON.stringify(todos));\\n}\\n\\nfunction loadTodos() {\\n  return JSON.parse(localStorage.getItem('cq_todos') || '[]');\\n}",
    "tests": "Assert todo adds to localStorage\\nAssert toggle changes completed property\\nAssert filter displays matching items"
  },
  {
    "id": "task-04",
    "cat": "frontend",
    "cat_label": "Frontend Web",
    "diff": "medium",
    "diff_label": "Medium",
    "xp": 85,
    "time": "15m",
    "title": "Debounced Live Search & Query Highlighter",
    "desc": "Implement an input listener that delays execution by 300ms using a debounce closure, filters client-side data, and highlights matched text substrings.",
    "criteria": [
      "Custom debounce(fn, delay) utility",
      "Case-insensitive substring matching",
      "Wraps query matches in <mark> tags dynamically"
    ],
    "tags": [
      "Performance",
      "Debounce",
      "RegexHighlight"
    ],
    "starter": "function debounce(fn, delay) {\\n  let timer;\\n  return function (...args) {\\n    clearTimeout(timer);\\n    timer = setTimeout(() => fn.apply(this, args), delay);\\n  };\\n}",
    "tests": "Assert fn only fires once within 300ms\\nAssert matched text contains <mark> tags\\nAssert empty query restores original list"
  },
  {
    "id": "task-05",
    "cat": "frontend",
    "cat_label": "Frontend Web",
    "diff": "easy",
    "diff_label": "Easy",
    "xp": 60,
    "time": "10m",
    "title": "Theme Switcher Engine with CSS Custom Variables",
    "desc": "Author a dark/light mode toggle that swaps [data-theme] attributes on document.documentElement, updates ARIA labels, and persists to localStorage.",
    "criteria": [
      "Root variables defined for --bg-surface and --text-primary",
      "Reads existing setting on page load with fallback",
      "Updates aria-label for screen reader accessibility"
    ],
    "tags": [
      "CSSVariables",
      "ThemeEngine",
      "A11yContrast"
    ],
    "starter": "function toggleTheme() {\\n  const curr = document.documentElement.getAttribute('data-theme') || 'dark';\\n  const next = curr === 'dark' ? 'light' : 'dark';\\n  document.documentElement.setAttribute('data-theme', next);\\n  localStorage.setItem('theme', next);\\n}",
    "tests": "Assert data-theme toggles between 'dark' and 'light'\\nAssert localStorage receives saved theme\\nAssert contrast passes WCAG AA"
  },
  {
    "id": "task-06",
    "cat": "frontend",
    "cat_label": "Frontend Web",
    "diff": "medium",
    "diff_label": "Medium",
    "xp": 80,
    "time": "15m",
    "title": "Form Validator with Real-Time Accessibility Errors",
    "desc": "Build an authentication form with email regex validation, password length checks, and accessible inline aria-live error announcements.",
    "criteria": [
      "RFC-compliant email pattern validation",
      "Minimum 8 characters with at least one number",
      "Displays error text linked via aria-describedby"
    ],
    "tags": [
      "FormValidation",
      "Regex",
      "A11yForms"
    ],
    "starter": "function validateEmail(email) {\\n  return /^[^\\\\s@]+@[^\\\\s@]+\\\\.[^\\\\s@]+$/.test(email);\\n}\\nfunction validatePassword(pass) {\\n  return pass.length >= 8 && /\\\\d/.test(pass);\\n}",
    "tests": "Assert invalid email shows error message\\nAssert short password fails validation\\nAssert valid credentials allow submission"
  },
  {
    "id": "task-07",
    "cat": "frontend",
    "cat_label": "Frontend Web",
    "diff": "medium",
    "diff_label": "Medium",
    "xp": 90,
    "time": "15m",
    "title": "Accessible Modal Dialog with Focus Trap & ESC Key",
    "desc": "Create a reusable modal component that traps keyboard Tab navigation within dialog bounds, closes on Escape, and restores previous activeElement.",
    "criteria": [
      "Traps Tab / Shift+Tab within focusable elements",
      "Keydown listener for Escape key dismissal",
      "Restores trigger button focus upon dialog close"
    ],
    "tags": [
      "A11yWCAG",
      "FocusTrap",
      "KeyboardNav"
    ],
    "starter": "function trapFocus(modalElement) {\\n  const focusables = modalElement.querySelectorAll('button, [href], input');\\n  const first = focusables[0];\\n  const last = focusables[focusables.length - 1];\\n  // Trap tab loop logic\\n}",
    "tests": "Assert modal has role='dialog'\\nAssert Escape key closes modal\\nAssert focus is trapped within modal boundaries"
  },
  {
    "id": "task-08",
    "cat": "frontend",
    "cat_label": "Frontend Web",
    "diff": "hard",
    "diff_label": "Hard",
    "xp": 120,
    "time": "20m",
    "title": "Drag-and-Drop Kanban Board with Native HTML5 DnD",
    "desc": "Implement a 3-column Kanban workflow board where tasks can be dragged and dropped between Todo, In-Progress, and Done columns with visual drop target styling.",
    "criteria": [
      "Native dragstart, dragover, drop, and dragend handlers",
      "Highlights receiving column during dragover",
      "Updates card DOM hierarchy and status attribute"
    ],
    "tags": [
      "HTML5DnD",
      "KanbanUX",
      "InteractiveDOM"
    ],
    "starter": "card.addEventListener('dragstart', (e) => {\\n  e.dataTransfer.setData('text/plain', card.id);\\n});\\n\\ncolumn.addEventListener('dragover', (e) => e.preventDefault());\\ncolumn.addEventListener('drop', (e) => {\\n  const id = e.dataTransfer.getData('text/plain');\\n  column.appendChild(document.getElementById(id));\\n});",
    "tests": "Assert card transfers to target column on drop\\nAssert drop target displays active hover style\\nAssert preventDefault called on dragover"
  },
  {
    "id": "task-09",
    "cat": "algorithms",
    "cat_label": "Algorithms",
    "diff": "easy",
    "diff_label": "Easy",
    "xp": 50,
    "time": "10m",
    "title": "Two-Sum Target Finder in Linear O(n) Time",
    "desc": "Given an array of integers and a target sum, return indices of the two numbers that add up to target in strictly linear O(n) time using a hash map.",
    "criteria": [
      "Linear O(n) time complexity",
      "Single-pass hash table compliment lookup",
      "Handles negative numbers, zeroes, and duplicate values"
    ],
    "tags": [
      "HashMap",
      "Arrays",
      "LinearTime"
    ],
    "starter": "def two_sum(nums, target):\\n    seen = {}\\n    for i, num in enumerate(nums):\\n        comp = target - num\\n        if comp in seen:\\n            return [seen[comp], i]\\n        seen[num] = i\\n    return []",
    "tests": "two_sum([2, 7, 11, 15], 9) -> [0, 1]\\ntwo_sum([3, 2, 4], 6) -> [1, 2]\\ntwo_sum([3, 3], 6) -> [0, 1]"
  },
  {
    "id": "task-10",
    "cat": "algorithms",
    "cat_label": "Algorithms",
    "diff": "easy",
    "diff_label": "Easy",
    "xp": 60,
    "time": "10m",
    "title": "Balanced Parentheses & Brackets Stack Evaluator",
    "desc": "Given a string containing '(', ')', '{', '}', '[' and ']', determine if the input string is valid and properly closed in correct chronological order.",
    "criteria": [
      "LIFO stack implementation",
      "Early false return on unmatched closing token",
      "O(n) time complexity and O(n) space complexity"
    ],
    "tags": [
      "StackDataStructure",
      "StringParsing",
      "SyntaxValidation"
    ],
    "starter": "def is_valid_brackets(s: str) -> bool:\\n    pairs = {')': '(', '}': '{', ']': '['}\\n    stack = []\\n    for char in s:\\n        if char in pairs.values():\\n            stack.append(char)\\n        elif char in pairs:\\n            if not stack or stack.pop() != pairs[char]:\\n                return False\\n    return len(stack) == 0",
    "tests": "is_valid_brackets('()[]{}') -> True\\nis_valid_brackets('(]') -> False\\nis_valid_brackets('([{}])') -> True"
  },
  {
    "id": "task-11",
    "cat": "algorithms",
    "cat_label": "Algorithms",
    "diff": "hard",
    "diff_label": "Hard",
    "xp": 150,
    "time": "25m",
    "title": "LRU (Least Recently Used) Cache with Doubly Linked List",
    "desc": "Design a memory cache following the LRU eviction policy with get(key) and put(key, value) operating in strictly O(1) constant time complexity.",
    "criteria": [
      "O(1) time complexity for get and put",
      "Hash Map paired with Doubly Linked List",
      "Evicts oldest accessed entry when capacity is exceeded"
    ],
    "tags": [
      "LRUCache",
      "DoublyLinkedList",
      "SystemDesign"
    ],
    "starter": "class Node:\\n    def __init__(self, key, val):\\n        self.key, self.val = key, val\\n        self.prev = self.next = None\\n\\nclass LRUCache:\\n    def __init__(self, capacity: int):\\n        self.cap = capacity\\n        self.map = {}\\n        self.head, self.tail = Node(0, 0), Node(0, 0)\\n        self.head.next = self.tail\\n        self.tail.prev = self.head",
    "tests": "cache = LRUCache(2)\\ncache.put(1, 1); cache.put(2, 2)\\ncache.get(1) -> 1\\ncache.put(3, 3) # evicts key 2\\ncache.get(2) -> -1"
  },
  {
    "id": "task-12",
    "cat": "algorithms",
    "cat_label": "Algorithms",
    "diff": "medium",
    "diff_label": "Medium",
    "xp": 90,
    "time": "15m",
    "title": "Merge Overlapping Calendar Intervals",
    "desc": "Given an array of meeting time intervals [start, end], merge all overlapping intervals into mutually exclusive contiguous slots.",
    "criteria": [
      "Sorts intervals by start time in O(n log n)",
      "Single-pass linear merge loop",
      "Correctly handles adjacent boundary times"
    ],
    "tags": [
      "Intervals",
      "Sorting",
      "GreedyAlgorithm"
    ],
    "starter": "def merge_intervals(intervals):\\n    if not intervals: return []\\n    intervals.sort(key=lambda x: x[0])\\n    merged = [intervals[0]]\\n    for curr in intervals[1:]:\\n        prev = merged[-1]\\n        if curr[0] <= prev[1]:\\n            prev[1] = max(prev[1], curr[1])\\n        else:\\n            merged.append(curr)\\n    return merged",
    "tests": "merge([[1,3],[2,6],[8,10],[15,18]]) -> [[1,6],[8,10],[15,18]]\\nmerge([[1,4],[4,5]]) -> [[1,5]]"
  },
  {
    "id": "task-13",
    "cat": "algorithms",
    "cat_label": "Algorithms",
    "diff": "medium",
    "diff_label": "Medium",
    "xp": 75,
    "time": "15m",
    "title": "Anagram Grouping & Frequency Vector Engine",
    "desc": "Group an array of arbitrary strings into sub-lists of anagrams where each group shares identical character frequencies.",
    "criteria": [
      "Character frequency count tuple keying",
      "Groups matching words into hash table lists",
      "Handles empty strings and single characters"
    ],
    "tags": [
      "Strings",
      "Anagrams",
      "FrequencyVector"
    ],
    "starter": "from collections import defaultdict\\n\\ndef group_anagrams(words):\\n    ans = defaultdict(list)\\n    for word in words:\\n        count = [0] * 26\\n        for c in word:\\n            count[ord(c) - ord('a')] += 1\\n        ans[tuple(count)].append(word)\\n    return list(ans.values())",
    "tests": "group_anagrams(['eat','tea','tan','ate','nat','bat']) -> [['eat','tea','ate'],['tan','nat'],['bat']]"
  },
  {
    "id": "task-14",
    "cat": "algorithms",
    "cat_label": "Algorithms",
    "diff": "medium",
    "diff_label": "Medium",
    "xp": 90,
    "time": "15m",
    "title": "Binary Search in a Rotated Sorted Array",
    "desc": "Find the index of a target value in an array sorted in ascending order but rotated at an unknown pivot index in strictly logarithmic O(log n) time.",
    "criteria": [
      "Logarithmic O(log n) runtime",
      "Determines whether left or right half is cleanly sorted",
      "Returns -1 if target is not found in array"
    ],
    "tags": [
      "BinarySearch",
      "DivideAndConquer",
      "Logarithmic"
    ],
    "starter": "def search_rotated(nums, target):\\n    low, high = 0, len(nums) - 1\\n    while low <= high:\\n        mid = (low + high) // 2\\n        if nums[mid] == target: return mid\\n        if nums[low] <= nums[mid]:\\n            if nums[low] <= target < nums[mid]: high = mid - 1\\n            else: low = mid + 1\\n        else:\\n            if nums[mid] < target <= nums[high]: low = mid + 1\\n            else: high = mid - 1\\n    return -1",
    "tests": "search_rotated([4,5,6,7,0,1,2], 0) -> 4\\nsearch_rotated([4,5,6,7,0,1,2], 3) -> -1"
  },
  {
    "id": "task-15",
    "cat": "algorithms",
    "cat_label": "Algorithms",
    "diff": "hard",
    "diff_label": "Hard",
    "xp": 130,
    "time": "20m",
    "title": "Deep Object Clone with Circular Reference Guard",
    "desc": "Implement a recursive deep clone function in JavaScript that handles nested objects, arrays, Dates, RegExps, and guards against circular references via WeakMap.",
    "criteria": [
      "Handles nested arrays, plain objects, and primitive values",
      "Guards circular references using a WeakMap memo cache",
      "Preserves RegExp and Date instance prototypes"
    ],
    "tags": [
      "DeepClone",
      "WeakMap",
      "Recursion"
    ],
    "starter": "function deepClone(obj, hash = new WeakMap()) {\\n  if (Object(obj) !== obj) return obj;\\n  if (hash.has(obj)) return hash.get(obj);\\n  const result = Array.isArray(obj) ? [] : {};\\n  hash.set(obj, result);\\n  for (const key of Object.keys(obj)) {\\n    result[key] = deepClone(obj[key], hash);\\n  }\\n  return result;\\n}",
    "tests": "Assert nested properties are cloned by value\\nAssert mutating clone does not affect original\\nAssert circular reference does not overflow stack"
  },
  {
    "id": "task-16",
    "cat": "algorithms",
    "cat_label": "Algorithms",
    "diff": "hard",
    "diff_label": "Hard",
    "xp": 140,
    "time": "20m",
    "title": "Promise.all & Promise.race Concurrency Polyfill",
    "desc": "Write custom polyfills for Promise.all and Promise.race from scratch without using the native built-in methods, preserving exact resolution ordering.",
    "criteria": [
      "Promise.all resolves only after all input promises resolve",
      "Preserves input index order in resolved output array",
      "Rejects immediately on the very first rejection"
    ],
    "tags": [
      "AsyncJS",
      "Promises",
      "Concurrency"
    ],
    "starter": "function promiseAll(promises) {\\n  return new Promise((resolve, reject) => {\\n    const results = [];\\n    let completed = 0;\\n    if (promises.length === 0) return resolve(results);\\n    promises.forEach((p, i) => {\\n      Promise.resolve(p).then((res) => {\\n        results[i] = res;\\n        completed++;\\n        if (completed === promises.length) resolve(results);\\n      }).catch(reject);\\n    });\\n  });\\n}",
    "tests": "Assert resolves array in exact order\\nAssert rejects on first reject\\nAssert handles non-promise values"
  },
  {
    "id": "task-17",
    "cat": "sql",
    "cat_label": "SQL Database",
    "diff": "easy",
    "diff_label": "Easy",
    "xp": 60,
    "time": "10m",
    "title": "Top 3 Highest Spending Customers via INNER JOIN",
    "desc": "Write an SQL query to join users and orders tables, calculate aggregate total spending per customer, and return the top 3 highest spenders.",
    "criteria": [
      "INNER JOIN users u ON u.id = o.user_id",
      "SUM(o.amount) aggregate aliased as total_spent",
      "ORDER BY total_spent DESC LIMIT 3"
    ],
    "tags": [
      "InnerJoin",
      "Aggregation",
      "TopNQuery"
    ],
    "starter": "SELECT u.id, u.name, SUM(o.amount) AS total_spent\\nFROM users u\\nINNER JOIN orders o ON u.id = o.user_id\\nGROUP BY u.id, u.name\\nORDER BY total_spent DESC\\nLIMIT 3;",
    "tests": "Assert exactly 3 rows returned\\nAssert total_spent sorted descending\\nAssert only users with orders are present"
  },
  {
    "id": "task-18",
    "cat": "sql",
    "cat_label": "SQL Database",
    "diff": "medium",
    "diff_label": "Medium",
    "xp": 90,
    "time": "15m",
    "title": "Monthly Active Users (MAU) & Retention Aggregator",
    "desc": "Calculate the count of distinct active users per calendar month, grouping by DATE_TRUNC('month', activity_date) with month-over-month active delta.",
    "criteria": [
      "DATE_TRUNC or strftime month grouping",
      "COUNT(DISTINCT user_id) active calculation",
      "Sorted chronologically by month"
    ],
    "tags": [
      "AnalyticsSQL",
      "DateTrunc",
      "CohortAnalysis"
    ],
    "starter": "SELECT strftime('%Y-%m', activity_date) AS active_month,\\n       COUNT(DISTINCT user_id) AS mau\\nFROM user_logins\\nGROUP BY active_month\\nORDER BY active_month ASC;",
    "tests": "Assert grouped by month string YYYY-MM\\nAssert distinct users count accurate\\nAssert ordered chronologically"
  },
  {
    "id": "task-19",
    "cat": "sql",
    "cat_label": "SQL Database",
    "diff": "medium",
    "diff_label": "Medium",
    "xp": 85,
    "time": "15m",
    "title": "Deduplicate Customer Records Retaining Minimum ID",
    "desc": "Identify all duplicate email addresses in a customer database, and draft a query that removes duplicate rows while preserving the row with the lowest id.",
    "criteria": [
      "Identifies emails where COUNT(*) > 1 via HAVING",
      "Filters WHERE id NOT IN (SELECT MIN(id) GROUP BY email)",
      "Safely deletes duplicate records"
    ],
    "tags": [
      "DataCleaning",
      "Subqueries",
      "HavingClause"
    ],
    "starter": "DELETE FROM customers\\nWHERE id NOT IN (\\n    SELECT MIN(id)\\n    FROM customers\\n    GROUP BY email\\n);",
    "tests": "Assert unique email constraint holds after execution\\nAssert lowest IDs are preserved\\nAssert total deleted count matches duplicates"
  },
  {
    "id": "task-20",
    "cat": "sql",
    "cat_label": "SQL Database",
    "diff": "medium",
    "diff_label": "Medium",
    "xp": 95,
    "time": "15m",
    "title": "Department Salary Rank via DENSE_RANK()",
    "desc": "Assign a dense ranking to employees within their respective departments ordered by salary descending without leaving gaps in the ranking order.",
    "criteria": [
      "Uses DENSE_RANK() window function",
      "PARTITION BY department_id",
      "ORDER BY salary DESC"
    ],
    "tags": [
      "WindowFunctions",
      "DenseRank",
      "PartitionBy"
    ],
    "starter": "SELECT employee_id, department_id, salary,\\n       DENSE_RANK() OVER (\\n           PARTITION BY department_id\\n           ORDER BY salary DESC\\n       ) AS salary_rank\\nFROM employees;",
    "tests": "Assert salary_rank resets per department_id\\nAssert tied salaries share rank without skipping numbers\\nAssert ordered from highest to lowest salary"
  },
  {
    "id": "task-21",
    "cat": "sql",
    "cat_label": "SQL Database",
    "diff": "easy",
    "diff_label": "Easy",
    "xp": 55,
    "time": "10m",
    "title": "Detect Inactive Customers via LEFT JOIN WHERE NULL",
    "desc": "Find all registered customers who have never placed an order by performing a LEFT JOIN between customers and orders, filtering for NULL foreign keys.",
    "criteria": [
      "LEFT JOIN orders o ON c.id = o.customer_id",
      "WHERE o.id IS NULL clause",
      "Returns customer_id, name, and registered_at"
    ],
    "tags": [
      "LeftJoin",
      "NullFiltering",
      "OrphanRecords"
    ],
    "starter": "SELECT c.id, c.name, c.email\\nFROM customers c\\nLEFT JOIN orders o ON c.id = o.customer_id\\nWHERE o.id IS NULL;",
    "tests": "Assert customers with orders are excluded\\nAssert only zero-order customers returned\\nAssert handles empty orders table"
  },
  {
    "id": "task-22",
    "cat": "sql",
    "cat_label": "SQL Database",
    "diff": "hard",
    "diff_label": "Hard",
    "xp": 110,
    "time": "20m",
    "title": "Cumulative Running Revenue with Window Partitioning",
    "desc": "Compute a cumulative running revenue balance across chronological transaction dates using an unbounded preceding window frame specification.",
    "criteria": [
      "SUM(amount) OVER (ORDER BY trans_date)",
      "ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW",
      "Calculates cumulative ledger balance"
    ],
    "tags": [
      "CumulativeSum",
      "WindowFrames",
      "FinancialSQL"
    ],
    "starter": "SELECT trans_date, amount,\\n       SUM(amount) OVER (\\n           ORDER BY trans_date\\n           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW\\n       ) AS running_total\\nFROM transactions;",
    "tests": "Assert running_total accumulates monotonically on positive amounts\\nAssert final row equals sum of all amounts"
  },
  {
    "id": "task-23",
    "cat": "systems",
    "cat_label": "Systems & C",
    "diff": "medium",
    "diff_label": "Medium",
    "xp": 80,
    "time": "15m",
    "title": "In-Place String Reversal Using Raw Pointer Arithmetic",
    "desc": "Reverse a null-terminated C string in-place without allocating auxiliary heap memory, advancing left and right pointer addresses until convergence.",
    "criteria": [
      "Two-pointer address swap arithmetic",
      "Zero auxiliary dynamic allocation (O(1) memory)",
      "Preserves terminal null byte '\\0'"
    ],
    "tags": [
      "Pointers",
      "CStrings",
      "InPlaceSwap"
    ],
    "starter": "void reverse_string(char *str) {\\n    if (!str) return;\\n    char *end = str;\\n    while (*end) end++;\\n    end--;\\n    while (str < end) {\\n        char temp = *str;\\n        *str++ = *end;\\n        *end-- = temp;\\n    }\\n}",
    "tests": "reverse_string('hello') -> 'olleh'\\nreverse_string('a') -> 'a'\\nreverse_string('') -> ''"
  },
  {
    "id": "task-24",
    "cat": "systems",
    "cat_label": "Systems & C",
    "diff": "easy",
    "diff_label": "Easy",
    "xp": 65,
    "time": "10m",
    "title": "Bitwise Permissions Mask (Read / Write / Exec)",
    "desc": "Implement a Unix-style file permission validator (READ=4, WRITE=2, EXEC=1) using bitwise AND (&), OR (|), and XOR (^) operators.",
    "criteria": [
      "Bit flag constants (1 << 2, 1 << 1, 1 << 0)",
      "Bitwise & check for permission verification",
      "Bitwise | and ~ for adding and revoking flags"
    ],
    "tags": [
      "BitwiseOperators",
      "BitMasks",
      "UnixPermissions"
    ],
    "starter": "#define PERM_READ  (1 << 2) // 4\\n#define PERM_WRITE (1 << 1) // 2\\n#define PERM_EXEC  (1 << 0) // 1\\n\\nint has_permission(int mask, int perm) {\\n    return (mask & perm) == perm;\\n}",
    "tests": "has_permission(7, PERM_READ) -> 1\\nhas_permission(3, PERM_READ) -> 0\\nhas_permission(6, PERM_WRITE) -> 1"
  },
  {
    "id": "task-25",
    "cat": "systems",
    "cat_label": "Systems & C",
    "diff": "hard",
    "diff_label": "Hard",
    "xp": 150,
    "time": "25m",
    "title": "Custom Dynamic Memory Pool Allocator (Malloc/Free)",
    "desc": "Build a static memory chunk allocator maintaining linked header blocks, chunk size metadata, allocation flags, and adjacent block coalescing.",
    "criteria": [
      "Header block structure containing size and is_free flag",
      "First-fit free block scanning strategy",
      "Coalesces adjacent free chunks upon free() execution"
    ],
    "tags": [
      "MemoryManagement",
      "MallocFree",
      "SystemsArchitecture"
    ],
    "starter": "typedef struct Block {\\n    size_t size;\\n    int is_free;\\n    struct Block *next;\\n} Block;\\n\\nstatic char memory_pool[1024 * 64]; // 64KB static pool\\n// Allocator implementation",
    "tests": "Assert pool allocates block of requested size\\nAssert freeing block marks is_free=1\\nAssert adjacent free blocks merge"
  },
  {
    "id": "task-26",
    "cat": "systems",
    "cat_label": "Systems & C",
    "diff": "medium",
    "diff_label": "Medium",
    "xp": 90,
    "time": "15m",
    "title": "Stack Frame & Activation Record Tracing Engine",
    "desc": "Trace the growth of the call stack during deep recursion, inspecting base pointer frame offsets and triggering early guards to prevent stack overflow.",
    "criteria": [
      "Monitors recursion call stack depth counter",
      "Calculates stack address growth direction",
      "Guards recursion ceiling threshold"
    ],
    "tags": [
      "CallStack",
      "StackFrames",
      "RecursionGuard"
    ],
    "starter": "void trace_stack(int depth, void *parent_addr) {\\n    int local_var = 42;\\n    printf(\\\"Depth %d | Stack Addr: %p | Delta: %ld\\\\n\\\",\\n           depth, (void*)&local_var, (char*)parent_addr - (char*)&local_var);\\n    if (depth < 5) trace_stack(depth + 1, (void*)&local_var);\\n}",
    "tests": "Assert stack grows downwards on x86_64\\nAssert depth ceiling halts execution safely"
  },
  {
    "id": "task-27",
    "cat": "systems",
    "cat_label": "Systems & C",
    "diff": "easy",
    "diff_label": "Easy",
    "xp": 55,
    "time": "10m",
    "title": "Bash Log Pipeline: Grep, Filter & Frequency Counter",
    "desc": "Construct a Unix command-line pipeline that parses a web server access.log, filters all HTTP 500 status codes, and prints a ranked top-10 offending IP list.",
    "criteria": [
      "Chains grep ' 500 ' | awk '{print $1}' | sort | uniq -c",
      "Sorts output descending by frequency count (sort -nr)",
      "Limits output to top 10 offending IPs (head -n 10)"
    ],
    "tags": [
      "BashPipeline",
      "UnixCli",
      "LogAnalysis"
    ],
    "starter": "#!/usr/bin/env bash\\n# Parse access.log for 500 errors\\ngrep \\\" 500 \\\" access.log | awk '{print $1}' | sort | uniq -c | sort -nr | head -n 10",
    "tests": "Assert pipeline matches HTTP 500 patterns\\nAssert output is ranked by count descending\\nAssert exactly top 10 printed"
  },
  {
    "id": "task-28",
    "cat": "systems",
    "cat_label": "Systems & C",
    "diff": "hard",
    "diff_label": "Hard",
    "xp": 140,
    "time": "20m",
    "title": "Producer-Consumer Buffer with Mutex Synchronization",
    "desc": "Implement a circular queue buffer shared between producer and consumer threads, preventing race conditions and deadlocks using mutex locking.",
    "criteria": [
      "Circular queue bounded buffer of fixed size N",
      "Mutex lock guards buffer insertion and extraction",
      "Condition variables signal buffer-not-full and not-empty"
    ],
    "tags": [
      "Concurrency",
      "MutexLocks",
      "ProducerConsumer"
    ],
    "starter": "#define BUFFER_SIZE 8\\nint buffer[BUFFER_SIZE];\\nint count = 0, in = 0, out = 0;\\n// Thread synchronization primitives logic",
    "tests": "Assert items produced equal items consumed\\nAssert buffer never exceeds BUFFER_SIZE\\nAssert zero race conditions or deadlocks"
  }
]
