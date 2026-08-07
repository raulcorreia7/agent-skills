# Java Quality Gates

Repository wrapper, pinned JDK/toolchain, and parent build conventions take
precedence. Repository CI and a parent POM or build script take precedence over
module configuration. Put shared rules in the parent POM or root Gradle build.
Do not add competing formatters, style linters, or general-purpose bug finders
to one module.

## Strict Baseline

Compile against the supported release, enable every standard compiler warning,
and fail on each warning. `--release` is stronger than `source` or `target`: it
also rejects APIs unavailable on the target release. Do not enable preview
features by default.

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

For Gradle Kotlin DSL, make the declared toolchain and bytecode/API release
match the supported release. Apply the arguments to main and test compilation:

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

Use one deterministic formatter (the repository's existing Spotless,
google-java-format, or equivalent) and make its check task fail CI. Use one
semantic analyzer that fits the codebase. Do not duplicate it with overlapping
rules from PMD, SpotBugs, Error Prone, or a hosted scanner. A selected analyzer
and every configured severity must run in the normal `verify` or `check`
lifecycle, not only in an IDE.

For example, when the repository already configures Spotless, make the
formatter explicit in the local check rather than relying on an IDE:

```text
./mvnw -B spotless:check verify
./gradlew spotlessCheck check
```

## Dependency And Build Integrity

- Pin the build tool through `mvnw` or `gradlew`. Build and test with the
  declared toolchain, not a developer's ambient JDK.
- Lock resolved dependencies for applications and commit the lock state.
  Gradle example: `dependencyLocking { lockAllConfigurations() }`, then update
  deliberately with `./gradlew dependencies --write-locks`. Do not lock
  changing or `SNAPSHOT` dependencies. Replace them with an immutable release
  first.
- In Gradle, commit `gradle/verification-metadata.xml` and verify artifact
  checksums or signatures. Do not bypass dependency verification for a normal
  configuration.
- In Maven, apply Enforcer centrally to require the supported JDK and explicit
  plugin versions, reject dynamic and snapshot release dependencies, and check
  dependency convergence. Route vulnerability scanning through the repository's
  approved SCA system and fail the build at its agreed threshold.

```xml
<!-- Inside the parent Maven Enforcer execution's <rules> -->
<requireJavaVersion><version>[${java.release},)</version></requireJavaVersion>
<requirePluginVersions/>
<banDynamicVersions/>
<requireReleaseDeps/>
<dependencyConvergence/>
```

## Sources

- [javac options](https://docs.oracle.com/en/java/javase/24/docs/specs/man/javac.html)
  and [Maven Compiler `--release`](https://maven.apache.org/components/plugins/maven-compiler-plugin/examples/set-compiler-release.html).
- [Maven Enforcer rules](https://maven.apache.org/components/enforcer/enforcer-rules/),
  [Gradle Java builds](https://docs.gradle.org/current/userguide/building_java_projects.html),
  [Gradle toolchains](https://docs.gradle.org/current/userguide/toolchains.html),
  [dependency locking](https://docs.gradle.org/current/userguide/dependency_locking.html),
  and [dependency verification](https://docs.gradle.org/current/userguide/dependency_verification.html).
