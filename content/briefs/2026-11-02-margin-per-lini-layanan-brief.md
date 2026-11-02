# Brief Konten: Margin per Lini Layanan

**Tanggal brief:** 2026-11-02
**Status:** Riset (Tahap 3 selesai sebagian, Tahap 4 tertahan)
**Pilar:** Model Bisnis & Keuangan
**Format:** Decision Notes
**Kode database:** IDEA-001

---

## 1. Masalah Audiens

**Siapa yang mengalami masalah ini?**
Pemilik bisnis jasa dengan tim 2–10 orang. Omzet sudah jalan, ada pelanggan berulang, tetapi uang
di rekening tidak bertambah sebanding.

**Apa masalah spesifiknya?**
Mereka tahu total omzet dan total laba. Mereka tidak tahu lini layanan mana yang membiayai lini
lain, sehingga tidak bisa memutuskan layanan mana yang dinaikkan harganya, dipertahankan, atau
dihentikan.

**Bukti bahwa masalah ini nyata:**
Median tayangan 183.822 untuk kueri keluarga margin per lini layanan di bisnis jasa, dengan celah
pasokan kelas Kosong. Artinya orang mencarinya dan tidak menemukan jawaban berbahasa Indonesia
yang membahas angkanya. Ini bukti permintaan, bukan bukti masalah. Bukti masalah dari audiens
sendiri belum dikumpulkan.

---

## 2. Kelayakan

| Kriteria | Isi | Sumber |
|---|---|---|
| Permintaan | Median tayangan 10 hasil teratas: 183.822. Rentang 3 putaran 1,17 kali. | `content/pindai/pindai-topik-2026-11-01.md` |
| Gap | Kosong. Tidak ada video Indonesia yang membahas margin per lini dengan angka. | Sama |
| Bukti | Tipe B. Empat klaim inti bersumber jurnal peer review. Bukti tipe A belum ada. | `…-fakta.md` |
| Kapasitas | 2 hari kerja | Database |
| **Skor** | **28 / 28** | `workflows/01-ideasi.md` Langkah 6 |

**Keputusan:** Produksi sekarang, dengan satu syarat: data sendiri harus dikumpulkan lebih dulu.

---

## 3. POV dan Artefak

**POV dalam satu kalimat:**
Omzet per layanan bukan margin per layanan. Selama biaya yang menempel ke tiap layanan tidak
dipisah, kenaikan omzet bisa menurunkan laba tanpa terlihat di laporan bulanan.

**Mengapa POV ini layak didengar:**
Empat klaim inti berasal dari jurnal peer review akses terbuka yang membaca langsung praktik
perhitungan laba di enam unit bisnis. Bukan opini, bukan rangkuman blog.

**Artefak utama yang akan terlihat di layar:**
**Belum ada.** Yang dibutuhkan: satu tabel berisi kolom layanan, omzet, biaya langsung, jam tim,
untuk satu periode yang sudah tutup buku. Rinciannya ada di bagian 10.

**Angka atau keputusan yang merugikan Fadhil:**
**Belum ada.** `content/log-keputusan.md` masih kosong.

---

## 4. Pengemasan

**Kata kunci utama:** margin per layanan
**Kata kunci turunan:** laba per layanan, harga pokok jasa, untung per layanan

**Lima opsi judul.** Dua dipertahankan.

| # | Judul | Entitas atau angka | Taruhan | Pertentangan | Status |
|---|---|---|---|---|---|
| 1 | Omzet Naik [X]%, Margin Turun [Y] Poin: Tiga Baris yang Menjelaskan | Angka | Kalau tidak tahu, kenaikan omzet dianggap kemajuan | Naik tetapi turun | **Terpilih** |
| 2 | Layanan Terlaris Saya Cuma Menyumbang [Y]% Laba | Entitas "saya" + angka | Layanan favorit bisa jadi sumber kebocoran | Ramai tetapi tipis | Ditolak, terlalu mirip nomor 1 |
| 3 | Bisnis Edukasi Saya: Omzet Naik, Uang di Rekening Tidak | Entitas "bisnis edukasi saya" | Uang hilang tanpa terlihat | Naik tetapi tidak bertambah | **Cadangan** |
| 4 | Kenapa Omzet Naik tapi Profit Tidak Ikut Naik | Tidak ada | Tidak ada | Ada | Ditolak, gagal aturan entitas dan angka |
| 5 | Cara Menghitung Margin per Layanan | Tidak ada | Tidak ada | Tidak ada | Ditolak, ini instruksi bukan taruhan |

