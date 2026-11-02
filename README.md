# Sistem Produksi Konten

Panduan lengkap ada di `AGENTS.md`. Berkas ini hanya menjelaskan cara menjalankan
bagian yang sudah punya alat.

## Database ide

Satu berkas: `database/database.db`. Skema: `database/skema.sql`. Penjelasan kolom
dan rumus: `database/README.md`.

```bash
python3 tools/ranking.py            # urut prioritas, lalu skor
python3 tools/ranking.py --detail   # dengan rincian skor
python3 tools/ranking.py --semua    # ikutkan yang gugur
python3 tools/tambah-ide.py x.json  # tambah ide baru dari hasil pindai
```

## Alat riset pasar

```bash
python3 tools/pindai-youtube.py "cara menaikkan margin"   # 3 putaran
python3 tools/cek-video.py <videoId>                      # baca chapter dan deskripsi
python3 tools/ambil-daftar-video.py Moon-Real             # daftar video channel
```

## Alur kerja

Dua pipeline, dipisah:

- **Produksi** — `workflows/produksi/`. Peta sepuluh tahap ada di
  `workflows/produksi/00-pipeline.md`. SOP per tahap dibuka hanya saat mengerjakan tahap itu.
- **Analisis** — `workflows/analisis/00-pipeline.md`. Review mingguan seluruh pipeline produksi.
  Belum berjalan; baru dipakai setelah video pilot punya data 7 hari.

Peta keduanya ada di `workflows/README.md`. Panduan utama proyek ada di `AGENTS.md`.

Hasil pindai tersimpan di `content/pindai/`. Ide yang lolos masuk ke database
lewat `tools/tambah-ide.py`. Catatan review pipeline mingguan masuk ke `content/analisis/`.

## Yang belum berjalan

- `content/log-keputusan.md` masih kosong. Ini satu-satunya sumber bukti tipe A.
  Selama kosong, tidak ada ide yang bisa mendapat skor bukti 5.
- Belum ada otomatisasi dari hasil pindai ke database. Berkas JSON untuk
  `tambah-ide.py` masih disusun manual setelah membaca hasil pindai.
- Belum ada video pilot yang terbit, jadi belum ada baseline metrik.
