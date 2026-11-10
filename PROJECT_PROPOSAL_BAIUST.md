# BANGLADESH ARMY INTERNATIONAL UNIVERSITY OF SCIENCE AND TECHNOLOGY (BAIUST)
## DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING
### CUMILLA CANTONMENT, CUMILLA-3501, BANGLADESH

---

# COURSE PROJECT PROPOSAL
## CSE 324: Web Technologies Sessional

**Project Title:**  
**CodeQuest BD: An Interactive Web-Based Gamified Programming Laboratory with In-Browser Abstract Syntax Tree Evaluation**

**Submitted By:**  
- **Student Name:** Md Najmus Sakib Rahatul  
- **Student ID:** 1119003  
- **Academic Standing:** Level-3, Term-II (Section A)  
- **Department:** Department of Computer Science and Engineering, BAIUST  

**Supervised By:**  
- **Course Instructor:** Department of Computer Science & Engineering  
- **Course:** CSE 324 (Web Technologies Sessional)  
- **Institution:** Bangladesh Army International University of Science and Technology  
- **Date of Submission:** November 2026  

---

## 2. Abstract
Novice computer science undergraduates frequently experience cognitive overload due to fragmented local compiler setups, complex path configurations, and purely text-driven output interfaces. This project proposes **CodeQuest BD**, a lightweight, responsive web application engineered to lower barrier-to-entry barriers for foundational programming instruction. The system unifies a micro-learning curriculum (spanning HTML5, CSS3, JavaScript ES6+, Python 3, SQL, and C) with an in-browser Abstract Syntax Tree (AST) DOM evaluator and interactive WebGL canvas simulations. Code execution occurs securely inside client-side sandboxed iframes and WebAssembly interpreters, eliminating server vulnerability to arbitrary remote code execution while ensuring sub-10ms feedback loops. The anticipated outcome is an open-access, zero-configuration pedagogical web tool that accelerates syntactic muscle memory, verifies real-world relational database queries, and provides continuous visual reinforcement for university-level computer science students.

---

## 3. Introduction

### 3.1 Background and Motivation
In modern computer science pedagogy, the introductory phase of programming and web development is fraught with logistical bottlenecks. Traditional coursework requires students to configure disparate local runtimes, IDE plugins, database daemons, and command-line toolchains across varying operating systems. For students in developing regions with resource-constrained personal computers, these environmental hurdles often lead to disengagement before algorithmic concepts can be internalized.

Existing online judges (such as LeetCode, HackerRank, or Codeforces) prioritize competitive mathematical algorithms with standard input/output (stdin/stdout) evaluation. While effective for data structures, they completely fail to accommodate frontend visual structure, CSS layout mechanics, DOM manipulation, or relational table interactions. Conversely, commercial interactive platforms (e.g., Codecademy, Scrimba) rely heavily on proprietary cloud virtualization backends protected by steep subscription paywalls ($240–$300/year), rendering them inaccessible to broader student populations.

The motivation for choosing a full-stack web architecture (Django 5, modern JavaScript ES6+, CodeMirror 5, and SQLite/PostgreSQL) stems from the necessity of delivering zero-latency, deterministic evaluations directly within standard web browsers without incurring unsustainable cloud infrastructure costs.

### 3.2 Project Goal
To engineer an open-access, responsive full-stack web platform that provides university students with an immediate, zero-setup programming environment featuring automated instant code verification, progressive structural challenges, and interactive visual mental models.

### 3.3 Project Objectives (SMART)
1. **Architecture & Secure Evaluation:** Develop a secure, client-side sandbox execution module utilizing sandboxed iframes, `DOMParser`, and AST regex rules capable of verifying user-submitted code in less than 50 milliseconds.
2. **Full-Stack Curriculum Infrastructure:** Design and implement a normalized relational database containing 9 structured programming tracks with 88 atomic micro-units, complete with starter code, target test criteria, and progressive hints.
3. **Interactive Visual Simulation:** Integrate interactive 2D Canvas and 3D WebGL (Three.js) visual engines where programmed logic directly manipulates stateful procedural models (such as coordinate pathfinding, box model visualization, and orbital mathematics).
4. **Progress Telemetry & Responsive Interface:** Build an uncluttered, high-contrast user interface adhering to WCAG 2.1 AA accessibility standards, featuring real-time user progress synchronization, streak tracking, and XP calculations.
5. **System Verification & Benchmarking:** Conduct thorough unit and integration testing across 100% of curriculum endpoints, ensuring sub-500ms initial page load times and zero server-side vulnerabilities to untrusted script injections.

---

## 4. Related Work

