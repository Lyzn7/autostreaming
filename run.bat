@echo off
REM Run Python Livestream Script
REM Cek Python dan jalankan livestream.py

cd /d "%~dp0"

cls
echo.
echo ============================================================
echo YouTube Livestreaming - Python Version
echo ============================================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python belum terinstall!
    echo.
    echo Download dari: https://www.python.org/downloads/
    echo.
    echo Atau gunakan livestream.py langsung dari Command Prompt:
    echo   python livestream.py
    echo.
    pause
    exit /b 1
)

REM Check config
if not exist "config.json" (
    echo [ERROR] config.json tidak ditemukan!
    pause
    exit /b 1
)

REM Run Python script
echo [INFO] Starting Python livestream...
echo.
python livestream.py

if errorlevel 1 (
    echo.
    echo [ERROR] Ada masalah. Cek error di atas.
    echo.
    pause
)

exit /b 0
