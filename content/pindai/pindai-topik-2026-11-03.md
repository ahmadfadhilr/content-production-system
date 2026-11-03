# Pindai Topik — 2026-11-03

**Tahap:** 1 — Memilih ide yang layak diproduksi  
**Tujuan:** Menguji ulang kandidat lama dengan kueri baru dan menantang keputusan bahwa margin per lini layanan adalah topik terbaik.  
**Metode:** Tiga putaran per kueri memakai `tools/pindai-youtube.py`; tiga video lokal yang paling relevan dibaca melalui `tools/cek-video.py`.  
**Status data:** *terverifikasi* untuk hasil alat, judul, tayangan yang ditampilkan YouTube, deskripsi, dan chapter. Klasifikasi relevansi, celah, serta keputusan kandidat adalah *simpulan*.

## Delapan Masalah Calon

| Pilar | Masalah audiens | Keputusan yang diuji | Kueri |
|---|---|---|---|
| Keuangan | Harga jasa tidak mencerminkan waktu tim | Harga perlu dihitung dari apa? | cara menentukan harga jasa |
| Keuangan | Pemilik tidak tahu kapan harga perlu berubah | Naikkan harga atau ubah layanan? | kapan menaikkan harga jasa |
| Keuangan | Margin layanan belum terlihat | Layanan mana yang harus diukur dulu? | cara menghitung margin bisnis jasa |
| Pertumbuhan | Pelanggan tidak membeli lagi | Perbaiki retensi atau cari pelanggan baru? | pelanggan tidak kembali lagi |
| Pertumbuhan | Repeat order rendah | Periksa repeat total atau retensi per kohort? | cara meningkatkan repeat order |
| Operasional | Founder merasa selalu sibuk | Apa yang harus dihentikan atau didelegasikan? | pemilik bisnis terlalu sibuk |
| Operasional | Kapasitas tim tidak terukur | Tambah penjualan atau tambah kapasitas? | cara mengukur kapasitas tim |
| Operasional | Tugas tim kecil tumpang tindih | Peran atau beban kerja apa yang perlu dibagi? | cara membagi tugas tim kecil |

## Hasil Pindai

| Kueri | Median 10 teratas | Rentang tiga putaran | Penilaian awal |
|---|---:|---:|---|
| cara menentukan harga jasa | 136.495 | 118.377–155.550, 1,3× | Lulus angka, tetapi sebagian hasil berupa HPP umum, harga proyek, dan ongkos tukang. |
| kapan menaikkan harga jasa | 10.665 | 10.665–10.665, 1,0× | Gugur. Hasil dominan adalah konten agama dan kuliner, bukan keputusan harga jasa. |
| cara menghitung margin bisnis jasa | 136.495 | 90.227–136.495, 1,5× | Lulus angka, tetapi hasil dominan adalah margin umum, HPP produk, dan video asing. |
| pelanggan tidak kembali lagi | 29.408 | 16.030–45.923, 2,9× | Lulus angka dengan hasil yang sebagian relevan, tetapi bercampur drama dan konten nonbisnis. |
| cara meningkatkan repeat order | 22.521 | 10.648–22.521, 2,1× | Lulus angka. Hasil lokal relevan, tetapi umumnya daftar tips. |
| pemilik bisnis terlalu sibuk | 25.363 | 25.363–25.363, 1,0× | Gugur. Enam hasil yang muncul didominasi drama dan video asing. |
| cara mengukur kapasitas tim | 14.784 | 13.401–75.920, 5,7× | Ditunda. Rentang melampaui batas lima kali dan hasilnya lebih dekat ke proyek atau produksi. |
| cara membagi tugas tim kecil | 132.741 | 22.956–242.526, 10,6× | Ditunda. Rentang melampaui batas lima kali; hasil lokal tidak konsisten dengan pembagian peran di bisnis jasa. |

Angka median di atas tidak boleh dipakai sebagai ukuran permintaan bersih. Kueri harga dan margin menang secara angka, tetapi sebagian besar tayangannya datang dari hasil yang hanya sebagian cocok. Karena itu keduanya diberi skor permintaan 3, bukan 5.

