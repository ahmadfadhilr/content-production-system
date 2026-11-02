# Tahap 1 — Ideasi Berbasis Data

> **Posisi:** Tahap pertama dari sepuluh.
> **Tahap berikutnya:** [02 — Pengemasan](./02-pengemasan.md)
> **Keluaran:** daftar Top N topik, sudah diskor, siap dikemas.

---

## Tujuan

Menghasilkan **daftar Top N topik** yang layak diproduksi. Setiap topik punya tiga hal: bukti
permintaan, celah supply, dan sumber bukti yang bisa dibuka orang lain.

Keluaran tahap ini bukan satu ide. Keluarannya peringkat, supaya keputusan memilih bisa
diperiksa, bukan berdasarkan selera.

---

## Prinsip

1. **Permintaan dulu, ide belakangan.** Topik yang tidak dicari dan tidak ditanyakan tidak masuk
   daftar, sekuat apa pun POV-nya.
2. **Gap adalah sudut yang belum dibahas, bukan topik yang belum ada.** Topik "margin" sudah ada
   di mana-mana. Sudut "margin per lini layanan di bisnis jasa" belum tentu ada.
3. **Bukti boleh dari riset.** Data sendiri, laporan tahunan, filing, statistik resmi, jurnal,
   dan studi kasus semuanya sah. Yang tidak sah adalah opini tanpa sumber.
4. **Setiap skor harus bisa diperiksa.** Kalau orang lain tidak bisa mengulang penilaianmu dari
   data yang sama, skornya tidak dipakai.
5. **Satu topik, satu pilar, satu masalah.** Kalau menyentuh dua pilar, pecah.

---

## Input

| Input | Sumber | Wajib? |
|---|---|---|
| Tiga pilar konten | Bagian di bawah | ✅ |
| Kueri benih | Disusun di Langkah 1 | ✅ |
| Data permintaan YouTube | `tools/pindai-youtube.py` | ✅ |
| Sumber bukti | Laporan, jurnal, filing, data sendiri | ✅ |
| Content bank | [`content-bank.md`](./content-bank.md) | Untuk cek duplikat |
| Log keputusan | `content/log-keputusan.md` | Sumber bukti tipe A |
| Komentar audiens | YouTube, Instagram, DM | Menambah keyakinan |

---

## Prosedur

### Langkah 1 — Susun Kueri Benih

Tulis 15 kueri: lima per pilar. Pakai bahasa yang diketik pemilik bisnis, bukan bahasa akademik.

| Pilar | Contoh kueri benih |
|---|---|
| **1. Model Bisnis & Keuangan** | cara menghitung margin usaha; kapan menaikkan harga; omzet naik profit turun |
| **2. Pertumbuhan Pendapatan** | leads banyak tidak closing; cara meningkatkan konversi; biaya akuisisi pelanggan |
| **3. Operasional & Kepemimpinan** | cara delegasi tugas; bisnis tidak berkembang karena owner; cara membuat SOP |

**Aturan:** kalau sebuah kueri terdengar seperti judul skripsi, ganti. "Analisis struktur biaya"
bukan bahasa pembeli. "Kenapa profit saya kecil" adalah bahasa pembeli.

---

### Langkah 2 — Ukur Permintaan

Jalankan:

```bash
python3 tools/pindai-youtube.py "kueri 1" "kueri 2" "kueri 3"
```

Skrip menjalankan tiga putaran per kueri secara bawaan. Itu bukan pemborosan: hasil pencarian
YouTube berubah antar permintaan. Pada uji 2026-11-01, kueri yang sama memberi median 13.368
sampai 65.923 dalam lima putaran. Satu putaran tidak cukup untuk menentukan skor.

Catat tiga angka per kueri, dan abaikan sisanya:

| Angka | Arti | Dipakai? |
|---|---|---|
| **Median 10 teratas** (median dari 3 putaran) | Minat yang wajar, bukan outlier | ✅ Ya |
| Rentang 3 putaran | Seberapa tidak stabil kueri itu | ✅ Ya |
| Jumlah video di atas 100 ribu | Bukti minat berulang | ⚠️ Hanya setelah diperiksa relevansinya |
| Tayangan tertinggi | Batas atas minat | ❌ Tidak |
| Jumlah hasil | Seberapa banyak supply | ❌ Tidak |

