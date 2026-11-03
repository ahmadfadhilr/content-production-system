# Pipeline Produksi — Peta dan Aturan Main

Satu halaman. Buka ini dulu, baru buka file tahap yang sedang dikerjakan. Detail tiap tahap tidak
diulang di sini; yang ada di sini hanya urutan, penanggung jawab, keluaran, aturan yang berlaku di
semua tahap, dan keputusan desain yang tidak dibuka ulang.

**Keluaran pipeline ini:** satu video per minggu — satu masalah, satu keputusan yang bisa diringkas
satu kalimat, satu bukti yang terlihat di layar.

**Yang sebenarnya dibangun:** bukan tumpukan video, melainkan satu channel dengan satu penonton
inti. Setiap unggahan harus memperbaiki keputusan unggahan berikutnya.

---

## Rantai Keputusan

Sepuluh tahap itu alat. Yang menentukan hasil hanya lima keputusan.

| # | Keputusan | Tahap | Pertanyaan yang dijawab |
|---|---|---|---|
| 1 | **Pilih** masalah yang sudah dicari dan belum dijawab | 1 | Adakah bukti berulang, bukan satu outlier? |
| 2 | **Kemas** menjadi janji yang khas dan bisa diuji | 2 | Apakah thumbnail ini menang di feed yang nyata? |
| 3 | **Penuhi** janji itu melebihi yang dijanjikan | 3–7 | Apakah penonton mendapat persis apa yang ia klik? |
| 4 | **Beri** langkah berikutnya yang berguna | 8 | Apakah ini pemberian, bukan permintaan? |
| 5 | **Ulangi** dengan bukti, bukan dengan perasaan | 10 → 1 | Apa yang dipertahankan, apa yang diubah? |

Kalau satu keputusan terlewat, kegagalannya senyap: video terbit, angka datang, dan tidak ada yang
tahu bagian mana yang salah. Dasar rantai ini dan batas penerapannya di pasar Indonesia:
`content/analisis/2026-11-03-jake-trinder/`.

---

## Sepuluh Tahap

| # | Tahap | Dikerjakan | Keluaran yang harus ada sebelum lanjut | Berkas |
|---|---|---|---|---|
| 1 | Ideasi | AI + Fadhil | Satu kandidat utama + maksimal dua cadangan (masalah, keputusan, jenis bukti, judul kerja, teks thumbnail), tiga temuan kemasan pembanding, **bukti negatif minimal dua video lokal yang gagal**, dan pembaruan peta permintaan maksimal tiga channel. Batch discovery tetap boleh sampai 20 kandidat. | [`01-ideasi.md`](./01-ideasi.md) |
| 2 | Pengemasan | AI + Fadhil | 5 judul → 2 dipilih (mulai dari judul kerja Tahap 1), 1–2 sketsa thumbnail, satu kalimat pembeda, thumbnail terpilih **diuji berdampingan lima thumbnail hasil kueri utama** | [`02-pengemasan.md`](./02-pengemasan.md) |
| 3 | Riset dan fakta | AI | Lembar fakta berlabel + artefak yang bisa ditampilkan | [`03-riset-dan-fakta.md`](./03-riset-dan-fakta.md) |
| 4 | Naskah | AI + Fadhil | Naskah siap direkam, bagian **Janji menyebut bentuk hasil dan isi video**, penanda visual lengkap, lalu **04.1** (penyisipan pengalaman) sebelum rekaman | [`04-penulisan-naskah.md`](./04-penulisan-naskah.md) |
| 5 | Rekaman | Fadhil | File mentah + room tone, sudah di-backup | [`05-rekaman.md`](./05-rekaman.md) |
| 6 | Riset visual | AI + Fadhil | Artefak terekam, peta visual, lisensi dicek | [`06-riset-visual.md`](./06-riset-visual.md) |
| 7 | Penyuntingan | Fadhil | Video final lulus ceklis teknis dan rubrik | [`07-penyuntingan.md`](./07-penyuntingan.md) |
| 8 | Penerbitan | Fadhil | Video live + metadata + ceklis menit pertama + **langkah berikutnya berupa artefak di layar, bukan produk** | [`08-penerbitan.md`](./08-penerbitan.md) |
| 9 | Distribusi ulang | Fadhil + AI | 3–6 klip terjadwal | [`09-distribusi-ulang.md`](./09-distribusi-ulang.md) |
| 10 | Evaluasi | AI + Fadhil | Post-mortem 7 hari, tiga proksi kepenuhan janji, pelajaran masuk ke berkas | [`10-evaluasi.md`](./10-evaluasi.md) |

