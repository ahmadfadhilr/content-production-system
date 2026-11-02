# AGENTS.md — Sistem Produksi Konten Personal Brand

File ini adalah panduan utama untuk AI yang bekerja di proyek ini. Baca bagian yang relevan
sebelum mengerjakan topiknya. Jangan mengandalkan ingatan.

---

## Konteks Proyek

**Proyek:** Sistem produksi konten end-to-end untuk personal brand Fadhil sebagai Business
Builder.

**Positioning:** Membagikan keputusan, eksperimen, dan sistem praktis untuk membantu pemilik
bisnis yang sudah berjalan tumbuh lebih sehat dengan sumber daya terbatas.

**Audiens:** Founder dan pemilik bisnis jasa, edukasi, atau digital yang sudah punya pelanggan
dan tim kecil. Mereka ingin meningkatkan pendapatan tanpa merusak margin, kualitas layanan,
atau kendali operasional.

**Channel utama:** YouTube — konten mendalam 8–15 menit.
**Distribusi sekunder:** Instagram Reels/Carousel dari materi YouTube yang sama. Jangan membuat
materi orisinal terpisah dulu.

**Tiga pilar konten:**

1. **Model Bisnis & Keuangan** — pricing, margin, unit economics, cash flow, bootstrapping,
   prioritas produk.
2. **Sistem Pertumbuhan Pendapatan** — akuisisi, funnel, konversi, retention, referral,
   CAC/LTV, channel marketing.
3. **Sistem Operasional & Kepemimpinan** — SOP, KPI, delegasi, kapasitas layanan, founder
   dependency, hiring, weekly review.

**Tiga format berulang:**

| Format | Struktur | Contoh judul |
|---|---|---|
| **Decision Notes** | Situasi → pilihan → kriteria → keputusan → trade-off | "Margin Tinggi vs Omzet Besar: Angka Apa yang Menentukan?" |
| **Business Breakdown** | Konteks → masalah → keputusan → dampak → pelajaran | "Mengapa Bisnis Pendidikan Mengubah Produk Belajar Mandiri Menjadi Tutoring?" |
| **Operating Playbook** | Masalah → langkah → contoh → ukuran keberhasilan → batas penggunaan | "Cara Menemukan Titik Bocor di Funnel Penjualan" |

**Fase saat ini:** Pilot — empat video pertama dalam empat minggu. Belum ada baseline. Jangan
menetapkan target view atau subscriber secara arbitrer. Bandingkan empat video satu sama lain,
lalu tetapkan baseline.

**Hubungan dengan Salam Cendekia:** Proyek ini untuk personal brand Fadhil, bukan untuk
perusahaan. Data Salam Cendekia boleh dipakai sebagai studi kasus **hanya jika** disamarkan dan
diizinkan Fadhil. Jangan membuka data pelanggan, tutor, keuangan detail, atau informasi
internal perusahaan.

---

## Prasyarat Sebelum Video Pertama

Empat pekerjaan ini harus selesai sebelum rekaman video pertama. Ini bukan bagian dari pipeline
10 tahap. Ini persiapan yang berjalan di sela-sela, dan tidak memblokir ideasi maupun penulisan
naskah.

| # | Pekerjaan | Selesai jika | Status |
|---|---|---|---|
| 1 | Finalisasi warna dan aset brand | Palet HEX, font, dan tiga templat thumbnail tersimpan di `brand_assets/` dan tertaut di `workflows/brand-guidelines.md` | ☐ |
| 2 | Isi brief empat video pilot | Empat file brief lengkap di `content/briefs/`, masing-masing lulus rubrik di `templates/brief-konten.md` | ☐ |
| 3 | Audit izin data Salam Cendekia | Ada daftar tegas: angka dan cerita mana yang boleh dibuka, mana yang harus disamarkan, mana yang tidak boleh disebut sama sekali | ☐ |
| 4 | Siapkan channel YouTube | Nama channel, deskripsi, banner, dan foto profil sudah terpasang | ☐ |

**Urutan pengerjaan:** nomor 3 lebih dulu, karena hasil audit menentukan brief mana yang boleh
dipakai. Nomor 1 dan 4 bisa dikerjakan paralel. Nomor 2 terakhir, karena butuh hasil nomor 1
dan 3.

**Kalau salah satu belum selesai:** jangan rekam. Tapi jangan menunda ideasi dan penulisan
naskah — dua pekerjaan itu tidak bergantung pada brand atau channel.

---

## Struktur Proyek

```
content-production-system/
├── AGENTS.md                       # Panduan utama (file ini)
├── Personal Brand Plan.docx        # Rencana brand dan riset audiens
├── review-setup-2026-11-01.md      # Review setup dan temuan yang belum ditindaklanjuti
├── review-pola-kreator-2026-11-01.md  # Review tujuh workflow terhadap pola kreator rujukan
│
├── workflows/                      # SOP per proses (baca sebelum mengerjakan)
│   ├── 01-ideasi.md
│   ├── 02-pengemasan.md
│   ├── 03-riset-dan-fakta.md
│   ├── 04-penulisan-naskah.md
│   ├── 05-rekaman.md
│   ├── 06-riset-visual.md
│   ├── 07-penyuntingan.md
│   ├── 08-penerbitan.md
│   ├── 09-distribusi-ulang.md
│   ├── 10-evaluasi.md
│   ├── content-bank.md             # 40 ide konten dengan pilar dan format
│   ├── brand-guidelines.md         # Identitas visual, warna, font, elemen
│   └── prinsip-editorial.md        # Prinsip kualitas dan rubrik terbit
│
├── templates/                      # Templat yang dipakai berulang
│   ├── brief-konten.md             # Brief per video
│   └── post-mortem.md              # Evaluasi per video
│
├── tools/                          # Skrip dan utilitas otomasi
│   ├── ambil-daftar-video.py       # Daftar video terbaru channel YouTube tanpa login
│   ├── pindai-youtube.py           # Ukur permintaan dan pasokan per kueri (3 putaran)
│   └── cek-video.py                # Baca chapter dan deskripsi video tanpa menonton
│
├── content/                        # File produksi per konten
│   ├── log-keputusan.md            # Bukti tipe A: keputusan, angka, hasil
│   ├── pindai/                     # Hasil pindai topik per tanggal
│   ├── briefs/                     # Brief yang sudah diisi
│   ├── scripts/                    # Naskah/outline per video
│   ├── assets/                     # Aset visual per video
│   └── exports/                    # File jadi (video, thumbnail, klip)
│
└── brand_assets/                   # Logo, palet warna, font file
```

