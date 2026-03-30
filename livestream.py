#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YouTube Livestreaming - Advanced with Progress
- Video random setiap 1 menit (terus-menerus)
- Music background looping
- Auto-stop setelah beberapa jam
- Progress indicator dengan persentase keseluruhan
"""

import glob
import json
import os
import random
import subprocess
import sys
import threading
import time


class AdvancedYouTubeLivestreamer:
    def __init__(self, config_file="config.json"):
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_file = self.resolve_config_path(config_file)
        self.config = self.load_config()
        self.ffmpeg_path = self.get_ffmpeg_path()
        self.start_time = None
        self.max_duration = None

    def resolve_config_path(self, config_file):
        """Resolve path config agar tetap benar saat dijalankan dari folder lain."""
        if os.path.isabs(config_file):
            return config_file
        return os.path.join(self.current_dir, config_file)

    def load_config(self):
        """Load konfigurasi dari file JSON."""
        try:
            with open(self.config_file, "r", encoding="utf-8") as file_handle:
                return json.load(file_handle)
        except FileNotFoundError:
            print(f"[ERROR] File {self.config_file} tidak ditemukan!")
            return None
        except json.JSONDecodeError:
            print(f"[ERROR] File {self.config_file} format invalid!")
            return None

    def get_ffmpeg_path(self):
        """Dapatkan binary FFmpeg dari config atau PATH sistem."""
        ffmpeg_binary = "ffmpeg.exe" if os.name == "nt" else "ffmpeg"

        ffmpeg_config = (self.config or {}).get("ffmpeg", {})
        configured_path = str(ffmpeg_config.get("path", "")).strip()
        if not configured_path:
            return ffmpeg_binary

        configured_path = os.path.expanduser(configured_path)
        if os.path.isdir(configured_path):
            ffmpeg_path = os.path.join(configured_path, ffmpeg_binary)
            if os.path.exists(ffmpeg_path):
                return ffmpeg_path
        elif os.path.isfile(configured_path):
            return configured_path

        return ffmpeg_binary

    def get_video_files(self):
        """Cari semua file video di folder script."""
        video_extensions = [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"]
        videos = []

        for ext in video_extensions:
            pattern = os.path.join(self.current_dir, f"*{ext}")
            videos.extend([path for path in glob.glob(pattern) if os.path.isfile(path)])

        if not videos:
            print("[ERROR] Tidak ada file video ditemukan!")
            return None

        return sorted(videos)

    def get_music_file(self):
        """Cari file musik dari config."""
        audio_config = (self.config or {}).get("audio", {})
        music_setting = audio_config.get("music_file")
        if not music_setting:
            return None

        if os.path.isabs(music_setting):
            music_path = music_setting
        else:
            music_path = os.path.join(self.current_dir, music_setting)

        if os.path.exists(music_path):
            return music_path

        print(f"[WARNING] Music file tidak ditemukan: {music_path}")
        return None

    def check_ffmpeg(self):
        """Cek apakah FFmpeg terinstall."""
        try:
            subprocess.run(
                [self.ffmpeg_path, "-version"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=5,
                check=False,
            )
            return True
        except Exception:
            return False

    def create_long_concat_file(self, videos, video_duration_seconds, max_stream_seconds):
        """Buat concat file dengan video random untuk durasi panjang."""
        concat_file = os.path.join(self.current_dir, "_temp_concat_long.txt")

        repeats_per_video = max(int(video_duration_seconds / 8), 1)
        num_videos_needed = max(int(max_stream_seconds / (video_duration_seconds * 0.8)), 100)

        with open(concat_file, "w", encoding="utf-8") as file_handle:
            for _ in range(num_videos_needed):
                video = random.choice(videos)
                for _ in range(repeats_per_video):
                    escaped_path = video.replace("\\", "\\\\").replace("'", "\\'")
                    file_handle.write(f"file '{escaped_path}'\n")

        return concat_file

    def build_ffmpeg_command(self, concat_file, music_file, max_duration_seconds):
        """Build perintah FFmpeg untuk streaming terus-menerus."""
        youtube_config = self.config["youtube"]
        streaming_config = self.config["streaming"]

        full_rtmp = f"{youtube_config['rtmp_url']}/{youtube_config['stream_key']}"
        command = [
            self.ffmpeg_path,
            "-re",
            "-protocol_whitelist",
            "file,http,https,tcp,tls,crypto",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            concat_file,
        ]

        if music_file:
            command.extend(["-stream_loop", "-1", "-i", music_file])

        command.extend(
            [
                "-c:v",
                "libx264",
                "-preset",
                "veryfast",
                "-b:v",
                streaming_config["bitrate"],
                "-maxrate",
                streaming_config["bitrate"],
                "-bufsize",
                streaming_config["bitrate"],
                "-s",
                streaming_config["resolution"],
                "-r",
                str(streaming_config["fps"]),
            ]
        )

        if music_file:
            command.extend(
                [
                    "-c:a",
                    "aac",
                    "-b:a",
                    streaming_config["audio_bitrate"],
                    "-filter_complex",
                    "[0:a][1:a]amix=inputs=2:duration=first:normalize=0[audio]",
                    "-map",
                    "0:v:0",
                    "-map",
                    "[audio]",
                ]
            )
        else:
            command.extend(
                [
                    "-c:a",
                    "aac",
                    "-b:a",
                    streaming_config["audio_bitrate"],
                ]
            )

        command.extend(
            [
                "-t",
                str(int(max_duration_seconds)),
                "-flvflags",
                "no_duration_filesize",
                "-f",
                "flv",
                full_rtmp,
            ]
        )
        return command

    def print_progress(self, elapsed, total, prefix=""):
        """Print progress bar dengan persentase."""
        if total <= 0:
            return

        percent = (elapsed / total) * 100
        filled = int(50 * elapsed // total)
        bar = "#" * filled + "-" * (50 - filled)
        print(
            f"\r{prefix} [{bar}] {percent:.1f}% "
            f"({self.format_time(elapsed)}/{self.format_time(total)})",
            end="",
            flush=True,
        )

    def start_streaming(self, videos, music_file):
        """Mulai streaming dengan satu proses FFmpeg continuous."""
        if not self.config:
            print("[ERROR] Konfigurasi tidak valid!")
            return False

        if not self.check_ffmpeg():
            print("[ERROR] FFmpeg belum terinstall atau tidak ada di PATH!")
            return False

        stream_key = self.config["youtube"]["stream_key"]
        if not stream_key or "GANTI" in stream_key or "YOUR" in stream_key:
            print("[ERROR] Stream key belum diatur!")
            return False

        video_duration = self.config["streaming"].get("video_duration_seconds", 60)
        max_hours = self.config["streaming"].get("max_stream_hours", 10)
        max_duration = max_hours * 3600

        self.start_time = time.time()
        self.max_duration = max_duration

        print("\n" + "=" * 70)
        print("YOUTUBE LIVESTREAMING - ADVANCED MODE")
        print("=" * 70)
        print(f"Mode: Video random setiap {video_duration}s + musik background (no-restart)")
        print(f"Videos: {len(videos)} file tersedia")
        if music_file:
            print(f"Musik: {os.path.basename(music_file)} (looping, tidak restart)")
        else:
            print("Musik: tidak dipakai")
        print(f"Auto-stop: {max_hours} jam ({self.format_time(max_duration)})")
        print(
            f"Kualitas: {self.config['streaming']['resolution']} @ "
            f"{self.config['streaming']['fps']}fps"
        )
        print(f"Bitrate: {self.config['streaming']['bitrate']}")
        print(f"FFmpeg: {self.ffmpeg_path}")
        print("=" * 70)

        print(f"[1] Membuat video concat file untuk {max_hours}h streaming...", end="", flush=True)
        concat_file = self.create_long_concat_file(videos, video_duration, max_duration)
        print(" OK")

        print("[2] Building FFmpeg command...")
        command = self.build_ffmpeg_command(concat_file, music_file, max_duration)

        print(f"[3] Starting FFmpeg stream (terus-menerus selama {max_hours} jam)...")
        print("\nStreaming progress (overall):")

        process = None
        try:
            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
            )

            print("[OK] FFmpeg started - streaming active\n")

            def read_output():
                for _line in process.stderr:
                    pass

            reader_thread = threading.Thread(target=read_output, daemon=True)
            reader_thread.start()

            last_update = time.time()
            while True:
                elapsed = time.time() - self.start_time

                if elapsed >= max_duration:
                    print(f"\n[INFO] Max {max_hours} jam reached!")
                    break

                now = time.time()
                if now - last_update >= 1:
                    self.print_progress(elapsed, max_duration, "Streaming:")
                    last_update = now

                if process.poll() is not None:
                    print("\n[INFO] FFmpeg process ended")
                    break

                time.sleep(0.1)

            print("\n\n[INFO] Stopping stream...")
            process.terminate()
            try:
                process.wait(timeout=5)
            except Exception:
                process.kill()

            print("[OK] Stream stopped")
            return True

        except KeyboardInterrupt:
            print("\n\n[INFO] Stopped by user")
            if process:
                try:
                    process.terminate()
                    process.wait(timeout=2)
                except Exception:
                    pass
            return True
        except Exception as exc:
            print(f"\n[ERROR] {str(exc)}")
            import traceback

            traceback.print_exc()
            return False

    def format_time(self, seconds):
        """Format detik ke HH:MM:SS."""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"

    def cleanup(self):
        """Cleanup temporary files."""
        temp_files = [
            os.path.join(self.current_dir, "_temp_concat_long.txt"),
            os.path.join(self.current_dir, "_temp_concat.txt"),
        ]
        for temp_file in temp_files:
            try:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
            except Exception:
                pass


def main():
    print("\n" + "=" * 70)
    print("YouTube Livestreaming - Advanced")
    print("(Continuous Music Loop - Video Random Per Minute)")
    print("=" * 70 + "\n")

    streamer = AdvancedYouTubeLivestreamer()

    print("[1] Mencari file video...")
    videos = streamer.get_video_files()
    if not videos:
        sys.exit(1)

    print(f"[OK] Ditemukan {len(videos)} video(s)")

    print("[2] Mencari file musik...")
    music_file = streamer.get_music_file()
    if music_file:
        print(f"[OK] Musik: {os.path.basename(music_file)}")
    else:
        print("[INFO] Musik tidak ditemukan - streaming tanpa musik")

    print("[3] Memulai streaming...")
    success = streamer.start_streaming(videos, music_file)

    streamer.cleanup()

    if not success:
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"\n[FATAL ERROR] {str(exc)}")
        import traceback

        traceback.print_exc()
        sys.exit(1)