Tahap 1–3 dan 10 boleh dikerjakan AI. Tahap 5 dan 7 hanya Fadhil. Tahap 4 di tengah: AI menyiapkan
draf, struktur, dan penanda visual, tetapi POV dan **04.1** hanya Fadhil. Untuk 04.1, AI menyiapkan
titik sisip dan memeriksa hasilnya, bukan mengarang isinya. Kalimat POV tidak boleh ditulis AI lalu
disetujui apa adanya.

---

## Sembilan Aturan yang Berlaku di Semua Tahap

1. **Bukti yang terlihat wajib.** Setiap video memuat minimal satu artefak yang terlihat di layar,
   bukan hanya disebut. Sumbernya bisa catatan sendiri, pengukuran untuk video ini, atau dokumen
   publik primer. Aturannya di `03-riset-dan-fakta.md` Langkah 3.
2. **Satu konten, satu masalah.** Kalau satu ide menyentuh dua pilar, pecah jadi dua video.
3. **Gerbang tidak boleh dilewati.** Kalau keluaran tahap sebelumnya belum ada, jangan lanjut.
   Menunda sehari lebih murah daripada menerbitkan tanpa bukti.
4. **Setiap klaim diberi label:** *terverifikasi*, *simpulan*, atau *tebakan* — plus jenis sumber
   (pengalaman sendiri, data publik, ilustrasi). Aturan ini berlaku juga untuk dokumen internal.
5. **Kemasan sebelum naskah.** Judul kerja dan teks thumbnail sudah ada sejak Tahap 1; Tahap 2
   menguji, membandingkan, dan memilih. Yang tidak boleh: menulis judul setelah naskah atau setelah
   video jadi.
6. **Satu inti, tiga lapisan akses.** Setiap video memakai pintu masuk yang dipahami orang yang
   belum punya bisnis, keputusan yang berguna bagi founder dengan bisnis berjalan, serta ukuran
   atau batas yang memberi kedalaman bagi operator yang lebih matang.
7. **Satu penonton inti.** Semua video channel ini harus bisa ditonton oleh penonton yang sama.
   Yang berubah antar video adalah kemasan dan format — bukan audiens sasarannya. Hit di luar topik
   berisiko mendatangkan penonton yang melewati video berikutnya. Diukur pada 3 November 2026, tiga
   channel Indonesia menunjukkan pola ini, termasuk channel yang video bisnisnya kalah jauh dari
   video motivasinya. Ini pola peringatan, bukan bukti sebab-akibat.
   Bukti: `content/analisis/2026-11-03-jake-trinder/` Temuan E.
8. **Bukti negatif wajib.** Setiap kandidat membawa minimal dua video lokal dengan topik atau format
   serupa yang tampil **di bawah median**, beserta dugaan sebabnya. Riset yang hanya membaca
   pemenang bisa membuktikan ide buruk apa pun. Satu format judul yang sama di Indonesia terbentang
   dari 238.893 sampai 308 tayangan. Bukti: Temuan B dan C di berkas analisis yang sama.
9. **Riset pra-terbit adalah hipotesis, bukan putusan.** Pindai membuktikan bahwa permintaan ada
   untuk bentuk janji yang **diuji**; ia tidak pernah membuktikan tayangan kita. Gerbang menentukan
   prioritas dan urutan, bukan hasil. Karena itu satu kandidat per empat video boleh dikerjakan
   sebagai **taruhan**: gagal gerbang permintaan, tetapi bukti negatifnya sudah diperiksa, pembedanya
   jelas, alasannya ditulis, dan hasilnya dibandingkan. Bukti: Temuan N.

---

## Yang Tidak Diserahkan ke AI Tanpa Pemeriksaan

POV dan sudut pandang · cerita dan pengalaman pribadi · penilaian trade-off bisnis · validasi angka
akhir · keputusan data apa yang aman dibuka · penilaian kualitas akhir sebelum terbit · keputusan
memilih taruhan di aturan 9.

Daftar lengkap: `AGENTS.md`, bagian "Batas Penggunaan AI".

---

## Keputusan Desain yang Sudah Diambil

Bagian ini ada supaya tidak ada yang membuka ulang perdebatan yang sama.

