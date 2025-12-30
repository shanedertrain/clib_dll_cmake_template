# mylib (Windows C DLL template)

Small Windows-only C library built with CMake + MSVC that installs to `dist/` and includes Python and C# smoke tests.

## Prerequisites
- Windows 10/11
- Visual Studio 2022 (or Build Tools) with MSVC + CMake component _or_ standalone CMake on PATH
- Python 3.8+
- .NET SDK 8.0+

> Tip: Open a “x64 Native Tools Command Prompt for VS 2022” (or Developer Command Prompt) so `cmake`/`cl`/`dotnet` are on PATH. If you installed via Chocolatey, open a new shell or run `refreshenv`.

## Quick start
Run from the repo root:

```bat
cd mylib

:: Build and install to dist/
scripts\build_dist.bat

:: Python ctypes smoke test
scripts\run_python_smoke_test.bat

:: C# P/Invoke smoke test
scripts\run_csharp_smoke_test.bat
```

Each smoke test prints `mylib_add_i32(2, 3) = 5` and exits `0` on success.

## Notes
- Build artifacts go to `mylib/dist` (`bin/mylib.dll`, `include/mylib.h`).
- Generated build files live in `mylib/build`; delete that folder to force a clean configure.
- The library exports `int32_t mylib_add_i32(int32_t a, int32_t b);` with `__cdecl` and `__declspec(dllexport)`. Add more functions in `mylib/include/mylib.h` and `mylib/src/mylib.c`, then rebuild.
- `scripts/clean.bat` removes `build/` and `dist/` for a fresh rebuild.

## License
This project is released under the Unlicense (public domain).
