# Pipeline Produksi — Peta dan Aturan Main

Satu halaman. Buka ini dulu, baru buka file tahap yang sedang dikerjakan. Detail tiap tahap tidak
diulang di sini; yang ada di sini hanya urutan, penanggung jawab, keluaran, dan aturan yang berlaku
di semua tahap.

**Keluaran pipeline ini:** satu video per minggu — satu masalah, satu keputusan yang bisa diringkas
satu kalimat, satu bukti yang terlihat di layar.

---

## Sepuluh Tahap

| # | Tahap | Dikerjakan | Keluaran yang harus ada sebelum lanjut | Berkas |
|---|---|---|---|---|
| 1 | Ideasi | AI + Fadhil | Top N berskor, sudah masuk database | [`01-ideasi.md`](./01-ideasi.md) |
| 2 | Pengemasan | AI + Fadhil | 5 judul → 2 dipilih, 1–2 sketsa thumbnail | [`02-pengemasan.md`](./02-pengemasan.md) |
| 3 | Riset dan fakta | AI | Lembar fakta berlabel + artefak + bukti yang tidak bisa ditiru dari riset | [`03-riset-dan-fakta.md`](./03-riset-dan-fakta.md) |
| 4 | Naskah | AI | Naskah siap direkam, penanda visual lengkap | [`04-penulisan-naskah.md`](./04-penulisan-naskah.md) |
| 5 | Rekaman | Fadhil | File mentah + room tone, sudah di-backup | [`05-rekaman.md`](./05-rekaman.md) |
| 6 | Riset visual | AI + Fadhil | Artefak terekam, peta visual, lisensi dicek | [`06-riset-visual.md`](./06-riset-visual.md) |
| 7 | Penyuntingan | Fadhil | Video final lulus ceklis teknis dan rubrik | [`07-penyuntingan.md`](./07-penyuntingan.md) |
| 8 | Penerbitan | Fadhil | Video live + metadata + 3 klip 9:16 siap | [`08-penerbitan.md`](./08-penerbitan.md) |
| 9 | Distribusi ulang | Fadhil + AI | 3–6 klip terjadwal | [`09-distribusi-ulang.md`](./09-distribusi-ulang.md) |
| 10 | Evaluasi | AI + Fadhil | Post-mortem 7 hari, pelajaran masuk ke berkas | [`10-evaluasi.md`](./10-evaluasi.md) |

Tahap 1–4 dan 10 boleh dikerjakan AI. Tahap 5 dan 7 hanya Fadhil.

---

## Lima Aturan yang Berlaku di Semua Tahap

1. **Bukti yang terlihat wajib.** Setiap video memuat minimal satu artefak yang terlihat di layar,
   bukan hanya disebut. Artefak boleh dari tiga jalur: catatan sendiri, pengukuran untuk video ini,
   atau dokumen publik primer ditambah batas pengalaman yang disebut eksplisit. Aturannya di
   `03-riset-dan-fakta.md` Langkah 5.
2. **Satu konten, satu masalah.** Kalau satu ide menyentuh dua pilar, pecah jadi dua video.
3. **Gerbang tidak boleh dilewati.** Kalau keluaran tahap sebelumnya belum ada, jangan lanjut.
   Menunda sehari lebih murah daripada menerbitkan tanpa bukti.
4. **Setiap klaim diberi label:** *terverifikasi*, *simpulan*, atau *tebakan* — plus jenis sumber
   (pengalaman sendiri, data publik, ilustrasi). Aturan ini berlaku juga untuk dokumen internal.
5. **Kemasan sebelum naskah.** Judul dan thumbnail dirancang di Tahap 2, bukan setelah video jadi.

---

## Yang Tidak Diserahkan ke AI Tanpa Pemeriksaan

POV dan sudut pandang · cerita dan pengalaman pribadi · penilaian trade-off bisnis · validasi angka
akhir · keputusan data apa yang aman dibuka · penilaian kualitas akhir sebelum terbit.

Daftar lengkap: `AGENTS.md`, bagian "Batas Penggunaan AI".