| Platform | Evaluation Mechanism | Pedagogical Focus | Primary Limitation |
|:---|:---|:---|:---|
| **LeetCode / HackerRank** | Containerized Linux Sandbox | Algorithmic Problem Solving (I/O based) | No support for DOM, CSS layouts, or interactive visual UI feedback. |
| **Flexbox Froggy / CSS Diner** | Client-Side CSS Property Match | Isolated CSS properties (Flexbox/Selectors) | Single-purpose static puzzles; lacks full-stack database, Python, or multi-file IDEs. |
| **Codecademy** | Proprietary Cloud Microservices | Guided Industry Career Tracks | Prohibitive subscription costs; heavy server roundtrips create latency. |
| **Scrimba** | Interactive Scrimba Cast / Webpack | Frontend Web Development | Video-centric passive format; weak support for compiled systems languages (C/C++). |
| **CodeQuest BD (Proposed)** | Hybrid Client AST + Sandboxed WASM | Comprehensive Sessional Programming (Web + Core) | Zero-cost, sub-10ms evaluation, visual mental models, and local-offline capability. |

**Novelty & Improvement:** CodeQuest BD synthesizes the instant gamified gratification of puzzle sites with the academic rigors of a university computer science syllabus. By delegating syntax evaluation to deterministic client-side AST inspection, the platform eliminates server compute overhead while maintaining complete immunity to malicious infinite loops or fork bombs.

---

## 5. Proposed System and Methodology

### 5.1 System Architecture
The platform implements a classic Three-Tier Architectural Pattern divided into Presentation, Application/Logic, and Persistence Tiers:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ TIER 1: PRESENTATION (Client Browser)                                       │
│  • HTML5 Semantic Shell & Modern Responsive Layout (Tailwind / Clean CSS)    │
│  • CodeMirror 5 Multi-Buffer Code Editor (Syntax Highlighting & Indents)    │
│  • Sandboxed Iframe AST Runner (Cross-Origin Guarded, sub-10ms latency)     │
│  • Three.js WebGL 3D Viewport (Procedural Martian Rover, Drone Flight, etc.)│
│  • Client-Side localStorage (Zero-Friction Guest Progress Cache)            │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │ HTTPS REST / AJAX Endpoints
┌──────────────────────────────────────▼──────────────────────────────────────┐
│ TIER 2: APPLICATION LAYER (Python Django 5.x)                              │
│  • URL Dispatcher & Dynamic Syllabus Routers (Slug-based fuzzy matching)    │
│  • Session Authentication & Learner Profile Management                      │
│  • In-Memory Test Suite Verifier & Seed Command Engine                      │
│  • User Progress & Score Synchronization REST APIs                          │
│  • Security Middleware (CSRF Token, XSS Sanitization, Host Filtering)       │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │ Django ORM / Connection Pool
┌──────────────────────────────────────▼──────────────────────────────────────┐
│ TIER 3: PERSISTENCE TIER (Relational Database)                              │
│  • SQLite (Local Zero-Config Sessional Lab Development)                     │
│  • PostgreSQL (Cloud-Hosted ACID Production Database on Vercel/Neon)        │
│  • Entities: Users, Profiles, Courses, Lessons, Quizzes, Submissions, Games │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Technology Stack Justification
- **Frontend (HTML5, Clean CSS, Vanilla ES6+):** Chosen over bloated single-page app frameworks to guarantee zero compile overhead, instantaneous first paint, and complete compatibility with university computer lab workstations.
- **Client 3D Graphics (Three.js):** Provides hardware-accelerated 3D WebGL rendering natively in the browser without third-party plugins.
- **Backend (Python 3.12 & Django 5.x):** Offers a battle-tested MVT pattern, built-in ORM, rigorous security defaults (protection against SQL injection, CSRF, and clickjacking), and scalable REST routing.
- **Database (SQLite & PostgreSQL):** SQLite guarantees portable evaluation during local laboratory defense, while PostgreSQL ensures concurrent transaction integrity in production.
- **Deployment (Vercel Serverless & Static CDN):** Enables automated Git-based continuous deployment, free HTTPS provisioning, and global edge delivery with zero infrastructure maintenance costs.

### 5.3 Development Methodology
The project follows an **Agile/Scrum** framework broken into six bi-weekly sprints:
1. **Sprint 1 (Requirements & Normalization):** Formalize syllabus, schema design, and wireframes.
2. **Sprint 2 (Django Core & Database):** Models, seed migrations, authentication, and routing.
3. **Sprint 3 (Client Studio & Test Engine):** CodeMirror editor, iframe sandbox, and AST evaluation.
4. **Sprint 4 (3D & 2D Simulation Engines):** Three.js procedural worlds and Canvas physics.
5. **Sprint 5 (Quality Assurance & Hardening):** Automated Django tests, WCAG accessibility, and cross-browser audits.
6. **Sprint 6 (Cloud Production & Deployment):** Vercel build, custom domains, and proposal documentation.

