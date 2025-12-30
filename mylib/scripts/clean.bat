@echo off
setlocal

cd /d "%~dp0\\.."

if exist build (
  echo Removing build\
  rmdir /s /q build
)

if exist dist (
  echo Removing dist\
  rmdir /s /q dist
)

echo Clean complete.
