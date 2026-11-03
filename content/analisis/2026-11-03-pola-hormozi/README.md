# Pola Judul Hormozi dan Uji Transfer ke Pasar Indonesia

Tanggal: 3 November 2026.
Pertanyaan: apakah judul yang menyerang **rasa sakit akibat tidak adanya** strategi, keuangan,
people, atau sistem bisa dipakai di pasar Indonesia, atau hanya bekerja di Amerika?

---

## 1. Yang dibaca

### Channel

`python3 tools/ambil-daftar-video.py AlexHormozi leilahormozi`

| Channel | Subscriber | Video terdaftar |
|---|---|---|
| Alex Hormozi | 4,61 juta | 30 |
| Leila Hormozi | 1,77 juta | 30 |

**Jebakan yang muncul saat membaca.** YouTube menyajikan judul Leila dalam bahasa Indonesia hasil
terjemahan otomatis ("Mengapa Anda Harus MENGHAPUS Masalah Anda Daripada Menyelesaikannya"). Yang
terbaca di daftar bukan judul aslinya. Untuk tiga video yang diperiksa satu per satu, judul asli
berbahasa Inggris didapat dari `tools/cek-video.py`. Ini kejadian yang sama dengan Temuan 8 di
`content/analisis/2026-11-03-pasar-indonesia/`: judul terjemahan adalah jebakan baca, bukan pola.

### Tiga video yang diperiksa

| ID | Judul asli | Durasi | Tayangan |
|---|---|---|---|
| `RdAKXJlMIZM` | How to get SO rich you question the meaning of making money | 3.13.57 | tidak dibaca |
| `9OkBN4uor5M` | Success is Hard Until You Build Systems Like This | 17.32 | 271 rb |
| `ZuJryiwxjDw` | Why you aren't making as much money as you want | 36.20 | tidak dibaca |

Tidak ada chapter di ketiganya. Transkrip diambil lewat `yt-dlp` untuk dua video
(`9OkBN4uor5M`, `ZuJryiwxjDw`). Yang dibaca hanya bagian pembuka, bukan seluruh isi.

---

## 2. Struktur judulnya

Tiga contoh, tiga mekanisme berbeda, satu kesamaan.

**`ZuJryiwxjDw` — "Why you aren't making as much money as you want".**
Kalimat pertama transkrip: *"You aren't making as much money as you want because you don't know how
to get it from the people who've got it."* Judulnya adalah **keluhan penonton sendiri, kata per
kata**. Isi videonya bukan tentang keluhan itu. Isinya distribusi kekayaan AS, lalu 80/20, lalu
harga. Penonton tidak pernah mencari "distribusi kekayaan AS". Ia mencari kelegaannya.

**`9OkBN4uor5M` — "Success is Hard Until You Build Systems Like This".**
Bentuknya `[X] susah sampai kamu punya [Y]`. Kalimat pertama: *"building a billion dollar company
from zero has nothing to do with working harder and everything to do with building better systems
... there is a reason that 99% people stay stuck and it is not lack of effort."* Yang diserang
bukan "cara bikin sistem", melainkan **keyakinan penonton bahwa masalahnya kurang usaha**.

**`RdAKXJlMIZM` — "How to get SO rich you question the meaning of making money".**
Bentuknya hasil ekstrem yang sengaja dibesar-besarkan, lalu dibayar dengan durasi 3 jam 13 menit.

**Kesamaannya, dan ini yang penting:** judulnya adalah **gejala atau hasil**, bukan topik. Topik
(mekanisme, sistem, harga, distribusi) ada di dalam video dan tidak pernah muncul di judul. Tidak
ada satu pun dari ketiganya yang berbentuk "Cara Membangun Sistem" atau "Cara Menentukan Harga".

Bandingkan dengan judul lain di channel yang sama, yang justru **gagal** memakai pola ini:
"How I Would Build a $10M Service Business (If I Had to Start Over)" dan "Building a $3,000,000
Business for a Stranger in 31 Minutes". Keduanya bergantung pada otoritas dan rekaman langsung
yang tidak dimiliki Fadhil. Jangan diambil.

---

## 3. Apa yang belum ada di `01-ideasi.md`

Empat hal, dan yang keempat adalah akar masalahnya.

**a. Langkah 1 dimulai dari ketidaktahuan, bukan dari gejala.**
Templatnya berbunyi "[Siapa] tidak tahu [hal], sehingga berisiko [akibat]". Bentuk ini menghasilkan
topik berpengetahuan: "cara menghitung margin". Bentuk Hormozi dimulai dari yang sudah dirasakan:
"omzet naik, tapi saya makin capek". Keduanya berakhir di tempat berbeda.

**b. Tidak ada inventaris ketiadaan.**
Tidak ada tempat yang menjawab: kalau pilar ini tidak ada, apa yang pertama rusak, dan apa yang
dikeluhkan pemiliknya? Tanpa itu, judul bergaya Hormozi hanya lahir kalau kebetulan terpikir.

