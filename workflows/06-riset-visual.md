# Tahap 6 — Riset Visual

## Tujuan

Mengumpulkan aset visual pendukung: rekaman artefak, B-roll, grafis data, screen recording, dan
stok.

Visual punya dua pekerjaan, dan urutannya penting:

1. **Membawa bukti.** Menampilkan angka, dokumen, dan keputusan yang dibahas.
2. **Menjaga perhatian.** Mengganti gambar ketika ide berganti.

Kebanyakan sistem hanya mengerjakan nomor 2. Hasilnya video yang ramai tetapi tidak membuktikan
apa pun.

---

## Aturan Artefak Wajib

Setiap video harus memuat **minimal satu artefak yang terlihat di layar**, bukan hanya disebut.

| Jenis artefak | Contoh | Kekuatan |
|---|---|---|
| Spreadsheet | Tabel margin per layanan | Paling kuat, bisa dipause penonton |
| Dashboard | Grafik churn bulanan | Menunjukkan skala |
| Invoice / tagihan | Nilai kontrak yang disamarkan | Konkret |
| Dokumen | SOP, kontrak, catatan rapat | Menunjukkan proses nyata |
| Tangkapan layar keputusan | Email, pesan, catatan | Personal |
| Foto / rekaman | Tempat, tim, produk | Konteks |

**Aturan:**

- Artefak diambil dari fact sheet Tahap 3. Bukan dibuat baru untuk kamera.
- Angka di layar harus sama dengan angka di naskah. Jangan dibulatkan berbeda.
- Kalau artefak sensitif, samarkan dulu sesuai aturan izin data.
- Kalau video tidak punya artefak, kembali ke Tahap 1. Jangan cari B-roll untuk menutupinya.

> [!IMPORTANT]
> B-roll kantor tidak membawa bukti. Rekaman layar spreadsheet milik sendiri membawa bukti.
> Prioritaskan yang kedua.

---

## Kategori Visual

| Kategori | Deskripsi | Contoh |
|---|---|---|
| **A-roll** | Rekaman utama | Talking head / voice over |
| **Artefak** | Rekaman dokumen dan data milik sendiri | Spreadsheet, dashboard, invoice |
| **B-roll** | Footage pendukung | Orang bekerja, rapat, layar |
| **Grafis data** | Visualisasi angka | Bar chart, line chart |
| **Diagram** | Visualisasi konsep | Flowchart, matriks |
| **Teks overlay** | Kata kunci dan penekanan | "Margin = 6%" |
| **Screen recording** | Rekaman alat | Demo spreadsheet |
| **Animasi** | Motion graphic | Alur funnel |

---

## Alur Kerja

### 1. Baca naskah per segmen

Setiap penanda `[B-ROLL]`, `[GRAFIS]`, `[TEKS-LAYAR]`, `[SCREEN-REC]`, `[ANIMASI]` membutuhkan
aset.

### 2. Tandai artefak utama

Cari penanda `[SCREEN-REC]` yang berasal dari fact sheet. Itu artefak wajib. Kerjakan paling awal,
karena kalau artefak tidak bisa direkam, video tidak bisa diproduksi.

### 3. Buat peta visual

| Segmen | Waktu | Jenis | Deskripsi | Sumber | Status |
|---|---|---|---|---|---|
| Hook | 0:00–0:05 | Teks overlay | "Omzet +31%, profit −9%" | Buat sendiri | ☐ |
| Bukti pertama | 0:05–0:30 | Screen rec | Spreadsheet margin, 3 baris ditandai | Rekam sendiri | ☐ |
| Poin 1 | 0:40–2:30 | Grafis | Omzet vs margin per layanan | Canva | ☐ |

### 4. Cari dan buat aset

**Artefak — rekam sendiri:**

- Buka file asli di layar penuh. Rekam dengan OBS atau QuickTime.
- Sorot bagian yang dibahas. Jangan biarkan penonton mencari sendiri.
- Pause di angka penting selama 2–3 detik.

**B-roll stok gratis:**

| Sumber | Lisensi |
|---|---|
| Pexels | CC0, komersial |
| Pixabay | CC0, komersial |
| Unsplash | Gratis, komersial (foto) |

**B-roll stok berbayar:** Storyblocks, Envato Elements.

**B-roll AI:**

- Boleh dipakai untuk ilustrasi konsep yang tidak bisa direkam.
- Wajib ditandai di `visual-map.md`: "AI — [alat] — [prompt ringkas]".
- Jangan dipakai untuk menampilkan orang yang seolah-olah Fadhil atau klien nyata.
- Jangan dipakai untuk menggantikan artefak. Artefak harus asli.

