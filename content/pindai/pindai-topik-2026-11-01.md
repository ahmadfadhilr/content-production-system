# Pindai Topik — 2026-11-01

**Tahap:** 1 (Ideasi)
**Metode:** `workflows/produksi/01-ideasi.md` versi 2026-11-01
**Alat:** `tools/pindai-youtube.py`, `tools/cek-video.py`
**Kueri dipindai:** 15 kueri benih + 4 kueri verifikasi
**Putaran per kueri:** 3

---

## Ringkasan

Satu topik siap produksi, dua topik layak tetapi belum lulus satu kriteria, satu topik gugur
karena permintaan tidak terbukti, dan dua topik gugur karena pasokan sudah dalam.

Rekomendasi: **kerjakan nomor 1. Jangan kerjakan nomor 2 dan 3 sebelum satu kriteria diperbaiki.**

---

## Tabel Skor

| # | Sudut | Pilar | Permintaan | Gap | Bukti | Kapasitas | Skor | Putusan |
|---|---|---|---|---|---|---|---|---|
| 1 | Margin per lini layanan di bisnis jasa | 1 | 5 | 5 | 3 (B) | 5 | **28** | Produksi sekarang |
| 2 | Kenaikan harga dan siapa yang benar-benar pergi | 1 | 3 | 3 | 3 (B) | 5 | **20** | Perbaiki satu kriteria |
| 3 | Retensi per kohort, bukan repeat order total | 2 | 3 | 3 | 3 (B) | 5 | **20** | Perbaiki satu kriteria |
| 4 | Founder bottleneck dengan jam dan rupiah | 3 | 3 | 3 | 1 (C) | 5 | 18 | Tunda, butuh bukti A |
| 5 | HPP per layanan di bisnis jasa | 1 | 3 | 3 | 3 (B) | 5 | 20 | Gabung ke nomor 1 |
| 6 | Arus kas bisnis kecil | 1 | 5 | 1 | 3 (B) | 5 | 20 | **Gugur: pasokan sudah dalam** |
| 7 | Funnel penjualan | 2 | 3 | 1 | 3 (B) | 5 | 16 | **Gugur: pasokan sudah dalam** |
| 8 | CAC / biaya akuisisi pelanggan | 2 | 1 | 5 | 3 (B) | 5 | 20 | **Gugur: permintaan tidak terbukti** |

> **Catatan tentang baris 6, 7, dan 8.** Ketiganya ditulis dengan model lama, yang masih memberi
> nilai 1 untuk "Gap Dalam" dan "permintaan nol". Di SOP yang sudah diperbaiki, ketiganya gugur di
> Langkah 3b dan tidak masuk penilaian sama sekali. Skornya ditampilkan di sini justru untuk
> menunjukkan mengapa model lama salah: ketiganya mendapat angka yang sama dengan topik layak.

Lima topik mendapat skor 20, dan tiga di antaranya tidak boleh diproduksi apa adanya: arus kas
karena pasokan sudah dalam, CAC karena tidak ada yang mencari, dan HPP per layanan karena
tumpang tindih dengan nomor 1. Itu bukan kebetulan. Skor tidak bisa memisahkan topik yang layak
dari topik yang tidak layak kalau kriteria gugurnya hanya dihitung sebagai angka kecil. Temuan ini
dicatat di bagian akhir.

---

## 1. Margin per Lini Layanan di Bisnis Jasa

**Sudut:** Bisnis jasa yang omzetnya naik tetapi marginnya turun, membahas cara menghitung margin
per lini layanan dan memutuskan lini mana yang dinaikkan harganya, mana yang dipertahankan, dan
mana yang dihentikan.

**Pilar:** 1 — Model Bisnis & Keuangan
**Format:** Decision Notes

### Permintaan — skor 5

