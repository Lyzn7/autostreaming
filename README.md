# YouTube Livestreaming - Python Version

Complete Python solution untuk streaming video ke YouTube dengan auto-looping.

## 📋 Quick Start

### 1. Install Python (Sekali saja)

Download dan install dari: https://www.python.org/downloads/

**PENTING**: Pilih "Add Python to PATH" saat install!

### 2. Install FFmpeg

Download dari:
- https://ffmpeg.org/download.html
- Atau: https://github.com/GyanD/codexffmpeg/releases

Extract ke `C:\ffmpeg` dan add `C:\ffmpeg\bin` ke Windows PATH

### 3. Setup YouTube Stream Key

1. Buka: https://www.youtube.com/live_dashboard
2. Klik: "Go Live"
3. Salin: Stream Key (bukan URL)
4. Edit: `config.json`
   ```json
   "stream_key": "xxxx-xxxx-xxxx-xxxxxxxxxx"
   ```

### 4. Run Python Script

**Option 1 - Command Prompt:**
```cmd
cd g:\asmr
python livestream.py
```

**Option 2 - Batch File:**
```cmd
Double-click: run.bat
```

## 📝 Config (config.json)

```json
{
  "youtube": {
    "rtmp_url": "rtmp://a.rtmp.youtube.com/live2",
    "stream_key": "YOUR_STREAM_KEY_HERE",
    "stream_title": "ASMR Livestream",
    "stream_description": "Looping livestream content"
  },
  "streaming": {
    "bitrate": "5000k",
    "resolution": "1920x1080",
    "fps": "30",
    "audio_bitrate": "192k",
    "enable_looping": true,
    "video_extension": ".mp4"
  }
}
```

### Quality Presets

**Low Bandwidth (Internet lambat):**
```json
"bitrate": "2500k",
"resolution": "1280x720",
"fps": "24"
```

**Standard (Recommended):**
```json
"bitrate": "5000k",
"resolution": "1920x1080",
"fps": "30"
```

**High Quality:**
```json
"bitrate": "8000k",
"resolution": "1920x1080",
"fps": "60"
```

## 🎥 Video Files

Semua file `.mp4`, `.mov`, `.avi`, `.mkv` di folder ini akan auto-detect. 

Contoh:
```
ASMR_nature_video_202603291409.mp4
ASMR_video_water_202603291411.mp4
Make_nature_ASMR_202603291409.mp4
```

Script akan menggunakan video pertama yang ditemukan.

## 🚀 Fitur

✅ Auto-detect video files
✅ Infinite looping
✅ Configurable quality
✅ Error handling
✅ Simple setup
✅ No batch file issues

## ❌ Troubleshooting

| Problem | Solution |
|---------|----------|
| "Python not found" | Install Python dari https://www.python.org/ |
| "FFmpeg not found" | Install dari https://ffmpeg.org/download.html |
| "config.json missing" | Run dari folder g:\asmr\ |
| "Stream key error" | Edit config.json dengan stream key yang benar |
| "Video not found" | Copy .mp4 files ke folder ini |

## 📂 Files

- `livestream.py` - Main Python script
- `config.json` - Configuration file
- `run.bat` - Batch launcher (optional)
- `README.md` - This file

## 💡 Tips

1. **Test First**: Stream ke private/unlisted video dulu
2. **Keep FFmpeg Window Open**: Jangan tutup saat streaming
3. **Bandwidth**: Min 10 Mbps upload untuk 5000k bitrate
4. **Stop Stream**: Press Ctrl+C di command prompt

## 🎓 Usage Examples

**Basic streaming:**
```cmd
python livestream.py
```

**Custom config:**
```python
# Edit livestream.py, ubah config_file parameter
streamer = YouTubeLivestreamer("custom_config.json")
```

## 🔗 Links

- YouTube Live: https://www.youtube.com/live_dashboard
- Get Stream Key: https://www.youtube.com/live_dashboard
- FFmpeg Docs: https://ffmpeg.org/
- Python Docs: https://python.org/

---

**Ready? Run: `python livestream.py` atau double-click `run.bat`** 🚀
