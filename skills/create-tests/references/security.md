# Security Tests

Trace each security test to a versioned requirement, threat, trust boundary,
or reproduced vulnerability. Add positive and negative cases.

Use the production-relevant stack for consequential claims. Select static
analysis, dynamic analysis, fuzzing, configuration checks, dependency checks,
or penetration tests from the assessed risk.

Use OWASP ASVS as a web-application requirement source. Use the OWASP Cheat
Sheet Series for reviewed implementation and test details, not as a substitute
for a threat model.

## Example

```text
Risk: a user can read another tenant's invoice by changing its identifier.
Oracle: versioned authorization requirement and tenant-isolation contract.
Cases: owner succeeds. Other tenant and anonymous caller receive no invoice data.
Level: integration test with the real authorization policy and data query.
```

## Evidence Base

- [NIST Secure Software Development Framework, PW.8](https://doi.org/10.6028/NIST.SP.800-218)
- [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
