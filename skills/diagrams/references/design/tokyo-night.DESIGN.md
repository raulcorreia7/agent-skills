---
version: alpha
name: "Tokyo Night Diagram Theme"
description: "Semantic diagram colors for light and dark destinations."
omitted:
  - section: typography
    reason: "The target renderer owns font availability and metrics."
  - section: spacing
    reason: "Diagram layout engines own spacing."
  - section: rounded
    reason: "Domain notation and renderer support control shapes."
  - section: components
    reason: "Diagram families define elements and relationships."
colors:
  primary: "#7AA2F7"
  actor: "#7DCFFF"
  service: "#73DACA"
  data: "#BB9AF7"
  process: "#2AC3DE"
  external: "#565F89"
  success: "#9ECE6A"
  warning: "#E0AF68"
  risk: "#F7768E"
  decision: "#BB9AF7"
  canvas-light: "#E1E2E7"
  edge-light: "#6172B0"
  secondary-text-light: "#6172B0"
  neutral-fill-light: "#D5D6DB"
  neutral-stroke-light: "#A1A6C5"
  neutral-text-light: "#3760BF"
  canvas-dark: "#1A1B26"
  edge-dark: "#A9B1D6"
  secondary-text-dark: "#A9B1D6"
  neutral-fill-dark: "#24283B"
  neutral-stroke-dark: "#414868"
  neutral-text-dark: "#C0CAF5"
---

# Tokyo Night Diagram Theme

## Overview

This file provides the Tokyo Night identity and color tokens for the shared diagram
rules in `visual.md`. Use it only when the user or project selects this theme.

## Colors

The `colors` map is normative. Use light tokens unless the destination
requires dark mode. This theme has no additional behavior exceptions.