## Periksa Celah Lokal

### Harga jasa ketika biaya utamanya waktu tim

Tiga hasil lokal yang diperiksa:

| Video | Temuan |
|---|---|
| EnricoJo, “Rumus Untuk Menentukan Harga Jasa Freelance Kita”, 13:42 | Deskripsi menyatakan pengalaman freelance dan tidak memiliki chapter. Sudutnya harga freelance, bukan harga layanan dengan kapasitas tim. |
| KJA ASP Official, “Begini cara menghitung HPP pada Perusahaan Jasa”, 45:00 | Deskripsi hanya satu kalimat dan tanpa chapter. Judul menunjukkan HPP perusahaan jasa, tetapi tidak cukup bukti bahwa video membahas keputusan harga saat jam tim menjadi biaya utama. |
| Hendra Hilman, “4 Cara Menentukan Harga Jual untuk Menaikkan Omset”, 21:46 | Deskripsi menjanjikan empat cara menaikkan omzet serta materi closing. Tidak terlihat fokus pada kapasitas tim atau trade-off harga. |

**Celah:** *simpulan — `sedang`.* Pasokan lokal membahas HPP, harga freelance, atau harga jual secara umum. Pembeda yang masih tersedia adalah keputusan harga untuk bisnis jasa ketika biaya utamanya kapasitas orang, bukan bahan baku.

**Jenis bukti awal:** *terverifikasi — sumber primer yang sudah tersimpan dari putaran sebelumnya.* Avlonitis dan Indounas (2007), DOI `10.1016/j.jretconser.2006.04.003`, serta Indounas (2006), DOI `10.1016/j.bushor.2006.02.003`. Tahap 3 harus membaca ulang sumber aslinya dan tidak mengubah temuannya menjadi klaim tentang bisnis jasa Indonesia.

**Hipotesis kemasan:** tabel perbandingan satu layanan: harga jual, jam tim, dan sisa kapasitas. Tabel hanya boleh memakai data Fadhil jika izinnya jelas; jika belum ada, gunakan artefak publik dan jangan mengaku sebagai pengalaman pribadi.

### Retensi per kohort, bukan repeat order total

Tiga hasil lokal yang diperiksa:

| Video | Temuan |
|---|---|
| Hendra Hilman, “7 Strategi Membuat Customer Kembali Lagi”, 45:00 | Deskripsi hanya menjanjikan tujuh strategi. Tidak ada chapter, kohort, definisi retensi, atau batas penggunaan yang terlihat. |
| Jaya Setiabudi, “Menaikkan Repeat Order”, 27:43 | Deskripsi hanya berisi profil dan promosi. Tidak ada bukti bahwa video membedakan repeat order total dari retensi per kohort. |
| Foodizz, “10 Tips Praktis Membuat Konsumen Repeat Order”, 18:20 | Jelas ditujukan untuk industri kuliner dan formatnya daftar tips. |

**Celah:** *simpulan — `sedang`.* Pasokan lokal membahas cara mendorong pembelian ulang, tetapi belum terlihat pembahasan yang membedakan angka repeat order total dari perilaku kohort pelanggan.

**Jenis bukti awal:** *terverifikasi untuk keberadaan sumber.* John Dawes (2009), “The Effect of Service Price Increases on Customer Retention”, DOI `10.1177/1094670508328986`, dan Eva Ascarza dkk. (2018), “Some Customers Would Rather Leave Without Saying Goodbye”, DOI `10.1287/mksc.2017.1057`. Tahap 3 harus menentukan klaim yang benar-benar didukung; dua sumber ini tidak otomatis membuktikan bahwa bisnis kecil Indonesia wajib memakai kohort.

**Hipotesis kemasan:** dua kelompok pelanggan yang sama-sama menghasilkan sepuluh repeat order, tetapi kelompok lama dan baru memiliki tingkat kembali yang berbeda.

### Margin per lini layanan

Tiga hasil lokal yang diperiksa:

