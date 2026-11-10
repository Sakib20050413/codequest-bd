# CodeQuest — Design Language & Visual System (DESIGN.md)

## 1. Design Direction: Minimalist Modern LLM Aesthetic

Inspired by high-craft software tools (**Claude, Linear, Cursor, and Vercel**), CodeQuest rejects distracting rainbow gradients and gamified neon visual noise. Fun comes from smooth micro-interactions, high performance, and crystal-clear feedback.

---

## 2. Color Palette & Contrast Tokens

- **Strict AA Contrast Compliance:** Every foreground/background pair passes WCAG 2.1 AA (≥ 4.5:1 for body text, ≥ 3:1 for large headers).
- **One Primary Accent:**
  - Dark Mode: Emerald `#10b981` (clean, calming indicator of code success)
  - Light Mode: Emerald `#059669`
- **Neutral Backgrounds:**
  - **Dark Mode (Obsidian):** Canvas `#090a0f`, Panels `#11141d`, Borders `rgba(255, 255, 255, 0.08)`
  - **Light Mode (Warm Paper):** Canvas `#f7f6f2`, Panels `#ffffff`, Borders `rgba(15, 23, 42, 0.09)`

---

## 3. Typography Hierarchy

Maximum two typefaces across the entire application:
1. **Primary Interface:** `Inter` or `Plus Jakarta Sans` (400 regular, 500 medium, 600 semi-bold, 700 bold). Crisp letter-spacing `-0.012em`.
2. **Code & Telemetry:** `JetBrains Mono` (400 regular, 500 medium). Used for syntax, keybindings, coordinates, and inline code pills.

---

## 4. 3D Hero Element (Three.js WebGL)

- **Landing Page Hero:** A single tasteful, interactive wireframe geometric cluster (code brackets / cube) rendered in Three.js at 60 FPS.
- **Micro-Interaction:** Slowly rotates on idle and subtly responds to mouse cursor coordinates.
- **Accessibility & Performance:**
  - Respects `@media (prefers-reduced-motion: reduce)` by disabling animation or rendering a static SVG wireframe.
  - Automatically lazy-loaded after primary page paint to ensure Lighthouse Performance score ≥ 90.

---

## 5. Gamification Micro-Interactions

- **Streak Flame:** Subtle animated SVG flame indicating consecutive daily learning days.
- **Progress Ring:** Minimal SVG radial progress indicator on course and lesson roadmaps.
- **Single Confetti Burst:** Gentle, lightweight single confetti burst upon lesson completion (no lingering clutter).
- **Audio Synthesis:** Clean Web Audio API sine/triangle tones with a prominent global mute toggle (`🔊`/`🔇`).
