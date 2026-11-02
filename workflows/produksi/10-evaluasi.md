# Tahap 10 — Evaluasi (Post-Mortem)

## Tujuan

Mengukur respons audiens, mencatat pelajaran, dan menentukan iterasi berikutnya. Evaluasi
bukan sekadar membaca angka — tujuannya membuat keputusan: apa yang diulang, apa yang diubah,
dan apa yang dihentikan.

---

## Jadwal Evaluasi

| Waktu | Fokus | Tindakan |
|---|---|---|
| **48 jam** | Sinyal awal | Catat CTR, AVD, retensi 30 detik, komentar awal |
| **7 hari** | Gambaran stabil | Update semua metrik, analisis traffic, baca semua komentar |
| **Bulanan** | Pola lintas video | Bandingkan empat video, identifikasi pola, tetapkan baseline |

---

## Metrik dan Cara Membacanya

| Kelompok | Metrik | Pertanyaan yang dijawab |
|---|---|---|
| **Penemuan** | Impressions, sumber traffic, views | Apakah video ditemukan? |
| **Ketertarikan** | CTR, retensi 30 detik pertama | Apakah kemasan dan pembukaan bekerja? |
| **Kedalaman** | AVD, titik penonton pergi | Apakah alur cerita mempertahankan perhatian? |
| **Kualitas audiens** | Komentar spesifik, pertanyaan lanjutan, DM dari pemilik bisnis | Apakah audiens target yang merespons? |
| **Biaya produksi** | Jam riset + tulis + rekam + edit | Apakah format ini bisa diulang tanpa mengganggu pekerjaan utama? |

---

## Alur Kerja

### Evaluasi 48 Jam

1. Buka YouTube Studio → Analytics untuk video tersebut.
2. Catat di post-mortem (`templates/post-mortem.md`):
   - Impressions
   - Views
   - CTR
   - AVD (menit:detik)
   - Retensi 30 detik pertama (persen)
   - Jumlah komentar dan likes
3. Periksa grafik retensi:
   - Di mana penonton pergi? Tandai titik drop-off.
   - Di mana retensi paling tinggi? Apa yang terjadi di segmen itu?
4. Baca **semua** komentar. Kategorikan:
   - Dari audiens target (pemilik bisnis) — paling berharga
   - Dari audiens umum
   - Spam
5. Catat: apakah ada komentar dari pemilik bisnis yang bertanya atau membagikan
   pengalamannya?
6. Periksa performa klip pendek (Reels/Shorts) yang sudah terbit.

### Evaluasi 7 Hari

1. Update semua metrik di post-mortem.
2. Analisis sumber traffic:
   - **Pencarian YouTube** — artinya SEO bekerja.
   - **Browse features** — artinya algoritma merekomendasikan.
   - **Suggested videos** — artinya konten terkait mendorong views.
   - **External** — artinya distribusi di luar YouTube bekerja.
3. Bandingkan dengan video sebelumnya (jika ada).
4. Identifikasi: apa yang berhasil? Apa yang tidak? Mengapa?
5. Periksa thumbnail A/B test jika berjalan — butuh minimal 1–2 minggu data.

### Evaluasi Bulanan (setelah 4 video)

1. Bandingkan empat video secara berdampingan:

| Metrik | Video 1 | Video 2 | Video 3 | Video 4 |
|---|---|---|---|---|
| CTR | | | | |
| AVD | | | | |
| Views (7 hari) | | | | |
| Kualitas komentar | | | | |
| Jam produksi | | | | |

2. Identifikasi pola:
   - Topik/pilar mana yang paling resonan?
   - Format mana yang paling mempertahankan perhatian?
   - Hook mana yang paling efektif?
   - Berapa jam produksi rata-rata?
3. Tetapkan baseline dari data empat video ini.
4. Keputusan: lanjut pendekatan saat ini / ubah format / geser topik?

---

## Aturan Evaluasi

