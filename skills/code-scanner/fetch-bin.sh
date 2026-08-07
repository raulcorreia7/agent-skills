#!/bin/sh
# fetch-bin.sh <url> <sha256> <bin|tar> <dest-dir> <name>
#
# Download a release artifact, verify its sha256, and install it:
#   bin — a raw binary, installed as <dest-dir>/<name> (0755)
#   tar — a tarball; member <name> is extracted into <dest-dir>
# Fails the build on checksum mismatch. Needs: curl, sha256sum, tar.
set -eu

usage() { echo "usage: fetch-bin.sh <url> <sha256> <bin|tar> <dest-dir> <name>" >&2; exit 1; }
[ "$#" -eq 5 ] || usage

url=$1
sha=$2
mode=$3
dest=$4
name=$5

tmp=$(mktemp)
trap 'rm -f "$tmp"' EXIT INT TERM

curl -sSL --proto '=https' -o "$tmp" "$url"
echo "$sha  $tmp" | sha256sum -c -

case "$mode" in
    bin) install -m 0755 "$tmp" "$dest/$name" ;;
    tar) tar -xzf "$tmp" -C "$dest" "$name" ;;
    *) usage ;;
esac