| Keputusan | Alasan |
|---|---|
| **Sepuluh tahap dipertahankan**, bukan dipangkas jadi lima keputusan | Lima keputusan menjelaskan **mengapa** tahapnya ada; sepuluh tahap menjaga **setiap jenis kegagalan punya gerbangnya sendiri**. Yang paling menentukan adalah Tahap 3: tanpa gerbang bukti, video ini jadi opini tambahan di antara opini yang sudah banyak. |
| **Permintaan tetap diukur** dengan pindai YouTube, tetapi metodenya diperbaiki | Pindai mencegah produksi topik mati. Sejak 3 November 2026, median kueri mentah tidak dipakai apa adanya: video terjemahan, video yang bukan masalah yang sama, dan channel dengan audiens berbeda dibuang lebih dulu, lalu tayangan kandidat dibandingkan dengan **median channel pengucapnya**. Median mentah satu kueri mencapai 787.353 sementara channel pengucapnya ber-median 16.500. Bukti: Temuan D. |
| **Median kueri bukan lagi gerbang tunggal; bukti berulang yang menentukan** | Satu video outlier hanyalah petunjuk. Topik yang lolos karena satu video 45× median channelnya gagal saat diverifikasi dengan kueri baru (median 38.121, satu video di atas 100 ribu). Yang dicari: topik yang berulang di beberapa channel. Bukti: Temuan A dan B. |
| **Bukti negatif menjadi syarat, bukan pelengkap** | Tanpa itu, riset hanya bisa mengonfirmasi apa yang sudah dipilih. Format judul "cara menghitung HPP" yang sama menghasilkan 238.893 dan 308 tayangan. Bukti: Temuan C. |
| **Gerbang permintaan dibaca sebagai prioritas, bukan larangan** | Pasar memberi putusan akhir. Satu slot taruhan per empat video menjaga disiplin tetap ada sambil mengizinkan pasar menguji dugaan yang belum terbaca di data. Taruhan tidak boleh mengubah aturan 7 (satu penonton inti). Bukti: Temuan N. |
| **Satu penonton inti per channel** | Channel adalah satu kampanye; video adalah kampanye per video. Hit di luar topik berisiko menarik penonton yang tidak kembali. Bukti: Temuan E. |
| **Bukti tipe A tidak diwajibkan** | Video boleh memakai catatan sendiri, pengukuran untuk video ini, atau dokumen publik primer. |
| **Pembeda diuji di Tahap 2, bukan di Tahap 3** | Sampai 3 November 2026, Tahap 3 menagih "bukti yang tidak bisa ditiru dari riset". Syarat itu mencampur kebenaran klaim dengan pembeda, dan tidak bisa dipenuhi selama `content/log-keputusan.md` kosong. Sekarang kebenaran klaim diuji di Tahap 3 lewat sumber primer, dan pembeda diuji di Tahap 2 lewat satu kalimat. |
| **"Bukti" di pembuka berarti artefak, bukan kredensial** | Di pasar Indonesia, video bisnis berperforma tinggi langsung mengajar dan tidak menyisipkan beat otoritas. Fadhil juga tidak punya kredensial publik, dan pipeline melarang perkenalan diri. Yang menjawab "kenapa dengar orang ini" adalah artefak miliknya sendiri. Bukti: Temuan F. |
| **Langkah berikutnya adalah artefak di layar, bukan produk** | Ajakan yang paling berguna di pasar Indonesia menempel pada isi video itu sendiri. Selama pilot belum menjual apa pun, yang bisa diberikan adalah alat yang sudah terlihat di video. Jalur monetisasi menunggu keputusan tujuan channel. Bukti: Temuan H. |
| **Ujian thumbnail berdampingan** | Uji 120 px menguji thumbnail sendiri. Uji baru menempelkannya di samping lima thumbnail hasil kueri utama, karena itu yang benar-benar bersaing di feed. Biaya nol. Bukti: Temuan M. |
| **Tiga klip tidak lagi menjadi syarat terbit** | Menahan terbit karena tugas platform sekunder adalah pertukaran yang buruk. Klip dipotong pada minggu yang sama, sesudah video terbit. |
| **Rekaman batch setelah pilot**, bukan sekarang | Merekam 2–4 naskah sebelum ada respons audiens berarti mempertaruhkan semuanya pada format yang belum terbukti. |
| **Tidak ada A/B test thumbnail di pilot** | CTR tidak bisa dibaca tanpa volume impresi. |
| **Tidak ada funnel leads di pilot** | Funnel menuntut tujuan channel yang belum diputuskan. Yang dipakai sementara hanya logika diagnosanya: setiap unggahan memperbaiki keputusan berikutnya. |
| **Produksi murah, bahan mahal** | Yang mahal harus riset dan bukti. Efek visual ditambahkan setelah ada baseline, bukan sebelum. Editing tidak bisa menyelamatkan ide lemah. |
| **Kepenuhan janji dibaca lewat proksi**, bukan lewat angka baru | CTR dan AVD hari pertama adalah derau, dan satisfaction tidak punya angka publik. Tiga proksi di Tahap 10: komentar menyebut mendapat apa yang dijanjikan judul, penonton kembali di video berikutnya, dan titik pergi tepat sebelum atau sesudah bukti pertama. Bukti: Temuan G. |
| **Naskah penuh tetap wajib untuk talking head**; segmen artefak cukup poin | Format ini adalah analisis talking head, bukan screen recording. Kedalaman naskah mengikuti jenis segmennya. Bukti: Temuan K. |
| **Tidak ada target view atau subscriber** | Belum ada baseline. Bandingkan empat video pilot satu sama lain. |
| **Judul kerja dibuat di Tahap 1**, bukan diserahkan seluruhnya ke Tahap 2 | Ide yang tidak bisa diberi judul dan teks thumbnail bukan ide. Menemukannya setelah riset berjalan membuang satu blok kerja. Tahap 2 tetap memegang lima opsi, sketsa, dan uji ponsel. |
| **Pengalaman pribadi disisipkan di 04.1**, setelah naskah utuh | Kalau disisipkan saat menulis draf, AI akan mengarang pengalaman untuk menutup lubang. Titik sisip ditandai lebih dulu, bahan disiapkan Fadhil, penyisipan terakhir. Langkahnya di [`04-penulisan-naskah.md`](./04-penulisan-naskah.md) Langkah 17. |

