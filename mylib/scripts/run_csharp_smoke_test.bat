@echo off
setlocal

cd /d "%~dp0\.."

if not exist "dist\bin\mylib.dll" (
  echo Missing dist\bin\mylib.dll
  echo Run scripts\build_dist.bat first.
  exit /b 1
)

dotnet run --project "bindings\csharp\Demo.csproj" -c Release
exit /b %errorlevel%
