# azure_explorer

Read-only explorer for Azure and Azure DevOps metadata, for Codex, Claude Code,
and omp. It reports resources, identities, access, exposure, health, pipelines,
and work items, and changes nothing.

## Prerequisites

- `az login` with an identity that has Reader on the subscriptions in scope and
  no Key Vault data-plane role.
- `AZURE_DEVOPS_ORG` set to the Azure DevOps organization name (Codex, Claude).
- `npx` on `PATH`.

## Install

| Client | Agent | MCP servers |
|---|---|---|
| Codex | `azure_explorer.toml` → `~/.codex/agents/` | Merge `codex-mcp.toml` into `~/.codex/config.toml` |
| Claude Code | `claude.md` → `~/.claude/agents/azure-explorer.md` | Declared in the agent; connected only while it runs |
| omp | `omp.md` → `~/.omp/agent/agents/azure-explorer.md` | Merge `omp-mcp.json` into `~/.omp/agent/mcp.json` |

## Tool policy

- Azure MCP runs with `--read-only` and a namespace allowlist. The allowlist
  leaves out namespaces that return secrets or business data or run commands:
  `keyvault`, `appconfig`, `storage`, `cosmos`, `kusto`, `postgres`, `mysql`,
  `search`, `iothub`, `deploy`, and `extension`.
- The Azure DevOps server has no read-only mode. Codex and Claude allow only
  its read tools; every `*_write` tool, `repo_create_branch`, `wiki_upsert_page`,
  `wit_backlog`, and the artifact and attachment downloads stay off.
- omp cannot limit MCP tools per agent or per server, so its package omits
  Azure DevOps. Its MCP servers reach every omp session.
- Codex agents cannot declare MCP servers, so `codex-mcp.toml` reaches every
  Codex session.
- The agent prompt is the same in all three files; change it in all three.

Pins: `@azure/mcp@3.0.0`, `@azure-devops/mcp@2.11.0`. Upgrading either is a
tool-policy change: re-check its read-only tools before bumping.