| Kueri | Median 10 teratas | Rentang 3 putaran | Hasil | Di atas 100 rb | Terpanjang |
|---|---|---|---|---|---|
| cara menghitung margin usaha | 183.822 | 181.950–212.591 | 19 | 8 | 17 menit |
| margin per layanan bisnis jasa | 101.880 | 60.048–143.713 | 16 | 3 | 20 menit |
| cara menghitung hpp bisnis jasa | 136.304 | 45.145–169.546 | 22 | 4 | 41 menit |
| margin per produk atau total | 146.147 | stabil | 12 | 7 | 17 menit |

Permintaan terbukti pada kata "margin". Tidak terbukti pada frasa "margin per layanan", karena
frasa itu tidak punya volume sendiri. Ini *simpulan*: orang mencari masalahnya, bukan istilah
teknisnya.

### Gap — skor 5 (Kosong)

Dari 19–23 hasil per kueri, tidak ada satu pun video Indonesia yang menghitung margin per lini
layanan. Isi pasokan yang ada:

- Margin toko, warung, ayam geprek, bahan bangunan, buah.
- HPP makanan dan minuman.
- Margin di Shopee dan marketplace.
- Tutorial Excel dan laporan keuangan.

Tiga video yang paling mendekati sudah diperiksa deskripsi dan chapternya:

| Video | Durasi | Temuan |
|---|---|---|
| Kelly Patricia — "BISNIS JASA di 2024? Ini Kunci Suksesnya" (`ffZ28wVumV0`) | 11:49 | Chapter "Keuangan" mulai di 09:00. Artinya keuangan bisnis jasa dibahas sekitar 2 menit 49 detik. |
| The Futur — "Cara Menentukan Harga Layanan Anda" (`qfA0RkYube8`) | 10:04 | Judul aslinya bahasa Inggris. YouTube menerjemahkan judulnya. Ini bukan pasokan Indonesia. |
| KJA ASP — "Begini cara menghitung HPP pada Perusahaan Jasa" (`F9USZ-bmJTM`) | 7:29 | Tanpa chapter, deskripsi 47 karakter, 3.894 tayangan. Gaya penjelasan akuntansi, bukan keputusan. |

Yang ada di Indonesia adalah cara **mencatat** laba per proyek, bukan cara **memutuskan** lini mana
yang harus dipertahankan. Itu dua pekerjaan berbeda, dan yang kedua yang belum ada.

### Bukti — skor 3 (tipe B)

| Sumber | Jenis | Isi | Status |
|---|---|---|---|
| Cugini & Pilonato (2017), *Managing customer profitability to improve corporate performance in PSF*, Corporate Ownership & Control 15(1-2), DOI 10.22495/cocv15i1c2p1 | Jurnal, peer review | Studi kasus di professional service firm. Tabel 4 menunjukkan laba per layanan yang dibeli satu klien. | *Terverifikasi* ada. Abstrak dan kutipan dibaca, isi penuh belum. |
| Lueg & Ilieva (2024), *Customer Profitability Analysis in decision-making*, PLOS ONE 19(5), DOI 10.1371/journal.pone.0296974 | Jurnal akses terbuka, peer review | Manajer menolak memutuskan pelanggan hanya dari angka CPA, karena pelanggan lama dan kompleksitas layanan tidak tertangkap. | *Terverifikasi* ada. Ini sumber trade-off. |
| The CPA Journal (2018), *Valuing Professional Service Firms* | Artikel praktisi | Margin EBITDA bisnis jasa profesional umumnya 15–30% dari pendapatan. | *Terverifikasi* ada. Angka pembanding. |

Tiga sumber ini cukup untuk membuka video, tetapi belum cukup untuk naskah. Setiap angka masih
harus dibaca di dokumen aslinya, bukan dari abstrak.

### Kapasitas — skor 5

Satu spreadsheet dengan margin per lini, satu tabel keputusan. Tidak butuh rekaman lapangan.
Perkiraan 2 hari kerja. Ini *tebakan*, belum diukur.

### Masalah audiens

