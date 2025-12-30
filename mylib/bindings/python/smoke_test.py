from __future__ import annotations

import ctypes
import os
import sys
from ctypes import c_int32
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    dist_bin = root / "dist" / "bin"
    dll_path = dist_bin / "mylib.dll"

    if not dll_path.exists():
        print(f"Missing: {dll_path}")
        print("Run scripts\\build_dist.bat first.")
        return 1

    # Required on Windows for dependent DLL resolution (Python 3.8+)
    if sys.version_info >= (3, 8):
        os.add_dll_directory(str(dist_bin))

    lib = ctypes.CDLL(str(dll_path))
    lib.mylib_add_i32.argtypes = [c_int32, c_int32]
    lib.mylib_add_i32.restype = c_int32

    got = int(lib.mylib_add_i32(2, 3))
    print(f"mylib_add_i32(2, 3) = {got}")

    return 0 if got == 5 else 2


if __name__ == "__main__":
    raise SystemExit(main())
