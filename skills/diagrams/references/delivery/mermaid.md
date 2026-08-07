# Mermaid Rendering

Use a native target renderer or pinned `@mermaid-js/mermaid-cli` and its browser
dependency. Native host rendering and local validation are separate contracts.

```text
mmdc --version
mmdc -i probe.mmd -o probe.png
mmdc -i checkout.mmd -o checkout.png -b white -s 2
mmdc -i wide.mmd -o wide.png -b white -w 1600 -s 1
```

`--scale` changes capture density; `--width` changes the browser viewport. For
wide families, increase width before scale. A local CLI can accept a family an
embedded host rejects. When native rendering is unavailable, retain `.mmd` and
publish a reviewed PNG.

Source: [Mermaid CLI](https://github.com/mermaid-js/mermaid-cli).
