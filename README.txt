# YouTube Livestream - Shortest Guide

## 3-Step Quick Start

### Step 1: YouTube Setup
1. Go: https://www.youtube.com/live_dashboard
2. Click: "Go Live"
3. Copy: Stream Key (not URL)

### Step 2: Edit stream.bat
1. Open: `stream.bat` with Notepad
2. Find: `set "STREAM_KEY=YOUR_YOUTUBE_STREAM_KEY_HERE"`
3. Replace with stream key from Step 1
4. Save

### Step 3: FFmpeg + Start
1. **Install FFmpeg:**
   - Download: https://ffmpeg.org/download.html (or https://github.com/GyanD/codexffmpeg/releases)
   - Extract to: `C:\ffmpeg`
   - Add to PATH: `C:\ffmpeg\bin`

2. **Put video in folder:** `g:\asmr\`

3. **Run:** Double-click `stream.bat`

## Done! 🎉

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "ffmpeg not found" | Install FFmpeg from https://ffmpeg.org |
| "Stream key error" | Edit stream.bat, check stream key is correct |
| "No video found" | Put .mp4/.mov/.avi/.mkv in g:\asmr\ |
| "Streaming offline" | Wait 5-10 sec, check stream key, try again |

## More Reference

- More options: Open `menu.bat`
- Advanced config: Edit `config.json`

---

**Ready? Double-click: `stream.bat` or `menu.bat`**