**Judul terpilih:** nomor 1, setelah [X] dan [Y] diisi angka sebenarnya.
**Judul cadangan:** nomor 3, dipakai kalau angkanya terlalu sensitif untuk dibuka.

> [!IMPORTANT]
> Tidak satu pun judul di sini boleh tayang dengan angka karangan. Aturan Tahap 2 melarang angka
> di thumbnail berbeda dari angka di video. Selama [X] dan [Y] kosong, Tahap 2 belum lulus.

**Konsep thumbnail A:**
- Pendekatan: Angka
- Subjek: dua angka besar bertumpuk, [X]% di atas, [Y] di bawah, panah berlawanan arah
- Teks (3–5 kata): "[X]% NAIK, [Y] TURUN"
- Latar: gelap polos
- Warna dominan: oranye untuk angka naik, biru dingin untuk angka turun

**Konsep thumbnail B:**
- Pendekatan: Kontras
- Subjek: dua batang berdampingan, batang omzet tinggi, batang margin pendek
- Teks (3–5 kata): "OMZET vs MARGIN"
- Latar: gelap polos
- Warna dominan: oranye lawan biru

**Hasil uji:** Kesatuan cerita [belum] | Feed test [belum] | Mobile 120 px [belum]

Ketiganya belum bisa diuji karena teks thumbnail masih berisi slot angka.

---

## 5. Alur Isi

**Hook (0–5 detik):**
"Omzet saya naik [X]%. Margin turun [Y] poin."

**Bukti pertama (5–30 detik):**
Spreadsheet margin per layanan. Penonton melihat kolom layanan, omzet, dan margin. Tiga baris
ditandai. Narasi menyebut apa yang sedang dilihat, tanpa menjelaskan metodologi.

**Janji (30–40 detik):**
"Di video ini saya tunjukkan tiga angka yang saya periksa sebelum menambah layanan lagi, dan kapan
angkanya berarti berhenti."

**Isi utama — maksimal tiga poin:**

- Poin 1: Omzet per layanan bukan margin per layanan. Bukti dari studi 2024. Contoh dari data
  sendiri. Trade-off: menghitung per lini makan waktu.
- Poin 2: Margin yang terlihat sehat sering baru margin kotor. Bukti dari tiga tingkat
  perhitungan di studi yang sama. Contoh dari data sendiri. Trade-off: membagi biaya tak langsung
  selalu mengandung taksiran.
- Poin 3: Jangan potong layanan hanya dari angka ini. Bukti kutipan manajer yang menolak memutuskan
  dari satu angka. Contoh: lini tipis yang membawa pelanggan ke lini tebal. Trade-off: kalau semua
  lini dituntut untung sendiri, pintu masuk bisa hilang.

**Titik catat setiap 90 detik:**
Menit 0–1,5 angka pembuka. Menit 1,5–3 daftar tiga tingkat perhitungan. Menit 3–4,5 cara memisah
biaya. Menit 6 peringatan jangan memotong. Menit 8 langkah aksi.

**Kesimpulan:**
"Omzet yang naik tanpa margin yang naik hanya menambah pekerjaan." Langkah: minggu ini buat satu
tabel tiga kolom, layanan, omzet, biaya langsung.

**CTA:**
"Layanan mana yang mau kamu hitung duluan? Tulis di komentar."

---

## 6. Bukti dan Referensi

