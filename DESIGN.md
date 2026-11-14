---
name: Lively Knowledge Engine
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#3c4a42'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#6c7a71'
  outline-variant: '#bbcabf'
  surface-tint: '#006c49'
  primary: '#006c49'
  on-primary: '#ffffff'
  primary-container: '#10b981'
  on-primary-container: '#00422b'
  inverse-primary: '#4edea3'
  secondary: '#855300'
  on-secondary: '#ffffff'
  secondary-container: '#fea619'
  on-secondary-container: '#684000'
  tertiary: '#006591'
  on-tertiary: '#ffffff'
  tertiary-container: '#23acf1'
  on-tertiary-container: '#003d59'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#6ffbbe'
  primary-fixed-dim: '#4edea3'
  on-primary-fixed: '#002113'
  on-primary-fixed-variant: '#005236'
  secondary-fixed: '#ffddb8'
  secondary-fixed-dim: '#ffb95f'
  on-secondary-fixed: '#2a1700'
  on-secondary-fixed-variant: '#653e00'
  tertiary-fixed: '#c9e6ff'
  tertiary-fixed-dim: '#89ceff'
  on-tertiary-fixed: '#001e2f'
  on-tertiary-fixed-variant: '#004c6e'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: '800'
    lineHeight: 48px
  headline-xl-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '800'
    lineHeight: 40px
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 30px
    fontWeight: '700'
    lineHeight: 38px
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 22px
    fontWeight: '700'
    lineHeight: 28px
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '700'
    lineHeight: 24px
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '500'
    lineHeight: 28px
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 15px
    fontWeight: '500'
    lineHeight: 22px
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 18px
  label-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '700'
    lineHeight: 18px
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 11px
    fontWeight: '800'
    lineHeight: 14px
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  gutter: 1.25rem
  margin: 1.5rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.25rem
---

## Brand & Style
This design system marries the structured, calm utility of modern modular workspaces with the joyful, gamified momentum of language-learning apps. The aesthetic balances crisp, uncluttered canvas space with warm, tactile, high-energy interactive components.

### Personality & Tone
- **Encouraging & Enthusiastic:** Interfaces celebrate micro-milestones, streaks, and focus states with delightful, dimensional feedback.
- **Structured Clarity:** High information density is supported through pristine typography, consistent spatial rhythms, and clear card hierarchies.
- **Friendly Modernism:** Approaches the user with generous curves, bouncy micro-interactions, and accessible, high-contrast ink text.

### Visual Style Direction
The visual style is **Tactile Modernist Pop**. It rejects sterile enterprise flatness in favor of physical, "pressable" 3D extruded buttons (solid bottom borders), pill-shaped tracking badges, clean modular card surfaces, and bold, chromatic focal points over an airy, soft-warm backdrop.

## Colors
The color architecture relies on a crisp, radiant canvas layered with vibrant, purposeful chromatic signals:

- **Primary (`#10B981` — Emerald / Quest Green):** Used for primary actions, completion states, progression meters, and affirmative feedback. Underneath, use a darker anchor border (`#059669`) for tactile 3D button depths.
- **Secondary (`#F59E0B` — Sunny Amber):** Reserved for energetic engagement, streaks, flame icons, coin balances, and alert highlights. Anchored by `#D97706`.
- **Tertiary (`#0EA5E9` — Sky Blue):** Applied to secondary interactive flows, exploration modes, information callouts, and multi-track tags. Anchored by `#0284C7`.
- **Accent Badges (`#8B5CF6` — Royal Violet):** Emphasizes achievements, rank statuses, special mastery tiers, and pro features. Anchored by `#7C3AED`.
- **Canvas & Neutrals:**
  - Base Background: `#F8FAFC` (clean crisp slate white) with subtle `#FFFFFF` raised card surfaces.
  - Surface Stroke: `#E2E8F0` for crisp Notion-like modular bounding boxes.
  - High-Contrast Ink: Headings render in `#0F172A` (deep slate ink) and body copy in `#1E293B` to maintain immaculate legibility. Muted labels rest on `#64748B`.

## Typography
Plus Jakarta Sans serves across all layers of the interface, leveraging its friendly geometric curves, generous x-height, and robust letterforms to balance Notion-esque organizational utility with warm Duolingo-style exuberance.

### Hierarchy Rules
- **Display & Headlines:** Utilize weights 700 and 800 with tight letter spacing (-0.02em) to provide punchy, game-like titles and assertive dashboard landmarks.
- **Body & Prose:** Use weight 500 on ink tones (`#1E293B`) to avoid hairline fragility on high-DPI screens and maintain effortless scanning.
- **Labels, Trackers & Chips:** Set in weights 700 or 800, occasionally formatted in small uppercase with +0.04em letter-spacing for mini streak counters, XP tallies, and lesson stages.

## Layout & Spacing
The layout follows a modular fluid grid system engineered to support structured lesson dashboards, daily quest boards, and reading environments.

