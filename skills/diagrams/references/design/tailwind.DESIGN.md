---
version: alpha
name: "Tailwind Diagram Theme"
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
  primary: "#4F46E5"
  actor: "#0284C7"
  service: "#0F766E"
  data: "#7C3AED"
  process: "#0891B2"
  external: "#64748B"
  success: "#16A34A"
  warning: "#D97706"
  risk: "#DC2626"
  decision: "#9333EA"
  canvas-light: "#FFFFFF"
  edge-light: "#475569"
  secondary-text-light: "#64748B"
  neutral-fill-light: "#F8FAFC"
  neutral-stroke-light: "#CBD5E1"
  neutral-text-light: "#0F172A"
  canvas-dark: "#0F172A"
  edge-dark: "#CBD5E1"
  secondary-text-dark: "#94A3B8"
  neutral-fill-dark: "#1E293B"
  neutral-stroke-dark: "#475569"
  neutral-text-dark: "#F8FAFC"
---

# Tailwind Diagram Theme

## Overview

This file provides the Tailwind identity and color tokens for the shared diagram
rules in `visual.md`. Use it only when the user or project selects this theme.

## Colors

The `colors` map is normative. Use light tokens unless the destination
requires dark mode. This theme has no additional behavior exceptions.