Pemilik bisnis jasa dengan 2–10 orang tim yang omzetnya naik tetapi uang di rekening tidak
bertambah, sehingga ia tidak tahu lini mana yang sebenarnya membiayai lini lain.

---

## 2. Kenaikan Harga dan Siapa yang Benar-Benar Pergi

**Sudut:** Bisnis jasa yang ingin menaikkan harga, membahas bahwa pelanggan lama dan pelanggan
baru bereaksi berbeda, sehingga churn tiga bulan kemudian bukan akibat kenaikan harga secara
umum.

**Pilar:** 1 — Model Bisnis & Keuangan
**Format:** Decision Notes

### Permintaan — skor 3

| Kueri | Median | Rentang | Hasil | Terpanjang |
|---|---|---|---|---|
| kapan sebaiknya menaikkan harga | 17.228 | 13.368–21.089 | 17 | 17 menit |

Masuk ambang (di atas 10 ribu), tetapi tidak kuat. Median di bawah 100 ribu berarti tidak ada satu
video pun yang benar-benar besar di topik ini.

### Gap — skor 3 (Dangkal)

Dari 17 hasil, semuanya pendek dan semuanya tips. Yang terpanjang 17 menit, dan itu video harga
jual umum, bukan keputusan menaikkan harga. Tujuh dari sepuluh teratas di bawah 10 menit.

Topiknya ada. Kedalamannya tidak. Tidak ada satu pun yang membahas bahwa dampak kenaikan harga
baru terlihat setelah beberapa bulan.

### Bukti — skor 3 (tipe B)

| Sumber | Jenis | Isi |
|---|---|---|
| Dawes (2009), *The Effect of Service Price Increases on Customer Retention*, Journal of Service Research 11(3), DOI 10.1177/1094670508328986 | Jurnal, peer review | Masa berlangganan menurunkan kepekaan terhadap kenaikan harga. Luasnya hubungan justru memperburuk dampak kenaikan harga terhadap retensi. Pelanggan baru dan pelanggan dengan hubungan luas paling berisiko. |
| Ascarza, Iyengar & Schleicher (2016), *The Perils of Proactive Churn Prevention Using Plan Recommendations*, Journal of Marketing Research 53(1), DOI 10.1509/jmr.13.0483 | Eksperimen lapangan, peer review | Kampanye retensi yang proaktif justru menaikkan churn: 6% di kelompok kontrol menjadi 10% di kelompok perlakuan. |

Dawes memberi kerangka. Ascarza memberi angka yang berlawanan dengan intuisi. Kombinasi ini kuat
untuk satu video.

### Kapasitas — skor 5

Tidak butuh data sendiri. Cukup dua jurnal dan satu tabel reaksi per tenure. *Tebakan* 2 hari.

### Yang harus diperbaiki

Permintaan. Skor 3 berasal dari median 17 ribu. Untuk naik ke 5, cari kueri dengan median di atas
100 ribu pada masalah yang sama, misalnya "takut naikkan harga" atau "pelanggan kabur setelah
harga naik". Kalau tidak ada, terima skor 3 dan produksi sebagai video pendek 7–8 menit, bukan
video utama 12 menit.

---

## 3. Retensi per Kohort, Bukan Repeat Order Total

**Sudut:** Bisnis jasa yang mengukur repeat order sebagai satu angka, membahas cara memisahkan
pelanggan berdasarkan bulan pertama mereka datang, sehingga kelihatan apakah retensi membaik atau
memburuk.

**Pilar:** 2 — Sistem Pertumbuhan Pendapatan
**Format:** Operating Playbook

### Permintaan — skor 3

| Kueri | Median | Rentang | Hasil | Terpanjang |
|---|---|---|---|---|
| cara menaikkan repeat order pelanggan | 22.466 | 22.466–25.159 | 23 | 63 menit |

### Gap — skor 3 (Dangkal)

