# Tahap 1 — Memilih Ide yang Layak Diproduksi

> **Posisi:** Tahap pertama dari sepuluh.
> **Tahap berikutnya:** [02 — Pengemasan](./02-pengemasan.md).
> **Keluaran:** satu kandidat utama dan maksimal dua cadangan, masing-masing dengan alasan yang dapat diperiksa.

---

## Tujuan

Memilih satu masalah audiens yang layak dijadikan video berikutnya. Ide yang lolos harus memiliki keputusan yang jelas, alasan penonton peduli, celah di YouTube Indonesia, dan jenis bukti awal yang realistis.

Tahap ini belum membuat judul, teks atau ilustrasi thumbnail, maupun outline video. Pekerjaan itu berada di Tahap 2 dan Tahap 4. Memaksakannya di sini membuat kemasan menjanjikan sesuatu sebelum riset membuktikan bahwa janji tersebut dapat dipenuhi.

## Keluaran Wajib

Setiap kandidat utama dan cadangan memuat tujuh hal berikut.

| Keluaran | Pertanyaan yang dijawab | Dipakai oleh |
|---|---|---|
| Pintu masuk | Situasi atau rasa sakit apa yang dikenali bahkan oleh calon pemilik bisnis? | Tahap 2–4 |
| Masalah audiens | Siapa yang mengalami masalah apa, dan apa akibatnya? | Tahap 2–4 |
| Sudut keputusan | Keputusan apa yang perlu dibuat penonton? | Tahap 2–4 |
| Ketegangan lanjut | Ukuran, trade-off, atau batas apa yang tetap penting bagi operator yang lebih matang? | Tahap 3–4 |
| Sinyal permintaan | Adakah bukti orang mencari atau membahas masalah ini? | Prioritas |
| Celah lokal | Bagian mana yang belum dibahas dengan baik di YouTube Indonesia? | Tahap 2 |
| Jenis bukti awal | Data, dokumen, atau pengukuran apa yang mungkin dipakai? | Tahap 3 |
| Hipotesis kemasan | Kontras atau bukti visual apa yang bisa membuat orang berhenti? | Tahap 2 |
| Alasan keputusan | Mengapa kandidat ini dipilih, ditunda, digabung, atau gugur? | Audit berikutnya |

**Pintu masuk** bukan penyederhanaan palsu. Ia menyebut keadaan yang bisa dikenali orang baru,
misalnya “pesanan bertambah, tetapi waktu tidak pernah cukup”. **Ketegangan lanjut** menjaga agar
video tidak berhenti di nasihat umum, misalnya “kapasitas tim tidak sama dengan jumlah orang”.

**Hipotesis kemasan** hanya satu kalimat. Contoh: “Perbandingan jam tim dan porsi omzet pada satu layanan.” Ini bukan kandidat judul atau desain thumbnail. Tahap 2 baru mengubahnya menjadi lima judul dan satu atau dua sketsa setelah bukti utamanya jelas.

## Prinsip

1. **Masalah lebih dulu, topik kemudian.** “Margin” bukan ide. “Pemilik bisnis jasa tidak tahu layanan mana yang menyerap jam tim paling banyak” adalah ide yang bisa diuji.
2. **Keputusan lebih penting daripada informasi.** Video harus membantu memilih, menghentikan, mengubah, atau mengukur sesuatu. Tutorial alat tanpa keputusan bisnis gugur.
3. **Permintaan adalah sinyal, bukan putusan.** Tayangan hasil pencarian membantu membandingkan minat. Tayangan tidak membuktikan bahwa penontonnya adalah audiens Fadhil.
4. **Gap harus berarti pembeda yang nyata.** Topik yang sudah banyak dibahas tetap dapat dipakai bila sudut, bukti, atau keputusan yang dibawa belum ada dalam video Indonesia yang relevan.
5. **Bukti dicari sebelum kemasan diputuskan.** Tahap ini hanya memastikan jenis buktinya ada. Tahap 3 yang memverifikasi klaim dan menyiapkan artefaknya.
6. **Satu kandidat utama cukup.** Pilot membuat satu video pada satu waktu. Dua kandidat lain hanya cadangan agar keputusan tidak perlu dimulai dari nol minggu depan.

## Input

| Input | Wajib | Kegunaan |
|---|---|---|
| Tiga pilar konten | Ya | Menjaga fokus positioning |
| Content bank dan brief yang ada | Ya | Mencegah pengulangan |
| Log keputusan dan inventaris bukti | Ya, jika tersedia | Mencari bukti yang khas |
| Pertanyaan audiens atau pengalaman langsung | Jika ada | Memperjelas masalah |
| Pindai YouTube | Ya | Mengukur sinyal permintaan dan pasokan lokal |
| Satu calon sumber primer atau rencana pengukuran | Ya | Memastikan riset dapat dimulai |

