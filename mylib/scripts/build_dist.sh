#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

mkdir -p build dist

cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release
cmake --install build --config Release --prefix dist

echo
echo "Built and installed to dist/"
if [ -d dist/bin ]; then
  echo "  dist/bin/$(ls dist/bin)"
else
  echo "  dist/bin/ (not created)"
fi
echo "  dist/include/mylib.h"