**c. Jangkar judul terlalu sempit.**
Tabel jangkar di Langkah 5 hanya mengizinkan situasi Fadhil, entitas, atau angka. Padahal jangkar
paling murah adalah **keadaan penonton sendiri**, yang tidak butuh data dan tidak butuh izin.

**d. Langkah 2 memaksa setiap masalah menjadi frasa pencarian.** Ini akarnya.
Kueri hanya bisa memuat hal yang sudah punya nama. "Cara menghitung laba bersih" punya nama.
"Budaya tim yang keracunan" tidak. Jadi gerbang permintaan menyaring masuk keuangan dan
operasional yang sudah bernama, dan membuang people serta sistem yang belum punya kata kunci.
Ini penjelasan mekanis untuk bias yang sudah terlihat sebelumnya, bukan dugaan.

---

## 4. Uji ke pasar Indonesia

14 kueri, masing-masing tiga putaran, `hl=id&gl=ID`.

### 4a. Yang diukur

Bukan median saja. Yang menentukan adalah **tayangan video yang benar-benar cocok dengan kueri**,
dibaca dari lima judul teratas. Median bisa datang dari video yang topiknya lain.

### 4b. Hasil

| Kueri | Median 10 teratas | Stabilitas | Video yang benar-benar cocok | Tayangannya |
|---|---|---|---|---|
| kenapa bisnis gak berkembang | 401.866 | 1,6x | "Kesalahan Fatal yang Bikin Bisnis Susah Berkembang" | 151.342 |
| kenapa bisnis gak bisa besar | 494.746 | 1,5x | "Kenapa Mayoritas Bisnis UMKM Kalian GAGAL" | 488.001 |
| cara membesarkan bisnis kecil | 568.402 | 1,6x | "4 CARA MEMBESARKAN BISNIS ANDA DENGAN CEPAT" | 365.879 |
| dari 100 juta jadi 1 miliar | 498.109 | 2,8x | "Dari 100 Juta Pertama Jadi 1 Miliar" | **12.297** |
| bisnis ramai tapi gak ada untung | 687.366 | 2,6x | "RAMAI TAPI TAK UNTUNG! Kenapa Jualan Laris..." | **22** |
| bisnis gak punya sistem | 1.228.167 | 1,0x | "BISNIS Tidak Cukup MODAL, Harus PUNYA SISTEM" | **4.914** |
| omzet naik untung gak nambah | 16.115 | **102,3x** | "OMZET NAIK, TAPI KEUNTUNGAN TIDAK BERTAMBAH?" | **3.843** |
| karyawan gak bisa diandalkan | 154.698 | **11,9x** | "10 TANDA KARYAWAN YANG DAPAT DIANDALKAN" | 18.131 |
| capek kerja tapi bisnis gak maju | 337.743 | 1,3x | "Kerja Capek, Karier Gak Maju" (tentang karyawan) | **2.482** |
| gak bisa lepas dari bisnis sendiri | 404.257 | 3,6x | tidak ada yang cocok (drama, karier) | — |
| semua dikerjain sendiri capek | 590.894 | 1,7x | tidak ada yang cocok (burnout, kesehatan mental) | — |
| bisnis stuck gak maju | 444.703 | 1,2x | "BISNIS ANDA STUCK?? MUNGKIN 3 KESALAHAN FATAL" | **1.762** |
| bisnis tergantung pemilik | 475.922 | 3,4x | "Peran Pemilik Bisnis dalam Mengelola Karyawan" | 38.369 |
| cara naikin omzet 10 kali | 260.545 | 1,9x | "Cara Meningkatkan Income 10 Kali Lipat" | 81.051 |

### 4c. Pola yang terbaca

Ada hubungan yang rapi dan monoton:

- Kueri pada level **hasil umum** ("kenapa bisnis gak bisa besar") menemukan video yang cocok
  dengan 150.000–488.000 tayangan.
- Kueri pada level **gejala spesifik** ("omzet naik untung gak nambah") menemukan video yang cocok
  dengan 22–18.000 tayangan.
- Kueri pada level **mekanisme** ("bisnis gak punya sistem") menemukan video yang cocok dengan
  4.914 tayangan, sementara mediannya 1,2 juta dari video "mulai bisnis dari nol".

Jadi di Indonesia, permintaan terkumpul di **level hasil**, bukan di level mekanisme. Ini kebalikan
dari yang dibutuhkan kalau judulnya menyebut mekanisme.

**Empat kueri gagal gerbang dan tidak boleh dipakai sebagai bukti apa pun:**

- `omzet naik untung gak nambah` — rentang 102,3x, median 16.115. Tidak stabil.
- `karyawan gak bisa diandalkan` — rentang 11,9x, dan hasil teratas adalah konten hubungan
  interpersonal, bukan konten manajemen.
- `semua dikerjain sendiri capek` — hasilnya konten burnout dan kesehatan mental (Raditya Dika
  2,3 juta, Lavendaire 4,6 juta). Tidak ada satu pun tentang bisnis.
