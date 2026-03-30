#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FFmpeg Auto-Download & Setup for Windows
Download pre-compiled FFmpeg dari GitHub
"""

import os
import urllib.request
import zipfile
import json
import shutil
from pathlib import Path

def download_ffmpeg():
    """Download FFmpeg pre-compiled binary"""
    
    print("\n" + "="*60)
    print("FFmpeg Auto-Download & Setup")
    print("="*60 + "\n")
    
    # Try multiple download sources
    urls = [
        "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip",
        "https://github.com/jin-eld/build-ffmpeg/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip",
    ]
    
    download_dir = "G:\\ffmpeg\\download"
    extract_dir = "G:\\ffmpeg\\ffmpeg-build"
    final_dir = "G:\\ffmpeg\\ffmpeg-8.1"
    
    url = None
    
    # Create download directory
    os.makedirs(download_dir, exist_ok=True)
    
    zip_file = os.path.join(download_dir, "ffmpeg.zip")
    
    print(f"[1] Downloading FFmpeg 8.1 from GitHub...")
    print(f"    URL: {url}")
    print(f"    Size: ~200MB (bisa lama)")
    print()
    
    try:
        # Download dengan progress
        def download_progress(block_num, block_size, total_size):
            downloaded = block_num * block_size
            percent = min(downloaded * 100 // total_size, 100)
            print(f"\r    Downloaded: {percent}%", end='', flush=True)
        
        urllib.request.urlretrieve(url, zip_file, download_progress)
        print()  # New line after progress
        
        print("[OK] Download selesai\n")
        
        print(f"[2] Extracting to {extract_dir}...")
        
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
        
        print("[OK] Extract selesai\n")
        
        # Find ffmpeg.exe dalam directoryi
        print(f"[3] Organizing files...")
        
        # Biasanya di extract_dir/ffmpeg-8.1-full_build-gpl/bin/
        for root, dirs, files in os.walk(extract_dir):
            if 'ffmpeg.exe' in files:
                bin_path = root
                ffmpeg_exe = os.path.join(bin_path, 'ffmpeg.exe')
                print(f"    Found: {ffmpeg_exe}")
                
                # Copy ke final location
                os.makedirs(final_dir, exist_ok=True)
                shutil.copy(ffmpeg_exe, os.path.join(final_dir, 'ffmpeg.exe'))
                
                # Copy dll juga jika ada
                for file in files:
                    if file.endswith('.dll'):
                        shutil.copy(os.path.join(bin_path, file), 
                                  os.path.join(final_dir, file))
                
                print("[OK] Files copied to", final_dir)
                break
        
        # Update config.json
        print(f"\n[4] Updating config.json...")
        
        config_path = os.path.join(os.path.dirname(__file__), "config.json")
        
        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            # Update path (dengan double backslash untuk JSON)
            config['ffmpeg'] = {
                'path': final_dir
            }
            
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            
            print(f"[OK] Config updated with: {final_dir}")
        
        # Cleanup
        print(f"\n[5] Cleaning up download files...")
        try:
            shutil.rmtree(download_dir)
            shutil.rmtree(extract_dir)
            print("[OK] Cleanup done")
        except:
            pass
        
        print("\n" + "="*60)
        print("✓ FFmpeg setup complete!")
        print("="*60)
        print("\nSekarang jalankan:")
        print("  python livestream.py")
        print()
        
        return True
        
    except Exception as e:
        print(f"\n[ERROR] {str(e)}")
        print("\n[INFO] Alternatively, download manual:")
        print("  1. https://ffmpeg.org/download.html")
        print("  2. Extract ke: G:\\ffmpeg\\ffmpeg-8.1\\bin")
        print("  3. Copy ffmpeg.exe dan dll files disana")
        return False

if __name__ == "__main__":
    try:
        success = download_ffmpeg()
        if not success:
            input("\nPress Enter to exit...")
            exit(1)
    except KeyboardInterrupt:
        print("\n\n[INFO] Download cancelled")
        exit(1)
