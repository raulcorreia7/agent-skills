---
version: alpha
name: "Gruvbox Diagram Theme"
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
  primary: "#458588"
  actor: "#83A598"
  service: "#689D6A"
  data: "#B16286"
  process: "#D65D0E"
  external: "#928374"
  success: "#98971A"
  warning: "#D79921"
  risk: "#CC241D"
  decision: "#B16286"
  canvas-light: "#FBF1C7"
  edge-light: "#665C54"
  secondary-text-light: "#665C54"
  neutral-fill-light: "#F2E5BC"
  neutral-stroke-light: "#A89984"
  neutral-text-light: "#3C3836"
  canvas-dark: "#1D2021"
  edge-dark: "#D5C4A1"
  secondary-text-dark: "#A89984"
  neutral-fill-dark: "#282828"
  neutral-stroke-dark: "#504945"
  neutral-text-dark: "#EBDBB2"
---

# Gruvbox Diagram Theme

## Overview

This file provides the Gruvbox identity and color tokens for the shared diagram
rules in `visual.md`. Use it only when the user or project selects this theme.

## Colors

The `colors` map is normative. Use light tokens unless the destination
requires dark mode. This theme has no additional behavior exceptions.