**Kenapa tayangan tertinggi dibuang.** Pada uji yang sama, kueri "cara membuat sop bisnis kecil"
memberi angka tertinggi 4.463.000 dan 828.200 pada putaran berbeda. Selisih lima kali, karena
video di posisi teratas berganti. Angka itu mengukur keberuntungan, bukan minat.

**Ambang lulus:**

- Median 10 teratas di atas 10 ribu tayangan, **dan**
- Rentang 3 putaran tidak lebih dari 5 kali.

Kalau median di bawah 10 ribu, kueri itu topik mati. Buang. Kalau rentangnya lebih dari 5 kali,
kueri itu terlalu tidak stabil untuk dinilai; pakai hanya sebagai sinyal pendukung, bukan sebagai
dasar skor.

> [!IMPORTANT]
> Ambang ini adalah lantai, bukan gerbang. Pada uji 2026-11-01, 11 dari 15 kueri lulus. Ambang
> yang meloloskan 73% hanya menyaring kasus ekstrem. Yang benar-benar memisahkan topik hidup dari
> topik mati adalah Langkah 3 dan Langkah 3b. Jangan berhenti di sini dan merasa sudah menyaring.

**Wajib: periksa relevansi.** Sebelum menghitung, buang video yang hanya cocok kata kuncinya.
Contoh nyata: kueri "omzet naik tapi profit turun" menampilkan video "Margin Keuntungan Dijelaskan
dalam Satu Menit" (210.719 tayangan). Video itu tidak membahas omzet yang naik. Tanpa dibuang,
topik mati terlihat hidup.

Pada putaran 2 tanggal 2026-11-01, tiga dari lima belas kueri memberi median tinggi yang seluruhnya
palsu setelah disaring: "bisnis ramai tapi tidak ada untung" 549.744 menjadi puluhan tayangan,
"marketing tidak menghasilkan penjualan" 591.555 menjadi ribuan, dan "cara menaikkan nilai transaksi"
79.291 menjadi sekitar 3.000. Itu 20 persen. Kalau relevansi tidak diperiksa, ketiganya akan duduk
di peringkat satu sampai tiga.

**Waspadai kueri berjargon.** Semakin istilah yang dipakai adalah jargon internal bisnis, semakin
besar kemungkinan hasilnya konten umum yang kebetulan memuat kata itu. "Nilai transaksi" memancing
konten "meningkatkan omset". "Menolak proyek" memancing berita penolakan proyek pemerintah. Uji
cepat: kalau sepuluh judul teratas tidak ada yang memakai kata kunci utama di judulnya, kueri itu
sedang mengukur hal lain.

**Periksa relevansi audiens, bukan hanya relevansi kata kunci.** Ini kesalahan yang lolos dari
pemeriksaan di atas. Kueri "cara membuat laporan mingguan" mendapat median 97.639 dengan rentang
1,0 kali, kestabilan tertinggi di seluruh putaran, dan seluruh dua puluh hasilnya benar-benar
tentang laporan mingguan. Relevansi kata kunci sempurna. Tetapi semuanya laporan proyek konstruksi,
karena yang mengetik frasa itu insinyur sipil, bukan pemilik bisnis jasa.

Pertanyaannya bukan "apakah video ini membahas kueri", melainkan **"apakah orang yang mengetik kueri
ini adalah audiens kita"**. Kalau seluruh hasil berasal dari satu industri yang bukan audiens kita,
topiknya gugur walau angkanya bagus dan stabil.

---

### Langkah 3 — Ukur Supply

Untuk kueri yang lulus, periksa 10 video teratas. Catat:

- Durasi.
- Nama channel.
- Apakah judul menjanjikan angka, kerangka, atau hanya pengantar.
- Tahun unggah.

**Pisahkan pasokan lokal dari terjemahan.** YouTube otomatis menerjemahkan judul video asing ke
bahasa Indonesia. Video The Futur tampil sebagai "Cara Menentukan Harga Layanan Anda", padahal
judul aslinya bahasa Inggris. Tanpa pemeriksaan ini, setiap gap akan terlihat lebih sempit daripada
kenyataan, karena video asing terhitung sebagai pasokan Indonesia.

