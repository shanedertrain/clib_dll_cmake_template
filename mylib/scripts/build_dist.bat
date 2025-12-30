@echo off
setlocal enabledelayedexpansion

cd /d "%~dp0\.."

if not exist build mkdir build
if not exist dist mkdir dist

cmake -S . -B build -G "Visual Studio 17 2022" -A x64
if errorlevel 1 exit /b 1

cmake --build build --config Release
if errorlevel 1 exit /b 1

cmake --install build --config Release --prefix dist
if errorlevel 1 exit /b 1

echo.
echo Built and installed to dist\
echo   dist\bin\mylib.dll
echo   dist\include\mylib.h
