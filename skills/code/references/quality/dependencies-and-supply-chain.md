# Dependencies And Supply Chain

- Define the required capability. Prefer a suitable standard-library feature
  or an established repository dependency.
- Do not reimplement mature, security-sensitive behavior only to reduce the
  dependency count.
- Verify the exact component and version against its official source and
  documentation. Check maintenance, security response, license, compatibility,
  transitive impact, safe defaults, and update path.
- Use the ecosystem lockfile and integrity controls. Preserve an inventory of
  direct and transitive components when the project supports one.
- Monitor relevant advisories. Triage reachability, exploitability, and product
  impact before selecting removal, upgrade, mitigation, or accepted risk.
- Treat popularity, age, scores, signatures, attestations, and inventories as
  evidence inputs. None proves that a component is safe or suitable.

Example—record a decision before you add a dependency:

```text
Capability: decode the required image formats
Candidate: exact package and version from the official registry
Evidence: maintained release, responsive security process, compatible license
Impact: transitive packages, binary size, supported platforms, update owner
Decision: add with lockfile integrity and monitor upstream advisories
```

Sources: [OpenSSF dependency evaluation](https://best.openssf.org/Concise-Guide-for-Evaluating-Open-Source-Software.html),
[NIST SSDF 1.1](https://doi.org/10.6028/NIST.SP.800-218),
[SLSA 1.2](https://slsa.dev/spec/v1.2/), and
[CISA SBOM Minimum Elements](https://www.cisa.gov/sites/default/files/2025-08/2025_CISA_SBOM_Minimum_Elements.pdf).
