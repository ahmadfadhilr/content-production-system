# Jake Trinder — Uji Konsep ke Pasar Indonesia, 3 November 2026

Sumber: `https://www.youtube.com/watch?v=Ar2DXQorEm4` — "Pelatihan YouTube Paling Berharga yang
Akan Pernah Anda Tonton", Jake Trinder, 37 menit 6 detik, 8 chapter. Transkrip dibaca penuh lewat
auto-caption; 8.925 kata.

Ini bukan penilaian terhadap orang atau hasil yang ia klaim. Ia menyebut angka sendiri
("$100.000/bulan per channel", "10x views Gary Vee dalam sebulan") dan angka itu **tidak
diverifikasi** di sini. Yang diuji hanya **konsep**, dan setiap konsep diuji ke pasar Indonesia
memakai alat yang sudah ada di `tools/`.

---

## Batas data, baca dulu

| Yang dipakai | Jumlah |
|---|---|
| Kueri dipindai | 4, satu putaran, `tools/pindai-youtube.py -d -r1` |
| Channel dibuka lewat `tools/urut-video.py` | 4 — Kelly Patricia, Jamu Otak, Jaya Setiabudi, Malaka |
| Deskripsi video dibaca | 4 |
| Transkrip Indonesia dibaca | 1 (pembuka 3 menit) |
| Chapter video sumber | 8 |
| **CTR, AVD, retensi, konversi** | **Tidak ada.** Hanya di YouTube Studio |

Satu putaran, bukan tiga, karena putaran di sini dipakai untuk **memeriksa keberadaan pola**, bukan
untuk menetapkan median. Semua angka tayangan adalah keluaran YouTube saat pemindaian.
"Median channel" dihitung dari 30 video terakhir dan bercampur usia, jadi ia bukan baseline bersih.

---

## Ringkasan verdict

| # | Konsep dari video | Verdict untuk sistem ini |
|---|---|---|
| A | Peta permintaan lewat penelusuran mendalam seluruh niche | Valid **terbatas** — bukan pembangkit topik |
| B | Satu outlier hanya petunjuk, butuh bukti berulang | **Valid** — masukkan sebagai aturan |
| C | Jangan hanya riset pemenang (bias positif) | **Valid** — masukkan sebagai gerbang |
| D | Median kueri mentah menyesatkan audiens | **Valid** — perbaiki cara mengukur |
| E | Kanal adalah satu kampanye, hit di luar topik merusak | **Valid** — masukkan sebagai aturan |
| F | Janji → bukti → rencana | Sebagian — "bukti = otoritas" tidak transfer |
| G | Kepenuhan janji > CTR dan retensi | Prinsip valid, belum terukur — pakai proksi |
| H | Ajakan yang memberi, langkah berikutnya paling berguna | Valid **dengan syarat** — pakai artefak, bukan produk |
| I | Analisis bottleneck funnel (views → leads → customers) | **Tahan** — belum ada jalur konversi |
| J | Spesifisitas memakan jangkauan | Sudah ada di sistem |
| K | Naskah penuh bisa memperburuk ahli | Tidak relevan sekarang |
| L | Produksi murah, bahan mahal | Sudah ada di sistem |
| M | Uji thumbnail berdampingan dengan kompetitor di feed | **Valid** dan murah — tambahkan |
| N | Riset pra-terbit tetap hipotesis, pasar yang memutuskan | **Valid** — ubah cara gerbang dibaca |

Dua konsep **sudah ada** di pipeline (J, L). Satu **ditahan** (I). Sisanya mengubah pipeline.

---

## A. Peta permintaan lewat penelusuran mendalam — valid terbatas

**Klaim video.** Mulai dari daftar kueri benih, ambil outlier, buka channel outlier, ambil outlier
channel itu, lanjut ke rekomendasi, ulangi "sampai seluruh niche selesai". Tujuannya "visibilitas
atas seluruh niche, bukan satu pesaing". Ini yang dipakai untuk menemukan topik, bukan sekadar
menghitung permintaan satu kueri.

