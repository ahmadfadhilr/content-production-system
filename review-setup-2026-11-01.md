# Review Setup — 1 November 2026

**Yang direview:** `AGENTS.md` (635 baris), 10 SOP workflow, 3 dokumen rujukan, 2 templat,
content bank, `Personal Brand Plan.docx`, dan 8 dokumen di `reference/`.

**Dasar penilaian:** prinsip dari delapan dokumen referensi. Yang paling menentukan:
*The Algorithm* (Hormozi), *The Answer to Organic Growth Is Disgusting Volume*,
*Organic Content 101*, *How I Would Build a Personal Brand in 2027*, dan
*If I Started A Personal Brand In 2026 (Dolly Parton)*.

---

## Skor

**5/10.**

Rinciannya:

| Sudut pandang | Skor | Alasan |
|---|---|---|
| Sebagai pustaka rujukan | 7/10 | Isinya jarang salah. Beberapa bagian lebih baik dari standar industri. |
| Sebagai sistem operasi untuk 30 hari ke depan | 3/10 | Belum menghasilkan satu video, dan desainnya membuat video pertama sulit terbit. |

Yang menaikkan skor dua poin: memangkas pipeline menjadi empat tahap, benar-benar menerbitkan
empat video, lalu menambah dua aset yang belum ada (log keputusan dan inventaris bukti).

---

## Empat masalah yang menentukan

### 1. Tujuan channel tidak pernah dinyatakan

