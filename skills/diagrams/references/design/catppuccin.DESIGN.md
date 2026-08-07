---
version: alpha
name: "Catppuccin Diagram Theme"
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
  primary: "#1E66F5"
  actor: "#209FB5"
  service: "#179299"
  data: "#8839EF"
  process: "#04A5E5"
  external: "#8C8FA1"
  success: "#40A02B"
  warning: "#DF8E1D"
  risk: "#D20F39"
  decision: "#7287FD"
  canvas-light: "#EFF1F5"
  edge-light: "#6C6F85"
  secondary-text-light: "#6C6F85"
  neutral-fill-light: "#E6E9EF"
  neutral-stroke-light: "#8C8FA1"
  neutral-text-light: "#4C4F69"
  canvas-dark: "#1E1E2E"
  edge-dark: "#BAC2DE"
  secondary-text-dark: "#BAC2DE"
  neutral-fill-dark: "#313244"
  neutral-stroke-dark: "#45475A"
  neutral-text-dark: "#CDD6F4"
---

# Catppuccin Diagram Theme

## Overview

This file provides the Catppuccin identity and color tokens for the shared diagram
rules in `visual.md`. Use it only when the user or project selects this theme.

## Colors

The `colors` map is normative. Use light tokens unless the destination
requires dark mode. This theme has no additional behavior exceptions.