**Uji.** Dua kueri benih (`"cara mengatur keuangan bisnis kecil"`, `"kenapa bisnis tidak
berkembang"`) menghasilkan empat channel relevan. Keempatnya dibuka dan daftar videonya diurutkan:
`@kelspatricia` (median 16.500), `@jamuotak` (14.500), `@JayaSetiabudi` (6.350), `@MalakaProjectid`
(93.500).

**Hasil.** Ekspansi channel menghasilkan **satu** kandidat topik baru yang tidak ada di daftar
kueri benih: "ketergantungan UMKM pada marketplace", berasal dari `@JayaSetiabudi` (286.000
tayangan, 45,0× median channelnya).

Kandidat itu lalu diverifikasi dengan kueri baru, sesuai aturan yang berlaku:

```
jualan di marketplace tidak untung     median 38.121, 1 video >100 rb
ketergantungan marketplace             (digabung ke putaran yang sama)
```

Hasilnya **gagal**: pasokan lokal untuk kueri itu bukan pemilik bisnis yang khawatir pada
ketergantungan platform, melainkan tutorial Facebook Marketplace. Hasil tertinggi adalah
"Rahasia Jualan Sukses di Marketplace Facebook" (165.896), dan sisanya 292–90.186.

**Verdict.** Konsepnya benar sebagai prinsip, tetapi **di niche ini ekspansi channel sering
memimpin keluar dari niche.** Channel yang mendominasi kueri bisnis Indonesia adalah channel
keuangan pribadi, motivasi, atau berita — bukan channel keputusan bisnis. Kelly Patricia adalah
channel keuangan pribadi yang video bisnisnya justru di bawah mediannya sendiri
("5 Strategi Naikin Omzet Usaha Kecil" = 3.900, 0,2×; "Cara HITUNG GAJI Karyawan" = 18.000, 1,1×).
Raymond Chin, yang paling dekat dengan positioning ini, sekarang outlier-nya justru di berita dan
AI ("Selamat, Purbaya Dipecat" 3,3 juta), bukan bedah bisnis.

**Yang diambil:** penelusuran channel dipakai untuk dua hal saja — mencari **bukti berulang** (topik
yang sama berulang di beberapa channel), dan mendeteksi **pergeseran tema**. Dibatas tiga channel
per minggu, tidak lebih. Topik yang ditemukan lewat ekspansi tetap wajib lulus verifikasi kueri.

---

## B & C. Bukti berulang dan bukti negatif — valid

**Klaim video.** "One viral video might be a clue... you need repeated evidence before you build
around it." Dan: "If you only research winners, you can prove any bad idea."

**Uji.** Kueri `"cara menghitung hpp"` (satu format judul yang sangat seragam di Indonesia).
19 hasil, median 164.240, 9 video di atas 100 ribu.

| Judul (format sama) | Tayangan |
|---|---:|
| Cara Menghitung HPP (HARGA POKOK PENJUALAN) MAKANAN | 238.893 |
| Gampang Banget! Hitung HPP Makanan dengan Cara Ini | 214.848 |
| Menghitung HPP — Harga Pokok Penjualan | 189.247 |
| CARA MENGHITUNG HPP DAN HARGA JUAL | 52.176 |
| CARA HITUNG HPP BISNIS BAKERY | 23.035 |
| CARA MENGHITUNG HARGA POKOK PRODUKSI (METODE FULL COSTING) | 11.560 |
| CARA PALING MUDAH HITUNG HPP UNTUK UMKM | 4.447 |
| Cara Menghitung HPP bagi Usaha Kecil | 1.239 |
| Cara Menghitung HPP di Excel | 308 |

**Verdict.** Satu format, **selisih 776 kali** antara teratas dan terbawah. Permintaan topik
terbukti (bukti berulang ada di banyak channel), tetapi hasil per video ditentukan hal lain:
kemasan, eksekusi, dan siapa yang mengucapkannya. Bukti negatifnya juga terbaca: 10 dari 19 video
format yang sama berada di bawah 100 ribu, dan beberapa jauh di bawah median.

Artinya, mengukur permintaan dengan "median 10 teratas" saja **membuang tepat separuh informasi
yang menentukan** — yaitu kapan format yang sama gagal.

