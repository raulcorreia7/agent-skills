# Shared Agents

Shared agents are optional, team-maintained configurations for recurring jobs
that need a distinct model, tool boundary, or operating policy. Skills remain
the portable default.

No shared agents are packaged yet.

The skills installer does not install agents. For Codex, place a copy of the
standalone TOML file at `$CODEX_HOME/agents/<name>.toml`. The source package
stays together here with its policy and operating notes.

## Add an agent

1. Create `agents/<agent_name>/` using snake_case.
2. Copy `templates/agent/agent.toml` to
   `agents/<agent_name>/<agent_name>.toml`.
3. Keep the TOML `name`, filename, and directory aligned.
4. Add only current, tested tool configuration.
5. Add a reviewed policy when external tools or sensitive data are in scope.
6. Add the agent to the table above.

Codex loads personal agents from `~/.codex/agents/` and project agents from
`.codex/agents/`. This repository packages shared agents but does not activate
them as project agents. See the
[Codex custom-agent contract](https://developers.openai.com/codex/subagents).
