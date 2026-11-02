# Pindai Topik — 2026-11-01 (Putaran 2)

> **Tujuan putaran ini:** menguji apakah Top N putaran 1 bertahan ketika kueri diganti seluruhnya.
> Lima belas kueri di bawah tidak satu pun sama dengan putaran 1. Kalau hasilnya mirip, peringkat
> itu milik pasar. Kalau hasilnya berbeda, peringkat itu milik daftar kueri saya.

---

## Hasil

| # | Sudut | Pilar | Permintaan | Gap | Bukti | Kapasitas | Skor |
|---|---|---|---|---|---|---|---|
| 1 | Harga jual layanan jasa yang biaya utamanya waktu orang, bukan bahan baku | 1 | 5/5 | 3/5 | 3/5 | 5/5 | **24/30** |
| 2 | Mengatur tim 3–8 orang: peran, ritme rapat, batas wewenang | 3 | 3/5 | 3/5 | 3/5 | 5/5 | **20/30** |
| 3 | Mendapatkan klien pertama tanpa portofolio dan tanpa jaringan | 2 | 3/5 | 3/5 | 1/5 | 5/5 | **18/30** |
| 4 | Mengukur produktivitas karyawan di bisnis jasa kecil | 3 | 3/5 | 3/5 | 1/5 | 4/5 | **17/30** |
| — | Cara membuat penawaran harga ke klien | 3 | 5/5 | 3/5 | 3/5 | 4/5 | 23/30 — **gugur di luar rumus** |

**Gerbang keluaran tidak lulus sepenuhnya.** Syarat nomor 4 menuntut tiga teratas punya bukti tipe
A atau B yang sudah diambil. Nomor 1 dan 2 punya. Nomor 3 dan 4 baru punya calon, jadi keduanya
tidak boleh naik ke Top 3 menurut aturan Langkah 5. Artinya putaran ini menghasilkan **dua topik
yang siap dikerjakan**, bukan tiga.

---

## Kenapa nomor 1, bukan nomor 2

Nomor 1 dan nomor 2 identik di tiga dari empat kriteria. Keduanya Gap 3, Bukti 3, Kapasitas 5.
Selisih empat poin seluruhnya berasal dari satu hal: nomor 1 melewati ambang 100 ribu tayangan,
nomor 2 tidak.

| | Nomor 1 | Nomor 2 |
|---|---|---|
| Median 10 teratas | 121.915 | 81.301 |
| Ambang 100 ribu | lewat | tidak lewat |
| Skor Permintaan (×2) | 5 → 10 poin | 3 → 6 poin |
| Skor total | 24 | 20 |

Karena Permintaan berbobot dua, melewati satu ambang bernilai empat poin. Tidak ada kriteria lain
yang membedakan.

**Ini harus dikatakan terang-terangan: selisih 121.915 lawan 81.301 bukan selisih yang berarti di
dunia nyata.** Yang terjadi adalah angka 81.301 jatuh di bawah garis yang saya gambar sendiri di
100 ribu. Kalau garisnya digeser ke 80 ribu, keduanya seri. Jadi nomor 1 menang bukan karena
pasarnya lebih besar, melainkan karena ambangnya.

Yang membuat nomor 1 lebih bisa dipertahankan bukan skornya, melainkan hal lain: keluarga topik
harga dan margin di bisnis jasa **muncul di kedua putaran**. Nomor 2 hanya muncul di putaran ini.
Konvergensi antar putaran adalah bukti yang lebih kuat daripada selisih empat poin.

---

## Kenapa nomor 2 tidak nomor 1

Tiga alasan, dari yang paling kuat ke yang paling lemah.

**Pertama, permintaannya di bawah ambang.** 81.301 masih di atas lantai 10 ribu, jadi topiknya
hidup, tetapi tidak cukup untuk disebut kuat. Angka ini juga berasal dari rentang yang lebar,
43.237 sampai 96.761 (2,2 kali). Nilai tengahnya bisa bergeser ke bawah 80 ribu pada putaran lain.

**Kedua, pemasok terdalamnya justru channel asing.** Tiga video "mengelola tim kecil" dengan
tayangan tertinggi adalah Leaders Talk (585.108), Leadership with Mike (298.847), dan Layla at
ProcessDriven (22.940). Ketiganya channel asing yang judulnya diterjemahkan otomatis YouTube.
Menurut aturan Langkah 3, ketiganya bukti permintaan, bukan bukti pasokan lokal. Kalau ketiganya
dihitung sebagai pasokan, celahnya terlihat tertutup padahal belum.