---

## Keputusan Desain yang Sudah Diambil

Bagian ini ada supaya tidak ada yang membuka ulang perdebatan yang sama.

| Keputusan | Alasan |
|---|---|
| **Sepuluh tahap dipertahankan**, bukan dipangkas jadi empat | Tiap gerbang mencegah satu jenis kegagalan. Yang paling menentukan adalah Tahap 3: tanpa gerbang bukti, video ini jadi opini tambahan di antara opini yang sudah banyak. |
| **Permintaan tetap diukur** dengan pindai YouTube | Memang bukan cara kreator rujukan memilih topik, tetapi untuk channel tanpa audiens, pindai mencegah produksi topik mati. Log keputusan tetap sumber bukti termurah. |
| **Bukti tipe A tidak diwajibkan** | Video boleh memakai tiga jalur: catatan sendiri, pengukuran untuk video ini, atau batas pengalaman yang disebut eksplisit. |
| **Rekaman batch setelah pilot**, bukan sekarang | Merekam 2–4 naskah sebelum ada respons audiens berarti mempertaruhkan semuanya pada format yang belum terbukti. |
| **Tidak ada A/B test thumbnail di pilot** | CTR tidak bisa dibaca tanpa volume impresi. |
| **Produksi murah, bahan mahal** | Yang mahal harus riset dan bukti. Efek visual ditambahkan setelah ada baseline, bukan sebelum. |
| **Tidak ada target view atau subscriber** | Belum ada baseline. Bandingkan empat video pilot satu sama lain. |

---

## Ritme Mingguan

Satu video per minggu. Kalau mengganggu pekerjaan utama, turunkan ke satu video per dua minggu dan
perpanjang pilot.

| Waktu | Blok | Tahap |
|---|---|---|
| Sabtu pagi, sebelum blok produksi | Analisis pipeline minggu lalu (30–45 menit) | lihat [`../analisis/00-pipeline.md`](../analisis/00-pipeline.md) |
| Sabtu pagi | Ideasi dan pengemasan (90 menit) | 1–2 |
| Sabtu siang | Riset (berhenti di 90 menit) | 3 |
| Sabtu sore | Naskah | 4 |
| Minggu pagi | Rekaman | 5 |
| Minggu sore | Riset visual | 6 |
| Senin–Selasa | Editing + potong tiga klip | 7, 9 |
| Rabu | Penerbitan | 8 |
| Rabu + 7 hari | Evaluasi | 10 |

Riset tidak muat satu pagi bersama ideasi dan pengemasan. Kalau dipaksa, verifikasi akan dilewati
atau jadwalnya geser setiap minggu. Kalau riset lewat 90 menit, ganti klaimnya — jangan tambah
waktunya.

---

## Kalau Macet, Buka Berkas Ini

| Gejala | Berkas |
|---|---|
| Tidak ada ide yang layak | `01-ideasi.md`, lalu `content/log-keputusan.md` |
| Judul terasa lemah, thumbnail tidak jelas | `02-pengemasan.md` |
| Riset melebar, klaim inti belum terbukti | `03-riset-dan-fakta.md` (batas 90 menit) |
| Naskah terasa seperti esai | `04-penulisan-naskah.md` |
| Audio buruk, rekaman tidak bersih | `05-rekaman.md` |
| Video ramai tetapi tidak membuktikan apa pun | `06-riset-visual.md` |
| Video terasa lambat, banyak diam kosong | `07-penyuntingan.md` |
| Video tidak ditemukan | `08-penerbitan.md` |
| Klip tidak pernah jadi | `08-penerbitan.md`, bagian "Potong klip sebelum terbit" |
| Angka turun tetapi tidak tahu kenapa | `10-evaluasi.md`, lalu pipeline analisis |

---

## Status Sekarang

Yang memblokir rekaman pertama: prasyarat 1 (aset brand), 3 (audit izin data), dan 4 (channel
YouTube). Ideasi dan penulisan naskah tidak terhambat. Daftar lengkap ada di `AGENTS.md`.