Aturannya: video dari channel asing adalah bukti **permintaan**, bukan bukti **pasokan lokal**.
Kalau yang membahas sebuah sudut hanya channel asing, sudut itu masih kosong di Indonesia.

Channel yang sudah terbukti menerjemahkan judul: Alex Hormozi, The Futur, Tony Robbins, Rory
Sutherland (Chris Williamson), Philip VanDusen, The Organic Chemistry Tutor, Modern School Bus,
Learn With Shopify, GaryVee, Success Before 30, Acumen Learning, The Legal CFO, One Minute
Economics, Young Entrepreneurs Forum, LYFE Marketing, Leaders Talk (ThinkEduca), Leadership with
Mike, Layla at ProcessDriven, I Started My Business, Rajiv Talreja, CEO Entrepreneur, Dan Martell,
Educationleaves, Valuetainment, Neil Patel, Ben Heath, Adam Erhart, Big Rob Unbothered, Thomas
Morgan. Daftar ini akan bertambah; periksa channel yang belum dikenal sebelum menghitungnya sebagai
pasokan lokal.

**Cara memeriksa:** jalankan `tools/cek-video.py`. Alat itu mencetak judul asli di samping judul
terjemahan, plus deskripsi. Deskripsi berbahasa Inggris, tautan Gumroad, atau nama chapter bahasa
Inggris adalah tanda channel asing.

> [!WARNING]
> **ID video dan judul harus diambil dalam satu permintaan.** Urutan hasil pencarian berubah antar
> permintaan. Kalau ID dicetak di baris terpisah dari judul, ID dari satu permintaan mudah
> dipasangkan dengan judul dari permintaan lain. Pada putaran 2, empat dari enam pemetaan salah
> sebelum ketahuan, dan klasifikasi supply sempat memakai video yang keliru tanpa gejala apa pun.
> Skrip sekarang mencetak ID sebaris dengan judul. Jangan memisahkannya lagi.

**Klasifikasi:**

| Kelas | Ciri | Boleh jadi gap? |
|---|---|---|
| **Kosong** | Tidak ada video Indonesia yang membahas sudut ini | Ya |
| **Dangkal** | Ada, tetapi di bawah 8 menit, atau tanpa angka, atau hanya pengantar | Ya |
| **Dalam** | Ada video 10 menit ke atas, dengan angka dan trade-off | Tidak |

> [!WARNING]
> Klasifikasi dari judul dan durasi hanya perkiraan. Sebelum masuk Top 3, buka dua video teratas
> dengan `tools/cek-video.py`. Chapter dan deskripsi menunjukkan apakah videonya benar-benar
> membahas sudut itu atau hanya menyinggungnya.

```bash
python3 tools/cek-video.py VIDEO_ID
```

Yang dicari di keluaran itu: ada chapter atau tidak, berapa lama bagian yang relevan, dan apakah
deskripsinya menyebut angka atau template. Video tanpa chapter dengan deskripsi satu baris
biasanya penjelasan singkat, bukan analisis.

> [!NOTE]
> Membaca chapter bukan menonton. Kalau chapter menunjukkan bagian yang relevan hanya 2–3 menit
> dari video 12 menit, itu bukti cukup untuk menyebutnya dangkal. Kalau chapternya justru
> menunjukkan pembahasan panjang, tonton sebelum menyimpulkan.

---

### Langkah 3b — Gugurkan Sebelum Menilai

Dua kondisi ini membatalkan topik, bukan menurunkan skornya:

| Kondisi | Tindakan |
|---|---|
| Gap kelas **Dalam** | Buang. Sudah ada yang mengerjakan lebih baik. |
| Permintaan gagal ambang Langkah 2 | Buang. Tidak ada yang mencari. |

Alasannya ditemukan saat menjalankan SOP ini: pada 2026-11-01, topik arus kas mendapat skor 20 dan
topik CAC juga 20, walau keduanya seharusnya gugur, satu karena pasokan sudah dalam dan satu karena
tidak ada yang mencari. Skor tinggi tidak bisa menyelamatkan topik yang seharusnya gugur di langkah
sebelumnya.


---

### Langkah 4 — Rumuskan Sudut

