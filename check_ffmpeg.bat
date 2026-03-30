@echo off
REM Verify FFmpeg Installation

cls
echo.
echo ============================================================
echo FFmpeg Verification
echo ============================================================
echo.

ffmpeg -version >nul 2>&1

if errorlevel 1 (
    echo [x] FFmpeg NOT installed
    echo.
    echo Download and install from:
    echo   https://ffmpeg.org/download.html
    echo.
    echo Or: https://github.com/GyanD/codexffmpeg/releases
    echo.
    echo After download:
    echo 1. Extract to C:\ffmpeg
    echo 2. Add C:\ffmpeg\bin to Windows PATH
    echo 3. Restart command prompt
    echo 4. Run this script again
    echo.
) else (
    echo [OK] FFmpeg is installed!
    echo.
    ffmpeg -version | findstr "ffmpeg version"
    echo.
    echo Ready to stream!
    echo.
    echo Next step: Edit stream.bat with your YouTube Stream Key
)

pause