**Yang diambil:** setiap kandidat wajib menyertakan bukti negatif minimal dua video lokal dengan
topik atau format serupa yang tampil di bawah median, beserta dugaan sebabnya.

---

## D. Median kueri mentah menyesatkan audiens — valid

**Uji.** Kueri `"cara mengatur keuangan bisnis kecil"`.

Median 10 teratas: **787.353**. Angka ini terlihat sangat sehat. Isi sepuluh teratas:

| Judul | Channel | Tayangan |
|---|---|---:|
| Cara Ngatur Duit Tanpa Ribet | Timothy Ronald | 1.467.918 |
| Semakin MUDA lu paham ini, Semakin CEPAT lu KAYA | Pertajam Pola Pikir | 1.195.617 |
| Biar Keuangan Beres.. | Raditya Dika | 1.033.001 |
| Harusnya Mindset KEUANGAN Para Sandwich Generation... | Suara Berkelas | 995.753 |
| Cara Mengelola Keuangan Usaha kecil Anda | Belajar Berbisnis | 939.369 |

Empat dari lima teratas adalah keuangan pribadi, motivasi, atau hiburan — bukan pemilik bisnis
dengan tim. Tayangan tinggi itu milik audiens yang berbeda.

Kontras yang paling tajam: channel yang muncul dengan angka tinggi di kueri ini, `@kelspatricia`,
punya **median channel 16.500** — sekitar 1/48 dari median kueri. Video yang tampil di pencarian
(238.924) adalah outliernya, bukan gambaran channelnya.

**Verdict.** Median kueri mentah mengukur "permintaan atas kata", bukan "permintaan audiens kita
atas masalah ini". Ia harus disaring relevansi dulu, lalu dibandingkan dengan baseline channel yang
benar-benar akan bersaing.

**Yang diambil:** median kueri hanya sah setelah tiga saringan — buang video terjemahan, buang video
yang bukan masalah yang sama, buang channel yang audiensnya berbeda — dan tayangan kandidat
dibandingkan dengan **median channel pengucapnya**, bukan dengan median kueri.

---

## E. Kanal adalah satu kampanye — valid

**Klaim video.** "Your channel is one overall campaign... the videos are individual campaigns."
Hit di luar topik menarik penonton yang mengabaikan video berikutnya, dan itu menekan channel.

**Uji.** `@jamuotak`, 28 video, median 14.500. Video terbesarnya bertema *mindset, logika, dan
komunikasi*, bukan operasi bisnis:

| Judul | Tayangan | × median |
|---|---:|---:|
| Rahasia Komunikasi dan Cara Berbicara Depan Umum | 1.000.000 | 69,0 |
| Mindset Orang Kaya Vs Mindset Orang Miskin | 758.000 | 52,3 |
| 25 Kesalahan Logika Yang Sering Terjadi | 484.000 | 33,4 |
| Apa itu ADHD? | 259.000 | 17,9 |

Video bisnisnya di channel yang sama: "Cara Validasi Ide Bisnis" 11.000 (0,8×), "6 Hukum Bisnis Dan
Kehidupan" 6.500 (0,4×), "Penawaran Bikin Jualan Laris" 64.000 (4,4×). Dan unggahan terbaru
(2–11 bulan) berada di 0,1–0,2× median, sementara puncaknya sekitar satu tahun lalu.

Dua contoh lain: `@kasisolusi` (median 31.500) punya satu video live peristiwa kapal sebagai outlier
13,6×, sisanya wawancara bisnis. `@MalakaProjectid` (median 93.500) punya video jam tangan 34,2× di
tengah konten politik dan gaya hidup.

**Verdict.** Polanya ada dan berulang. Sebab-akibatnya **tidak terbukti** — penurunan bisa
disebabkan hal lain. Tetapi cukup untuk dijadikan aturan pencegahan, karena biaya salahnya besar
dan biaya menghindarinya nol.

Bukti tambahan yang mendukung, dari data yang sudah ada di repo: video high-view untuk topik
"operasi dan kepemimpinan" di Indonesia berasal dari konten motivasi. `@jamuotak` "Kenapa Bisnis
Selalu Gagal dan Tidak Berkembang" (220.930, 15,2×) adalah **ringkasan buku E-Myth** — self-help,
bukan keputusan operasional.