---

## Perbaikan Berkelanjutan

File ini adalah memori hidup. Tujuannya: **jangan memulai dari nol dua kali.**

**Catat saat kamu:**
- Menemukan cara yang berhasil setelah sempat bingung — catat cara dan jebakan.
- Menemukan alat, URL, atau pengaturan yang benar — catat di tempat yang tepat.
- Memecahkan masalah produksi (audio, edit, upload) — catat gejala → penyebab → perbaikan.
- Menemukan cara lebih baik daripada yang tercatat — **ganti** catatan lama, jangan menambah.
- Mempelajari preferensi audiens dari data evaluasi — catat di `workflows/10-evaluasi.md`.

**Cara mencatat:**
- Prosedur berulang → file di `workflows/`
- Fakta kecil / jebakan → edit file topik yang tepat di `workflows/`
- Skrip yang bisa dijalankan → simpan di `tools/`
- Jujur soal apa yang belum berjalan
- **Jangan mencatat password, token, atau rahasia**

---

## Peta Pengetahuan

Baca file topiknya **sebelum** mengerjakan. Jangan dari ingatan.

| Kalau pekerjaannya menyentuh… | Baca dulu |
|---|---|
| Mencari ide konten, memilih topik, memvalidasi ide | `workflows/01-ideasi.md` |
| Membuat judul, merancang konsep thumbnail | `workflows/02-pengemasan.md` |
| Riset fakta, data, referensi, studi kasus | `workflows/03-riset-dan-fakta.md` |
| Menulis outline, naskah, hook, struktur cerita | `workflows/04-penulisan-naskah.md` |
| Persiapan rekaman, ceklis peralatan, pengaturan ruang | `workflows/05-rekaman.md` |
| Mencari B-roll, stok video/gambar, grafis, visualisasi data | `workflows/06-riset-visual.md` |
| Mengedit video, audio, warna, grafis, teks di layar | `workflows/07-penyuntingan.md` |
| Mengunggah, menulis metadata, SEO YouTube, menjadwalkan | `workflows/08-penerbitan.md` |
| Memotong klip pendek, membuat Reels/Shorts/TikTok | `workflows/09-distribusi-ulang.md` |
| Membaca analitik, menulis post-mortem, menentukan iterasi | `workflows/10-evaluasi.md` |
| Memilih ide dari bank konten, memprioritaskan brief | `workflows/content-bank.md` |
| Warna, font, elemen visual, templat thumbnail | `workflows/brand-guidelines.md` |
| Standar kualitas, rubrik terbit, prinsip editorial | `workflows/prinsip-editorial.md` |
| Positioning, audiens, pilar, riset awal | `Personal Brand Plan.docx` |

---

## Pipeline Produksi Konten — 10 Tahap

Sepuluh tahap berurutan. Setiap tahap punya **gerbang keluaran** — jangan lanjut kalau
gerbangnya belum lulus. SOP lengkap ada di file `workflows/` masing-masing.

```
┌──────────┐   ┌───────────┐   ┌───────┐   ┌──────────┐   ┌─────────┐
│ 1.Ideasi │──▶│2.Kemasan  │──▶│3.Riset│──▶│4.Naskah  │──▶│5.Rekam  │
└──────────┘   └───────────┘   └───────┘   └──────────┘   └─────────┘
                                                               │
┌──────────┐   ┌───────────┐   ┌────────┐   ┌─────────┐       │
│10.Evalu- │◀──│9.Distri-  │◀──│8.Ter-  │◀──│7.Sun-   │◀──┌──▼──────┐
│  asi     │   │  busi     │   │  bit   │   │  ting   │   │6.Visual │
└──────────┘   └───────────┘   └────────┘   └─────────┘   └─────────┘
      │
      ▼
  [Umpan balik ke Tahap 1]
```

### Tahap 1 — Ideasi

**Tujuan:** Menghasilkan daftar Top N topik yang layak diproduksi, sudah diskor, berbasis data
permintaan dan celah pasokan.

**Aturan utama:**
- Mulai dari celah: sudut yang dicari orang tetapi belum dibahas dalam di YouTube Indonesia.
- Permintaan diukur, bukan dirasakan. Median tayangan 10 hasil teratas, tiga putaran per kueri.
- Bukti boleh dari riset: data sendiri, laporan tahunan, filing, BPS, jurnal, siaran pers resmi.
- Setiap ide harus masuk ke salah satu dari tiga pilar konten.
- Topik boleh aktual. Yang tidak boleh berubah adalah lensanya: keputusan, margin, kapasitas.

