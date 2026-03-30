# Menjalankan Stream di Android via Termux

Panduan ini membuat HP Android Anda menjadi host proses streaming. Script tetap push ke YouTube RTMP, jadi Android bertindak sebagai mesin/server yang menjalankan FFmpeg dan Python.

## 1. Install paket di Termux

```bash
pkg update && pkg upgrade
pkg install python ffmpeg openssh termux-tools
```

Opsional tapi direkomendasikan:

```bash
pkg install tmux
termux-wake-lock
```

`termux-wake-lock` penting supaya proses tidak tidur saat layar mati.

## 2. Pindahkan project ke storage Android

Contoh:

```bash
termux-setup-storage
cp -r /sdcard/Download/asmr ~/asmr
cd ~/asmr
```

Atau copy project ke `~/asmr`.

## 3. Ubah `config.json`

Pada Android/Termux, ubah blok `ffmpeg` jadi:

```json
"ffmpeg": {
  "path": ""
}
```

Kosong berarti script akan memakai `ffmpeg` dari PATH Termux.

## 4. Jalankan stream

```bash
cd ~/asmr
python livestream.py
```

## 5. Jika Android ingin Anda akses seperti server

Jalankan SSH server di Termux:

```bash
sshd
```

Cek user dan IP:

```bash
whoami
ip addr show wlan0
```

Port default Termux SSH adalah `8022`, jadi dari laptop:

```bash
ssh -p 8022 <user-termux>@<ip-android>
```

Setelah itu Anda bisa start stream dari jarak jauh dan Android tetap menjadi host prosesnya.

## 6. Menjaga stream tetap hidup

Pakai `tmux`:

```bash
tmux new -s ytstream
cd ~/asmr
python livestream.py
```

Keluar tanpa menghentikan stream:

```bash
Ctrl+B lalu D
```

Masuk lagi:

```bash
tmux attach -t ytstream
```

## Catatan penting

- Upload internet Android harus stabil.
- Matikan optimasi baterai untuk Termux.
- Gunakan charger saat stream panjang.
- Jika video ada di `/sdcard`, aksesnya lebih lambat daripada di `~/asmr`.