**Yang diambil:** satu aturan baru di `00-pipeline.md` — semua video satu channel harus punya satu
penonton inti yang sama. Yang berubah antar video adalah kemasan dan format, bukan audiensnya.

---

## F. Janji → bukti → rencana — sebagian valid

**Klaim video.** Tiga pertanyaan penonton setelah klik: "apakah saya dapat yang saya klik?",
"kenapa saya dengar orang ini?", "apakah sisanya layak waktu saya?" Jawabannya: promise, proof, plan.
Proof = alasan mempercayai pembicara.

**Uji.** Transkrip pembuka video Indonesia berperforma tinggi, Kelly Patricia, "Cara Mudah Hitung
HPP Usaha Kecil" (238.924 tayangan, jauh di atas median channelnya sendiri 16.500), 3 menit pertama:

> "semua orang udah tahu ya kalau mau jualan pasti butuh modal tapi belum banyak yang tahu kalau
> harga modal produk mereka itu berapa... jangan-jangan kamu hitungnya juga masih kira-kira. stop
> ya, yuk temenin aku sharing cara hitung harga modal untuk usaha kecil. **let's go.** [...] tapi di
> video kali ini aku bakal fokus di HPP aja dan aku bakal share cara hitung HPP untuk bisnis produk,
> untuk bisnis jasa, plus di akhir video aku bakal share rumus shortcut untuk hitung HPP biar kamu
> cukup hitung satu kali aja sebulan dan beres."

Strukturnya: **janji** (situasi + "stop") → **rencana** (apa yang akan dibahas, termasuk
"di akhir video rumus shortcut") → langsung mengajar. **Tidak ada beat otoritas.** Tidak ada
"kenapa saya layak didengar". Ia membuktikan dengan mengajar, bukan dengan mengaku.

Raymond Chin, video 488.103 tayangan, juga langsung ke masalah: "Banyak banget UMKM di Indonesia
yang gagal di 1-2 tahun pertamanya karena banyak faktor."

**Verdict.** Janji dan rencana transfer. **"Bukti = otoritas" tidak.** Fadhil tidak punya kredensial
publik, dan pipeline sudah melarang perkenalan diri. Memaksakan beat otoritas akan memperlambat
pembuka — kesalahan yang justru dibunuh oleh aturan hook 5 detik.

**Yang diambil:** struktur naskah tetap lima bagian, tetapi bagian **Janji** diperjelas: ia harus
menyebut bentuk hasil dan isi video seperti contoh di atas ("di akhir video, rumus shortcut"),
bukan hanya "video ini membahas margin". Ini yang membuat penonton berkomitmen. Bukti tetap berupa
**artefak yang dimiliki**, bukan kredensial.

---

## G. Kepenuhan janji, bukan CTR — prinsip valid, belum terukur

**Klaim video.** "The goal of every video is viewer satisfaction, not retention... those are noisy
metrics." Dan: "What most editing gurus call retention is just decoration."

**Uji.** CTR, AVD, dan retensi tidak bisa dibaca dari luar YouTube Studio. Jadi klaim ini **tidak
bisa diuji** dengan alat yang ada. Yang bisa diuji adalah konsekuensinya: apakah video Indonesia
berperforma tinggi benar-benar menepati janji judulnya dalam menit pertama.

Kelly Patricia menjanjikan "shortcut hitung HPP di akhir video" dan memang menyusun chapter
"Shortcut Hitung HPP" sebagai bagian tersendiri. Janji dibayar.

**Verdict.** Prinsipnya benar dan tidak bertentangan dengan pipeline — tetapi ia tidak bisa
menggantikan metrik, karena satisfaction tidak punya angka publik. Yang bisa dilakukan: menambah
**proksi** di Tahap 10, dan menegakkan aturan lama "judul tidak boleh menjanjikan lebih dari isi".

---

## H. Ajakan yang memberi — valid dengan syarat

