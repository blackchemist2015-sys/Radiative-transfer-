#!/usr/bin/env bash
# Build the two course PDFs from the Markdown lectures:
#   Radiative_Transfer_Course.pdf   (courses/radiative-transfer, RT*.md)
#   Stellar_Atmospheres_Course.pdf  (courses/stellar-atmospheres, SA*.md)
# Requirements: pandoc (>= 2.19), Node.js with `katex` and `playwright-core`
# in $NODE_DIR, and a Chromium/headless-shell binary ($CHROME).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
NODE_DIR="${NODE_DIR:-$ROOT/build/node}"
CHROME="${CHROME:-/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell}"
if [ ! -d "$NODE_DIR/node_modules/katex" ]; then
  mkdir -p "$NODE_DIR" && (cd "$NODE_DIR" && npm init -y >/dev/null && npm install katex@0.16.9 playwright-core@1.47.2 >/dev/null)
fi
KATEX="file://$NODE_DIR/node_modules/katex/dist/"

build_course () {
  local dir="$1" title="$2" out="$3" prefix="$4"
  cd "$ROOT/courses/$dir"
  pandoc "$ROOT/build/$title" ${prefix}*.md \
    --from markdown+tex_math_dollars+pipe_tables-implicit_figures \
    --to html5 --standalone --toc --toc-depth=2 \
    --katex="$KATEX" --css "$ROOT/build/course.css" \
    -o .course.html
  NODE_PATH="$NODE_DIR/node_modules" CHROME="$CHROME" node "$ROOT/scripts/print_pdf.js" .course.html "$ROOT/$out"
  rm -f .course.html
  echo "wrote $out"
}
build_course radiative-transfer  title_rt.md Radiative_Transfer_Course.pdf  RT
build_course stellar-atmospheres title_sa.md Stellar_Atmospheres_Course.pdf SA