**Dua hal yang menggugurkan topik sebelum dinilai:** pasokan sudah dalam, atau permintaan di bawah
ambang. Skor tidak bisa menyelamatkan topik yang seharusnya gugur di sini.

**Sumber ide:** pindai YouTube (`tools/pindai-youtube.py`), log keputusan sebagai bukti tipe A,
content bank untuk cek duplikat, komentar dan pertanyaan audiens sebagai sinyal pendukung.

**Gerbang keluaran:** ✅ Minimal 10 kueri dipindai, minimal 5 kandidat diskor, tiga teratas punya
skor minimal 18 dengan bukti tipe A atau B yang sudah diambil. Hasil disimpan di
`content/pindai/pindai-topik-[tanggal].md`.

**SOP lengkap:** `workflows/01-ideasi.md`

---

### Tahap 2 — Pengemasan (Packaging)

**Tujuan:** Merancang judul dan konsep thumbnail **sebelum** menulis naskah.

> **Ini tahap paling kritis.** Kalau ide tidak bisa dikemas menjadi judul dan thumbnail yang
> menarik, jangan lanjut ke penulisan. Ubah sudut pandang atau ganti ide.

**Aturan judul:**
- Wajib ada entitas bernama atau angka. "Bisnis edukasi saya" dan "Rp450 ribu" sah sebagai entitas.
- Wajib ada taruhan: apa yang hilang atau berubah kalau penonton tidak tahu isinya.
- Wajib ada pertentangan yang terbaca dari judul saja.
- Total di bawah 70 karakter. Kata kunci di awal adalah preferensi, bukan syarat.
- Jangan klaim berlebihan. Jangan clickbait yang tidak bisa dipenuhi isi.
- Judul dan thumbnail saling melengkapi, bukan mengulang.
- Bahasa Indonesia percakapan yang biasa dipakai audiens.

**Aturan thumbnail:**
- Maksimal tiga elemen: subjek + teks pendek + latar.
- Teks: 3–5 kata, font sans-serif tebal, kontras tinggi.
- Uji: apakah terbaca di layar ponsel ukuran 120 px?
- Jangan taruh teks di pojok kanan bawah (zona durasi video).
- Kalau video punya angka, pertimbangkan menampilkan angka itu. Harus sama dengan angka di video.

**Gerbang keluaran:** ✅ Lima opsi judul, dua dipertahankan, ditambah 1–2 sketsa thumbnail untuk
judul terbaik. Minimal satu kombinasi lolos uji lima detik: ada nama atau angka, ada taruhan, ada
pertentangan, dan bisa dipenuhi isi video.

**SOP lengkap:** `workflows/02-pengemasan.md`

---

### Tahap 3 — Riset dan Verifikasi Fakta

**Tujuan:** Mengumpulkan bukti, data, studi kasus, dan referensi yang mendukung POV konten.

**Aturan utama:**
- Pisahkan tiga jenis sumber: (1) pengalaman langsung, (2) data publik dengan sumber jelas,
  (3) ilustrasi/hipotesis. Beri tanda di naskah.
- Setiap klaim inti wajib punya sumber primer. Artikel berita dan blog yang mengutip laporan
  bukan sumber primer.
- Setiap angka harus punya definisi, periode, dan sumber.
- Jangan menyajikan ilustrasi sebagai data nyata. Selalu beri label.
- Data internal Salam Cendekia: samarkan dan pastikan izin Fadhil sebelum dipakai.
- Setiap video memuat minimal satu angka atau keputusan yang merugikan Fadhil.
- Riset berhenti di 90 menit. Kalau klaim inti belum terbukti, ganti klaimnya.

**Gerbang keluaran:** ✅ Lembar fakta tersusun. Setiap butir ditandai: *terverifikasi*, *simpulan*,
atau *tebakan*, plus label jenis sumber. Ada artefak yang bisa ditampilkan dan satu angka yang
merugikan.

**SOP lengkap:** `workflows/03-riset-dan-fakta.md`

---

### Tahap 4 — Penulisan Naskah

**Tujuan:** Menyusun outline atau naskah yang siap direkam.

**Struktur wajib:**

```
1. HOOK (0–5 detik)
   Pernyataan kontarian, angka mengejutkan, atau pertanyaan tajam.
   Jangan pembukaan basa-basi. Jangan "Halo semuanya".

2. BUKTI PERTAMA (5–30 detik)
   Tunjukkan satu angka atau artefak dari lembar fakta.
   Jangan pakai 30 detik pertama untuk janji. YouTube menilai jendela ini sebagai Intro.

3. JANJI (30–40 detik)
   Satu kalimat: apa yang penonton dapat, dalam bentuk apa.

4. ISI UTAMA (40 detik – akhir minus 60 detik)
   Maksimal tiga poin utama.
   Setiap poin: klaim → bukti → contoh → trade-off.
   Setiap 90 detik harus ada satu hal yang bisa dicatat penonton.
   Tandai [B-ROLL], [GRAFIS], [TEKS-LAYAR], dan [SCREEN-REC] sebagai panduan visual.

5. KESIMPULAN & CTA (60 detik terakhir)
   Ringkas dalam satu kalimat.
   Beri satu langkah yang bisa diterapkan penonton minggu ini.
   CTA ringan: pertanyaan di komentar, atau tonton video terkait.
   Jangan jual produk. Belum waktunya.
```

**Kerangka penulisan:**
- **PAS (Problem → Agitate → Solution)** — untuk Decision Notes.
- **Cerita (konteks → masalah → keputusan → dampak → pelajaran)** — untuk Business Breakdown.
- **Langkah (masalah → langkah → contoh → ukuran → batas)** — untuk Operating Playbook.