**Klaim video.** "The action should feel like the most useful next step... instead of being a take,
a give." Contoh: video yang menjelaskan strategi, lalu menawarkan library iklan sebagai langkah
berikutnya.

**Uji.** Deskripsi tiga video Indonesia berperforma tinggi:

| Video | Tayangan | Langkah berikutnya di deskripsi |
|---|---:|---|
| Kelly Patricia, Cara Mudah Hitung HPP Usaha Kecil | 238.924 | Kelas "Small Business Finance" — **produk**, tetapi topiknya persis video |
| Jamu Otak, Kenapa Bisnis Selalu Gagal | 220.930 | Tautan beli buku *E-Myth Revisited* — buku yang **dijelaskan di video** |
| Raymond Chin, Kenapa Mayoritas Bisnis UMKM Gagal | 488.103 | Tidak ada tawaran, hanya sosial media |

**Verdict.** Di pasar Indonesia, ajakan yang memberi memang ada dan **menempel pada isi video**,
bukan ditempel. Tetapi semuanya bergantung pada model bisnis: kelas berbayar, afiliasi buku, atau
murni media. Fadhil belum menetapkan tujuan channel dan pipeline melarang menjual di pilot.

**Yang diambil:** selama pilot, "yang paling berguna berikutnya" bukan produk, melainkan **artefak
yang sudah terlihat di layar** — spreadsheet, tabel, atau template dari video itu. Ini tidak
menambah pekerjaan baru (artefak sudah wajib) dan tidak melanggar larangan menjual. Jalur
monetisasi tetap menunggu keputusan tujuan channel di `AGENTS.md`.

---

## I. Analisis bottleneck funnel — ditahan

**Klaim video.** Funnel: views → leads → qualified calls → customers → revenue. Diagnosa di mana
drop-off, lalu perbaiki.

**Uji.** Konsep ini menuntut ada jalur konversi. Di sistem ini belum ada: tujuan channel belum
diputuskan, dan pipeline melarang CTA produk selama pilot (`AGENTS.md`, "Tujuan channel").

**Verdict.** Tidak bisa diterapkan sekarang, dan memaksakannya berarti membangun funnel untuk
sasaran yang belum dipilih. Yang diambil bukan funnel, melainkan **logika diagnosanya**: setiap
unggahan harus memperbaiki keputusan berikutnya, dan drop-off dibaca per penyebab, bukan per angka
mentah. Ini masuk Tahap 10 sebagai cara membaca, bukan sebagai metrik baru.

Konsep ini juga **memperkuat** pertanyaan terbuka di `AGENTS.md`: selama tujuan belum diputuskan,
pipeline hanya bisa mengukur penemuan dan kedalaman, bukan nilai komersial.

---

## J, K, L. Tiga konsep yang tidak mengubah apa pun

| Konsep | Verdict | Alasan |
|---|---|---|
| Spesifisitas memakan jangkauan; selebar mungkin tanpa kehilangan resonansi | Sudah ada | Bentuk A vs B dan "satu inti, tiga lapisan akses" sudah menerapkannya. Data `2026-11-03-pola-hormozi`: kueri mekanisme 4.914, kueri hasil 150.000–488.000 |
| Naskah penuh bisa memperburuk ahli | Tidak relevan | Format sistem ini adalah talking head analisis; naskah penuh tetap wajib. Hanya segmen artefak/screen recording yang cukup poin |
| Editing tidak bisa menyelamatkan ide lemah | Sudah ada | Keputusan desain "produksi murah, bahan mahal" sudah tertulis di `00-pipeline.md` |

---

## M. Uji thumbnail berdampingan — valid dan murah

**Klaim video.** "Simulate what your thumbnail will look like against other videos that are being
posted on YouTube right now... so you can judge the packaging beside the videos it will actually
compete against."

**Uji.** Pipeline sekarang punya uji 120 px, tetapi menguji thumbnail **sendiri**. Ia tidak pernah
menguji thumbnail berdampingan dengan thumbnail yang muncul untuk kueri yang sama. Kueri yang sudah
dipindai di Tahap 1 selalu menghasilkan lima thumbnail nyata yang bisa diunduh
(`https://i.ytimg.com/vi/<ID>/maxresdefault.jpg`).

