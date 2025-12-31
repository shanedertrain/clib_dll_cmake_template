from __future__ import annotations

import ctypes
import os
import sys
from ctypes import c_int32
from pathlib import Path
from typing import Iterable


def _first_existing(candidates: Iterable[Path]) -> Path | None:
    for path in candidates:
        if path.exists():
            return path
    return None


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    dist_root = root / "dist"
    dist_bin = dist_root / "bin"
    dist_lib = dist_root / "lib"
    dll_path = _first_existing(
        [
            dist_bin / "mylib.dll",
            dist_bin / "libmylib.so",
            dist_bin / "libmylib.dylib",
            dist_lib / "libmylib.so",
            dist_lib / "libmylib.dylib",
        ]
    )

    if dll_path is None:
        print(f"Missing library in {dist_bin} or {dist_lib}")
        print("Run scripts/build_dist.bat or scripts/build_dist.sh first.")
        return 1

    # Required on Windows for dependent DLL resolution (Python 3.8+)
    if sys.version_info >= (3, 8) and os.name == "nt":
        os.add_dll_directory(str(dist_bin))

    lib = ctypes.CDLL(str(dll_path))
    lib.mylib_add_i32.argtypes = [c_int32, c_int32]
    lib.mylib_add_i32.restype = c_int32

    got = int(lib.mylib_add_i32(2, 3))
    print(f"mylib_add_i32(2, 3) = {got}")

    return 0 if got == 5 else 2


if __name__ == "__main__":
    raise SystemExit(main())
