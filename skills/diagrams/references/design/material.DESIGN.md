---
version: alpha
name: "Material Diagram Theme"
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
  primary: "#1A73E8"
  actor: "#039BE5"
  service: "#00897B"
  data: "#5E35B1"
  process: "#00838F"
  external: "#546E7A"
  success: "#2E7D32"
  warning: "#ED6C02"
  risk: "#D32F2F"
  decision: "#7B1FA2"
  canvas-light: "#FFFBFE"
  edge-light: "#79747E"
  secondary-text-light: "#49454F"
  neutral-fill-light: "#F7F2FA"
  neutral-stroke-light: "#79747E"
  neutral-text-light: "#1D1B20"
  canvas-dark: "#1C1B1F"
  edge-dark: "#CAC4D0"
  secondary-text-dark: "#CAC4D0"
  neutral-fill-dark: "#313033"
  neutral-stroke-dark: "#938F99"
  neutral-text-dark: "#E6E1E5"
---

# Material Diagram Theme

## Overview

This file provides the Material identity and color tokens for the shared diagram
rules in `visual.md`. Use it only when the user or project selects this theme.

## Colors

The `colors` map is normative. Use light tokens unless the destination
requires dark mode. This theme has no additional behavior exceptions.
