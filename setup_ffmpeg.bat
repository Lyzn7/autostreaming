@echo off
REM FFmpeg Setup - Add to PATH or extract to custom location
REM For manual setup, Anda bisa extract FFmpeg ke path apapun

cd /d "%~dp0"

cls
echo.
echo ============================================================
echo FFmpeg Setup Helper
echo ============================================================
echo.
echo Anda memiliki 2 pilihan:
echo.
echo [1] Saya sudah punya FFmpeg di G:\ffmpeg\ffmpeg-8.1
echo     (Ubah path di config.json)
echo.
echo [2] Download & Extract FFmpeg otomatis (PowerShell)
echo.

set /p choice="Pilihan (1 atau 2): "

if "!choice!"=="1" (
    goto setup_existing
) else if "!choice!"=="2" (
    goto download_ffmpeg
) else (
    goto invalid
)

:setup_existing
cls
echo.
echo [INFO] Setup untuk existing FFmpeg...
echo.
echo Path yang dicek: G:\ffmpeg\ffmpeg-8.1\bin
echo.

if exist "G:\ffmpeg\ffmpeg-8.1\bin\ffmpeg.exe" (
    echo [OK] FFmpeg found!
    echo.
) else (
    echo [ERROR] ffmpeg.exe tidak ditemukan di:
    echo   G:\ffmpeg\ffmpeg-8.1\bin\ffmpeg.exe
    echo.
    echo Silakan:
    echo 1. Check path-nya benar
    echo 2. Atau extract ke lokasi yang benar
    echo.
    pause
    exit /b 1
)

REM Test python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python belum terinstall!
    pause
    exit /b 1
)

echo [INFO] Testing FFmpeg...
G:\ffmpeg\ffmpeg-8.1\bin\ffmpeg.exe -version >nul 2>&1

if errorlevel 1 (
    echo [ERROR] ffmpeg.exe tidak bisa dijalankan
    pause
    exit /b 1
)

echo [OK] FFmpeg berfungsi dengan baik!
echo.
echo Sekarang jalankan:
echo   python livestream.py
echo.
pause
exit /b 0

:download_ffmpeg
cls
echo.
echo [INFO] Download FFmpeg...
echo.
echo Silakan download manual dari:
echo   https://ffmpeg.org/download.html
echo.
echo Atau gunakan PowerShell:
echo.
echo 1. Buka PowerShell sebagai Administrator
echo.
echo 2. Copy-paste command ini:
echo.
echo    $url = 'https://ffmpeg.org/releases/ffmpeg-snapshot-win64.zip'
echo    $zip = 'ffmpeg.zip'
echo    $extract = 'ffmpeg-extracted'
echo    Invoke-WebRequest -Uri $url -OutFile $zip
echo    Expand-Archive -Path $zip -DestinationPath $extract
echo    Get-ChildItem $extract -Recurse -Filter 'ffmpeg.exe' ^| Select-Object -First 1 -ExpandProperty DirectoryName ^| Copy-Item -Destination 'G:\ffmpeg\ffmpeg-8.1' -Recurse
echo.
echo 3. Tunggu selesai
echo.
echo 4. Kemudian jalankan:
echo    python livestream.py
echo.
pause
exit /b 0

:invalid
echo [ERROR] Input tidak valid
timeout /t 2 /nobreak
goto menu
