# syntax=docker/dockerfile:1

# Code Scanner toolbox: fallback scanners when no native binary exists.
# Tools pin (version + sha256) for reproducible builds; base floats
# (`python:slim`) for the newest stable Python. Bump: ARG + sha, rebuild.

# builder: installs everything
FROM python:slim AS builder

ARG OSV_SCANNER_VERSION=2.5.1
ARG OSV_SCANNER_SHA256=f9f25499a2c8cc367b3af45df2ea7eeca7fbccceab9c35079968f4b3652194be
ARG OSV_SCANNER_URL=https://github.com/google/osv-scanner/releases/download/v${OSV_SCANNER_VERSION}/osv-scanner_linux_amd64
ARG TRIVY_VERSION=0.74.0
ARG TRIVY_SHA256=2ae6fe3ee734b7fdf11335663e18c75ea12dccc76062f09f164a3b0f8be4371a
ARG TRIVY_URL=https://github.com/aquasecurity/trivy/releases/download/v${TRIVY_VERSION}/trivy_${TRIVY_VERSION}_Linux-64bit.tar.gz
ARG GITLEAKS_VERSION=8.30.1
ARG GITLEAKS_SHA256=551f6fc83ea457d62a0d98237cbad105af8d557003051f41f3e7ca7b3f2470eb
ARG GITLEAKS_URL=https://github.com/gitleaks/gitleaks/releases/download/v${GITLEAKS_VERSION}/gitleaks_${GITLEAKS_VERSION}_linux_x64.tar.gz
ARG TRUFFLEHOG_VERSION=3.97.4
ARG TRUFFLEHOG_SHA256=dc24007c2f233bd61c05beabeb44aa27ea9b43288166279209abe0458c5ce76b
ARG TRUFFLEHOG_URL=https://github.com/trufflesecurity/trufflehog/releases/download/v${TRUFFLEHOG_VERSION}/trufflehog_${TRUFFLEHOG_VERSION}_linux_amd64.tar.gz
ARG HADOLINT_VERSION=2.15.1
ARG HADOLINT_SHA256=c7187db94eeeeca956519a6af171adc31453941a1e777961f6e680f697c8c507
ARG HADOLINT_URL=https://github.com/hadolint/hadolint/releases/download/v${HADOLINT_VERSION}/hadolint-linux-x86_64
ARG GOSEC_VERSION=2.29.0
ARG GOSEC_SHA256=6431b119741c1f4a50fdfcf94e782e16b9e642afc8c7fa9b5d39d48bf3003095
ARG GOSEC_URL=https://github.com/securego/gosec/releases/download/v${GOSEC_VERSION}/gosec_${GOSEC_VERSION}_linux_amd64.tar.gz
ARG SEMGREP_VERSION=1.176.0
COPY fetch-bin.sh /bin/fetch-bin.sh

WORKDIR /tools

# deps, scanners, semgrep venv in one layer
RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates curl \
    && rm -rf /var/lib/apt/lists/* \
    && fetch-bin.sh ${OSV_SCANNER_URL} ${OSV_SCANNER_SHA256} bin /tools osv-scanner \
    && fetch-bin.sh ${TRIVY_URL} ${TRIVY_SHA256} tar /tools trivy \
    && fetch-bin.sh ${GITLEAKS_URL} ${GITLEAKS_SHA256} tar /tools gitleaks \
    && fetch-bin.sh ${TRUFFLEHOG_URL} ${TRUFFLEHOG_SHA256} tar /tools trufflehog \
    && fetch-bin.sh ${HADOLINT_URL} ${HADOLINT_SHA256} bin /tools hadolint \
    && fetch-bin.sh ${GOSEC_URL} ${GOSEC_SHA256} tar /tools gosec \
    && python3 -m venv /opt/semgrep \
    && /opt/semgrep/bin/pip install --no-cache-dir semgrep==${SEMGREP_VERSION}

# runner: copies results, experimental via apt
FROM python:slim

# scanners
COPY --from=builder \
    /tools/osv-scanner \
    /tools/trivy \
    /tools/gitleaks \
    /tools/trufflehog \
    /tools/hadolint \
    /tools/gosec \
    /usr/local/bin/
COPY --from=builder /opt/semgrep /opt/semgrep

# runtime deps: git for churn; ctags and ripgrep aid navigation
RUN apt-get update \
    && apt-get install -y --no-install-recommends git universal-ctags ripgrep \
    && rm -rf /var/lib/apt/lists/*

# nonroot user
RUN ln -s /opt/semgrep/bin/semgrep /usr/local/bin/semgrep \
    && useradd -m scanner

WORKDIR /src
USER scanner
