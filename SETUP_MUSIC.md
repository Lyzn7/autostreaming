# YouTube Livestreaming - Setup Advanced Mode

## 🚀 Quick Setup (3 Steps)

### Step 1️⃣: Get Music File
Put your MP3 file here:
```
G:\asmr\assets\music.mp3
```

Folder structure should look like:
```
g:\asmr\
├── livestream.py
├── config.json
├── assets\
│   └── music.mp3         ← PUT YOUR MUSIC HERE!
├── ffmpeg-master-latest-win64-gpl\
└── *.mp4 (videos)
```

### Step 2️⃣: Verify Setup
```cmd
cd G:\asmr
python setup_advanced.bat
```

Or check manually:
- ✅ Python working
- ✅ FFmpeg working
- ✅ Video files exist
- ✅ Music file at `assets\music.mp3`

### Step 3️⃣: Start Streaming
```cmd
python livestream.py
```

---

## 📋 Status Report

**Your Stream Configuration:**
- Resolution: **1280x720** (720p HD)
- Bitrate: **2500 kbps** (optimized for most internet)
- FPS: **30 fps**
- Video Duration: **60 seconds** (each video plays 1 min then random change)
- Music: **Looping background**
- Auto-Stop: **10 hours**

---

## 📊 Real-Time Output

When streaming, you'll see:
```
[CYCLE 1] 00:00:15 / 09:59:45
  Video: ASMR_nature_video.mp4
  Audio: Background music
  Duration: 60s ✓

[CYCLE 2] 00:01:20 / 09:58:40
  Video: ASMR_water_video.mp4
  Audio: Background music
  Duration: 60s ✓
```

Showing:
- Current cycle number
- Time elapsed / Time remaining
- Which video is playing
- Status of music playback

---

## 🎵 Music Format

Supported formats:
- .mp3 (recommended, most compressed)
- .wav
- .aac
- .flac

**Tips:**
- Looping music recommended (no abrupt endings)
- Duration: 1-2 minutes is ideal
- Check file in: `G:\asmr\assets\music.mp3`

---

## ⚙️ Customize Settings

Edit `config.json`:

**Change video duration to 2 minutes:**
```json
"video_duration_seconds": 120
```

**Change to 24 hours (instead of 10):**
```json
"max_stream_hours": 24
```

**Unlimited duration (no auto-stop):**
```json
"max_stream_hours": 0
```

**Lower bitrate (for slower internet):**
```json
"bitrate": "1500k",
"resolution": "1024x576"
```

---

## 📞 Troubleshooting

**"Music file tidak ditemukan"**
- Check: Is file at `G:\asmr\assets\music.mp3`?
- Verify: File is named exactly `music.mp3`

**"Video tidak berganti setiap 1 menit"**
- Check: `video_duration_seconds` is 60 in config.json
- Verify: FFmpeg is running properly

**"Stream stops after 10 hours"**
- This is normal! Set `max_stream_hours: 0` for unlimited
- Or set to `24` for 24 hours

**"Lag/stuttering during stream"**
- Lower bitrate: `2500k` → `1500k`
- Lower resolution: `1280x720` → `1024x576`
- Lower FPS: `30` → `24`

**"Can't find video files"**
- Make sure `.mp4` files in `G:\asmr\` folder
- Check folder is not empty: `dir G:\asmr\*.mp4`

---

## ✅ Verification Checklist

Before streaming:
- [ ] `config.json` has YOUR YouTube stream key
- [ ] `assets\music.mp3` exists and is not corrupted
- [ ] `G:\asmr\*.mp4` video files exist (at least 1)
- [ ] FFmpeg working: `ffmpeg.exe -version` runs OK
- [ ] Internet is stable
- [ ] YouTube dashboard is accessible

---

## 🎯 Start Now!

```cmd
cd G:\asmr
python livestream.py
```

**Video will be random every 60 seconds, music plays throughout, auto-stops after 10 hours!** 🚀

For detailed guide: See `ADVANCED_GUIDE.md`
