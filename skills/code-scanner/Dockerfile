# syntax=docker/dockerfile:1

# Code Scanner toolbox: the scanners for machines without a native binary.
# Every pinned version lives in this file. To bump a tool, change its
# VERSION and SHA256 together: take the hash from the release's checksums
# file. By default take a release once it is 3 days old, so a pulled or
# hijacked release has time to surface; a security fix, or the maintainer's
# explicit call, may skip the wait.
#
# Bump Python: only to a version every semgrep dependency ships wheels for.
# Do not strip semgrep-core: osemgrep resolves symbols from it at run time.
# The install refuses source builds, as the image has no compiler.

ARG DEBIAN_IMAGE=debian:trixie-slim
ARG PYTHON_IMAGE=python:3.14-slim-trixie
ARG UV_IMAGE=ghcr.io/astral-sh/uv:0.13.7
ARG SEMGREP_VERSION=1.185.0

FROM ${UV_IMAGE} AS uv

# bins: one block per scanner. ADD verifies each download against its sha256
# before the build continues.
FROM ${DEBIAN_IMAGE} AS bins

# https://github.com/google/osv-scanner/releases
ARG OSV_SCANNER_VERSION=2.7.1
ARG OSV_SCANNER_SHA256=fb7dab19a8bd9bbe5c3189f09d4b7ee1820c9553a23bac202648a56efd2f6ee8
ADD --checksum=sha256:${OSV_SCANNER_SHA256} --chmod=755 \
    https://github.com/google/osv-scanner/releases/download/v${OSV_SCANNER_VERSION}/osv-scanner_linux_amd64 \
    /tools/osv-scanner

# https://github.com/hadolint/hadolint/releases
ARG HADOLINT_VERSION=2.15.1
ARG HADOLINT_SHA256=c7187db94eeeeca956519a6af171adc31453941a1e777961f6e680f697c8c507
ADD --checksum=sha256:${HADOLINT_SHA256} --chmod=755 \
    https://github.com/hadolint/hadolint/releases/download/v${HADOLINT_VERSION}/hadolint-linux-x86_64 \
    /tools/hadolint

# https://github.com/aquasecurity/trivy/releases
ARG TRIVY_VERSION=0.76.2
ARG TRIVY_SHA256=bc0fc726e017b8927a62b2d3531d7a84ee01769daf5c99ed866dced54089fdbf
ADD --checksum=sha256:${TRIVY_SHA256} \
    https://github.com/aquasecurity/trivy/releases/download/v${TRIVY_VERSION}/trivy_${TRIVY_VERSION}_Linux-64bit.tar.gz \
    /archives/trivy.tar.gz

# https://github.com/gitleaks/gitleaks/releases
ARG GITLEAKS_VERSION=8.30.1
ARG GITLEAKS_SHA256=551f6fc83ea457d62a0d98237cbad105af8d557003051f41f3e7ca7b3f2470eb
ADD --checksum=sha256:${GITLEAKS_SHA256} \
    https://github.com/gitleaks/gitleaks/releases/download/v${GITLEAKS_VERSION}/gitleaks_${GITLEAKS_VERSION}_linux_x64.tar.gz \
    /archives/gitleaks.tar.gz

# https://github.com/trufflesecurity/trufflehog/releases
ARG TRUFFLEHOG_VERSION=3.99.8
ARG TRUFFLEHOG_SHA256=7c3b02f160f28929a467e29e20fba98746e0729f6e37c3c25761e4f8789abe08
ADD --checksum=sha256:${TRUFFLEHOG_SHA256} \
    https://github.com/trufflesecurity/trufflehog/releases/download/v${TRUFFLEHOG_VERSION}/trufflehog_${TRUFFLEHOG_VERSION}_linux_amd64.tar.gz \
    /archives/trufflehog.tar.gz

# https://github.com/securego/gosec/releases
ARG GOSEC_VERSION=2.30.0
ARG GOSEC_SHA256=3fcce2c4e802ff4169217874602a7df355e9a37bcb6ffaa34b08f3d5f336cdfb
ADD --checksum=sha256:${GOSEC_SHA256} \
    https://github.com/securego/gosec/releases/download/v${GOSEC_VERSION}/gosec_${GOSEC_VERSION}_linux_amd64.tar.gz \
    /archives/gosec.tar.gz

# Each archive holds its binary under the tool's name. gosec ships unstripped.
# Debian package pins break once the archive drops a version; the base tag pins.
# hadolint ignore=DL3008
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked   \
    rm -f /etc/apt/apt.conf.d/docker-clean                  \
    && apt-get update                                       \
    && apt-get install -y --no-install-recommends binutils  \
    && for tool in trivy gitleaks trufflehog gosec; do      \
        tar -xzf "/archives/$tool.tar.gz" -C /tools "$tool"; \
    done                                                    \
    && strip /tools/gosec

# semgrep: a venv from prebuilt wheels only, on the runner's base
FROM ${PYTHON_IMAGE} AS semgrep

ARG SEMGREP_VERSION
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy     \
    UV_PYTHON_DOWNLOADS=never

RUN --mount=from=uv,source=/uv,target=/usr/local/bin/uv \
    --mount=type=cache,target=/root/.cache/uv           \
    uv venv /opt/semgrep                                \
    && uv pip install                                   \
        --python /opt/semgrep/bin/python                \
        --only-binary :all:                             \
        "semgrep==${SEMGREP_VERSION}"

# runner
FROM ${PYTHON_IMAGE}

# git for churn and history scans; ctags and ripgrep aid navigation
# hadolint ignore=DL3008
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked   \
    rm -f /etc/apt/apt.conf.d/docker-clean                  \
    && apt-get update                                       \
    && apt-get install -y --no-install-recommends git ripgrep universal-ctags

COPY --from=bins /tools/ /usr/local/bin/
COPY --from=semgrep /opt/semgrep /opt/semgrep

# The cache directory seeds a named volume (see `scripts/code-scanner`) with the
# scanner user as owner, so vulnerability databases persist across runs.
RUN ln -s /opt/semgrep/bin/semgrep /usr/local/bin/semgrep     \
    && useradd --create-home --uid 10001 --user-group scanner \
    && install -d -o scanner -g scanner /home/scanner/.cache

# The scan mount is read-only: never try to write bytecode next to sources.
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /src
USER 10001:10001
