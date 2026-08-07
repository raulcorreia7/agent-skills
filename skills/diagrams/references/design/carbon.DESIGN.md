---
version: alpha
name: "Carbon Diagram Theme"
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
  primary: "#0F62FE"
  actor: "#1192E8"
  service: "#009D9A"
  data: "#6929C4"
  process: "#005D5D"
  external: "#60758F"
  success: "#24A148"
  warning: "#F1C21B"
  risk: "#DA1E28"
  decision: "#8A3FFC"
  canvas-light: "#FFFFFF"
  edge-light: "#525252"
  secondary-text-light: "#525252"
  neutral-fill-light: "#F4F4F4"
  neutral-stroke-light: "#8D8D8D"
  neutral-text-light: "#161616"
  canvas-dark: "#161616"
  edge-dark: "#C6C6C6"
  secondary-text-dark: "#C6C6C6"
  neutral-fill-dark: "#262626"
  neutral-stroke-dark: "#525252"
  neutral-text-dark: "#F4F4F4"
---

# Carbon Diagram Theme

## Overview

This file provides the Carbon identity and color tokens for the shared diagram
rules in `visual.md`. Use it only when the user or project selects this theme.

## Colors

The `colors` map is normative. Use light tokens unless the destination
requires dark mode. This theme has no additional behavior exceptions.