*Terverifikasi.* `AGENTS.md` menjelaskan apa yang **tidak** boleh ditargetkan ("jangan
menetapkan target view atau subscriber secara arbitrer") tetapi tidak pernah menyebut untuk
apa channel ini dibangun.

Ini bukan detail administratif. Tanpa tujuan, "berhasil" tidak bisa didefinisikan, dan pilot
tidak bisa dievaluasi. Empat kemungkinan tujuan menuntut sistem yang berbeda:

| Kalau tujuannya… | Sistem yang cocok |
|---|---|
| Mendapat leads untuk jasa konsultasi | Sedikit video, sangat dalam, CTA jelas, audiens sempit |
| Membangun otoritas untuk buku atau kelas | Volume tinggi, topik konsisten, distribusi luas |
| Menjadi aset kredibilitas saat menjual | Kualitas produksi tinggi, siklus lambat tidak masalah |
| Membangun audiens media | Volume tinggi, biaya per unit rendah, iterasi cepat |

Sistem yang sekarang dibangun mengasumsikan tujuan keempat (audiens media), tetapi
positioning-nya menggambarkan tujuan pertama atau ketiga. Dua hal ini bertabrakan.

**Akibatnya:** halaman "Pilot Empat Minggu" menguji empat hipotesis tanpa menyebut kriteria
lulus. Kalau tidak ada tujuan, tidak ada kriteria.

### 2. Sistem dibangun untuk fase yang salah

*Simpulan*, berdasarkan hitungan isi repo dan prinsip *The Algorithm*.

4.473 baris dokumentasi untuk empat video yang belum ada. Itu sekitar 1.100 baris proses per
video. Hormozi menyebut urutan yang benar: pertanyakan syarat, hapus, sederhanakan, percepat,
otomatiskan. Setup ini melompat ke "spesifikasikan semuanya" sebelum sempat menghapus apa pun.

Bukti bahwa sistem ini dirancang untuk fase yang salah:

- Tahap 7 mewajibkan LUT channel, sound design sinematik, dan motion graphics. Hormozi justru
  menghapus color grading dari prosesnya setelah bertanya "apakah ini penting?" dan mendapat
  jawaban "tidak ada buktinya".
- Tahap 6 mewajibkan ganti visual setiap 3–5 detik dan melarang talking head statis lebih dari
  10 detik. Untuk video 12 menit, itu 150–200 pergantian visual. Itu pekerjaan editor penuh
  waktu, bukan pekerjaan sampingan seorang operator.
- Tahap 2 mewajibkan 3–5 opsi judul, 1–2 sketsa thumbnail per judul, uji feed, dan uji 120 px,
  untuk channel yang belum punya penonton. CTR tidak bisa diuji tanpa impressions.
- Evaluasi 48 jam mencatat CTR dan AVD pada video yang mungkin baru dilihat 40 orang. Angkanya
  derau, bukan sinyal.

**Biayanya:** setiap tambahan syarat menambah jam kerja dan menambah alasan untuk menunda
terbit. Sistem dengan 50 kotak centang di 10 gerbang akan ditinggalkan pada video kedua.

### 3. Dua aset yang paling menentukan belum ada

*Terverifikasi* lewat pembacaan seluruh repo.

**(a) Mesin pasokan ide.** `01-ideasi.md` menyebut lima sumber ide: content bank, sinyal
audiens, keyword, pengalaman langsung, dan isu terkini. Tidak ada satu pun yang berjalan
otomatis setiap minggu. Content bank berisi 40 ide statis. Sinyal audiens belum ada karena
belum ada audiens. Keyword riset adalah pekerjaan khusus, bukan kebiasaan.

Hormozi menyebut empat ember topik: *Real Time*, *Recent Past*, *Far Past*, *Manufactured*.
Dua ember pertama adalah yang paling murah dan paling khas, dan keduanya tidak ada di sistem
ini. Padahal Fadhil membuat keputusan bisnis setiap minggu. Setiap keputusan harga, setiap
perekrutan, setiap perubahan SOP adalah bahan konten yang tidak bisa ditiru kreator lain.

Tanpa log keputusan, sistem ini akan kehabisan ide di minggu keenam dan kembali ke content
bank yang sudah basi.

**(b) Inventaris bukti.** Referensi paling keras soal ini: "proof is the pudding". Personal
brand tumbuh dari pekerjaan nyata, bukan dari dokumentasi. Sistem ini punya templat lembar
fakta, tetapi tidak punya daftar aset bukti yang dimiliki Fadhil.

Pertanyaan yang belum terjawab: apa 5–10 fakta konkret dan bisa diverifikasi tentang bisnis
Fadhil yang tidak bisa dikatakan kreator bisnis Indonesia lain? Kalau daftar itu tidak ada,
channel ini hanya pendapat tambahan di antara pendapat yang sudah banyak.

Ada ketegangan yang tidak diselesaikan sistem: kredibilitas datang dari pekerjaan yang
ditunjukkan, tetapi aturan datanya adalah samarkan semaksimal mungkin. Bukti anonim lebih
lemah daripada bukti bernama. Ini keputusan yang harus diambil Fadhil, bukan default ke
kehati-hatian maksimum.

**(c) Jawaban "kenapa Fadhil".** `brand-guidelines.md` (133 baris) menghabiskan hampir
seluruhnya untuk warna dan font yang belum ada. Tidak ada satu halaman pun yang menjawab:
apa keyakinan Fadhil yang bertentangan dengan arus, apa ciri khas yang tidak dimiliki enam
kreator pembanding di Personal Brand Plan, dan apa pola yang dia patahkan.

Uji Dolly Parton: sebutkan tiga sifat langka yang biasanya tidak muncul bersamaan pada satu
orang, dan yang dimiliki Fadhil. Sistem ini tidak pernah menanyakannya. Padahal jawabannya
gratis dan jauh lebih menentukan daripada templat thumbnail.

### 4. Desain pilot mengacaukan variabel

*Terverifikasi* dari tabel "Pilot Empat Minggu" di `AGENTS.md`.

| Minggu | Pilar | Format | Hipotesis |
|---|---|---|---|
| 1 | 1 | Business Breakdown | Cerita pribadi |
| 2 | 1 | Decision Notes | Sudut finansial |
| 3 | 2 | Operating Playbook | Playbook akuisisi |
| 4 | 3 | Business Breakdown | Topik operasi |

Empat video, empat variabel berubah sekaligus: pilar, format, jenis bukti, dan hipotesis.
Kalau video 2 menang, tidak ada cara tahu apakah karena formatnya, topiknya, atau kebetulan.

Referensi menawarkan desain yang lebih baik: buat banyak, lihat 10% teratas, cari kesamaan,
tambahkan dua butir ke ceklis berikutnya. Itu butuh jumlah. Dengan empat video, satu-satunya
perbandingan yang bersih adalah memegang format tetap dan memvariasikan satu hal.

---

## Temuan teknis: klaim dan rujukan yang tidak konsisten

Bagian ini kecil-kecil, tetapi semuanya akan mengganggu pada video pertama.

**Rujukan mati.** `AGENTS.md` mencantumkan `ref-AGENTS.md` di struktur proyek. File itu tidak
ada. *Terverifikasi.*

**Kontradiksi soal A/B test.** `AGENTS.md` menulis "Uji thumbnail A/B minimal 1–2 minggu".
`02-pengemasan.md` menulis "Jangan A/B test thumbnail dulu. Belum ada volume traffic yang
cukup." Keduanya benar di konteksnya, tetapi saling bertentangan tanpa penjelasan.
*Terverifikasi.*

**Klaim yang melanggar prinsip bukti sistem sendiri.** `AGENTS.md` bagian "Jebakan yang
Menggigit Diam-diam" menyatakan "Nama file video dibaca algoritma" sebagai fakta. YouTube
tidak memakai nama file untuk penemuan. *Simpulan*, berdasarkan pengetahuan saya, bukan hasil
uji. Yang jadi masalah bukan benar-salahnya, tetapi sistem ini menetapkan aturan bukti untuk
naskah lalu melanggarnya di dokumennya sendiri.

Klaim serupa yang tidak punya sumber: "70%+ penonton YouTube di Indonesia pakai ponsel",
"auto-caption akurasi 70–85%", "Shorts yang diunggah sekaligus banyak bisa mengurangi
jangkauan". Yang terakhir bahkan bertentangan dengan referensi yang dikutip sistem ini.
Hormozi: "Don't worry about it... one of the biggest Instagram accounts posts 100 times a day."

**Mitos SEO lain.** "Tags: 5–8 tag" adalah saran dari era ketika tag masih berpengaruh. Dampak
tag sekarang minimal. *Simpulan.*

**Jadwal yang tidak masuk akal.** Tabel jadwal menempatkan Tahap 1, 2, dan 3 dalam satu pagi
Sabtu. Tahap 3 menuntut pencarian sumber primer dan verifikasi angka. Itu bukan pekerjaan
satu pagi. Yang akan terjadi: verifikasi dilewati, atau jadwalnya geser setiap minggu.
*Simpulan.*

**Batch recording prematur.** `05-rekaman.md` menyarankan merekam 2–4 naskah per sesi.
Pada pilot, ini berarti menulis 2–4 naskah sebelum ada satu pun respons audiens. Itu
mempercepat langkah 4 sebelum langkah 2 (hapus) dan tanpa sinyal apa pun. Batch masuk akal
setelah format terbukti, bukan sebelumnya.

**Link absolut.** `04-penulisan-naskah.md` dan `05-rekaman.md` memakai
`file:///Users/ahmadfadhilramadhan/...`. Link ini rusak kalau folder dipindah atau dibuka di
mesin lain. *Terverifikasi.*

**Placeholder tertinggal.** `04-penulisan-naskah.md` diakhiri dengan
`*Terakhir diperbarui: _(perbarui setiap ada perubahan prosedur)_*`. `01-ideasi.md` punya
changelog, file lain tidak. *Terverifikasi.*

**Content bank dipadatkan untuk mencapai angka 40.** Beberapa ide tumpang tindih:
nomor 1, 2, dan 5 sama-sama soal omzet versus margin. Nomor 12 (ARPU) mengulang nomor 2.
Nomor 14 mengulang nomor 13. Nomor 20 dan 25 mengulang tema retention. *Terverifikasi.*

Yang lebih serius: content bank tidak punya kolom **"bukti yang tersedia"**. Itu satu-satunya
kolom yang menentukan apakah sebuah ide bisa diproduksi atau tidak. Sistem memilih ide
berdasarkan topik, lalu mencari bukti belakangan. Urutannya terbalik.

**Dua set kreator rujukan yang tidak nyambung.** Personal Brand Plan menganalisis delapan
kreator bisnis Indonesia (Raymond Chin, Fellexandro Ruby, Denny Santoso, dan seterusnya).
`AGENTS.md` menganalisis lima kreator gaya pendek Barat (Hormozi, Ferry Irwandi, Big A Story,
Moon). Workflow meminjam taktik produksi dari set kedua tanpa memeriksa apakah taktik itu
cocok dengan positioning yang lahir dari set pertama. Gaya potong setiap 2 detik adalah
estetika *direct response*. Channel "Decision Notes" untuk operator lebih dekat ke estetika
studi kasus. Menyalin taktiknya bisa melemahkan positioningnya.

---

## Yang sudah benar dan jangan diubah

Ini bukan pujian basa-basi. Semuanya punya alasan.

**Positioning dan definisi audiens.** "Pemilik bisnis yang sudah berjalan, punya tim kecil,
ingin naik tanpa merusak margin" adalah segmentasi yang tegas. Bukan "semua orang yang mau
bisnis". Ini aset paling berharga di seluruh repo.

**Sistem label bukti.** Tiga label (terverifikasi, simpulan, tebakan) plus tiga jenis sumber
(pengalaman, data publik, ilustrasi) lebih disiplin daripada kebanyakan ruang redaksi
profesional. Pertahankan.

**Prinsip editorial nomor 7.** "Jujur soal batas pengalaman" adalah pembeda yang nyata di
ruang konten bisnis Indonesia, yang penuh klaim tanpa batas.

**Batas penggunaan AI.** Daftar "jangan serahkan ke AI tanpa pemeriksaan manusia" jelas dan
benar. Jangan dilunakkan.

**Menolak target arbitrer sebelum baseline.** Langka dan tepat.

**Larangan konten orisinal terpisah untuk Instagram selama pilot.** Disiplin lingkup yang
benar.

**Prioritas audio di atas kamera.** Benar dan murah.

---

## Satu rekomendasi

**Pakai `AGENTS.md` sebagai kontrak, dan 4.473 baris sisanya sebagai perpustakaan rujukan yang
dibuka saat ada masalah spesifik — bukan sebagai urutan gerbang yang harus dilewati.**

Konkretnya: ganti pipeline 10 tahap menjadi empat tahap untuk 30 hari ke depan.

| Tahap baru | Isi | Batas waktu |
|---|---|---|
| **1. Putuskan** | Satu masalah, satu POV, satu judul, satu kalimat bukti | 60 menit |
| **2. Tulis** | Naskah dengan hook, 3 poin, trade-off, satu langkah aksi | 3 jam |
| **3. Rekam dan potong** | Rekam, potong jeda, teks di layar, ekspor | 4 jam |
| **4. Terbitkan dan baca** | Metadata, unggah, baca semua komentar | 90 menit |

Total sekitar 9 jam per video, bukan 18. Dua kali lebih cepat, dan cukup untuk empat video
dalam empat minggu tanpa mengorbankan pekerjaan utama.

Lalu tambahkan dua aset yang belum ada:

1. **`content/decision-log.md`** — satu baris per keputusan bisnis nyata: tanggal, keputusan,
   angka yang terlibat, hasil sementara. Diisi 5 menit setiap Jumat. Ini memasok ide dari
   ember *Real Time* dan *Recent Past*, dan sekaligus menjadi inventaris bukti.
2. **`content/proof-inventory.md`** — daftar fakta konkret yang boleh dibuka, sudah
   disamarkan, dengan status izin. Diisi sekali di awal, diperbarui setiap bulan.

**Biayanya.** Video pertama akan terlihat lebih kasar daripada yang dibayangkan sistem lama.
Sebagian syarat kualitas yang sekarang tertulis akan hilang, dan sebagian mungkin perlu
dikembalikan setelah ada baseline. Ada juga risiko membangun format yang salah selama empat
minggu. Itu risiko nyata, bukan risiko kecil.

**Yang membuat saya berubah pikiran.** Kalau tujuan channel ini bukan audiens, melainkan aset
kredibilitas untuk menjual jasa ke sedikit klien bernilai tinggi, maka rekomendasi ini salah.
Untuk tujuan itu, empat video yang sangat dipoles dalam empat bulan lebih masuk akal daripada
empat video kasar dalam empat minggu. Jawaban atas pertanyaan tujuan di bagian 1 akan
menentukan mana yang benar.

---

## Catatan untuk disimpan

- Tujuan channel belum dinyatakan di mana pun. Ini harus dijawab sebelum mengubah workflow.
- `ref-AGENTS.md` tidak ada, tetapi tercantum di struktur proyek.
- Kontradiksi A/B test: `AGENTS.md` minta uji 1–2 minggu, `02-pengemasan.md` melarang uji
  saat pilot.
- Content bank tidak punya kolom "bukti tersedia" — kolom yang paling menentukan.
- Belum ada mekanisme pencatatan ide harian. Ini penyebab kehabisan ide yang paling sering.
- Belum ada inventaris bukti. Ini penyebab konten terasa generik yang paling sering.
- Perkiraan waktu produksi per video dengan sistem sekarang: 18 jam. *Tebakan*, berdasarkan
  penjumlahan estimasi tiap tahap, belum diukur.