Pasokan ada dan cukup banyak, tetapi hampir semuanya daftar tips: "5 cara", "7 strategi",
"10 tips". Yang panjang pun (27 menit, 20 menit) masih berbentuk daftar. Tidak ada yang memisahkan
pelanggan per kohort atau menunjukkan angka retensi per bulan.

### Bukti — skor 3 (tipe B)

| Sumber | Jenis | Isi |
|---|---|---|
| Ascarza, Iyengar & Schleicher (2016), DOI 10.1509/jmr.13.0483 | Eksperimen lapangan | Upaya retensi tanpa segmentasi bisa memperburuk churn. |
| *The effects of churn on the growth of subscription services* (2026), Journal of Retailing, ScienceDirect S0167811625000254 | Jurnal | Kenaikan churn 20% menurunkan puncak pertumbuhan 2–15% pada beberapa perusahaan langganan. |

Sumber kedua lemah untuk audiens UMKM jasa karena sampelnya perusahaan langganan besar. Pakai
sebagai konteks, bukan sebagai klaim utama.

### Kapasitas — skor 5

Satu tabel kohort di spreadsheet. *Tebakan* 2 hari.

### Yang harus diperbaiki

Gap. Skor 3 karena pasokan dangkal. Untuk naik ke 5, cari sudut yang benar-benar kosong, misalnya
"retensi dihitung per tutor" atau "retensi per paket". Kalau tidak ada, topik ini lebih baik
digabung ke nomor 2 sebagai satu bagian, bukan video sendiri.

---

## Topik yang Gugur

| Topik | Skor | Alasan gugur |
|---|---|---|
| Arus kas bisnis kecil | 20 | Pasokan sudah dalam. Kelly Patricia 238.265 tayangan (12:41), kasisolusi 635.144 (1:12:26), William Basri 352.558 (12:53). Tidak ada celah. |
| Funnel penjualan | 16 | DennySantoso punya tiga video khusus funnel. Raymond Chin 2,35 juta. Sudah dalam. |
| CAC / biaya akuisisi | 20 | Median 1.198 tayangan. Delapan hasil. Nol video di atas 100 ribu. Istilah ini tidak dipakai pemilik bisnis Indonesia. Sama seperti "unit economics". |
| Founder bottleneck | 18 | Median 493.865 terlihat besar, tetapi isinya motivasi dan mindset: Tony Robbins, Raymond Chin, "3 Kesalahan Fatal Pengusaha Pemula" 1,58 juta. Bukan bottleneck yang diukur. Bukti tipe A belum ada karena log keputusan kosong. |

---

## Temuan Metode

Lima hal ini baru kelihatan setelah dijalankan, bukan setelah dirancang.

### 1. Ambang lulus di Langkah 2 hampir tidak menyaring

Sebelas dari lima belas kueri lulus. Ambang yang meloloskan 73% bukan gerbang yang tegas, hanya
saringan kasar. Akibatnya Langkah 2 tidak memisahkan topik hidup dari topik mati, dan keputusan
pindah seluruhnya ke Langkah 6.

Empat yang gagal: omzet naik tetapi profit turun (2.907), cara meningkatkan konversi penjualan
(8.535), biaya akuisisi pelanggan (1.198), dan cara delegasi tugas ke karyawan (8.148).

### 2. Angka tayangan tertinggi tidak bisa dipakai

Kueri "cara membuat sop bisnis kecil" memberi tayangan tertinggi 4.463.000 pada satu putaran dan
828.200 pada putaran lain. Selisihnya lima kali. Penyebabnya video yang muncul di posisi teratas
berganti-ganti antar permintaan.

Median 10 teratas jauh lebih stabil: 14.216 sampai 17.726 pada kueri yang sama. Jadi yang dipakai
median, bukan tertinggi. Kolom "di atas 100 rb" juga perlu diperiksa manual karena video yang
hanya cocok kata kuncinya ikut terhitung.

### 3. Hasil pencarian berubah antar putaran

