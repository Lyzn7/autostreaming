# FFmpeg Setup Guide - For G:\ffmpeg\ffmpeg-8.1

## 📋 Current Situation

- ✅ Config file adalah: `G:\asmr\config.json`
- ✅ Path sudah set ke: `G:\ffmpeg\ffmpeg-8.1\bin`
- ⚠️ FFmpeg executable belum ada di sana

## 🚀 Solution: Download Pre-compiled FFmpeg

### Option 1: Download Manual (Recommended)

1. **Download FFmpeg binary:**
   - Go to: https://ffmpeg.org/download.html
   - Click: Windows Builds
   - Download latest ZIP (e.g., `ffmpeg-master-latest-win64-gpl.zip`)

2. **Extract:**
   - Extract ZIP file
   - Di dalam ZIP, cari folder `bin` yang contains `ffmpeg.exe`
   - Copy semua file dari `bin` folder

3. **Paste ke:**
   ```
   G:\ffmpeg\ffmpeg-8.1\bin\
   ```
   
   File yang diperlukan:
   ```
   ffmpeg.exe
   ffplay.exe (optional)
   ffprobe.exe (optional)
   *.dll files
   ```

### Option 2: Download dengan PowerShell (Advanced)

Buka PowerShell as Administrator dan jalankan:

```powershell
# Download FFmpeg
$url = "https://ffmpeg.org/releases/ffmpeg-snapshot-win64.zip"
$zip = "$env:TEMP\ffmpeg.zip"
$extract = "$env:TEMP\ffmpeg-extract"

Write-Host "Downloading FFmpeg..."
Invoke-WebRequest -Uri $url -OutFile $zip

Write-Host "Extracting..."
Expand-Archive -Path $zip -DestinationPath $extract -Force

# Find ffmpeg.exe dan copy
Write-Host "Finding ffmpeg.exe..."
$ffmpeg = Get-ChildItem -Path $extract -Recurse -Filter "ffmpeg.exe" | Select-Object -First 1

if ($ffmpeg) {
    $binPath = $ffmpeg.DirectoryName
    Write-Host "Found at: $binPath"
    
    # Create destination folder
    New-Item -Type Directory -Path "G:\ffmpeg\ffmpeg-8.1\bin" -Force | Out-Null
    
    # Copy all files
    Copy-Item "$binPath\*" -Destination "G:\ffmpeg\ffmpeg-8.1\bin\" -Force
    Write-Host "Copied to G:\ffmpeg\ffmpeg-8.1\bin"
} else {
    Write-Host "ffmpeg.exe not found!"
}

# Cleanup
Remove-Item $zip
Remove-Item $extract -Recurse
```

### Option 3: Use Pre-compiled Builds

Alternative downloads:
- https://github.com/BtbN/FFmpeg-Builds/releases (latest builds)
- https://www.gyan.dev/ffmpeg/builds/ (GUI installer available)

## ✅ Verification

Setelah extract, verify bahwa FFmpeg berfungsi:

```cmd
G:\ffmpeg\ffmpeg-8.1\bin\ffmpeg.exe -version
```

Should output FFmpeg version info.

## 🎯 Next Steps

Setelah FFmpeg siap, jalankan:

```cmd
cd G:\asmr
python livestream.py
```

## 📞 Troubleshooting

**Error: ffmpeg.exe not found**
- Check path: `G:\ffmpeg\ffmpeg-8.1\bin\ffmpeg.exe` harus exist
- Verify dengan: `dir G:\ffmpeg\ffmpeg-8.1\bin`

**Error: ffmpeg.exe is not executable**
- Copy semua .dll files juga dari bin folder
- Check Windows Defender tidak block ffmpeg.exe

**Error: Python tidak menemukan FFmpeg**
- Pastikan path di config.json benar
- Restart Python setelah extract FFmpeg

---

**Done? Run: `python livestream.py`** 🚀
