# Tahap 7 — Penyuntingan (Editing)

## Tujuan

Menggabungkan rekaman, visual, audio, dan grafis menjadi video final yang siap terbit.

Standar file ini dibagi dua: **wajib** dan **nanti**. Yang wajib harus selesai sebelum terbit.
Yang nanti ditambahkan setelah ada data yang menunjukkan gunanya.

---

## Dua Tingkat Pekerjaan

| Tingkat | Isi | Kapan |
|---|---|---|
| **Wajib** | Potong jeda dan filler, audio bersih, artefak terlihat, caption benar, end screen | Setiap video |
| **Nanti** | LUT, SFX transisi, motion graphics, bumper pembuka, sound design sinematik | Setelah baseline |

Alasannya sederhana. Empat video pilot belum punya data retensi. Menambah efek sebelum ada data
berarti menebak, dan menebak dengan biaya jam kerja.

---

## Alur Editing Tiga Lapis

### Lapis 1 — Rough Cut (V1): Cerita dan Alur

1. Impor footage. Susun A-roll sesuai naskah.
2. Potong semua jeda, filler ("eh", "hmm"), kesalahan, dan pengulangan.
3. Periksa alur: masuk akal dari awal sampai akhir?
4. Periksa durasi: target 8–15 menit.
5. Review: hook kuat? bukti pembuka dikenali penonton dan satu angka spesifik sebelum detik 60? kesimpulan jelas?

**Keluaran:** video kasar yang ceritanya utuh.

### Lapis 2 — Fine Cut (V2): Bukti dan Visual

1. Masukkan artefak utama. Ini pekerjaan pertama di lapis ini, bukan yang terakhir.
2. Masukkan B-roll di titik yang ditandai naskah.
3. Tambahkan grafis data dengan progressive reveal.
4. Tambahkan teks overlay untuk kata kunci dan angka.
5. Punch zoom 100→110% untuk penekanan. Jangan setiap kalimat.
6. Potong dead air. Targetnya **tidak ada diam kosong**, bukan hitungan detik.
7. Periksa: ada segmen lebih dari 60 detik tanpa perubahan visual?
8. Review sebagai penonton.

**Keluaran:** video dengan bukti dan visual lengkap.

### Lapis 3 — Polish (V3): Teknis

**Audio — wajib:**

1. High-pass filter 80 Hz.
2. Noise reduction dengan room tone.
3. Kompresi dialog.
4. Loudness −14 LUFS.
5. Musik latar −20 sampai −25 dB di bawah dialog.
6. Peak tidak melebihi −1 dBTP.

**Audio — nanti:** SFX transisi, sound design sinematik.

**Video — wajib:**

1. White balance konsisten.
2. Exposure matching.
3. Color space Rec.709.

**Video — nanti:** LUT channel.

**Caption — wajib:**

1. Hasilkan auto-caption.
2. Periksa setiap baris manual. Akurasi bahasa Indonesia 70–85%. Kesalahan umum: nama, istilah
   bisnis, angka, singkatan.
3. Pastikan timing sinkron.
4. Font bold sans-serif, kontras tinggi.

**Elemen akhir — wajib:**

1. End screen: subscribe + video terkait, 15–20 detik terakhir.
2. Full playthrough.

**Elemen akhir — nanti:** bumper pembuka.

---

## Aturan Potong

Aturan lama — "jump cut setiap 1–3 detik, selalu" — diganti.

Itu estetika direct response untuk konten cepat. Format Decision Notes adalah studi kasus.
Potongan setiap dua detik membuatnya terdengar seperti iklan, bukan analisis.

**Yang dipakai:**

- **Potong semua dead air.** Diam kosong, filler, kalimat yang diulang.
- **Biarkan jeda yang disengaja.** Jeda sebelum angka penting, atau setelah pertanyaan.
- **Jangan potong di tengah penjelasan** hanya untuk mencapai hitungan detik.
- **Targetnya tidak ada diam kosong**, bukan jumlah potongan.

---

## Aturan Teks di Layar

Setiap teks di layar harus berasal dari naskah yang sudah diverifikasi di Tahap 3.

- Editor tidak menambah klaim.
- Editor tidak membulatkan angka.
- Editor tidak mengubah "31%" menjadi "sekitar 30%".
- Kalau teks butuh angka baru, angka itu harus masuk fact sheet dulu.