Kueri "kapan sebaiknya menaikkan harga" memberi median 13.368 sampai 65.923 dalam lima putaran.
Rasio 4,9 kali. Satu putaran tidak cukup untuk menentukan skor.

Perbaikannya: tiga putaran per kueri, ambil median dari ketiga median. Biayanya tiga kali lipat,
tetapi tetap di bawah empat menit untuk 15 kueri.

### 4. YouTube menerjemahkan judul video asing ke bahasa Indonesia

Ini yang paling berbahaya. Video The Futur tampil sebagai "Cara Menentukan Harga Layanan Anda",
padahal judul aslinya "How To Price Your Services To Make MORE Money & Give MORE Value".

Akibatnya pindai **melebih-lebihkan pasokan Indonesia**. Video Alex Hormozi, Tony Robbins, The
Futur, Rory Sutherland, dan Philip VanDusen semuanya terhitung sebagai hasil berbahasa Indonesia.

Yang harus dilakukan: setiap video teratas diperiksa kanalnya. Kalau kanalnya asing, ia bukti
permintaan, bukan bukti pasokan lokal. Tanpa langkah ini, setiap gap akan terlihat lebih sempit
daripada kenyataannya.

### 5. Skor tidak bisa menggantikan kriteria gugur

Lima topik mendapat 20. Tiga di antaranya tidak boleh diproduksi apa adanya: arus kas karena
pasokan sudah dalam, CAC karena permintaan tidak ada, dan HPP per layanan karena tumpang tindih
dengan nomor 1. Tetapi ketiganya mendapat skor yang sama dengan topik yang layak.

Sebabnya: "Gap dalam" hanya bernilai 1, dan "permintaan nol" hanya bernilai 1. Dua angka kecil itu
tidak cukup untuk menjatuhkan topik yang unggul di tiga kriteria lain.

Perbaikannya: jadikan keduanya gugur **sebelum** penilaian, bukan sebagai angka di dalamnya.

---

## Yang Belum Terverifikasi

| Klaim | Status |
|---|---|
| Pasokan margin per lini layanan kosong | *Simpulan* dari judul, durasi, chapter, dan deskripsi 3 video. Belum menonton satu video penuh. |
| Video lokal dangkal | *Simpulan* dari durasi dan bentuk judul. Belum ditonton. |
| Kapasitas 2 hari kerja | *Tebakan*. Belum pernah diukur. |
| Bobot 2-2-1-1 | *Tebakan*. Belum diuji pada satu video pun. |
| Sumber tipe B cocok untuk audiens Indonesia | *Simpulan*. Ketiga sumber berbahasa Inggris dan berasal dari konteks luar. |
| Permintaan "margin" berasal dari pemilik bisnis jasa | *Tebakan*. Penonton video margin yang ada sebagian besar pedagang, bukan pemilik bisnis jasa. |

Satu hal yang tidak bisa saya kerjakan: menonton video. Karena itu gerbang nomor 6 di
`01-ideasi.md` ("dua video teratas per kandidat sudah ditonton") **belum lulus**. Penggantinya
adalah membaca chapter dan deskripsi, yang lebih lemah daripada menonton.

---

## Waktu

| Pekerjaan | Perkiraan SOP | Aktual |
|---|---|---|
| Susun kueri | 10 menit | 15 menit |
| Jalankan pindai | 10 menit | 40 menit (termasuk 3 putaran dan perbaikan skrip) |
| Klasifikasi pasokan | 20 menit | 55 menit |
| Rumuskan sudut | 15 menit | 20 menit |
| Tentukan bukti dan skor | 20 menit | 45 menit (termasuk mencari 3 sumber) |
| Tulis masalah audiens | 10 menit | 10 menit |
| **Total** | **85 menit** | **185 menit** |

Perkiraan 85 menit terlalu optimistis untuk putaran pertama. Sebagian karena skripnya masih rusak.
Putaran kedua seharusnya mendekati 100–120 menit, dan itu pun hanya kalau sumber bukti tidak
dicari dari nol.