1. **Belum ada baseline.** Jangan tetapkan target CTR, AVD, atau views secara arbitrer.
   Bandingkan video satu sama lain sampai pola terlihat.

2. **CTR tinggi + bounce langsung lebih buruk** daripada CTR sedang + retensi tinggi. Yang
   pertama berarti kemasan menipu; yang kedua berarti konten memuaskan.

3. **Komentar dari pemilik bisnis yang bertanya** lebih berharga daripada 1.000 likes dari
   akun acak. Satu komentar spesifik dari audiens target bernilai lebih dari metrik kuantitatif
   manapun di fase awal.

4. **Jangan A/B test thumbnail di fase pilot.** Volume belum cukup untuk membaca hasil. Setelah
   empat video, bandingkan CTR antar video lebih dulu. Kalau volume sudah cukup, uji A/B minimal
   1–2 minggu dan jangan hentikan berdasarkan data hari pertama.

5. **Jangan bandingkan metrik lintas video** tanpa memperhitungkan topik, format, dan sumber
   traffic. Video tentang funnel dan video tentang leadership menarik audiens berbeda.

6. **View dari audiens bukan target itu berbahaya.** Video viral dari topik clickbait menarik
   subscriber yang tidak akan menonton video berikutnya. Ini merusak sinyal algoritma jangka
   panjang.

7. **Jangan membuat perubahan besar** berdasarkan satu video yang underperform. Tunggu pola
   dari minimal tiga video.

---

## Tempat Mencatat Pelajaran

Pelajaran bukan hanya untuk dibaca — harus masuk ke proses yang benar.

| Jenis pelajaran | Catat di mana |
|---|---|
| Post-mortem per video | `content/briefs/[nama-video]/post-mortem.md` |
| Perbaikan proses produksi | File di `workflows/produksi/` yang relevan |
| Insight konten/topik | `workflows/produksi/content-bank.md` (tambah catatan di ide terkait) |
| Insight pengemasan | `workflows/produksi/02-pengemasan.md` |
| Pemahaman audiens | Catatan di `Personal Brand Plan.docx` |

---

## Feedback Loop yang Harus Terjadi

| Temuan | Tindakan | Workflow terkait |
|---|---|---|
| Drop-off di hook | Perbaiki cara menulis hook | `04-penulisan-naskah.md` |
| CTR rendah | Perbaiki judul dan thumbnail | `02-pengemasan.md` |
| AVD rendah | Perbaiki struktur naskah dan titik catat setiap 90 detik | `04-penulisan-naskah.md` |
| Audiens salah yang komentar | Revisi targeting dan pemilihan topik | `01-ideasi.md` |
| Jam produksi terlalu tinggi | Sederhanakan editing | `07-penyuntingan.md` |
| Klip pendek performa tinggi | Jadikan topik video panjang berikutnya | `01-ideasi.md` |
| Audio/visual bermasalah | Perbarui ceklis rekaman | `05-rekaman.md` |

---

## Gerbang Keluaran

✅ Post-mortem selesai (menggunakan `templates/post-mortem.md`). Pelajaran sudah dimasukkan ke
file di `workflows/produksi/` yang relevan. Keputusan iterasi berikutnya (topik, format, atau
perubahan teknis) sudah dicatat.

---

## Kesalahan Umum

- Menetapkan target arbitrer sebelum punya baseline dari empat video.
- Menilai video berdasarkan data hari pertama — tunggu minimal 7 hari.
- Hanya melihat views tanpa memeriksa kualitas audiens.
- Tidak membaca komentar — kehilangan sinyal kualitatif paling berharga.
- Tidak mendokumentasikan pelajaran — memulai dari nol di video berikutnya.
- Membandingkan video tanpa memperhitungkan perbedaan topik dan format.
- Membuat perubahan besar berdasarkan satu video yang underperform.
- Menambah pilar, format, channel, atau otomasi sebelum empat konten pilot selesai.