Sudut bukan topik. Sudut adalah topik + penonton spesifik + keputusan yang dibahas.

| Topik | Sudut |
|---|---|
| Margin | Margin per lini layanan di bisnis jasa yang omzetnya naik tetapi profitnya turun |
| Harga | Kapan menaikkan harga ketika churn baru terasa tiga bulan kemudian |
| Delegasi | Tugas apa yang tidak boleh didelegasikan saat kapasitas layanan mulai penuh |

**Format:**

```
SUDUT: [topik] untuk [penonton spesifik], membahas [keputusan]
```

---

### Langkah 5 — Tentukan Jenis Bukti

| Tipe | Contoh | Status |
|---|---|---|
| **A. Data sendiri** | Spreadsheet, invoice, dashboard, log keputusan | Terkuat |
| **B. Riset primer** | Laporan tahunan, filing IDX, BPS, jurnal, siaran pers resmi | Kuat |
| **C. Riset sekunder** | Artikel berita, blog, video kreator lain | Lemah, hanya pendukung |
| **D. Tanpa sumber** | Opini, "biasanya begini" | Tidak boleh |

**Aturan:** setiap topik di Top 3 wajib punya minimal satu bukti tipe A atau B. Topik yang hanya
punya tipe C boleh masuk daftar, tetapi tidak boleh masuk tiga teratas.

---

### Langkah 6 — Skor dan Peringkat

Hanya topik yang lolos Langkah 3b yang masuk sini.

| Kriteria | Bobot | Skor 5 | Skor 3 | Skor 1 |
|---|---|---|---|---|
| **Permintaan** | ×2 | Median di atas 100 rb | Median 10–100 rb | Median di bawah 10 rb |
| **Gap** | ×2 | Kosong | Dangkal | — |
| **Bukti** | ×1 | Tipe A | Tipe B | Tipe C |
| **Kapasitas** | ×1 | 2 hari kerja | 4 hari kerja | Lebih dari 1 minggu |

Gap tidak punya skor 1. Gap kelas Dalam sudah dibuang di Langkah 3b, jadi topik yang sampai di
sini paling buruk hanya Dangkal.

**Skor maksimum: 30.**

| Total | Arti |
|---|---|
| 24–30 | Produksi sekarang |
| 18–23 | Layak, tetapi perbaiki satu kriteria dulu |
| Di bawah 18 | Simpan di content bank |

> [!NOTE]
> Bobot di atas adalah tebakan awal, bukan hasil pengukuran. Ganti setelah empat video, memakai
> data mana yang benar-benar memprediksi performa.

**Batas yang harus diakui:** skor ini memeringkat, bukan memutuskan. Pada uji 2026-11-01, lima
topik mendapat nilai sama (20) padahal mutunya berbeda jauh: dua siap dikerjakan setelah satu
perbaikan, satu harus digabung, dua seharusnya gugur. Kalau dua topik berselisih kurang dari 3
poin, jangan pakai skornya sebagai alasan memilih. Pakai satu pertanyaan: mana yang buktinya sudah
di tangan, bukan baru calon.

**Ambang 100 ribu adalah garis yang saya gambar, bukan fakta pasar.** Karena Permintaan berbobot
dua, melewati ambang ini bernilai empat poin. Pada putaran 2, nomor 1 (121.915) dan nomor 2
(81.301) identik di tiga kriteria lain; seluruh selisih empat poin berasal dari satu garis itu.
Kalau ambangnya digeser ke 80 ribu, keduanya seri. Jangan menyebut selisih seperti ini sebagai
"pasarnya lebih besar".

**Rumus ini tidak punya kriteria kesesuaian pilar.** Pada putaran 2, "cara membuat penawaran harga
ke klien" mendapat 23 dan seharusnya duduk di peringkat dua. Isinya tutorial Excel dan aplikasi
quotation: itu keterampilan alat, bukan keputusan bisnis, jadi tidak punya POV dan tidak bisa
lulus rubrik editorial. Topik seperti ini harus digugurkan dengan alasan di luar rumus, dan
alasannya ditulis, bukan disembunyikan. Kandidat perbaikan: tambah kriteria kelima "Keputusan"
(apakah ada satu keputusan yang dibahas, bukan satu alat yang diajarkan). Belum diputuskan.