| No | Klaim | Tingkat | Sumber | Primer / Sekunder | Jenis | Reliabilitas |
|---|---|---|---|---|---|---|
| 1 | Omzet sama tidak berarti laba sama | Inti | Lueg & Ilieva 2024, DOI 10.1371/journal.pone.0296974 | Primer | Data publik | Terverifikasi |
| 2 | Tiga tingkat perhitungan, tingkat I mengabaikan biaya tak langsung | Inti | Sama | Primer | Data publik | Terverifikasi |
| 3 | Jangan memutuskan dari satu angka laba | Inti | Sama | Primer | Data publik | Terverifikasi |
| 4 | Perhitungan biaya per lini punya batas praktis | Inti | Sama | Primer | Data publik | Terverifikasi |
| 5 | Laba per layanan bisa dihitung dari satu klien | Pendukung | Cugini & Pilonato 2017, DOI 10.22495/cocv15i1c2p1 | Primer | Data publik | Simpulan, teks penuh belum terbaca |

**Data Salam Cendekia yang dipakai:** tidak ada
**Sudah diizinkan Fadhil:** [ ] Ya / [ ] Tidak / [x] Tidak perlu
**Sudah disamarkan:** [ ] Ya / [ ] Tidak / [x] Tidak perlu

---

## 7. Kebutuhan Visual

| Segmen | Jenis Visual | Deskripsi | Status |
|---|---|---|---|
| Hook | Teks layar | Dua angka besar | Belum, menunggu data |
| Bukti pertama | Artefak | Spreadsheet margin per layanan, tiga baris ditandai | Belum, menunggu data |
| Poin 1 | Grafis | Dua lini: omzet besar, margin tipis | Belum, menunggu data |
| Poin 2 | Grafis | Tiga tingkat perhitungan, bertingkat | Bisa dibuat dari sumber |
| Poin 3 | Grafis | Satu lini tipis yang membawa pelanggan | Butuh ilustrasi berlabel |
| Kesimpulan | Teks layar | Tiga kolom tabel yang harus dibuat | Siap |

---

## 8. Rubrik Sebelum Produksi

| Pemeriksaan | Lulus? | Catatan |
|---|---|---|
| Audiens jelas | Ya | Pemilik bisnis jasa, tim 2–10 orang |
| ⭐ Masalah spesifik | Ya | Satu pertanyaan: lini mana yang membiayai lini lain |
| ⭐ POV satu kalimat | Ya | Ada, dan bisa diucapkan dalam satu tarikan napas |
| ⭐ Bukti | **Tidak** | Sumber primer ada. Artefak sendiri tidak ada. Angka merugikan tidak ada |
| Trade-off disebutkan | Ya | Poin 2 dan 3 |
| Ada langkah yang bisa diterapkan | Ya | Satu tabel tiga kolom |
| Judul punya entitas atau angka, dan taruhan | **Tidak** | Slot angka belum terisi |
| Bukan pengulangan | Ya | Tidak ada di content bank, tidak ada di YouTube Indonesia |

**Keputusan:** Tunda produksi sampai dua butir yang gagal terisi.

---

## 9. Catatan Produksi

**Tanggal rekaman:**
**Tanggal edit selesai:**
**Tanggal terbit:**
**Durasi final:**
**Jam produksi:** riset: 55 menit | naskah: 45 menit | rekam: _ | edit: _ | total: _

---

## 10. Yang Harus Dikumpulkan Sebelum Rekaman

Satu tabel. Empat kolom. Satu periode yang sudah tutup buku.

| Layanan | Omzet | Biaya langsung | Jam tim |
|---|---|---|---|
| | | | |

Aturan pengisian:

1. **Layanan** adalah hal yang dijual terpisah di invoice, bukan departemen.
2. **Omzet** adalah yang ditagih, bukan yang diterima setelah diskon yang belum dibayar.
3. **Biaya langsung** hanya biaya yang hilang kalau layanan itu tidak dijual: honor pengajar,
   materi, biaya platform per sesi.
4. **Jam tim** adalah jam kerja yang benar-benar dipakai, dari catatan jadwal, bukan perkiraan.

Dari tabel itu, ambil empat angka:

- [X] persentase kenaikan omzet periode ini.
- [Y] perubahan margin, dalam poin persen.
- [Z] jumlah lini yang marginnya di bawah rata-rata tertimbang.
- [W] satu lini yang marginnya paling tipis padahal jam timnya paling banyak.

Kalau [W] tidak ada, video ini tidak punya temuan dan sebaiknya diganti topik.
