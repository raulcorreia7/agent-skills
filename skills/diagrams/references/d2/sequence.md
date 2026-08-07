# D2 Sequence Pattern

Use a D2 sequence diagram when explicit stages separate setup from steady-state
traffic. Direction and labels already distinguish requests and responses.

```d2
shape: sequence_diagram
backend: Backend UDP server
local: Local relay
ssh: SSH relay host
remote: Remote UDP client
startup: Startup {
  local -> ssh: "1. Open SSH session"
  ssh -> local: "2. Authentication accepted"
  local -> ssh: "3. Copy UDP relay helper"
  local -> ssh: "4. Start relay helper"
}
active: Active relay {
  remote -> ssh.request: "Send UDP request"
  ssh.request -> local.request: "Forward to local UDP client"
  local.request -> backend: "Forward to backend UDP server"
  backend -> local.response: "Return response payload"
  local.response -> ssh.response: "Forward response to SSH relay"
  ssh.response -> remote: "Return UDP response"
}
```

Use the team's selected default layout. The sequence shape owns stage order.

Source: [D2 gallery](https://d2lang.com/examples/overview/).