**Alasan:** teks di layar adalah klaim. Penonton memotret layar dan mengutipnya. Satu angka yang
berbeda dari naskah cukup untuk merusak kredibilitas.

---

## Standar Teknis Audio

| Parameter | Standar |
|---|---|
| Loudness | −14 LUFS |
| High-pass filter | 80 Hz |
| Dialog | Kompresi agar konsisten |
| Musik latar | −20 sampai −25 dB di bawah dialog |
| Peak level | Tidak melebihi −1 dBTP |

## Standar Teknis Video

| Parameter | Standar |
|---|---|
| Resolusi output | 1920×1080 |
| Resolusi sumber | 3840×2160 untuk zoom |
| Codec | H.264 atau H.265, VBR 2-pass |
| Bitrate | 15–25 Mbps |
| Frame rate | 30 fps |
| Color space | Rec.709 |

## Standar Teks

- Font sans-serif tebal. Maksimal dua font.
- Minimal 5% tinggi frame.
- Kontras: putih + outline hitam, atau latar semi-transparan.
- Safe zone: jangan di 20% bawah dan 10% atas.
- Caption klip pendek: 1–3 kata per flash.

---

## Struktur Track Timeline

```
V4+   : Teks overlay, callout
V3    : Grafis data, diagram
V2    : Artefak, B-roll, screen recording
V1    : A-roll
──────────────────────────
A1–A2 : Dialog
A3–A4 : SFX
A5–A6 : Musik
```

---

## Teknik dari Kreator Rujukan

| Teknik | Dari siapa | Kapan dipakai |
|---|---|---|
| Potong dead air | Semua | Selalu |
| Punch zoom 100→110% | Hormozi, Raymond Chin | Saat penekanan |
| Kinetic captions | Hormozi | Klip pendek wajib, video panjang opsional |
| Motion graphics data | Raymond Chin | Segmen data, setelah baseline |
| Progressive reveal grafis | Raymond Chin | Semua grafis data |

**Yang tidak dipakai sebagai rujukan proses:**

- **Moon.** Moon mengunggah 30 video dalam sekitar empat bulan, sebagian berdurasi 20 menit ke
  atas, dan dua video dalam tujuh jam pada satu hari. Itu operasi tim. Menjadikannya rujukan
  motion graphics untuk produksi solo adalah cara memasukkan beban kerja yang tidak ada
  pemiliknya. Tonton Moon sebagai contoh hasil, bukan contoh proses.
- **Big A Story.** Channel bisnis sepak bola. Pola judulnya bisa dipinjam. Gaya produksinya tidak
  relevan untuk format ini.

---

## Ceklis Ekspor

**Wajib:**

- [ ] Audio: level konsisten, tidak clipping, musik tidak menutupi dialog
- [ ] Video: tidak ada frame hitam, tidak ada lompatan, warna konsisten
- [ ] Artefak utama terlihat dan terbaca
- [ ] Teks: terbaca, tanpa typo, dalam safe zone, angkanya sama dengan naskah
- [ ] Caption: diperiksa manual, timing benar
- [ ] End screen terpasang
- [ ] Full playthrough selesai

**Opsional:**

- [ ] Nama file mengandung kata kunci
- [ ] Bumper pembuka

---

## Gerbang Keluaran

✅ Video final yang lulus ceklis wajib dan rubrik editorial di
[`prinsip-editorial.md`](./prinsip-editorial.md).

---

## Kesalahan Umum

- Caption tidak diperiksa — istilah bisnis Indonesia sering salah.
- Musik terlalu keras.
- Tidak ada kompresi dialog.
- Over-editing: efek menambah jam kerja tanpa bukti menaikkan retensi.
- Lupa end screen.
- Tidak full playthrough.
- Zoom dipakai setiap kalimat.
- Memotong setiap dua detik sampai video terasa seperti iklan.
- Menambah angka di teks layar yang tidak ada di fact sheet.

---

## Hubungan dengan Tahap Lain

| Dari | Yang diterima |
|---|---|
| Tahap 5 — Rekaman | Footage |
| Tahap 6 — Visual | Artefak, B-roll, grafis, peta visual |
| Tahap 4 — Naskah | Struktur, penanda, angka terverifikasi |

| Ke | Yang dikirim |
|---|---|
| Tahap 8 — Penerbitan | Video final, caption, thumbnail |
| Tahap 9 — Distribusi | Master untuk klip pendek |