**Aturan sudut pandang:**
- Keputusan dan pengalaman memakai "saya". Instruksi memakai "kamu".
- Jangan mencampur keduanya dalam satu paragraf. "Kita" menyembunyikan siapa yang memutuskan.
- Setiap naskah harus punya satu kalimat yang tidak bisa diucapkan kreator lain tanpa berbohong.

**Aturan bahasa naskah:**
- Bahasa Indonesia percakapan yang biasa dipakai pemilik bisnis. Bukan bahasa buku.
- Satu ide per kalimat. Jangan bertele-tele.
- Istilah bisnis umum boleh langsung: KPI, SOP, OKR, CAC, funnel, margin.
- Jangan jargon yang harus dijelaskan — ganti dengan kata biasa.
- Uji: kalau dibaca sekali dan tidak langsung dipahami, tulis ulang.

**Gerbang keluaran:** ✅ Outline atau naskah lengkap yang bisa direkam tanpa persiapan
tambahan. Hook, alur isi, dan bukti sudah lengkap. Tandai visual sudah ada.

**SOP lengkap:** `workflows/04-penulisan-naskah.md`

---

### Tahap 5 — Rekaman

**Penanggung jawab:** Fadhil (voice over atau talking head langsung). AI tidak mengerjakan
tahap ini, tapi menyediakan ceklis dan panduan.

**Ceklis sebelum rekam:**
- [ ] Audio: mikrofon bersih, tidak ada dengung AC/kipas, ruangan sunyi
- [ ] Gambar: pencahayaan konsisten, latar bersih, kamera stabil
- [ ] Frame: resolusi 4K jika ada (untuk fleksibilitas zoom saat edit), rasio 16:9
- [ ] Naskah/outline sudah final dan terbuka di layar
- [ ] Air minum tersedia
- [ ] Room tone: rekam 10 detik keheningan ruangan untuk noise reduction

**Aturan produksi:**
- Rekam dalam **batch**: 2–4 naskah per sesi. Ganti baju untuk variasi visual.
- Jangan mengejar sempurna saat rekam — kesalahan dipotong saat edit.
- Tandai kesalahan dengan jeda + tepuk tangan (mudah ditemukan di timeline).
- Simpan file mentah ke `content/assets/[YYYY-MM-DD]-[judul-pendek]/` segera.
- Prioritaskan audio di atas gambar. Audio buruk lebih merusak daripada gambar sederhana.
- Jangan beli perlengkapan mahal sebelum pilot selesai.

**Gerbang keluaran:** ✅ File rekaman audio/video yang jelas dan cukup bersih untuk diedit.
Backup tersimpan.

**SOP lengkap:** `workflows/05-rekaman.md`

---

### Tahap 6 — Riset Visual

**Tujuan:** Mengumpulkan aset visual pendukung: B-roll, grafis data, screen recording, stok
gambar/video.

**Aturan:**
- Setiap video wajib punya minimal satu artefak yang terlihat di layar: spreadsheet, dashboard,
  invoice, dokumen, atau tangkapan layar keputusan. B-roll kantor tidak menghitung.
- Artefak diambil dari lembar fakta Tahap 3, bukan dibuat baru untuk kamera.
- Baca naskah per segmen. Tandai setiap penanda visual yang butuh aset.
- Kategorikan visual: A-roll, artefak, B-roll, grafis data, teks overlay, screen recording,
  animasi.
- Sumber stok: Pexels, Pixabay, Storyblocks (cek lisensi). Jangan pakai aset tanpa lisensi.
- Grafis data: sederhanakan untuk layar ponsel. Hilangkan gridline dan teks kecil.
  Warna brand untuk data utama, abu-abu untuk pembanding. Tampilkan bertahap sesuai narasi.
- Aturan 60-30-10 untuk grafis: 60% latar dominan, 30% warna struktural, 10% aksen brand.

**Pacing visual:**
- Satu ide, satu visual. Visual berganti ketika idenya berganti, bukan ketika stopwatch berbunyi.
- Tidak ada segmen lebih dari 60 detik tanpa perubahan visual. Ini standar pilot.
- Segmen data boleh lebih cepat: kalau satu kalimat memuat tiga angka, tampilkan tiga kali.
- Artefak boleh diam lama. Penonton sedang membaca.

**Gerbang keluaran:** ✅ Minimal satu artefak terekam, folder aset dan peta visual lengkap di
`content/assets/`, semua lisensi dicek, aset AI ditandai.

**SOP lengkap:** `workflows/06-riset-visual.md`

---

### Tahap 7 — Penyuntingan (Editing)

**Tujuan:** Menggabungkan rekaman, visual, audio, dan grafis menjadi video final.

**Alur editing tiga lapis:**

| Lapis | Fokus | Ceklis |
|---|---|---|
| **V1 — Rough Cut** | Cerita dan alur | Potong jeda, filler, kesalahan. Susun sesuai naskah. |
| **V2 — Fine Cut** | Bukti dan visual | Artefak dulu, lalu B-roll, grafis, teks overlay, zoom punch. |
| **V3 — Polish** | Teknis | Audio, warna, caption, end screen. |

**Dua tingkat pekerjaan:**

| Tingkat | Isi | Kapan |
|---|---|---|
| **Wajib** | Potong dead air, audio bersih, artefak terlihat, caption diperiksa, end screen | Setiap video |
| **Nanti** | LUT, SFX transisi, motion graphics, bumper pembuka, sound design sinematik | Setelah baseline |

**Aturan potong:**
- Potong semua dead air: diam kosong, filler, kalimat yang diulang.
- Biarkan jeda yang disengaja sebelum angka penting atau setelah pertanyaan.
- Jangan potong di tengah penjelasan hanya untuk mencapai hitungan detik.
- Targetnya tidak ada diam kosong, bukan jumlah potongan.

