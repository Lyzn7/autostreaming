@echo off
REM Setup Helper untuk Advanced Livestreaming
REM Membantu setup musik dan verify setup

cd /d "%~dp0"

cls
echo.
echo ============================================================
echo Advanced Livestreaming Setup Helper
echo ============================================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python belum terinstall!
    pause
    exit /b 1
)

REM Check FFmpeg
"%~dp0ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe" -version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] FFmpeg belum ada di path yang benar!
    pause
    exit /b 1
)

echo [OK] Python terinstall
echo [OK] FFmpeg ditemukan
echo.

REM Check video files
echo [INFO] Mencari video files...
set "found_video=0"
for %%F in (*.mp4 *.mov *.avi *.mkv) do (
    echo   ✓ %%F
    set "found_video=1"
)

if "!found_video!"=="0" (
    echo   [!] Tidak ada video file!
    echo.
    pause
    exit /b 1
)

echo.

REM Check musik
echo [INFO] Checking musik...
if exist "assets\music.mp3" (
    echo [OK] Musik ditemukan: assets\music.mp3
) else (
    echo [!] Musik belum ada di: assets\music.mp3
    echo.
    echo Cara setup musik:
    echo 1. Siapkan file musik .mp3
    echo 2. Copy ke folder: %~dp0assets\
    echo 3. Rename menjadi: music.mp3
    echo.
    echo Atau, untuk test tanpa musik, run:
    echo    python livestream.py
    echo.
) 

echo.
echo ============================================================
echo READY TO STREAM!
echo ============================================================
echo.
echo Mode: Advanced (Random Video + Music Background)
echo Durasi per video: 60 detik
echo Auto-stop: 10 jam
echo Kualitas: 1280x720 @ 30fps
echo Bitrate: 2500 kbps
echo.
echo Mulai streaming dengan:
echo    python livestream.py
echo.
pause