| Video | Temuan |
|---|---|
| Kelly Patricia, “Cara HITUNG LABA BERSIH untuk Usaha Kecil”, 12:29 | Chapter membahas omzet, laba kotor, biaya variabel, biaya tetap, dan laba bersih. Video menjawab laba total, bukan margin per lini layanan. |
| Denny Santoso, “Pilih Customer Banyak, Margin Dikit atau Customer Dikit, Margin Besar?”, 15:38 | Judul membahas trade-off margin dan jumlah pelanggan. Deskripsi tidak menunjukkan pembagian biaya atau jam tim per lini. |
| KJA ASP Official, “Begini cara menghitung HPP pada Perusahaan Jasa”, 45:00 | Video membahas HPP perusahaan jasa, tetapi deskripsi terlalu pendek untuk membuktikan bahwa ia menghitung margin per lini. |

**Celah:** *simpulan — `sedang`.* Sudut per lini layanan belum tampak dalam hasil yang diperiksa. Namun kandidat belum siap menjadi utama karena artefak pembeda yang dijanjikan—catatan jam tim per layanan—belum ada.

**Jenis bukti awal:** *terverifikasi — sumber primer publik tersedia.* Lueg dan Ilieva (2024), DOI `10.1371/journal.pone.0296974`. Bukti khas Fadhil masih belum ada.

**Hipotesis kemasan:** satu baris tabel dengan porsi jam tim jauh di atas porsi omzet. Saat ini belum boleh dipakai karena belum diukur.

## Keputusan Putaran Ini

### Kandidat utama — IDEA-009

- **Sudut:** Harga jual layanan jasa untuk bisnis yang waktu orangnya terbatas.
- **Pintu masuk:** Pelanggan bilang harga mahal, padahal tim sudah kewalahan.
- **Masalah audiens:** Pemilik bisnis jasa dengan tim kecil dapat menetapkan harga dari HPP sederhana atau harga pesaing, sehingga harga tidak mencerminkan kapasitas tim yang dipakai.
- **Keputusan:** Harga dinaikkan, ruang lingkup dipersempit, atau layanan dihentikan?
- **Ketegangan lanjut:** Harga, ruang lingkup, dan kapasitas tim perlu diputuskan bersama.
- **Sinyal permintaan:** *terverifikasi — ada, tetapi relevansinya parsial.* Kueri harga jasa menghasilkan median 136.495 dengan rentang 1,3×. Setelah relevansi diperiksa, nilainya tidak layak diberi skor tertinggi.
- **Celah lokal:** *simpulan — `sedang`.*
- **Jenis bukti awal:** B, sumber primer sudah teridentifikasi.
- **Hipotesis kemasan:** perbandingan harga, jam tim, dan kapasitas tersisa.
- **Skor:** permintaan 3, celah 3, bukti 3, kapasitas 5. Total 20.
- **Alasan:** Keluarga harga dan margin muncul kembali pada putaran sebelumnya dan putaran ini. Kandidat ini tidak membutuhkan klaim bahwa Fadhil sudah memiliki tabel margin per lini.

### Cadangan pertama — IDEA-003

- **Sudut:** Retensi per kohort, bukan repeat order total.
- **Pintu masuk:** Pesanan berulang terlihat naik, tetapi pelanggan lama tidak terasa bertahan.
- **Masalah audiens:** Pemilik bisnis tidak tahu apakah repeat order datang dari pelanggan baru atau pelanggan lama, sehingga mereka dapat salah mendiagnosis retensi.
- **Keputusan:** Perbaiki retensi pelanggan yang ada atau terus mengejar pelanggan baru?
- **Ketegangan lanjut:** Repeat order total dapat menyembunyikan retensi tiap kohort pelanggan.
- **Sinyal permintaan:** *terverifikasi — cukup dan stabil.* Dua kueri retensi berada sekitar 22–29 ribu dengan rentang 2,1× dan 2,9×.
- **Celah lokal:** *simpulan — `sedang`.*
- **Jenis bukti awal:** B, dua artikel primer telah diidentifikasi.
- **Hipotesis kemasan:** perbandingan dua kohort dengan total repeat order yang sama.
- **Skor:** permintaan 3, celah 3, bukti 3, kapasitas 5. Total 20.
- **Alasan:** Bukti dan kemasannya belum khas tanpa data pelanggan yang aman dibuka. Naik menjadi utama hanya jika Tahap 2 menghasilkan kemasan kuat tanpa menyamarkan masalah menjadi ilustrasi umum.