## Prosedur

### 1. Mulai dari pintu masuk, masalah, dan keputusan

Tulis 8 masalah calon. Ambil minimal dua dari setiap pilar, lalu gunakan dua sisanya untuk masalah dari log keputusan, komentar, atau pertanyaan audiens.

```text
[Pintu masuk yang mudah dikenali].
[Siapa] tidak tahu [hal yang perlu diketahui], sehingga mereka berisiko [akibat].
Keputusan yang dibahas: [pilihan yang harus dibuat].
Ketegangan lanjut: [ukuran, trade-off, atau batas].
```

Contoh:

> Pesanan bertambah, tetapi waktu tim semakin habis dan uang tidak terasa ikut bertambah.
> Pemilik bisnis jasa dengan tim kecil tidak tahu layanan mana yang memakai kapasitas paling besar, sehingga mereka dapat menambah penjualan pada layanan yang justru membebani laba.
> Keputusan yang dibahas: layanan mana yang perlu diukur, diubah, atau dipertahankan.
> Ketegangan lanjut: jam kerja bukan biaya langsung, tetapi tetap membatasi kapasitas yang dibayar bisnis.

Buang masalah yang tidak punya satu keputusan. “Cara memakai aplikasi X” dan “tips bisnis lebih produktif” tidak cukup spesifik untuk masuk pipeline ini.

### 2. Uji bahasa dan sinyal permintaan

Ubah setiap masalah menjadi satu atau dua frasa yang mungkin diketik pemilik bisnis. Gunakan bahasa audiens, bukan istilah internal.

```bash
python3 tools/pindai-youtube.py "frasa pertama" "frasa kedua" "frasa ketiga"
```

Skrip melakukan tiga putaran untuk setiap frasa. Catat median tayangan dan rentang hasilnya.

Sebelum memakai angkanya, periksa sepuluh hasil teratas.

- Apakah hasilnya benar-benar membahas masalah yang sama?
- Apakah orang yang menontonnya adalah pemilik bisnis jasa, edukasi, atau digital dengan tim kecil?
- Apakah hasil tinggi berasal dari video asing yang judulnya diterjemahkan otomatis?

Buang hasil yang hanya kebetulan memuat kata yang sama. Video asing boleh menjadi tanda minat, tetapi tidak dihitung sebagai pasokan lokal.

**Batas awal:** median di bawah 10.000 atau rentang lebih dari lima kali tidak dapat menjadi dasar utama pemilihan. Kandidat masih boleh disimpan jika ada bukti audiens yang lebih kuat, misalnya pertanyaan berulang dari calon penonton. Tandai alasan pengecualian itu sebagai *simpulan*.

### 3. Periksa celah lokal

Untuk kandidat yang sinyalnya cukup, buka dua hasil Indonesia yang paling relevan. Gunakan `tools/cek-video.py` untuk membaca judul asli, deskripsi, dan chapter.

| Kelas | Arti |
|---|---|
| `lebar` | Tidak ada video Indonesia yang membahas keputusan ini secara langsung. |
| `sedang` | Ada yang membahas topiknya, tetapi tanpa keputusan jelas, bukti, atau trade-off. |
| `sempit` | Ada video Indonesia yang sudah membahas keputusan, bukti, dan batasnya dengan baik. |

Kelas **sempit** tidak otomatis membuat topik gugur. Kandidat hanya lanjut jika ada pembeda yang dapat disebut dalam satu kalimat: bukti yang lebih kuat, audiens yang lebih spesifik, atau keputusan yang lebih sempit. Jika tidak ada, gugurkan. Membuat versi yang sama tidak memberi alasan bagi penonton untuk memilih video ini.

### 4. Tetapkan jenis bukti awal

Setiap kandidat harus memiliki satu jenis bukti awal sebelum diberi peringkat.

| Jenis bukti awal | Bukti awal yang cukup di Tahap 1 | Yang dilakukan di Tahap 3 |
|---|---|---|
| A. Catatan sendiri | Nama dokumen atau catatan yang ada dan aman dibuka | Periksa angka, izin, dan samaran |
| B. Sumber primer publik | Tautan laporan, filing, statistik resmi, jurnal, atau siaran pers | Baca sumber asli dan verifikasi klaim |
| C. Pengukuran untuk video | Apa yang diukur, siapa yang mencatat, dan kapan selesai | Jalankan pengukuran dan simpan artefaknya |
| D. Batas pengalaman | Batas yang akan disebut eksplisit dan dokumen publik pendukung | Pastikan video tidak mengaku punya data sendiri |

