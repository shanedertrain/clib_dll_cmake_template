# mylib (Windows C DLL template)

Small Windows-only C library built with CMake + MSVC that installs to `dist/` and includes Python and C# smoke tests.

## Prerequisites
- Windows 10/11 or Linux
- Windows: Visual Studio 2022 (or Build Tools) with MSVC + CMake component _or_ standalone CMake on PATH
- Linux: CMake + a C compiler (gcc/clang)
- Python 3.8+
- .NET SDK 8.0+

> Windows tip: Open a “x64 Native Tools Command Prompt for VS 2022” (or Developer Command Prompt) so `cmake`/`cl`/`dotnet` are on PATH. If you installed via Chocolatey, open a new shell or run `refreshenv`.

## Quick start (Windows, cmd)
Run from the repo root (`mylib` folder contains CMakeLists):

```bat
cd mylib

:: Build and install to dist/
scripts\build_dist.bat

:: Python ctypes smoke test
scripts\run_python_smoke_test.bat

:: C# P/Invoke smoke test
scripts\run_csharp_smoke_test.bat
```

## Quick start (Linux, bash)
Run from the repo root:

```bash
cd mylib

# Build and install to dist/
./scripts/build_dist.sh

# Python ctypes smoke test
./scripts/run_python_smoke_test.sh

# C# P/Invoke smoke test
./scripts/run_csharp_smoke_test.sh
```

Each smoke test prints `mylib_add_i32(2, 3) = 5` and exits `0` on success.

## Notes
- Linux toolchain install (Ubuntu/WSL example):
  ```bash
  sudo apt-get update
  sudo apt-get install -y build-essential cmake python3 python3-venv
  wget https://packages.microsoft.com/config/ubuntu/24.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
  sudo dpkg -i packages-microsoft-prod.deb
  rm packages-microsoft-prod.deb
  sudo apt-get update
  sudo apt-get install -y dotnet-sdk-8.0
  ```
- Build artifacts go to `mylib/dist` (`bin/mylib.dll` on Windows, `bin/libmylib.so` on Linux, plus `include/mylib.h`).
- Generated build files live in `mylib/build`; delete that folder to force a clean configure.
- The library exports `int32_t mylib_add_i32(int32_t a, int32_t b);` with `__cdecl` and `__declspec(dllexport)`. Add more functions in `mylib/include/mylib.h` and `mylib/src/mylib.c`, then rebuild.
- `scripts/clean.bat` removes `build/` and `dist/` for a fresh rebuild.
- `scripts/clean.sh` does the same on Linux.

## License
This project is released under the Unlicense (public domain).