---

### Langkah 7 — Tulis Masalah Audiens

Untuk setiap topik di Top 3, tulis satu kalimat.

```
MASALAH AUDIENS:
[Siapa] yang [mengalami apa] sehingga [dampak negatif apa].
```

**Uji:** kalau kalimatnya bisa dipakai untuk dua topik berbeda, terlalu lebar.

---

### Langkah 8 — Periksa Duplikat

- Buka `workflows/produksi/content-bank.md` dan `content/briefs/`. Sudah ada yang mirip?
- Cari sudut itu di YouTube. Sudah dibahas dengan angka?
- Kalau sudah, ubah sudutnya atau gugurkan topiknya.

---

## Output

Simpan hasil di `content/pindai/pindai-topik-[YYYY-MM-DD].md`. Satu file per putaran, bukan
menimpa file lama, supaya perubahan peringkat antar bulan bisa dibandingkan.

```markdown
# Pindai Topik — [Tanggal]

| # | Sudut | Pilar | Permintaan | Gap | Bukti | Kapasitas | Skor |
|---|---|---|---|---|---|---|---|
| 1 | | | /5 | /5 | /5 | /5 | /30 |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |
| 5 | | | | | | | |

## Bukti per Topik

### 1. [Sudut]
- Sumber: [tautan / dokumen]
- Jenis: [A / B / C]
- Angka kunci: [___]
- Masalah audiens: [satu kalimat]
```

---

## Gerbang Keluaran

| # | Syarat | Cek |
|---|---|---|
| 1 | Minimal 10 kueri dipindai, masing-masing 3 putaran | ☐ |
| 2 | Minimal 5 kandidat diskor | ☐ |
| 3 | Tiga teratas punya skor minimal 18 | ☐ |
| 4 | Tiga teratas punya bukti tipe A atau B yang sudah diambil, bukan baru calon | ☐ |
| 5 | Setiap bukti punya tautan, DOI, atau nama dokumen | ☐ |
| 6 | Video yang hanya cocok kata kuncinya sudah dibuang dari hitungan | ☐ |
| 7 | Video dari channel asing tidak dihitung sebagai pasokan lokal | ☐ |
| 8 | Chapter dan deskripsi dua video teratas per kandidat Top 3 sudah dibaca | ☐ |
| 9 | Tidak ada duplikat dengan bank atau brief | ☐ |

> **Catatan jujur tentang gerbang 8.** Versi sebelumnya menuntut "dua video teratas sudah
> ditonton". Itu tidak bisa dikerjakan tanpa menonton, dan menonton 6 video untuk 3 kandidat
> menambah 60–120 menit ke langkah yang seharusnya 85 menit. Yang sekarang dituntut: baca chapter
> dan deskripsi. Itu bukti lebih lemah, dan harus ditulis sebagai *simpulan*, bukan
> *terverifikasi*. Kalau topik akan diproduksi, tonton satu video teratas sebelum menulis naskah.

---

## Alat

| Alat | Fungsi |
|---|---|
| `tools/pindai-youtube.py` | Mengukur permintaan dan supply. Bawaan 3 putaran per kueri. |
| `tools/cek-video.py` | Membaca chapter dan deskripsi satu video tanpa menonton |
| YouTube Autocomplete | Melihat bahasa yang benar-benar diketik |
| Google Trends | Membandingkan minat antarkueri, region Indonesia |
| Laporan tahunan / IDX / BPS / jurnal | Sumber bukti tipe B |
| Google Scholar, Scopus, DOAJ | Mencari sumber tipe B untuk topik yang tidak punya data sendiri |

---

## Kesalahan Umum

