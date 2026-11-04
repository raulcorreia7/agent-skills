# Shared Agents

Shared agents are optional, team-maintained configurations for recurring jobs
that need a distinct model, tool boundary, or operating policy. Skills remain
the portable default.

No shared agents are packaged yet.

The skills installer does not install agents. Codex loads personal agents from
`$CODEX_HOME/agents/<name>.toml` (default `~/.codex/agents/`) and project agents
from `.codex/agents/`; copy the TOML file there. The package here keeps the TOML
with its policy and operating notes. See the
[Codex custom-agent contract](https://developers.openai.com/codex/subagents).

## Add an agent

1. Create `agents/<agent_name>/` using snake_case.
2. Copy `templates/agent/agent.toml` to
   `agents/<agent_name>/<agent_name>.toml`.
3. Keep the TOML `name`, filename, and directory aligned.
4. Add only current, tested tool configuration.
5. Add a reviewed policy when external tools or sensitive data are in scope.
6. List the agent in this README, replacing the "No shared agents" line.