**Ketiga, pasokan lokal yang ada membahas hal yang berbeda.** Yang tersedia dalam bahasa Indonesia
adalah motivasi dan team building: Tom MC Ifle (90.891, 4 menit 51 detik), Hendra Hilman (32.275,
15 menit 16 detik), Fanny Winara (37.942, briefing). Tidak ada satu pun yang membahas pembagian
peran, ritme rapat, atau batas wewenang. Itu sebabnya Gap dinilai 3, bukan 5: ada video, tetapi
sudutnya berbeda. Kalau suatu hari ada video 15 menit berbahasa Indonesia yang membahas desain
peran di tim kecil, kelas gap ini berubah jadi Dalam dan topiknya gugur.

---

## Kenapa nomor 3 dan 4 tidak boleh naik

Nomor 3 dan 4 punya calon sumber tipe B, bukan sumber yang sudah diambil. Aturan Langkah 5
melarang topik bertipe C masuk tiga teratas. Keduanya tetap dicatat karena skornya di atas 18,
tetapi statusnya "layak, tunggu bukti", bukan "siap produksi".

Nomor 3 juga kalah dari nomor 2 walau skornya hanya beda satu poin, dan itu bukan karena angkanya.
Aturan tiebreak di Langkah 6 berbunyi: kalau selisih di bawah tiga poin, jangan pakai skor, pakai
pertanyaan "mana yang buktinya sudah di tangan". Nomor 2 sudah punya. Nomor 3 belum.

---

## Topik yang gugur, dan alasannya

| Kueri | Median | Alasan gugur |
|---|---|---|
| bisnis ramai tapi tidak ada untung | 549.744 | **Relevansi.** Sepuluh hasil teratas adalah ide usaha tahan krisis. Tiga video yang benar-benar cocok berjudul persis itu hanya punya 11, 12, dan 3 tayangan. |
| marketing tidak menghasilkan penjualan | 591.555 | **Relevansi.** Hasilnya konten marketing umum. Dua video yang benar-benar cocok berjudul itu hanya 1.056 dan 24.339 tayangan. |
| kapan menolak proyek | 66.287 | **Relevansi.** Seluruhnya berita penolakan proyek pemerintah: IKN, nikel, geotermal. Tidak ada satu pun tentang menolak klien. |
| cara menghitung biaya operasional usaha | 71.528 | **Gap Dalam.** Kelly Patricia punya lima video, ditambah Foodizz, Master SOP, dan Rizki Arfian 15 menit. Sudah dikerjakan tuntas. |
| kapan bisnis butuh sistem | 161.778 | **Gap Dalam.** Raymond Chin, Hendra Hilman, kasisolusi, Dr. Indrawan. Rentang putaran juga 3,6 kali, mendekati batas. |
| karyawan tidak mau ikut aturan | 23.458 | **Gap Dalam.** Tom MC Ifle, 18 menit 2 detik, 151.959 tayangan, judulnya persis sudut ini. |
| cara membuat laporan mingguan | 97.639 | **Audiens.** Relevansi kata kunci sempurna, bahkan rentangnya 1,0 kali. Tetapi dua puluh hasil teratas seluruhnya laporan proyek konstruksi. Yang mencari frasa ini insinyur sipil, bukan pemilik bisnis jasa. |
| cara memisahkan uang pribadi dan usaha | 806.782 | **Rentang 11,8 kali.** Melewati batas 5 kali, jadi tidak boleh jadi dasar skor. |
| pelanggan tidak kembali lagi | 1.276 | **Rentang 10,7 kali, ditambah relevansi gagal.** Hasil teratas drama 80 juta tayangan. |
| cara membuat penawaran harga ke klien | 104.899 | **Di luar rumus.** Skornya 23, tetapi isinya tutorial Excel dan aplikasi quotation. Itu bukan keputusan bisnis, jadi tidak punya POV. Rumus tidak punya kriteria kesesuaian pilar, jadi topik ini harus digugurkan dengan alasan di luar rumus. |

---

## Bukti per Topik

### 1. Harga jual layanan jasa

