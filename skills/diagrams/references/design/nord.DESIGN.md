---
version: alpha
name: "Nord Diagram Theme"
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
  primary: "#5E81AC"
  actor: "#88C0D0"
  service: "#8FBCBB"
  data: "#81A1C1"
  process: "#5E81AC"
  external: "#4C566A"
  success: "#A3BE8C"
  warning: "#EBCB8B"
  risk: "#BF616A"
  decision: "#B48EAD"
  canvas-light: "#ECEFF4"
  edge-light: "#4C566A"
  secondary-text-light: "#4C566A"
  neutral-fill-light: "#E5E9F0"
  neutral-stroke-light: "#81A1C1"
  neutral-text-light: "#2E3440"
  canvas-dark: "#2E3440"
  edge-dark: "#D8DEE9"
  secondary-text-dark: "#D8DEE9"
  neutral-fill-dark: "#3B4252"
  neutral-stroke-dark: "#4C566A"
  neutral-text-dark: "#ECEFF4"
---

# Nord Diagram Theme

## Overview

This file provides the Nord identity and color tokens for the shared diagram
rules in `visual.md`. Use it only when the user or project selects this theme.

## Colors

The `colors` map is normative. Use light tokens unless the destination
requires dark mode. This theme has no additional behavior exceptions.