Sumber sekunder hanya boleh membantu menemukan sumber primer. Kalau tidak ada jenis bukti awal, kandidat tidak masuk peringkat. Jangan mencari lima sumber di tahap ini. Satu jenis bukti yang nyata sudah cukup untuk mengirim topik ke Tahap 3.

Huruf A–D di sini adalah **jenis bukti awal**, bukan tiga jalur bukti di
`03-riset-dan-fakta.md` Langkah 5. Pemetaan ke kolom `jenis_bukti`: A → `data sendiri` (skor 5),
B dan C → `riset primer` (skor 3), D → `tanpa sumber primer` (skor 1). Tiga jalur di Tahap 3
memakai nomor 1–3: catatan sendiri, pengukuran untuk video, dan batas pengalaman.

### 5. Uji hipotesis kemasan

Tuliskan satu kalimat tentang hal yang secara visual akan membuat masalah ini terasa nyata.

| Masalah | Hipotesis kemasan |
|---|---|
| Layanan ramai menguras kapasitas | Satu baris tabel yang jam timnya jauh lebih besar daripada porsi omzetnya. |
| Harga jasa tidak menutup kerja tambahan | Perbandingan harga awal dengan biaya revisi yang muncul sesudahnya. |
| Founder menjadi persetujuan untuk semua pekerjaan | Kalender yang penuh rapat persetujuan dibandingkan jam kerja tim yang menunggu. |

Jika tidak ada kontras, artefak, atau pertanyaan tajam yang dapat disebut, kandidat boleh disimpan. Namun jangan menjadi kandidat utama sebelum Tahap 2 menunjukkan kemasan yang benar-benar bekerja.

### 6. Beri nilai untuk mengurutkan, lalu putuskan dengan gerbang

Gunakan skor database yang sudah ada. Skor membantu mengurutkan kandidat, bukan memberi izin produksi.

| Kriteria | Nilai 5 | Nilai 3 | Nilai terendah |
|---|---|---|---|
| Permintaan | Median di atas 100.000 | Median 10.000–100.000 | Di bawah 10.000 atau tidak stabil (1) |
| Celah | `lebar` | `sedang`, atau `sempit` dengan pembeda yang jelas | `sempit` tanpa pembeda (0) |
| Bukti | Catatan sendiri yang aman dibuka | Sumber primer atau pengukuran siap jalan | Hanya sumber sekunder atau batas pengalaman tanpa dokumen pendukung (1) |
| Kapasitas | Dapat disiapkan dalam dua hari kerja | Empat hari kerja | Lebih dari satu minggu (1) |

Rumus database tetap:

```text
skor_total = (skor_permintaan × 2) + (skor_celah_pasokan × 2) + skor_bukti + skor_kapasitas
```

Gunakan `skor_prioritas_konsep` hanya untuk menunjukkan dampak masalah jika dibiarkan salah. Ia tidak boleh mengalahkan gerbang di bawah.

**Gerbang kandidat utama:**

- pintu masuk, masalah, keputusan, dan ketegangan lanjut jelas;
- sinyal permintaan relevan atau ada alasan pengecualian yang tertulis;
- celah lokal ada, atau pembeda terhadap video yang sudah dalam dapat dijelaskan;
- jenis bukti awal yang nyata;
- tidak mengulang ide, brief, atau video Fadhil yang sudah ada;
- hipotesis kemasan ada.

Kandidat yang lolos semua gerbang dengan skor tertinggi menjadi **utama**. Simpan maksimal dua berikutnya sebagai **cadangan**. Kandidat lain diberi status `perlu perbaikan`, `ditunda`, `digabung`, atau `gugur` beserta satu alasan.

### 7. Catat hasil dan serahkan ke Tahap 2

Simpan hasil pindai di `content/pindai/pindai-topik-[tanggal].md`, lalu masukkan kandidat yang masih hidup ke database melalui `tools/tambah-ide.py`.

Tahap 2 hanya menerima kandidat utama beserta tujuh keluaran pada tabel pertama. Tahap 2 wajib membuat kandidat judul, teks thumbnail, dan sketsa thumbnail. Jika kemasannya tidak lulus, kembali ke kandidat cadangan atau revisi sudutnya.

## Format Hasil Pindai

