@echo off
REM Direct FFmpeg YouTube Streaming - Paling Simpel
REM Dijalankan via cmd.exe /c langsung

cd /d "%~dp0"

title YouTube Livestream - Direct Stream

cls
echo.
echo ============================================================
echo YouTube Livestreaming - Direct Stream
echo ============================================================
echo.

REM CONFIG - EDIT BAGIAN INI
set "STREAM_KEY=YOUR_YOUTUBE_STREAM_KEY_HERE"
set "RTMP_URL=rtmp://a.rtmp.youtube.com/live2"
set "BITRATE=5000k"
set "RESOLUTION=1920x1080"
set "FPS=30"
set "AUDIO_BITRATE=192k"

REM Cek stream key
if "!STREAM_KEY!"=="YOUR_YOUTUBE_STREAM_KEY_HERE" (
    echo [ERROR] Stream key belum diatur!
    echo.
    echo Cara setup:
    echo 1. Edit file ini dengan Notepad
    echo 2. Cari: set "STREAM_KEY=YOUR_YOUTUBE_STREAM_KEY_HERE"
    echo 3. Ganti dengan stream key dari https://www.youtube.com/live_dashboard
    echo 4. Simpan dan jalankan lagi
    echo.
    pause
    exit /b 1
)

REM Cari video pertama
set "VIDEO_FILE="
for %%F in (*.mp4 *.mov *.avi *.mkv) do (
    set "VIDEO_FILE=%%F"
    goto found_video
)

echo [ERROR] Tidak ada video file ditemukan (.mp4, .mov, .avi, .mkv)
pause
exit /b 1

:found_video
echo [VIDEO] %VIDEO_FILE%
echo [RTMP] %RTMP_URL%
echo [BITRATE] %BITRATE% video, %AUDIO_BITRATE% audio
echo [QUALITY] %RESOLUTION% @ %FPS%fps
echo.
echo [INFO] Streaming dimulai... (Jangan tutup window)
echo [INFO] Untuk berhenti: Press Ctrl+C
echo.

set "FULL_RTMP=%RTMP_URL%/%STREAM_KEY%"

ffmpeg -re -stream_loop -1 -i "%VIDEO_FILE%" ^
  -c:v libx264 -preset veryfast -b:v %BITRATE% -maxrate %BITRATE% -bufsize %BITRATE% ^
  -s %RESOLUTION% -r %FPS% ^
  -c:a aac -b:a %AUDIO_BITRATE% ^
  -f flv "%FULL_RTMP%"

echo.
echo [INFO] Streaming stopped
pause