### Grid & Layout Strategy
- **Desktop (1024px+):** 12-column grid with a maximum container width of 1240px, 1.25rem gutters, and 2rem outer padding. Navigation lives either as a left docked tactile sidebar (260px) or floating top modular shell.
- **Tablet (640px - 1023px):** 8-column layout with 1.25rem gutters and 1.5rem margins. Secondary task panels collapse into bottom drawers or slide-in sheets.
- **Mobile (<640px):** 4-column layout with 1rem gutters and 1rem margins. Main game actions, continuous lesson bars, and streak headers remain pinned top/bottom.

### Spacing Philosophy
Compact padding (`space-xs`, `space-sm`) clusters interactive icons, badge values, and streak tokens. Roomy outer padding (`space-lg`, `space-xl`) inside cards preserves a clean Notion-like atmosphere that keeps gamified elements from overwhelming the user.

## Elevation & Depth
Rather than diffuse atmospheric blur shadows, depth is communicated through a synthesis of **Tactile Extrusion** and **Clean Surface Outlines**:

### The 3D Tactile Border
Interactive components (primary buttons, quest cards, category tiles) utilize a solid, physical drop border:
- **Default State:** A solid 4px bottom rim (`box-shadow: 0 4px 0 0 [Darker Tint]`) paired with a 2px full border (`border: 2px solid [Color]`).
- **Hover State:** Translate Y by -1px and increase bottom extrusion to 5px.
- **Pressed / Active State:** Translate Y down 4px with bottom extrusion reduced to 0px, providing an instantaneous physical "click" feel.

### Surface Elevation
- **Level 0 (Canvas):** `#F8FAFC`.
- **Level 1 (Card / Container):** Crisp pure white `#FFFFFF` surface bounded by a 2px outline in `#E2E8F0` with a soft 0 3px 0 0 `#E2E8F0` bottom edge.
- **Level 2 (Popovers / Modals):** White card overlay equipped with 2px solid `#CBD5E1` outline and a crisp ambient drop: `0 12px 24px -4px rgba(15, 23, 42, 0.08)`.

## Shapes
A pill-shaped, generous corner language (`roundedness: 3`) underpins the approachable, safe, and toy-like feel of the system:

- **Buttons & Action Controls:** Full pills (`rounded-full` or 9999px radius) for primary calls to action, answer nodes, and streak pills.
- **Cards & Surfaces:** Large comfortable rounded corners (24px to 32px / `rounded-xl`) soften data tables and modular Notion-style blocks.
- **Form Inputs & Search:** Pill-style (9999px) for interactive query bars and filter toggles; 16px radius for multi-line inputs.
- **Badges & Avatars:** Rounded squircles (12px to 16px) or circular avatar portals bordered by bold 3px tactile outlines.

## Components

### Buttons
- **Primary 3D Push Button:** Rendered with `#10B981` background, `#FFFFFF` bold text, full-pill radius, 2px stroke, and a solid 4px bottom border in `#059669`. When clicked, transforms downward by 4px as the bottom border flattens to 0px.
- **Secondary Action Button:** Pure white background, `#0EA5E9` text and border, with a solid `#BAE6FD` 4px bottom rim.
- **Ghost/Tertiary Button:** Transparent background, `#64748B` typography, transitioning to a soft `#F1F5F9` pill on hover without vertical translation.

### Streak Counters & Game Badges
- **Streak Pill:** Pill wrapper featuring a soft sunny amber wash (`#FEF3C7`), high-contrast ink text (`#78350F`), a glowing fire icon (`#F59E0B`), and a 2px `#FDE68A` border with a 2px `#F59E0B` bottom press depth.
- **Achievement Badges:** Hexagonal or squircle badge shells bordered in vibrant purple (`#8B5CF6`) with a 3D `#6D28D9` base, framing reward tokens and tier counts.

### Cards & Lesson Nodes
- **Content Cards:** Clean white canvas framed in 2px `#E2E8F0` with 24px border radius. Hover introduces a subtle translateY(-2px) and elevates bottom stroke depth from 2px to 4px in `#CBD5E1`.
- **Lesson Track Node (Duolingo Style):** 64px circular interactive milestones with 5px solid bottom borders. Completed nodes feature `#10B981` fills with star glyphs; locked nodes feature `#E2E8F0` fills and `#94A3B8` icon stamps.

### Form Inputs & Search
- Inputs feature `#FFFFFF` backgrounds, 2px borders in `#E2E8F0`, 16px horizontal padding, and full pill curves. Focus state transitions border to 2px solid `#0EA5E9` with a subtle `0 0 0 3px rgba(14, 165, 233, 0.15)` aura.

### Checkboxes & Radio Buttons
- 24px rounded squircle checkboxes (8px radius) and circular radio targets with 2.5px solid outlines in `#CBD5E1`. Checked state fills instantly with `#10B981`, a crisp white tick or bullseye, and an animated pop scaling effect (scale 1.1 down to 1.0).

### Chips & Filter Tags
- Compact pills with 10px vertical and 16px horizontal padding, label-md typography, `#F1F5F9` background, and 1.5px solid border. Active filter state adopts `#0F172A` dark ink fill with white text or lively `#10B981` primary fill.