**Standar teknis audio:**

| Parameter | Standar |
|---|---|
| Loudness | −14 LUFS (standar YouTube) |
| High-pass filter | 80 Hz (hilangkan dengung) |
| Dialog | Kompresi agar volume konsisten |
| Musik latar | −20 sampai −25 dB di bawah dialog |
| SFX transisi | Halus: whoosh, pop, klik. Tidak mengganggu. |

**Standar teknis video:**

| Parameter | Standar |
|---|---|
| Resolusi output | 1920×1080 (dari sumber 4K untuk zoom) |
| Codec | H.264 atau H.265, VBR 2-pass |
| Bitrate | 15–25 Mbps untuk 1080p |
| Frame rate | 30 fps |
| Color space | Rec.709 |

**Standar teks di layar dan caption:**
- Font: sans-serif tebal (Montserrat, Inter, atau font brand). Maksimal dua font.
- Ukuran: terbaca di layar ponsel (minimal 5% tinggi frame).
- Kontras: teks putih + outline hitam tebal, atau latar semi-transparan.
- Safe zone: jangan taruh teks di 20% bawah dan 10% atas frame.
- Caption untuk klip pendek: kata per kata (kinetic), 1–3 kata per flash.

**Teknik editing dari kreator rujukan:**

| Teknik | Dari siapa | Kapan dipakai |
|---|---|---|
| Potong dead air | Semua | Selalu |
| Punch zoom 100→110% | Hormozi, Raymond Chin | Saat penekanan, bukan setiap kalimat |
| Kinetic captions | Hormozi | Klip pendek wajib, video panjang opsional |
| Progressive reveal grafis | Raymond Chin | Semua grafis data |
| Motion graphics data | Raymond Chin | Setelah baseline, bukan di pilot |
| Sound design sinematik | Ferry Irwandi | Setelah baseline |

**Yang tidak dipakai sebagai rujukan proses:** Moon mengunggah sekitar 30 video dalam empat bulan,
sebagian berdurasi 20 menit ke atas, dan pernah dua video dalam tujuh jam. Itu operasi tim.
Menjadikannya rujukan motion graphics untuk produksi solo berarti memasukkan beban kerja yang
tidak ada pemiliknya. Tonton Moon sebagai contoh hasil, bukan contoh proses.

**Struktur track timeline (rekomendasi):**
```
V3+   : Grafis, teks overlay, callout
V2    : B-roll, stok, screen recording
V1    : A-Roll (rekaman utama)
A1–A2 : Dialog (utama + cadangan)
A3–A4 : SFX
A5–A6 : Musik (stereo)
```

**Gerbang keluaran:** ✅ Video final yang lulus ceklis teknis dan rubrik editorial (lihat
`workflows/prinsip-editorial.md`).

**SOP lengkap:** `workflows/07-penyuntingan.md`

---

### Tahap 8 — Penerbitan (Publishing)

**Tujuan:** Mengunggah video dengan metadata yang dioptimalkan untuk ditemukan.

**Ceklis metadata YouTube, diurutkan berdasarkan dampak:**

**Wajib sebelum terbit:**
- [ ] Thumbnail dari Tahap 2, sudah diuji di layar ponsel 120 px
- [ ] Judul dari Tahap 2, di bawah 70 karakter, ada entitas atau angka dan taruhan
- [ ] 30 detik pertama lulus: bukti pertama muncul sebelum detik 30, tanpa sapaan
- [ ] End screen terpasang di 15–20 detik terakhir
- [ ] Deskripsi: 150 karakter pertama = kata kunci + alasan menonton
- [ ] Deskripsi body: 150–200 kata, kata kunci turunan alami, tanpa spam
- [ ] Chapter untuk setiap bagian utama
- [ ] Subtitle/caption diperiksa manual (auto-caption akurasi 70–85% untuk bahasa Indonesia)
- [ ] Komentar terpin: rangkuman isi atau pertanyaan diskusi
- [ ] Tiga klip 9:16 sudah dipotong sebelum Publish

**Opsional, jangan menunda terbit:**
- [ ] Tags: 5–8, kata kunci utama pertama
- [ ] Nama file video mengandung kata kunci (`cara-naikkan-margin.mp4`)
- [ ] Hashtag: 2–3 di akhir deskripsi
- [ ] Kategori dan cards

**Jalur cepat:** kalau ada peristiwa bisnis besar yang relevan dengan tiga pilar, video 6–8 menit
dalam 48 jam mengalahkan video 12 menit dalam dua minggu. Syaratnya: peristiwa terjadi dalam 7
hari terakhir, ada POV Fadhil, ada satu artefak, dan rubrik editorial tetap lulus.

**Aturan SEO YouTube Indonesia:**
- Audiens Indonesia mencari dengan format: "Cara...", "Tutorial...", "Tips...", "Kenapa...",
  "Review...", "Rekomendasi..."
- Gunakan long-tail keyword untuk channel baru (misal "cara naikkan margin bisnis jasa" bukan
  hanya "tips bisnis").
- Validasi: YouTube Autocomplete, Google Trends region Indonesia, VidIQ, TubeBuddy.
- Perbarui metadata video lama secara berkala — SEO bukan tugas sekali jalan.

**Gerbang keluaran:** ✅ Video live atau terjadwal, seluruh ceklis wajib lulus, tiga klip siap.

**SOP lengkap:** `workflows/08-penerbitan.md`

---

### Tahap 9 — Distribusi Ulang (Repurposing)

