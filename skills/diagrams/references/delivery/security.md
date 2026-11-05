# Rendering Security Boundary

Apply this boundary before rendering source, renderer configuration, themes,
fonts, images, icons, links, raw HTML, imports, or includes that were not
reviewed in the current task.

- Review the complete input set before rendering. Reject secrets, credentials,
  executable content, unexpected plugins, remote URLs, and unreviewed local
  imports or includes. Supply each required local asset explicitly.
- Render with least privilege: no credentials, no network, read-only reviewed
  inputs, an isolated temporary output directory, and no local-file access
  beyond those inputs. The bundled helper selects renderers but does not create
  this sandbox. Do not render when the boundary cannot be enforced.
- Publish only reviewed static output. Do not publish interactive SVG, HTML,
  configuration, or unreviewed source. Retain reviewed source under normal
  repository access.
- Sending private or unreviewed source to a public renderer is approval-gated.
- Prefer pinned local fonts, icons, and images. Remote resources create privacy,
  integrity, availability, CSP, and offline risks.
- Use an explicit background for fixed assets unless every destination
  background was verified. Keep generated IDs, timestamps, and environment
  paths out of committed output where supported.
