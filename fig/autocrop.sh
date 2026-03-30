#!/usr/bin/env sh

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

for f in "$script_dir"/*.pdf; do
    [ -f "$f" ] || continue
    pdfcrop "$f" "$f"
done