- `gak bisa lepas dari bisnis sendiri` — hasil teratas drama keluarga.

### 4d. Jawaban atas hipotesis "dari 100 juta jadi 1 miliar"

**Tidak bekerja, dan datanya jelas.** Median 498.109 itu datang dari konten saham dan investasi
("BEDAH PORTOFOLIO SAHAM! 100 JUTA BISA JADI 1 MILIAR??" 89.648; "KENAPA 1 MILIAR LEBIH MUDAH
SETELAH 100 JUTA PERTAMA" 5.913). Video yang benar-benar memakai kerangka "dari 100 juta jadi 1
miliar" untuk bisnis hanya mendapat 12.297 tayangan.

Kalimatnya terdengar masuk akal karena enak diucapkan, bukan karena ada orang yang mencarinya.
Ini persis jebakan yang sudah tercatat di Langkah 5: enak diucapkan bukan bukti ada yang menonton.

Yang bekerja adalah versi **tanpa angka**: "kenapa bisnis gak bisa besar" (494.746, stabil 1,5x).

---

## 5. Kesimpulan

**Pola Hormozi tidak bisa dipindahkan apa adanya, tetapi bukan karena pasar Indonesia berbeda
selera.** Ia tidak bisa dipindahkan karena **cara kita mengukur permintaan tidak cocok untuk judul
jenis itu**.

Judul Hormozi dirancang untuk feed dan rekomendasi. Tidak ada orang yang mengetik "why you aren't
making as much money as you want". Kalau judul seperti itu diuji dengan median pencarian, ia selalu
gugur — bukan karena tidak akan ditonton, tetapi karena metodenya tidak mengukur hal itu.

Maka aturan yang diambil:

1. **Judul tetap di level hasil.** Mekanisme masuk ke dalam video, bukan ke judul.
2. **Permintaan diukur di level hasil, bukan level mekanisme.** Kueri "bisnis gak punya sistem"
   tidak boleh dipakai untuk menilai ide bersistem; yang diukur "kenapa bisnis gak bisa besar".
3. **Celah dinilai di level mekanisme.** Kalau lima judul teratas membahas hasilnya tanpa
   menjelaskan sebabnya, celahnya ada — meskipun permintaannya besar.
4. **Angka di judul hanya kalau angkanya milik Fadhil.** Bukan angka ambisi seperti "1 miliar".

Status bukti: tabel di 4b *terverifikasi* dari keluaran `tools/pindai-youtube.py` pada 3 November
2026. Kesimpulan di bagian 5 adalah *simpulan*, bukan temuan. Klaim tentang cara Hormozi memilih
judul tidak dibuat di sini — yang dibaca hanya judul, tayangan, dan pembuka transkrip.

---

## 6. Kalibrasi tambahan: presisi kueri bukan prediksi tayangan

Pada 3 November 2026, delapan kueri tambahan diuji tiga putaran untuk menjawab apakah kueri yang
lebih presisi memberi perkiraan tayangan yang lebih baik.

| Kueri | Median | Rentang | Pembacaan relevansi |
|---|---:|---:|---|
| harga jasa jam kerja tim | 44 | 570,7x | Dua hasil; keduanya tidak membahas harga jasa berbasis jam tim. Tidak layak dipakai. |
| cara menghitung harga jasa | 155.591 | 1,0x | Stabil; ada video relevan tentang HPP jasa dan harga freelance, meskipun campur niche. |
| biaya tenaga kerja harga jasa | 9.771 | 2,4x | Mayoritas hasil adalah kuliah akuntansi. Sinyal lemah. |
| semua dikerjain sendiri bisnis | 1.533.083 | 1,0x | Median didominasi video asing dan konten "memulai bisnis sendiri". Tidak layak dipakai. |
| owner bisnis jadi bottleneck | 12.816 | 542,8x | Hasil sangat tercemar video asing dan konten bangkrut. Tidak layak dipakai. |
| bisnis tidak berkembang karena owner | 537.913 | 1,5x | Stabil; ada video lokal relevan "Kesalahan Fatal yang Bikin Bisnis Susah Berkembang" (151.342). |
| cara delegasi bisnis kecil | 279.570 | 1,9x | Ada video relevan, tetapi banyak hasil tentang rekrutmen dan delegasi umum. |

**Simpulan:** kueri persis tidak otomatis lebih prediktif; ia dapat terlalu sempit atau justru
memanggil industri lain. Pada channel baru, tidak ada kueri yang memprediksi tayangan karena view
bergantung pula pada baseline channel, impresi, CTR, dan retensi. Jalan tengah yang dipakai adalah
dua bukti terpisah: kueri hasil yang relevan untuk ukuran pasar, dan preseden kemasan lokal yang
semantik dekat untuk mengkalibrasi janji serta thumbnail. Keduanya mengurutkan prioritas; tidak ada
yang dijadikan janji view.