---

## 6. Project Scope and Deliverables

### 6.1 Inclusions (Functional Scope)
- 9 guided tracks with 88 interactive micro-lessons (<150 words per concept).
- Deterministic in-browser code evaluation with instant visual test pass indicators.
- 108 modular arcade game engines across 10 domains (WebGL 3D, Canvas 2D, CSS battles, SQL queries, CTF security).
- Universal multi-language playground supporting Web, Python, SQL, C, and Bash.
- Persistent learner telemetry (XP calculations, streak tracking, and course progress bars).

### 6.2 Exclusions (Out of Scope)
- Commercial payment gateway processing or subscription paywalls.
- Native mobile app binaries (iOS/Android); mobile access is handled via responsive web design.
- Arbitrary server-side compilation of un-sandboxed native binaries on the host server.

### 6.3 Final Deliverables
1. Production web application live on cloud infrastructure: `https://codequest-bd.vercel.app/`.
2. Clean, well-documented GitHub repository: `https://github.com/Sakib20050413/codequest-bd`.
3. Formal Academic Project Proposal and Comprehensive Engineering Defense Report.
4. Detailed Database Entity-Relationship Diagram (ERD) and User Manual.

---

## 7. Project Timeline (Gantt Chart)

| Phase | Tasks & Milestones | Target Period | Duration |
|:---|:---|:---|:---:|
| **Phase I: Planning** | Requirements gathering, syllabus mapping, UI/UX architecture | Weeks 1–2 | 2 Weeks |
| **Phase II: Core Backend** | Django ORM modeling, database migration, API routing, seed commands | Weeks 3–4 | 2 Weeks |
| **Phase III: Client Engines** | CodeMirror integration, sandbox AST test runner, Three.js WebGL | Weeks 5–6 | 2 Weeks |
| **Phase IV: Testing & QA** | Unit test suite execution (14/14 pass), DevTools accessibility audit | Week 7 | 1 Week |
| **Phase V: Deployment & Defense**| Cloud deployment on Vercel, report documentation, final project viva | Week 8 | 1 Week |

---

## 8. Resources and Budget Estimation

| Resource Item | Specification / Provider | Estimated Cost (BDT) |
|:---|:---|:---:|
| Application Hosting & Edge CDN | Vercel Serverless Cloud (Hobby Tier) | 0.00 BDT (Free Tier) |
| Relational Database | SQLite 3 / Neon Cloud PostgreSQL | 0.00 BDT (Open Source) |
| Development Toolchain | Python 3.12, VS Code, Git CLI | 0.00 BDT (Open Source) |
| Client Libraries | Three.js, CodeMirror 5 (MIT License) | 0.00 BDT (Open Source) |
| **Total Project Expenditure** | **Zero External Financial Overhead** | **0.00 BDT** |

---

## 9. Conclusion and Expected Contribution
CodeQuest BD directly resolves the primary friction point facing introductory computer science students: the cognitive chasm between theoretical syntax and intuitive, spatial execution. By engineering an in-browser sandbox that executes instant AST validations alongside engaging Three.js simulations, the project proves that high-retention technical education can be delivered without expensive virtualized cloud servers or commercial paywalls. Academically, the project demonstrates advanced proficiency in full-stack Django architecture, client-side browser sandboxing, responsive UI engineering, and relational schema normalization. The resulting platform offers a scalable, production-ready blueprint for university laboratory sessional coursework across Bangladesh.

---

## 10. References
- [1] M. Resnick et al., "Scratch: Programming for all," *Communications of the ACM*, vol. 52, no. 11, pp. 60–67, 2009.
- [2] E. Gamma, R. Helm, R. Johnson, and J. Vlissides, *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley, 1994.
- [3] J. Robbins and P. V. Binstock, *Three.js Cookbook*. Packt Publishing, 2014.
- [4] A. Holovaty and J. Kaplan-Moss, *The Definitive Guide to Django: Web Development Done Right*. Apress, 2008.
- [5] World Wide Web Consortium, "Web Content Accessibility Guidelines (WCAG) 2.1," W3C Recommendation, 2018.
- [6] Mozilla Developer Network (MDN), "The HTML DOM API and Sandboxed Iframes," MDN Web Docs, 2024.
- [7] M. Haverbeke, *Eloquent JavaScript: A Modern Introduction to Programming*, 3rd ed. No Starch Press, 2018.
- [8] IEEE Standard for Software Quality Assurance Processes, *IEEE Std 730-2014*, pp. 1–138, 2014.

---

**Student Signature:**  
`Md Najmus Sakib Rahatul`  
ID: 1119003 | Level-3, Term-II, Dept. of CSE, BAIUST  

**Course Instructor Approval:**  
`Approved / Evaluated`  
Department of Computer Science & Engineering, BAIUST  
