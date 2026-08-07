---
version: alpha
name: "Dracula Diagram Theme"
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
  primary: "#BD93F9"
  actor: "#8BE9FD"
  service: "#50FA7B"
  data: "#FF79C6"
  process: "#8BE9FD"
  external: "#6272A4"
  success: "#50FA7B"
  warning: "#FFB86C"
  risk: "#FF5555"
  decision: "#BD93F9"
  canvas-light: "#F8F8F2"
  edge-light: "#6272A4"
  secondary-text-light: "#6272A4"
  neutral-fill-light: "#E6E6D8"
  neutral-stroke-light: "#6272A4"
  neutral-text-light: "#282A36"
  canvas-dark: "#282A36"
  edge-dark: "#F8F8F2"
  secondary-text-dark: "#BDC0CE"
  neutral-fill-dark: "#44475A"
  neutral-stroke-dark: "#6272A4"
  neutral-text-dark: "#F8F8F2"
---

# Dracula Diagram Theme

## Overview

This file provides the Dracula identity and color tokens for the shared diagram
rules in `visual.md`. Use it only when the user or project selects this theme.

## Colors

The `colors` map is normative. Use light tokens unless the destination
requires dark mode. This theme has no additional behavior exceptions.