- **Sumber B:** Hinterhuber, A. (2004). *Towards value-based pricing—An integrative framework for
  decision making.* Industrial Marketing Management, 33(8), 765–778.
  DOI: 10.1016/j.indmarman.2003.10.006
- **Sumber B:** Avlonitis, G. J. & Indounas, K. A. (2007). *Service pricing: An empirical
  investigation.* Journal of Retailing and Consumer Services, 14(1), 83–94.
  DOI: 10.1016/j.jretconser.2006.04.003 — 170 perusahaan di enam sektor jasa.
- **Sumber B:** Indounas, K. (2006). *Making effective pricing decisions.* Business Horizons,
  49(5), 415–424. DOI: 10.1016/j.bushor.2006.02.003
- **Angka kunci:** pada perusahaan dengan laba operasi 10%, kenaikan harga jual bersih 1%
  menaikkan laba operasi sekitar 10%. Ini dari Indounas 2006, bukan hitungan sendiri.
- **Angka yang merugikan:** Avlonitis & Indounas menemukan perusahaan jasa justru menaruh harga
  pesaing dan sikap pelanggan di atas biaya dan margin sebagai dasar penetapan harga. Artinya
  nasihat "hitung HPP lalu tambah margin" bertentangan dengan perilaku pasar. Fadhil harus
  mengakui ini di video, bukan menyembunyikannya.
- **Masalah audiens:** Pemilik bisnis jasa yang menetapkan harga dari HPP bahan dan jam kerja,
  sehingga harga yang terbentuk tidak mencerminkan kapasitas tim yang terbatas dan akhirnya
  menang kontrak yang tidak menguntungkan.
- **Status bukti:** tipe B terverifikasi. Tipe A belum ada.

### 2. Mengatur tim 3–8 orang

- **Sumber B:** Gallup (2026). *Span of Control: What's the Optimal Team Size for Managers?*
  Meta-analisis 92.252 tim, 897.971 karyawan, 104 organisasi, 26 industri. Median rentang kendali
  enam orang; tim kecil didefinisikan 4–9 orang.
- **Sumber B:** Nasrallah, W. F., Ouba, C. J., Yassine, A. A. & Srour, I. M. (2015). *Modeling the
  span of control of leaders with different skill sets.* Computational and Mathematical
  Organization Theory, 21(3). DOI: 10.1007/s10588-015-9187-8
- **Sumber B:** Belloc, F., Dughera, S. & Landini, F. (2025). *Incentive pay, managerial skills and
  span of control.* Journal of Economic Behavior & Organization, 237, 107151.
  DOI: 10.1016/j.jebo.2025.107151
- **Angka kunci:** median rentang kendali enam orang. Di bawah itu, menambah satu orang mengubah
  beban manajerial lebih banyak daripada yang biasanya diperkirakan.
- **Angka yang merugikan:** Nasrallah dkk. menemukan kemampuan manajerial menaikkan kinerja tim
  hanya sampai satu titik, lalu menurun. Menambah kemampuan manajer bukan solusi tanpa batas.
  Ini memotong nasihat "perbaiki diri dulu sebagai pemimpin".
- **Masalah audiens:** Pemilik bisnis jasa dengan tiga sampai delapan orang yang mengeluh timnya
  tidak jalan, padahal masalahnya bukan motivasi melainkan peran yang tidak pernah didefinisikan.
- **Status bukti:** tipe B terverifikasi. Tipe A belum ada.

### 3. Mendapatkan klien pertama

- **Sumber:** belum diambil. Calon: literatur akuisisi pelanggan usaha kecil.
- **Angka kunci:** median 38.598, hanya dua video di atas 100 ribu, dan keduanya channel asing
  (Alex Hormozi 1.604.331, Adam Erhart 13.265).
- **Masalah audiens:** Pemilik bisnis jasa yang baru berdiri dan tidak punya portofolio, sehingga
  tidak tahu harus membuktikan apa lebih dulu kepada calon klien.
- **Status bukti:** tipe C. Tidak boleh masuk tiga teratas.

### 4. Mengukur produktivitas karyawan

- **Sumber:** belum diambil.
- **Angka kunci:** median 33.585, satu video di atas 100 ribu, dan itu channel asing
  (Educationleaves 42.120).
- **Masalah audiens:** Pemilik bisnis jasa yang tidak bisa membedakan karyawan yang sibuk dari
  karyawan yang menghasilkan, sehingga kenaikan gaji dan penambahan orang diputuskan dari kesan.
