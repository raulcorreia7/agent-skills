---
version: alpha
name: "Solarized Diagram Theme"
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
  primary: "#268BD2"
  actor: "#2AA198"
  service: "#859900"
  data: "#6C71C4"
  process: "#2AA198"
  external: "#657B83"
  success: "#859900"
  warning: "#B58900"
  risk: "#DC322F"
  decision: "#D33682"
  canvas-light: "#FDF6E3"
  edge-light: "#657B83"
  secondary-text-light: "#657B83"
  neutral-fill-light: "#EEE8D5"
  neutral-stroke-light: "#93A1A1"
  neutral-text-light: "#073642"
  canvas-dark: "#002B36"
  edge-dark: "#839496"
  secondary-text-dark: "#839496"
  neutral-fill-dark: "#073642"
  neutral-stroke-dark: "#586E75"
  neutral-text-dark: "#EEE8D5"
---

# Solarized Diagram Theme

## Overview

This file provides the Solarized identity and color tokens for the shared diagram
rules in `visual.md`. Use it only when the user or project selects this theme.

## Colors

The `colors` map is normative. Use light tokens unless the destination
requires dark mode. This theme has no additional behavior exceptions.
