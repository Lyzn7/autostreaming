@echo off
REM Menu Utama - Pilih opsi streaming

setlocal enabledelayedexpansion

cd /d "%~dp0"

:menu
cls
echo.
echo ============================================================
echo YOUTUBE LIVESTREAM - MENU UTAMA
echo ============================================================
echo.
echo Pilih opsi:
echo.
echo [1] Direct Stream - Mulai streaming langsung
echo [2] Setup FFmpeg - Install FFmpeg 
echo [3] Guides - Buka panduan
echo [Q] Quit - Keluar
echo.
set /p choice="Pilihan (1-3, Q): "

if /i "!choice!"=="1" goto stream
if /i "!choice!"=="2" goto ffmpeg_setup
if /i "!choice!"=="3" goto guides
if /i "!choice!"=="Q" exit /b 0

goto menu

:stream
cls
echo.
echo Launching direct stream...
echo.
call stream.bat
goto menu

:ffmpeg_setup
cls
echo.
echo === FFmpeg Installation ===
echo.
echo Method 1 - Download Standalone (No Admin Needed):
echo   1. Go to: https://ffmpeg.org/download.html
echo   2. Download Windows build
echo   3. Extract to: C:\ffmpeg
echo   4. Add C:\ffmpeg\bin to Windows PATH
echo.
echo Method 2 - Chocolatey (Admin Required):
echo   1. Open PowerShell as Administrator
echo   2. Run: Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
echo   3. Restart PowerShell
echo   4. Run: choco install ffmpeg -y
echo.
echo Method 3 - Use pre-compiled (Easiest):
echo   1. Download from https://github.com/GyanD/codexffmpeg/releases
echo   2. Extract and add to PATH
echo.
pause
goto menu

:guides
cls
echo.
echo === QUICK START ===
echo.
echo Step 1: Get YouTube Stream Key
echo   - Go to: https://www.youtube.com/live_dashboard
echo   - Click: Go Live
echo   - Copy: Stream Key from RTMP server details
echo.
echo Step 2: Edit stream.bat
echo   - Open: stream.bat with Notepad
echo   - Find: set "STREAM_KEY=YOUR_YOUTUBE_STREAM_KEY_HERE"
echo   - Replace with your actual stream key
echo   - Save
echo.
echo Step 3: Start Streaming
echo   - Make sure FFmpeg is installed
echo   - Make sure .mp4 video file is in this folder
echo   - Run: stream.bat
echo.
echo Step 4: Verify on YouTube
echo   - Go to: https://www.youtube.com/live_dashboard
echo   - Check status: Should show "streaming"
echo.
pause
goto menu