- **Status bukti:** tipe C. Tidak boleh masuk tiga teratas.

---

## Temuan metode

Empat hal ini ditemukan saat menjalankan putaran ini, bukan sebelumnya.

**1. Kueri berjargon menaikkan median tanpa menaikkan permintaan.** Kueri "cara menaikkan nilai
transaksi" memberi median 79.291. Tetapi empat belas hasil teratas adalah konten "meningkatkan
omset" dan "trik marketing". Setelah disaring relevansi, enam video yang benar-benar membahas nilai
transaksi punya median sekitar 3.000 tayangan. Angkanya turun 26 kali. Pola yang sama muncul di
"bisnis ramai tapi tidak ada untung" (549.744 menjadi puluhan tayangan) dan "marketing tidak
menghasilkan penjualan" (591.555 menjadi ribuan). Tiga dari lima belas kueri, atau 20 persen,
memberi angka tinggi yang seluruhnya palsu.

**2. Relevansi kata kunci tidak sama dengan relevansi audiens.** "Cara membuat laporan mingguan"
mendapat median 97.639 dengan rentang 1,0 kali, kestabilan paling tinggi di seluruh putaran ini.
Relevansi kata kuncinya sempurna. Tetapi seluruh dua puluh hasil adalah laporan proyek konstruksi.
Yang mengetik frasa itu adalah insinyur sipil. SOP sekarang tidak punya pemeriksaan untuk kasus
ini, dan tanpa pemeriksaan itu topik ini akan lolos ke peringkat dua.

**3. ID video dan judul harus dicetak sebaris.** Urutan hasil pencarian berubah antar permintaan.
Saat ID dicetak di baris terpisah dari judul, ID dari satu permintaan mudah dipasangkan dengan
judul dari permintaan lain. Pada putaran ini empat dari enam pemetaan salah sebelum diperbaiki.
Akibatnya klasifikasi supply bisa memakai video yang keliru tanpa terlihat. Skrip sudah diperbaiki.

**4. Daftar channel asing yang judulnya diterjemahkan bertambah.** Yang baru terkonfirmasi:
Leaders Talk (ThinkEduca), Leadership with Mike, Layla at ProcessDriven, I Started My Business,
Rajiv Talreja, CEO Entrepreneur, Dan Martell, Educationleaves, Valuetainment, Neil Patel, Ben
Heath, Adam Erhart, Big Rob Unbothered, Thomas Morgan, Alex Hormozi. Daftar ini masuk ke
`workflows/produksi/01-ideasi.md`.

---

## Perbandingan dengan putaran 1

| | Putaran 1 | Putaran 2 |
|---|---|---|
| Nomor 1 | Margin per lini layanan di bisnis jasa (28) | Harga jual layanan jasa (24) |
| Nomor 2 | Kenaikan harga dan siapa yang benar-benar pergi (20) | Mengatur tim 3–8 orang (20) |
| Nomor 3 | Retensi per kohort (20) | Mendapatkan klien pertama (18) |
| Nomor 4 | Founder bottleneck (18) | Produktivitas karyawan (17) |
| Kueri | 19 | 15, tidak satu pun sama |

Dua daftar ini nyaris tidak beririsan. Hanya keluarga harga dan margin yang muncul di keduanya,
dan sudutnya pun berbeda: putaran 1 bertanya soal margin per lini, putaran 2 bertanya soal menetapkan
harga jasa.

**Kesimpulan yang jujur:** satu kali jalan dengan 15 kueri tidak menghasilkan peringkat yang stabil.
Yang dihasilkan adalah kumpulan kandidat, dan urutan di dalamnya sebagian besar ditentukan oleh
kueri mana yang kebetulan saya tulis. Peringkat yang bisa dipercaya lahir dari konvergensi antar
putaran, bukan dari satu putaran.

Yang bertahan di kedua putaran hanya satu: **harga dan margin di bisnis jasa**. Itu satu-satunya
sinyal dengan dua konfirmasi independen.

---

## Waktu

Tidak diukur dengan stopwatch. Perkiraan dari urutan pekerjaan: 15 menit menyusun kueri, 15 menit
memindai, 45 menit memeriksa relevansi, 40 menit mengklasifikasi supply, 25 menit mencari dan
memverifikasi sumber tipe B, 20 menit menulis. Sekitar 160 menit, di bawah 185 menit putaran 1.
