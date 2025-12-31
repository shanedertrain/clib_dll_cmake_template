#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

if [[ ! -f "dist/bin/mylib.dll" && ! -f "dist/bin/libmylib.so" && ! -f "dist/bin/libmylib.dylib" && ! -f "dist/lib/libmylib.so" && ! -f "dist/lib/libmylib.dylib" ]]; then
  echo "Missing dist/bin or dist/lib library"
  echo "Run scripts/build_dist.sh or scripts/build_dist.bat first."
  exit 1
fi

python "bindings/python/smoke_test.py"
