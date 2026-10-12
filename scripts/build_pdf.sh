#!/usr/bin/env bash
# Build Radiative_Transfer_Course.pdf from the Markdown lectures.
# Requirements: pandoc (>= 2.19), Node.js with `katex` and `playwright-core`
# installed in $NODE_DIR, and a Chromium binary ($CHROME).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
NODE_DIR="${NODE_DIR:-$ROOT/build/node}"
CHROME="${CHROME:-/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell}"
if [ ! -d "$NODE_DIR/node_modules/katex" ]; then
  mkdir -p "$NODE_DIR" && (cd "$NODE_DIR" && npm init -y >/dev/null && npm install katex@0.16.9 playwright-core@1.47.2 >/dev/null)
fi
KATEX="file://$NODE_DIR/node_modules/katex/dist/"
cd "$ROOT/course"
pandoc ../build/title.md L0*.md L1*.md \
  --from markdown+tex_math_dollars+pipe_tables-implicit_figures \
  --to html5 --standalone --toc --toc-depth=2 \
  --katex="$KATEX" \
  --css ../build/course.css \
  --metadata title="Radiative Transfer" \
  -o ../build/course.html
cd "$ROOT"
NODE_PATH="$NODE_DIR/node_modules" CHROME="$CHROME" node scripts/print_pdf.js build/course.html Radiative_Transfer_Course.pdf
echo "wrote Radiative_Transfer_Course.pdf"