**Tujuan:** Satu video YouTube → 3–6 klip pendek untuk Reels, Shorts, dan TikTok.

**Alur kerja:**

1. **Seleksi klip:** Identifikasi 5–7 momen. Kriteria: punya hook sendiri, bisa dipahami tanpa
   konteks video asli, ada payoff dalam 30–60 detik.
2. **Edit ulang:** Reframe ke 9:16. Tambahkan caption kinetik. Tulis hook baru di 3 detik
   pertama jika pembukaan asli terlalu lambat.
3. **Optimasi per platform:**
   - YouTube Shorts: judul pendek + #shorts, tautkan ke video utama di komentar.
   - Instagram Reels: CTA di caption/komentar terpin, jangan banjiri — sebar beberapa hari.
   - TikTok: teks di layar mengandung kata kunci, estetika autentik.
4. **Jadwalkan:** Sebar 3–5 klip selama 1–2 minggu setelah video utama terbit.

**Aturan:**
- Jangan membuat materi orisinal terpisah untuk Instagram selama fase pilot.
- Klip dengan performa terbaik → kandidat ide video panjang berikutnya (feedback loop).
- Uji setiap klip: "Apakah ini masuk akal untuk orang yang belum pernah melihat video aslinya?"
- Alat bantu klip: OpusClip, Vizard, Descript (untuk batch pertama). Hasilnya selalu diperiksa
  manusia — jangan terbitkan keluaran AI mentah.

**Gerbang keluaran:** ✅ 3–6 klip terjadwal di platform sekunder, masing-masing bisa berdiri
sendiri.

**SOP lengkap:** `workflows/09-distribusi-ulang.md`

---

### Tahap 10 — Evaluasi (Post-Mortem)

**Tujuan:** Mengukur respons, mencatat pelajaran, menentukan iterasi berikutnya.

**Jadwal evaluasi:**
- **48 jam:** CTR, AVD, retensi 30 detik pertama, komentar awal.
- **7 hari:** Total views, sumber traffic, komentar audiens target, performa klip pendek.
- **Bulanan:** Bandingkan empat video, identifikasi pola, tetapkan baseline.

**Metrik dan cara membacanya:**

| Kelompok | Metrik | Pertanyaan |
|---|---|---|
| Penemuan | Impressions, sumber traffic, views | Apakah video ditemukan? |
| Ketertarikan | CTR, retensi 30 detik pertama | Apakah kemasan dan pembukaan bekerja? |
| Kedalaman | AVD, titik penonton pergi | Apakah alur cerita mempertahankan perhatian? |
| Kualitas audiens | Komentar spesifik, pertanyaan lanjutan, DM dari pemilik bisnis | Apakah audiens target yang merespons? |
| Biaya produksi | Jam riset + tulis + rekam + edit | Apakah bisa diulang tanpa mengganggu pekerjaan utama? |

**Aturan evaluasi:**
- Belum ada baseline. Jangan tetapkan target arbitrer. Bandingkan video satu sama lain.
- CTR tinggi + bounce langsung lebih buruk daripada CTR sedang + retensi tinggi.
- Komentar dari pemilik bisnis yang bertanya lebih berharga daripada 1.000 likes acak.
- Uji thumbnail A/B minimal 1–2 minggu. Jangan hentikan berdasarkan data hari pertama.
- Catat post-mortem setiap video di `content/briefs/` memakai `templates/post-mortem.md`.

**Gerbang keluaran:** ✅ Post-mortem selesai. Pelajaran dimasukkan ke `workflows/` yang
relevan. Keputusan iterasi berikutnya (topik, format, atau teknis) dicatat.

**SOP lengkap:** `workflows/10-evaluasi.md`

---

## Jadwal Produksi Batch (Rekomendasi)

Untuk satu video per minggu selama pilot. Sesuaikan dengan jadwal pekerjaan utama.

| Hari | Blok kerja | Tahap |
|---|---|---|
| Sabtu pagi | Ideasi + Pengemasan + Riset | Tahap 1–3 |
| Sabtu sore | Penulisan naskah | Tahap 4 |
| Minggu pagi | Rekaman (batch 2 video jika bisa) | Tahap 5 |
| Minggu sore | Riset visual | Tahap 6 |
| Senin–Selasa | Editing + potong tiga klip 9:16 | Tahap 7 dan 9 |
| Rabu | Penerbitan | Tahap 8 |
| Rabu sampai dua minggu berikutnya | Sebar klip sisanya | Tahap 9 |
| Rabu+7 hari | Evaluasi | Tahap 10 |

Kalau produksi mulai mengganggu pekerjaan utama, turunkan ke satu video per dua minggu dan
perpanjang pilot.

---

## Prinsip Editorial dan Rubrik Terbit

**Tujuh prinsip editorial:**

1. **Masalah nyata lebih dulu.** Jangan mulai dari framework yang ingin dipamerkan.
2. **Satu konten, satu masalah utama.** Jangan mencoba mengajarkan tiga pilar dalam satu video.
3. **Punya kesimpulan.** Jangan berhenti pada "tergantung" tanpa menjelaskan faktor penentunya.
4. **Tunjukkan alasan dan bukti.** Jelaskan sumber dan periode data.
5. **Buka trade-off.** Sebut biaya, risiko, dan kapan rekomendasi tidak berlaku.
6. **Berikan penerapan.** Audiens harus tahu tindakan apa yang bisa dibawa ke bisnisnya.
7. **Jujur soal batas pengalaman.** Bedakan pengalaman sendiri, contoh perusahaan lain, fakta
   publik, dan hipotesis.