**Tips pencarian:** cari dalam bahasa Inggris, unduh resolusi tertinggi.

### 5. Buat grafis data

**Aturan layar ponsel:**

- Hilangkan gridline dan legenda jauh.
- Label langsung pada data.
- Warna brand untuk data utama, abu-abu untuk pembanding.
- Satu grafis = satu pesan.
- Progressive reveal sesuai narasi.

**Warna 60-30-10:** 60% latar, 30% struktur, 10% aksen.

**Tipe grafis:**

| Tipe | Kapan |
|---|---|
| Bar horizontal | Perbandingan item |
| Line | Tren waktu, maksimal 2–3 garis |
| Angka callout | Satu statistik |
| Matriks 2×2 | Keputusan dua variabel |
| Diagram alur | Proses |
| Side-by-side | Dua pilihan |

**Angka callout:** angka besar 40–60 pt, satu baris konteks 16–20 pt, sumber selalu disertakan.

### 6. Tulis teks overlay

- 5–7 kata per overlay.
- Untuk kata kunci, definisi, takeaway.
- Font konsisten dengan brand.
- Safe zone: jangan di 20% bawah dan 10% atas.

### 7. Organisasi file

```
content/assets/[YYYY-MM-DD]-[judul-pendek]/
├── artefak/
│   ├── margin-per-layanan.mp4
│   └── dashboard-churn.png
├── b-roll/
├── graphics/
├── overlays/
├── screen-rec/
└── visual-map.md
```

### 8. Periksa lisensi

- [ ] Boleh komersial
- [ ] Atribusi siap (kalau perlu)
- [ ] Resolusi minimal 1920×1080
- [ ] Aset AI ditandai

---

## Aturan Pacing Visual

Aturan lama — "ganti visual setiap 3–5 detik" dan "tidak ada talking head lebih dari 10 detik" —
dihapus. Tidak ada sumbernya, dan untuk video 12 menit artinya 150–240 pergantian. Itu pekerjaan
editor penuh waktu, bukan pekerjaan sampingan pemilik bisnis.

**Yang dipakai sekarang:**

1. **Satu ide, satu visual.** Visual berganti ketika idenya berganti, bukan ketika stopwatch
   berbunyi.
2. **Tidak ada segmen lebih dari 60 detik tanpa perubahan visual.** Ini standar pilot, bukan
   standar final.
3. **Segmen data boleh lebih cepat.** Kalau satu kalimat memuat tiga angka, tampilkan tiga kali.
   Di sini pergantian tiap 3–5 detik masuk akal, karena setiap angka butuh ruang sendiri.
4. **Artefak boleh diam lama.** Spreadsheet yang sedang dijelaskan tidak perlu dipotong setiap
   lima detik. Penonton sedang membaca.

**Alur variasi:** A-roll → artefak → grafis → A-roll → teks → B-roll.

> [!TIP]
> Kalau ragu antara menambah visual atau membiarkan satu visual lebih lama, biarkan lebih lama.
> Visual yang tepat selama 20 detik lebih baik daripada lima visual acak.

---

## Alat

| Alat | Fungsi |
|---|---|
| Canva Pro | Grafis, diagram, templat |
| Figma | Grafis kustom |
| After Effects / Premiere | Animasi |
| OBS Studio | Screen recording |
| QuickTime | Screen recording sederhana |

---

## Gerbang Keluaran

- [ ] Minimal satu artefak terekam dan masuk peta visual
- [ ] Folder aset di `content/assets/`
- [ ] Peta visual lengkap, ditandai per segmen
- [ ] Semua lisensi dicek
- [ ] Aset AI ditandai
- [ ] Tidak ada segmen lebih dari 60 detik tanpa perubahan visual

---

## Kesalahan Umum

- Tidak punya artefak, lalu menutupinya dengan B-roll.
- Memakai aset tanpa memeriksa lisensi.
- Grafis terlalu rumit untuk ponsel.
- Chart statis tanpa progressive reveal.
- B-roll tidak relevan dengan yang dibahas.
- Tidak membuat peta visual.
- Mengunduh resolusi rendah.
- Mengejar pergantian visual setiap beberapa detik sampai editing tidak pernah selesai.
- Memakai aset AI untuk menggantikan dokumen asli.

---

## Hubungan dengan Tahap Lain

| Dari | Yang diterima |
|---|---|
| Tahap 4 — Naskah | Penanda visual dan artefak |
| Tahap 3 — Riset | Angka dan dokumen asli |

| Ke | Yang dikirim |
|---|---|
| Tahap 7 — Editing | Folder aset dan peta visual |
| Tahap 8 — Penerbitan | Thumbnail dan aset pendukung |
