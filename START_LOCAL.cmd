@echo off
title 3D SITE 1-10-2026 (port 18792)
cd /d "%~dp0"
echo Serving folder: %~dp0
echo Port 18792 (falls back to the next free port if busy)
if exist "%LOCALAPPDATA%\Programs\Python\Python313\python.exe" (
  "%LOCALAPPDATA%\Programs\Python\Python313\python.exe" "%~dp0serve.py" --port 18792
  goto done
)
where py >nul 2>nul
if not errorlevel 1 (
  py -3 "%~dp0serve.py" --port 18792
  goto done
)
where python >nul 2>nul
if not errorlevel 1 (
  python "%~dp0serve.py" --port 18792
  goto done
)
echo Python 3 is required. Install Python 3, then run this file again.
:done
pause