**Rubrik sebelum terbit — jika Masalah, POV, atau Bukti tidak lulus, jangan terbitkan dulu:**

| Pemeriksaan | Lulus jika |
|---|---|
| **Audiens** | Jelas siapa yang sedang mengalami masalah ini |
| ⭐ **Masalah** | Ada satu pertanyaan yang spesifik dan penting |
| ⭐ **POV** | Ada jawaban atau keputusan yang bisa diringkas satu kalimat |
| ⭐ **Bukti** | Klaim inti punya sumber primer. Ada artefak milik sendiri. Ada satu angka yang merugikan Fadhil. Data internal aman dibuka |
| **Trade-off** | Dampak negatif dan batas saran disebutkan |
| **Kegunaan** | Ada langkah atau keputusan yang bisa diterapkan |
| **Judul** | Ada entitas atau angka, dan taruhan. Tanpa klaim berlebihan |
| **Keaslian** | Bukan pengulangan konten sendiri atau ringkasan konten orang lain |

---

## Pola dari Kreator Rujukan

Pola-pola ini diekstrak dari lima kreator yang dipelajari. Bukan untuk ditiru mentah — ambil
yang cocok dengan positioning dan sumber daya yang ada.

### Kreator Rujukan

Lima channel ini adalah dasar pola di bawah. Buka lewat handle, jangan mencari nama tampilan di
mesin pencari. Pencarian nama menghasilkan channel lain dengan nama mirip, dan kegagalan mencari
bukan bukti bahwa channelnya tidak ada.

| Kreator | Tautan | Isi | Skala saat diperiksa (1 November 2026) |
|---|---|---|---|
| Alex Hormozi | `https://www.youtube.com/@AlexHormozi` | Bisnis, penawaran, akuisisi | 4,6 juta subscriber |
| Raymond Chin | `https://www.youtube.com/@RaymondChins` | Bedah bisnis perusahaan Indonesia | 3,52 juta subscriber |
| Ferry Irwandi | `https://www.youtube.com/@ferryirwandi` | Investigasi lapangan dan ekonomi | 2,44 juta subscriber |
| Moon | `https://www.youtube.com/@Moon-Real` | Video esai ekonomi dan teknologi, bahasa Inggris | 1,79 juta subscriber |
| Big A Story | `https://www.youtube.com/@WeAreBigAStory` | Bisnis sepak bola, bahasa Indonesia | 58,1 ribu subscriber |

**Cara membaca daftar video tanpa login.** Jalankan:

```bash
python3 tools/ambil-daftar-video.py Moon-Real WeAreBigAStory
```

Skrip itu membuka halaman `/videos`, membaca objek `ytInitialData`, lalu mencetak durasi,
tayangan, waktu unggah, dan judul. Tiga jebakan yang sudah terbukti: feed RSS
`youtube.com/feeds/videos.xml?channel_id=...` mengembalikan 404 atau 500 untuk channel-channel
ini; halaman `/videos` sekarang memakai `lockupViewModel`, bukan `videoRenderer`; dan pencarian
berdasarkan nama tampilan menemukan channel yang salah.

**Yang belum terverifikasi.** Saya belum menonton video Moon dan Big A Story. Yang terbaca hanya
judul, durasi, tayangan, dan waktu unggah. Klaim tentang gaya visual keduanya belum saya periksa
sendiri, jadi jangan dipakai sebagai dasar keputusan produksi sebelum ditonton.

### Yang layak diadopsi

| Pola | Dari siapa | Cara mengadopsi |
|---|---|---|
| Hook 3–5 detik tanpa basa-basi | Semua lima kreator | Naskah dimulai dari pernyataan kontarian, angka, atau pertanyaan tajam, bukan sapaan |
| Punch zoom dari rekaman 4K | Alex Hormozi, Raymond Chin | Rekam 4K, potong di 1080p dengan zoom 100→110% saat penekanan |
| Kinetic captions kata per kata | Alex Hormozi | Pakai di klip pendek; opsional di video panjang |
| Business Breakdown berbasis data | Raymond Chin | Format studi kasus dengan data divisualisasikan |
| Gaya investigatif riset berat | Ferry Irwandi | Untuk topik mendalam, jika buktinya kuat |
| Judul pertanyaan dengan entitas dan taruhan uang | Big A Story | Sebut klub atau perusahaan, angkanya, lalu pertentangan yang terbaca dari judul |
| Video esai panjang dengan produksi tim | Moon | Tonton sebagai contoh hasil, bukan contoh proses yang bisa dikerjakan sendiri |
| Batch recording 2–4 video/sesi | Alex Hormozi | Kurangi waktu setup, naikkan output per hari |
| Thumbnail minimalis gelap | Alex Hormozi | Uji gaya ini melawan thumbnail dengan wajah |
| 1 video → banyak klip pendek | Alex Hormozi | Mulai dari 3–5 klip per video |

> **Yang sengaja tidak diadopsi.** Jump cut setiap 1–3 detik adalah estetika direct response
> untuk konten cepat. Format Decision Notes adalah studi kasus. Potongan setiap dua detik membuat
> video terdengar seperti iklan, bukan analisis. Yang dipakai: potong dead air, biarkan jeda yang
> disengaja.

### Yang tidak perlu ditiru

- Mesin produksi lintas platform dengan tim besar (Raymond Chin). Belum relevan di fase pilot.
- Irama unggah Moon, sekitar 30 video dalam empat bulan dengan durasi 12 menit sampai 3 jam. Itu
  kerja tim, bukan kerja satu orang.
