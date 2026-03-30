# YouTube Livestreaming - Advanced Mode

## 📋 Fitur Baru

✅ **Video Random** - Setiap 60 detik, video diganti dengan video random lainnya
✅ **Music Background** - File musik MP3 diputar looping di background sepanjang stream
✅ **720p Quality** - Kualitas HD dengan bitrate 2500k (lebih ringan)
✅ **Auto-Stop** - Streaming otomatis berhenti setelah 10 jam
✅ **Intelligent Cycling** - Video di-loop dalam kategori 1 menit sebelum berganti

---

## 🚀 Setup

### 1. Siapkan File Musik

**Folder Structure:**
```
g:\asmr\
├── livestream.py
├── config.json
├── assets/
│   └── music.mp3  ← Taruh musik di sini!
├── ffmpeg-master-latest-win64-gpl/
└── *.mp4 (video files)
```

**Cara setup musik:**
1. Cari file MP3 favorit Anda
2. Copy ke folder: `G:\asmr\assets\music.mp3`
3. Nama **harus** `music.mp3`!

### 2. Verifikasi Config

Buka `config.json`, pastikan seperti ini:

```json
{
  "youtube": {
    "stream_key": "rxyq-75rp-xu9x-ecvw-2r8d"
  },
  "streaming": {
    "bitrate": "2500k",
    "resolution": "1280x720",
    "fps": "30",
    "video_duration_seconds": 60,
    "max_stream_hours": 10
  },
  "audio": {
    "music_file": "assets/music.mp3"
  },
  "ffmpeg": {
    "path": "G:\\asmr\\ffmpeg-master-latest-win64-gpl\\ffmpeg-master-latest-win64-gpl\\bin"
  }
}
```

---

## ▶️ Cara Menjalankan

```cmd
cd G:\asmr
python livestream.py
```

**Output akan terlihat seperti:**
```
======================================================================
YOUTUBE LIVESTREAMING - ADVANCED MODE
======================================================================
Mode: Video random setiap 60s + musik background
Videos: 7 file tersedia
Musik: music.mp3 (looping)
Auto-stop: 10 jam
Kualitas: 1280x720 @ 30fps
Bitrate: 2500k
======================================================================

[INFO] Streaming... (Press Ctrl+C to stop)

[CYCLE 1] 00:00:05 / 09:59:55
  Video: ASMR_nature_video.mp4
  Audio: Background music
  Duration: 60s ✓

[CYCLE 2] 00:01:10 / 09:59:00
  Video: ASMR_video_water.mp4
  Audio: Background music
  Duration: 60s ✓
```

---

## ⚙️ Konfigurasi Detail

### `video_duration_seconds`
Berapa lama tiap video ditampilkan sebelum random ke video berikutnya.
- Default: 60 (1 menit)
- Ubah ke 120 untuk 2 menit per video

### `max_stream_hours`
Berapa jam stream akan berjalan sebelum auto-stop.
- Default: 10
- Ubah ke 24 untuk 24 jam
- Ubah ke 0 untuk unlimited (tidak ada auto-stop)

### `music_file`
Path ke file musik relative dari folder utama.
- Default: `assets/music.mp3`
- Harus `.mp3` format
- Jika tidak ada, stream berjalan tanpa musik

### `bitrate` & `resolution`
**Presets untuk berbagai kecepatan internet:**

**1 Mbps:**
```json
"bitrate": "1000k",
"resolution": "640x360"
```

**2.5 Mbps (Default):**
```json
"bitrate": "2500k",
"resolution": "1280x720"
```

**5 Mbps:**
```json
"bitrate": "5000k",
"resolution": "1920x1080"
```

---

## 🎵 Musik Background

### Format Support
- .mp3 (recommended)
- .wav
- .aac
- .flac

### Tips Musik:
1. **Looping Seamless** - Gunakan musik yang bisa loop smooth
2. **Durasi Panjang** - Minimal 1-2 menit agar tidak terdengar repetitif
3. **Format** - MP3 lebih ringan dibanding WAV
4. **Volume** - Pastikan tidak terlalu keras saat di-stream

### Cara Crop Musik (14 detik jadi 1 menit):
Gunakan Audacity atau ffmpeg:
```cmd
ffmpeg -i original.mp3 -ss 0 -t 60 music.mp3
```

---

## 📊 Live Monitoring

### Cek Status di YouTube
- Dashboard: https://www.youtube.com/live_dashboard
- Lihat live view: https://www.youtube.com/@YourChannel/live

### Terminal Output
Setiap cycle menampilkan:
- **Elapsed Time** - Berapa lama sudah streaming
- **Remaining Time** - Sisa waktu sampai 10 jam
- **Current Video** - Video mana yang diputar
- **Duration** - Berapa lama video ini

---

## 🛑 Stop Streaming

**Graceful Stop:**
```
Press Ctrl+C di terminal
```

**Force Stop:**
```
Close FFmpeg window
atau task kill ffmpeg.exe
```

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| "Music file tidak ditemukan" | Pastikan path `assets/music.mp3` benar |
| "Video tidak berganti-ganti" | Check `video_duration_seconds` di config |
| "Stream stop sendiri di 10 jam" | Set `"max_stream_hours": 0` untuk unlimited |
| Stream lag/stuttering | Turunkan bitrate ke 1500k atau resolution ke 640x360 |
| FFmpeg error | Verify FFmpeg sudah installed & musik/video exist |

---

## 📈 Performance Tips

1. **CPU Usage**
   - Preset `veryfast` sudah optimized
   - Jika masih lag, ubah ke `ultrafast`

2. **Bandwidth**
   - Bitrate 2500k butuh ~312 KB/s upload
   - Untuk internet 10 Mbps cukup aman

3. **Long Runs**
   - Untuk 24+ jam, monitor temperature
   - Pastikan FFmpeg tidak crash

4. **Audio Sync**
   - Audio musik dengan video sync otomatis
   - `-shortest` flag memastikan durasi sama

---

## 📝 Config Cheat Sheet

**Keep Stream Running (Unlimited):**
```json
"max_stream_hours": 0
```

**Change video every 5 minutes:**
```json
"video_duration_seconds": 300
```

**Use custom music location:**
```json
"music_file": "D:/Music/my_background_music.mp3"
```

**Ultra Low Bandwidth:**
```json
"bitrate": "1000k",
"resolution": "640x360",
"fps": "24"
```

---

## ✅ Checklist Sebelum Stream

- [x] `config.json` sudah benar dengan stream key
- [x] `assets/music.mp3` sudah di-copy
- [x] Video files ada di `G:\asmr\`
- [x] FFmpeg terinstall dan working
- [x] Internet connection stabil
- [x] Cek YouTube dashboard siap

---

## 🚀 Mulai Streaming

```cmd
cd G:\asmr
python livestream.py
```

**Selesai! Stream akan berjalan dengan video random setiap 1 menit + musik background, otomatis stop setelah 10 jam.** 🎉

---

For issues: Check config.json, verify music.mp3 exists, and ensure FFmpeg working properly.