---

## Ritme Mingguan

Satu video per minggu. Kalau mengganggu pekerjaan utama, turunkan ke satu video per dua minggu dan
perpanjang pilot.

| Waktu | Blok | Tahap |
|---|---|---|
| Sabtu pagi, sebelum blok produksi | Analisis pipeline minggu lalu (30–45 menit) | lihat [`../analisis/00-pipeline.md`](../analisis/00-pipeline.md) |
| Sabtu pagi | Ideasi + perbarui peta permintaan (maksimal 90 menit, termasuk 15 menit ekspansi maksimal tiga channel) | 1 |
| Sabtu siang | Pengemasan (maksimal 30 menit) | 2 |
| Sabtu sore | Riset (berhenti di 90 menit) | 3 |
| Sabtu malam | Naskah | 4 |
| Minggu pagi | Rekaman | 5 |
| Minggu sore | Riset visual | 6 |
| Senin–Selasa | Editing | 7 |
| Rabu | Penerbitan | 8 |
| Rabu–Jumat | Potong dan jadwalkan tiga klip | 9 |
| Rabu + 7 hari | Evaluasi | 10 |

Riset tidak muat satu pagi bersama ideasi dan pengemasan. Kalau dipaksa, verifikasi akan dilewati
atau jadwalnya geser setiap minggu. Kalau riset lewat 90 menit, ganti klaimnya — jangan tambah
waktunya. Aturan yang sama berlaku untuk peta permintaan: kalau ekspansi channel lewat 15 menit,
**kurangi jumlah channel, jangan tambah waktu**. Peta dibangun lintas minggu, bukan sekali jadi.

---

## Kalau Macet, Buka Berkas Ini

| Gejala | Berkas |
|---|---|
| Tidak ada ide yang layak | `01-ideasi.md`, lalu `content/log-keputusan.md` |
| Ide ada, tetapi tidak ada judul yang layak | `01-ideasi.md` Langkah 5 — sudutnya belum tajam |
| Satu video meledak, video berikutnya jatuh | Aturan 7 — penontonnya berbeda. Cek peta permintaan, `01-ideasi.md` |
| Topik lulus gerbang tetapi tidak ada format lokal yang terbukti | Aturan 8 — bukti negatif belum diperiksa, `01-ideasi.md` |
| Judul terasa lemah, thumbnail tidak jelas | `02-pengemasan.md` |
| Riset melebar, klaim inti belum terbukti | `03-riset-dan-fakta.md` (batas 90 menit) |
| Naskah terasa seperti esai | `04-penulisan-naskah.md` |
| Audio buruk, rekaman tidak bersih | `05-rekaman.md` |
| Video ramai tetapi tidak membuktikan apa pun | `06-riset-visual.md` |
| Video terasa lambat, banyak diam kosong | `07-penyuntingan.md` |
| Video tidak ditemukan | `08-penerbitan.md` |
| Klip tidak pernah jadi | `08-penerbitan.md`, bagian "Klip tidak menahan terbit" |
| Angka turun tetapi tidak tahu kenapa | `10-evaluasi.md`, lalu pipeline analisis |

---

## Status Sekarang

Yang memblokir rekaman pertama: prasyarat 1 (aset brand), 3 (audit izin data), dan 4 (channel
YouTube). Ideasi dan penulisan naskah tidak terhambat. Daftar lengkap ada di `AGENTS.md`. Urutan
empat video pilot tetap diambil dari `content/pindai/`, bukan dari dokumen rencana.
