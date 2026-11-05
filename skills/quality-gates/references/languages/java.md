# Java Quality Gates

The build wrapper, the pinned JDK toolchain, and the parent POM or root Gradle
build own shared rules. Put new rules there, not in one module, and keep one
formatter and one semantic analyzer.

## Strict baseline

Compile against the supported release with every standard warning enabled, and
fail on warnings. `--release` is stronger than `source` or `target`: it also
rejects APIs missing from the target release. Leave preview features off.

In an existing Maven Compiler Plugin configuration, use the project release
property and add the arguments below. The parent owns the plugin version.

```xml
<properties>
  <!-- java.release is declared by the repository support policy. -->
  <maven.compiler.release>${java.release}</maven.compiler.release>
</properties>

<plugin>
  <artifactId>maven-compiler-plugin</artifactId>
  <configuration>
    <compilerArgs>
      <arg>-Xlint:all</arg>
      <arg>-Werror</arg>
    </compilerArgs>
  </configuration>
</plugin>
```

For Gradle Kotlin DSL, match the toolchain and the bytecode and API release to
the supported release, and apply the arguments to main and test compilation:

```kotlin
// javaRelease is declared in root gradle.properties or equivalent policy.
val javaRelease = providers.gradleProperty("javaRelease").get().toInt()

java {
    toolchain.languageVersion.set(JavaLanguageVersion.of(javaRelease))
}
tasks.withType<JavaCompile>().configureEach {
    options.release.set(javaRelease)
    options.compilerArgs.addAll(listOf("-Xlint:all", "-Werror"))
}
```

Use the repository's existing deterministic formatter (Spotless,
google-java-format, or equivalent) and make its check task fail CI. Pick one
semantic analyzer that fits the codebase rather than stacking overlapping
rules from PMD, SpotBugs, Error Prone, or a hosted scanner. Attach the
formatter, the analyzer, and every configured severity to the normal `verify`
or `check` lifecycle so they run outside the IDE.

## Dependency and build integrity

- Pin the build tool through `mvnw` or `gradlew`, and build with the declared
  toolchain rather than the ambient JDK.
- Lock resolved dependencies for applications and commit the lock state. In
  Gradle: `dependencyLocking { lockAllConfigurations() }`, updated with
  `./gradlew dependencies --write-locks`. Replace changing or `SNAPSHOT`
  dependencies with an immutable release before locking.
- In Gradle, commit `gradle/verification-metadata.xml` and verify artifact
  checksums or signatures for every normal configuration.
- In Maven, apply Enforcer centrally to require the supported JDK and explicit
  plugin versions, reject dynamic and snapshot release dependencies, and check
  dependency convergence. Run vulnerability scanning through the repository's
  approved SCA system at its agreed threshold.

```xml
<!-- Inside the parent Maven Enforcer execution's <rules> -->
<requireJavaVersion><version>[${java.release},)</version></requireJavaVersion>
<requirePluginVersions/>
<banDynamicVersions/>
<requireReleaseDeps/>
<dependencyConvergence/>
```

## Gate commands

```text
./mvnw -B spotless:check verify
./gradlew spotlessCheck check
```

Run only the wrapper the repository uses. A cold cache downloads the build tool
and dependencies, so the first run is approval-gated.

Sources: `java` in [sources.yml](../sources.yml).