| Kesalahan | Kenapa berbahaya | Perbaikan |
|---|---|---|
| Menilai gap dari jumlah hasil | Topik mati terlihat seperti gap | Lihat median tayangan |
| Memakai tayangan tertinggi | Berubah 5 kali antar putaran | Pakai median 3 putaran |
| Satu putaran per kueri | Skor bisa berubah 5 kali lipat | Tiga putaran |
| Menghitung video terjemahan sebagai pasokan lokal | Gap terlihat lebih sempit daripada kenyataan | Periksa nama channel |
| Memakai istilah akademik | Tidak ada yang mencarinya | Pakai bahasa pembeli |
| Menganggap topik ramai sebagai peluang | Berarti supply sudah dalam | Cari sudut, bukan topik |
| Memberi skor tanpa data | Peringkat jadi selera | Setiap skor harus punya angka |
| Memindai 40 kueri | Menghabiskan waktu, hasilnya sama | Batasi 15 kueri |
| Mempercayai skor untuk memutuskan | Tiga topik bisa dapat nilai sama padahal beda mutu | Skor memeringkat; kriteria gugur memutuskan |
| Memakai kueri berjargon | Hasilnya konten umum, median naik 26 kali lipat | Uji: kata kunci utama harus muncul di judul hasil |
| Memeriksa relevansi kata kunci saja | Topik industri lain lolos ke peringkat dua | Tanya: apakah pengetik kueri ini audiens kita |
| Mengambil ID video di permintaan terpisah | ID tertukar antar permintaan, supply salah dinilai tanpa gejala | Ambil ID dan judul dalam satu permintaan |
| Membaca satu putaran sebagai peringkat final | Dua putaran bisa nyaris tidak beririsan | Peringkat yang dipercaya lahir dari konvergensi |

---

## Waktu

Angka di kolom tengah adalah hasil pengukuran 2026-11-01 pada 15 kueri, bukan perkiraan.

| Pekerjaan | Perkiraan awal | Aktual | Catatan |
|---|---|---|---|
| Susun 15 kueri | 10 menit | 15 menit | |
| Jalankan pindai | 10 menit | 40 menit | Termasuk 3 putaran dan perbaikan skrip |
| Klasifikasi supply | 20 menit | 55 menit | Bagian termahal. Membaca 10 judul per kueri. |
| Rumuskan sudut | 15 menit | 20 menit | |
| Tentukan bukti dan skor | 20 menit | 45 menit | Mencari 3 sumber tipe B dari nol |
| Tulis masalah audiens | 10 menit | 10 menit | |
| **Total** | **85 menit** | **185 menit** | |

Putaran kedua seharusnya 100–120 menit, karena kueri dan skrip sudah ada. Kalau masih di atas
150 menit, kurangi kueri dari 15 menjadi 10, jangan kurangi putaran.

**Kenyataan putaran 2:** sekitar 160 menit, tidak diukur dengan stopwatch. Lebih cepat 25 menit dari
putaran 1, tetapi masih di atas 120 menit. Yang menyerap waktu bukan pemindaian, melainkan
memeriksa relevansi 15 kueri satu per satu dan mencari sumber tipe B dari nol. Kalau ini diulang
rutin, bagian pencarian sumber yang harus dipangkas lebih dulu: pakai sumber yang sudah terkumpul
di putaran sebelumnya sebelum mencari yang baru.

---

## Hubungan dengan Tahap Lain

| Ke | Yang dikirim |
|---|---|
| Tahap 2 — Pengemasan | Sudut, penonton, masalah audiens, angka kunci |
| Tahap 3 — Riset | Sumber bukti yang harus diverifikasi |
| `content/pindai/` | Arsip hasil pindai per tanggal |
| Content bank | Kandidat yang tidak masuk Top 3 |

---

## Changelog

| Tanggal | Perubahan |
|---|---|
| 2026-10-31 | Versi awal |
| 2026-11-01 | Tambah log keputusan, empat filter, kata kunci sebagai penentu prioritas |
| 2026-11-01 | Ditulis ulang. Gap-first, bukti boleh dari riset primer, keluaran berupa peringkat Top N |
| 2026-11-01 | Setelah dijalankan: 3 putaran per kueri, tayangan tertinggi dibuang, Langkah 3b (gugurkan sebelum menilai), peringatan judul terjemahan, gerbang "tonton" diganti "baca chapter", waktu aktual 185 menit |
| 2026-11-01 | Setelah putaran 2: relevansi audiens (bukan hanya kata kunci), peringatan kueri berjargon, ID dan judul wajib satu permintaan, ambang 100 ribu diakui sebagai garis sendiri, catatan bahwa rumus tidak punya kriteria kesesuaian pilar, daftar channel asing ditambah 15 |