**Verdict.** Valid, biayanya nol, dan ia menutup lubang yang sudah ada: aturan "jangan tiru gaya
yang paling sering muncul" di `01-ideasi.md` menyuruh membaca kompetitor, tetapi tidak pernah
menyuruh **meletakkan thumbnail sendiri di sebelah mereka**.

**Yang diambil:** gerbang Tahap 2 menambah satu uji wajib — thumbnail terpilih ditempelkan di
samping lima thumbnail hasil kueri utama, dibaca di lebar ponsel.

---

## N. Riset pra-terbit tetap hipotesis — valid

**Klaim video.** "Pre-published research is still a hypothesis. The market gets the final vote."

**Uji.** Kandidat "marketplace dependency" berasal dari satu outlier 45,0× (`@JayaSetiabudi`).
Kueri verifikasinya menghasilkan median 38.121 dan satu video di atas 100 ribu. Kalau satu outlier
saja dipercaya, topik itu akan dianggap terbukti — padahal bukti berulangnya tidak ada.

Sebaliknya: topik "cara menghitung HPP" lulus gerbang dengan median 164.240, tetapi 10 dari 19
video dengan format sama di bawah 100 ribu. Lulus gerbang tetap tidak menjamin tayangan kita.

**Verdict.** Keduanya benar: gerbang permintaan **memilih prioritas**, ia tidak **memutuskan hasil**.
Pipeline sekarang menulis "Skor hanya mengurutkan; gerbang menentukan kandidat utama" — kalimat itu
benar, tetapi belum menyatakan bahwa hasilnya tetap hipotesis yang harus diuji oleh tayangan.

**Yang diambil:** dua hal. Pertama, kalimat di `00-pipeline.md` diperjelas: riset pra-terbit
membuktikan bahwa permintaan **ada untuk bentuk janji yang diuji**; ia tidak pernah membuktikan
tayangan kita. Kedua, satu pintu yang sah untuk taruhan terukur: satu kandidat per empat video yang
gagal gerbang permintaan tetapi punya bukti negatif yang sudah diperiksa dan pembeda yang jelas,
boleh dikerjakan dengan status **taruhan**, alasannya dicatat, hasilnya dibandingkan.

---

## Yang dipakai, dan ke berkas mana

| Temuan | Perubahan | Berkas |
|---|---|---|
| B, C | Setiap kandidat wajib punya bukti negatif (≥2 video lokal di bawah median) | `01-ideasi.md`, gerbang `00-pipeline.md` |
| D | Median kueri disaring relevansi; kandidat dibandingkan dengan median channel pengucapnya | `01-ideasi.md` |
| A | Ekspansi channel dibatasi 3 channel/minggu, hanya untuk bukti berulang dan deteksi pergeseran tema | `01-ideasi.md` |
| E | Aturan baru: satu penonton inti untuk semua video | `00-pipeline.md` (aturan) |
| F | Bagian Janji menyebut bentuk hasil + isi; bukti tetap artefak, bukan kredensial | `04-penulisan-naskah.md`, `00-pipeline.md` (aturan) |
| G | Proksi kepenuhan janji di Tahap 10 | `10-evaluasi.md` |
| H | Langkah berikutnya = artefak di layar, bukan produk | `08-penerbitan.md` |
| M | Uji thumbnail berdampingan lima hasil kueri | `02-pengemasan.md`, gerbang Tahap 2 |
| N | Gerbang dibaca sebagai hipotesis; satu kandidat "taruhan" per empat video | `00-pipeline.md` (aturan) |
| I | Ditahan sampai tujuan channel diputuskan | `AGENTS.md` (pertanyaan terbuka) |

---

## Berkas pendukung

- `pindai-mentah.txt` — keluaran `tools/pindai-youtube.py -d -r1` untuk empat kueri.
- `channel-mentah.txt` — daftar video dan umur unggah empat channel, `tools/urut-video.py`.
- Transkrip video sumber tidak disimpan di repo; diambil ulang dengan
  `yt-dlp --skip-download --write-auto-subs --sub-langs "en-orig"`.