```markdown
# Pindai Topik — [Tanggal]

## Kandidat utama

- **Sudut:** [satu kalimat]
- **Pilar dan format:** [pilar] / [format]
- **Pintu masuk:** [situasi yang mudah dikenali]
- **Masalah audiens:** [siapa, masalah, akibat]
- **Keputusan yang dibahas:** [satu keputusan]
- **Ketegangan lanjut:** [ukuran, trade-off, atau batas]
- **Sinyal permintaan:** [kueri, median, rentang, pemeriksaan relevansi]
- **Celah lokal:** [lebar/sedang/sempit + pembeda]
- **Jenis bukti awal:** [A/B/C/D + tautan atau nama dokumen]
- **Hipotesis kemasan:** [satu kontras, artefak, atau pertanyaan]
- **Skor:** [rincian dan total]
- **Keputusan:** Utama, karena [alasan].

## Kandidat cadangan

### [Sudut]
[Tujuh keluaran yang sama, lebih ringkas.]

## Kandidat tidak dipilih

| Sudut | Status | Alasan |
|---|---|---|
| | `perlu perbaikan` / `ditunda` / `digabung` / `gugur` | |
```

## Gerbang Keluaran

- [ ] Delapan masalah calon telah ditulis; masing-masing punya pintu masuk, keputusan, dan ketegangan lanjut.
- [ ] Minimal enam kueri relevan telah dipindai, masing-masing dalam tiga putaran.
- [ ] Hasil yang tidak relevan dan channel asing telah ditandai sebelum angka dibaca.
- [ ] Dua hasil lokal paling relevan untuk kandidat utama telah diperiksa melalui deskripsi dan chapter.
- [ ] Satu kandidat utama dan maksimal dua cadangan memiliki tujuh keluaran wajib.
- [ ] Kandidat utama memiliki jenis bukti awal yang nyata, bukan hanya ide mencari bukti.
- [ ] Kandidat utama memiliki hipotesis kemasan, bukan judul atau thumbnail final.
- [ ] Kandidat yang tidak dipilih memiliki alasan singkat dan tercatat.
- [ ] Kandidat hidup telah masuk ke `database/database.db`.

## Batas Waktu

Gunakan batas kerja 90 menit setelah kueri dan sumber yang sering dipakai sudah tersedia. Jika waktunya habis, jangan memperdalam semua kandidat. Pilih kandidat yang bukti awalnya paling dekat, simpan sisanya sebagai cadangan, lalu lanjut ke Tahap 2.

Ini target uji, bukan waktu yang sudah terbukti. Versi lama membutuhkan sekitar 160–185 menit.
Ukur empat putaran berikutnya sebelum menetapkan batas permanen. Jika masih melewati 90 menit,
catat penyebabnya. Biasanya masalahnya salah satu dari tiga: kueri terlalu banyak, pemeriksaan
relevansi belum punya aturan yang jelas, atau riset primer seharusnya dipindahkan ke Tahap 3.

## Kesalahan Umum

| Kesalahan | Dampak | Perbaikan |
|---|---|---|
| Memulai dari daftar topik luas | Video berakhir sebagai penjelasan umum | Mulai dari masalah dan satu keputusan |
| Menganggap tayangan sebagai permintaan murni | Topik dari industri lain ikut lolos | Periksa relevansi hasil dan audiens |
| Menilai supply dari jumlah hasil | Topik mati terlihat seperti peluang | Periksa dua video lokal yang paling relevan |
| Menggunakan skor untuk memutuskan | Kandidat lemah terlihat objektif | Pakai skor untuk urutan; pakai gerbang untuk memilih |
| Mencari lima sumber sebelum memilih kandidat | Tahap 1 berubah menjadi riset penuh | Cukup pastikan satu jenis bukti awal yang nyata |
| Membuat judul dan thumbnail final di Tahap 1 | Janji dibuat sebelum bukti diperiksa | Kirim hipotesis kemasan ke Tahap 2 |
| Membuat outline lengkap di Tahap 1 | Naskah dibangun sebelum fakta terkumpul | Tahap 1 hanya menetapkan keputusan yang akan dijawab |
| Memilih tiga topik untuk diproduksi sekaligus | Minggu berikutnya harus memilih ulang | Pilih satu utama dan dua cadangan |

## Hubungan dengan Tahap Lain

| Ke | Yang dikirim |
|---|---|
| Tahap 2 — Pengemasan | Pintu masuk, masalah, sudut keputusan, ketegangan lanjut, pembeda, jenis bukti awal, hipotesis kemasan |
| Tahap 3 — Riset | Jenis bukti awal yang harus diverifikasi |
| Content bank | Kandidat tunda, gabung, dan gugur beserta alasan |
| Database ide | Kandidat hidup beserta skor dan status |

*Terakhir diperbarui: 3 November 2026*