- Wawancara sebagai format utama (butuh akses tamu yang stabil).
- Cakupan topik terlalu lebar di luar tiga pilar.
- Gaya "coach untuk semua orang" dengan janji hasil berlebihan.
- Efek visual berlebihan yang menaikkan biaya produksi tanpa bukti menaikkan retensi.
- Konten motivasi atau tips jualan umum — bukan positioning Fadhil.

---

## Batas Penggunaan AI

**Gunakan AI untuk:**
- Menyusun outline dan draf naskah
- Merapikan transkrip rekaman
- Riset fakta, menemukan referensi dan data publik
- Menghasilkan daftar pertanyaan riset
- Menulis metadata (judul, deskripsi, tags) — Fadhil memilih final
- Menemukan kandidat klip untuk distribusi ulang
- Analisis komentar dan respons audiens
- Menyusun brief konten dari content bank
- Membuat konsep visual dan grafis data

**Jangan serahkan ke AI tanpa pemeriksaan manusia:**
- Keputusan POV dan sudut pandang konten
- Pengalaman pribadi dan cerita bisnis — hanya Fadhil yang tahu
- Penilaian trade-off bisnis
- Validasi angka dan data akhir
- Keputusan data apa yang aman untuk dibuka secara publik
- Penilaian kualitas akhir sebelum terbit
- Keputusan positioning dan perubahan pilar

**Jangan otomatisasi sebelum:**
- Alur manual sederhana terbukti berjalan (empat konten pilot)
- Format dan positioning sudah divalidasi oleh respons audiens
- Baseline metrik sudah ada

---

## Jebakan yang Menggigit Diam-diam

Setiap butir berdasarkan pengalaman atau best practice terdokumentasi. Daftar ini sengaja
pendek. Jika menambah, pastikan masalahnya sungguhan dan kegagalannya senyap.

**Pengemasan & penerbitan:**
- Metadata yang ditulis setelah video selesai hampir selalu lebih buruk daripada yang dirancang
  sebelum produksi. Rancang judul dan thumbnail **sebelum** menulis naskah.
- Auto-caption YouTube akurasinya 70–85% untuk bahasa Indonesia. Selalu periksa manual.
- Nama file video, tag, dan hashtag dampaknya kecil. Isi kalau sempat, jangan menunda terbit
  karena itu. `cara-naikkan-margin-bisnis.mp4` tetap lebih rapi daripada `video_final_v3.mp4`.
- Shorts yang diunggah sekaligus banyak bisa mengurangi jangkauan. Sebar 3–5 klip selama 1–2
  minggu.

**Naskah & konten:**
- Hook lebih dari 5 detik sebelum masalah disebut membunuh retensi.
- Konten yang mencoba membahas tiga pilar sekaligus tidak membahas satupun dengan baik.
- Angka ilustrasi yang tidak diberi label "ilustrasi" akan dianggap audiens sebagai data nyata.
- Menyebut data Salam Cendekia tanpa izin dan tanpa disamarkan bisa merusak kepercayaan tim.
- Bahasa Indonesia terlalu baku ("bahasa buku") membuat audiens berhenti menonton. Audiens
  Indonesia mencari dengan bahasa percakapan.

**Produksi:**
- Audio buruk lebih merusak daripada gambar sederhana. Prioritaskan mikrofon di atas kamera.
- Rekaman tanpa room tone membuat noise reduction tidak konsisten antar segmen.
- Editing terlalu halus (banyak efek, transisi, animasi) menaikkan biaya produksi tanpa bukti
  menaikkan retensi. Mulai sederhana, tambahkan setelah ada baseline.

**Evaluasi:**
- View tinggi dari audiens bukan target lebih berbahaya daripada view rendah dari audiens yang
  tepat. View viral dari clickbait mengundang subscriber yang tidak menonton video berikutnya.
- CTR dan AVD hari pertama sangat tidak stabil. Tunggu minimal 7 hari.
- Jangan bandingkan metrik lintas video tanpa memperhitungkan topik, format, dan sumber traffic.
- Jangan menambah pilar, format, channel, atau otomasi sebelum empat konten pilot selesai.

---

## Pilot Empat Minggu

Jadwal pilot dari Personal Brand Plan. Satu video per minggu menguji satu hipotesis.

| Minggu | Konten | Hipotesis yang diuji | Status pindai 2026-11-01 |
|---|---|---|---|
| 1 | Kapan Produk Konten Perlu Ditambah Layanan? | Apakah cerita pengalaman pribadi membuat audiens percaya dan bertanya? | Belum dipindai. Tidak ada data permintaan. |
| 2 | Omzet Naik, tetapi Bisnis Makin Berat | Apakah audiens merespons sudut pandang finansial yang praktis? | Gugur. Median 2.907 tayangan, di bawah ambang. |
| 3 | Leads Banyak tetapi Pelanggan Sedikit | Apakah playbook akuisisi dan konversi menarik pemilik bisnis yang tepat? | Lemah. Median 12.884, tidak stabil 3,9 kali. |
| 4 | Lima Tanda Founder Sudah Menjadi Bottleneck | Apakah topik operasi dan kepemimpinan menghasilkan diskusi yang relevan? | Permintaan tidak terbukti. Median besar berasal dari konten motivasi. |

**Jadwal ini belum berlaku.** Urutannya ditulis sebelum ada pindai, dan tiga dari empat ide tidak
lolos ambang permintaan. Urutan baru harus diambil dari `content/pindai/`, bukan dari dokumen ini.
Desain empat hipotesis berbeda tetap dipakai; yang berubah hanya ide dan urutannya.

**Sesudah empat video:** Evaluasi. Keputusan: lanjut, ubah format, atau pindah fokus.

