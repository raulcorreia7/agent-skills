# Java Verification

Run the existing CI-equivalent lifecycle first. Typical minimal sequences are:

```text
./mvnw -B verify
./mvnw -B test                         # focused module/profile as appropriate
./gradlew check
./gradlew test                         # focused task/filter as appropriate
```

Run only the applicable wrapper. Verify formatter, analyzer, dependency lock,
and vulnerability or SCA tasks are attached to `verify` or `check`. `build` is
not a substitute unless the build declares that lifecycle. Update dependency
locks or verification metadata only after reviewing the resolved graph and
artifact provenance.
