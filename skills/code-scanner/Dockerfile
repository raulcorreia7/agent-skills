# syntax=docker/dockerfile:1

# Code Scanner toolbox: the fallback scanners for machines without a native
# binary. Scanner binaries are pinned in tools.txt and installed by
# fetch-tools, the same script used natively; base images are pinned below.
#
# Bump Python: only to a version every semgrep dependency ships wheels for.
# The install refuses source builds, as the image has no compiler.

ARG DEBIAN_IMAGE=debian:trixie-slim
ARG PYTHON_IMAGE=python:3.14-slim-trixie
ARG UV_IMAGE=ghcr.io/astral-sh/uv:0.13.7
ARG SEMGREP_VERSION=1.183.0

FROM ${UV_IMAGE} AS uv

# bins: the scanner binaries from tools.txt. gosec ships unstripped.
# Debian package pins break once the archive drops a version; the base tag pins.
FROM ${DEBIAN_IMAGE} AS bins

COPY fetch-tools tools.txt /build/

# hadolint ignore=DL3008
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked                     \
    --mount=type=cache,target=/var/lib/apt,sharing=locked                       \
    rm -f /etc/apt/apt.conf.d/docker-clean                                      \
    && apt-get update                                                           \
    && apt-get install -y --no-install-recommends binutils ca-certificates curl \
    && /build/fetch-tools /tools                                                \
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

# The cache directory seeds a named volume (see `code-scanner`) with the
# scanner user as owner, so vulnerability databases persist across runs.
RUN ln -s /opt/semgrep/bin/semgrep /usr/local/bin/semgrep     \
    && useradd --create-home --uid 10001 --user-group scanner \
    && install -d -o scanner -g scanner /home/scanner/.cache

WORKDIR /src
USER 10001:10001
