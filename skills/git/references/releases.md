# Generated Release Flow

When release metadata or changelogs are generated:

1. Merge process or tooling changes separately.
2. Run the repository release tool to generate the version and changelog.
3. Keep the generated version or changelog PR last and focused.
4. Review and merge it.
5. Tag only the reviewed merge commit.

If generated output is wrong, fix commit metadata, adjust the selected version,
or rerun the generator. Do not hand-edit generated changelog content.

Example release result:

```text
Version: 1.4.0
Generated changelog: 1.4.0 section
Expected tag: v1.4.0
Tag target: reviewed release-PR merge commit
```

## Release section in a PR template

When a PR template has a release section and the PR is a process or tooling
change rather than a version bump, say so explicitly:

```text
## Release PR

- Version: Not a version bump PR.
- Generated changelog checked: Not applicable; unchanged in this PR.
- Expected tag: Not created by this PR.
- Release trigger: Follow-up release flow after this PR merges.
```