### Cadangan kedua — IDEA-001

- **Sudut:** Margin per lini layanan di bisnis jasa.
- **Pintu masuk:** Satu layanan selalu paling sibuk, tetapi uangnya tidak terasa bertambah.
- **Masalah audiens:** Pemilik bisnis jasa tidak tahu layanan mana yang menghabiskan kapasitas paling besar.
- **Keputusan:** Layanan mana yang perlu diukur, diubah, atau dipertahankan?
- **Ketegangan lanjut:** Jam tim membatasi kapasitas meskipun belum dicatat sebagai biaya langsung.
- **Sinyal permintaan:** *terverifikasi — ada, tetapi parsial.* Kueri margin jasa berada di rentang 90.227–136.495.
- **Celah lokal:** *simpulan — `sedang`.*
- **Jenis bukti awal:** B tersedia; pengukuran jam tim (C) belum dikerjakan.
- **Hipotesis kemasan:** tabel jam tim dibanding porsi omzet, tetapi artefaknya belum ada.
- **Skor:** permintaan 3, celah 3, bukti 3, kapasitas 3. Total 18.
- **Alasan:** Tidak lagi menjadi utama. Kekuatan video ini bergantung pada pengukuran jam tim yang belum tersedia. Tanpa itu, ia akan kembali menjadi penjelasan jurnal dan ilustrasi.

## Kandidat Tidak Dipilih

| Sudut | Status | Alasan |
|---|---|---|
| Kapan menaikkan harga jasa | `gugur` | Hasil pencarian tidak relevan dengan keputusan harga bisnis jasa. |
| Pelanggan tidak kembali lagi | `digabung` | Masalah yang sama masuk kandidat retensi. |
| Founder terlalu sibuk | `gugur` | Hasil dominan tidak relevan. |
| Mengukur kapasitas tim | `ditunda` | Rentang hasil 5,7× dan audiens hasil campur. |
| Membagi tugas tim kecil | `ditunda` | Rentang hasil 10,6× dan hasil teratas tidak menjawab pembagian peran bisnis jasa. |

## Perbandingan dengan Putaran Sebelumnya

| Pertanyaan | Margin per lini | Harga jasa berbasis waktu tim |
|---|---|---|
| Apakah keluarganya bertahan di beberapa putaran? | Ya | Ya |
| Apakah bukti primer tersedia? | Ya | Ya |
| Apakah artefak khas Fadhil sudah ada? | Tidak | Tidak |
| Apakah kemasan dapat diuji tanpa mengarang hasil pribadi? | Lemah | Cukup, memakai keputusan harga dan batas ruang lingkup |
| Status setelah putaran ini | Cadangan | Utama |

Keputusan ini adalah *simpulan*, bukan fakta pasar. Yang dapat mengubahnya: pencatatan jam tim satu minggu yang menunjukkan ketimpangan nyata. Jika itu tersedia dan aman dibuka, IDEA-001 dapat kembali mengalahkan IDEA-009 karena artefaknya menjadi lebih khas.

## Catatan Metode

- Skrip gagal dijalankan di lingkungan terbatas karena akses YouTube tidak tersedia. Setelah akses jaringan tersedia, skrip berjalan normal. Ini *terverifikasi* pada putaran ini.
- Jangan memperlakukan median tinggi sebagai permintaan bersih sebelum memeriksa relevansi. Kueri “cara membagi tugas tim kecil” menghasilkan median 132.741, tetapi rentangnya 10,6× dan hasilnya tidak konsisten.
- Database tidak ditambah baris baru. Ketiga kandidat hidup sudah ada sebagai IDEA-009, IDEA-003, dan IDEA-001. Menambah baris baru akan menduplikasi sudut yang sama.

*Terakhir diperbarui: 3 November 2026*
