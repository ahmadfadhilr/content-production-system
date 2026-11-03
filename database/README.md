# Database Ide Konten

Satu baris = satu calon video. Isinya ada di `database.db`, tabel `ide`.
Berkas ini menjelaskan arti setiap kolom, setiap nilai, dan cara memakainya.

## Baca dalam satu menit

Lima hal ini yang menentukan keputusan. Sisanya penjelasan dan arsip.

| Yang dibaca | Artinya |
|---|---|
| `status` | Posisi ide: siap, perlu perbaikan, ditunda, gugur, atau digabung. |
| `skor_total` | Seberapa layak diproduksi. Makin tinggi makin baik. Dihitung database. |
| `skor_prioritas_konsep` | Seberapa dasar konsepnya. 5 = paling dasar, 1 = alat/dokumen. |
| `konsep_bisnis` | Konsep yang diajarkan, mis. "Penetapan harga". |
| `judul_kerja` | Judul kerja dari Tahap 1. Bukan judul final video. |

Urutan baca: **kode → judul → status → skor → konsep → isi → bukti**.

## Cara membaca

```bash
python3 tools/ranking.py                  # papan: ide hidup, urut prioritas lalu skor
python3 tools/ranking.py --detail         # tambah rincian empat skor
python3 tools/ranking.py --semua          # ikutkan yang gugur dan digabung
python3 tools/ranking.py --pilar=keuangan # hanya satu pilar (1/2/3 juga bisa)

python3 tools/lihat-ide.py                # daftar ide hidup
python3 tools/lihat-ide.py IDEA-009       # satu ide, semua kolom berlabel

sqlite3 database/database.db "select * from papan_ide;"
```

`papan_ide` adalah tampilan siap baca: hanya ide hidup, hanya kolom pendek, sudah
diurutkan. Untuk membaca kolom panjang satu ide, pakai `lihat-ide.py`.

## Contoh satu baris dibaca

```
IDEA-009 · siap
Harga Jasa Terlihat Untung, Tetapi Tim Terus Kehabisan Waktu

Konsep bisnis       Penetapan harga
Prioritas konsep    5 dari 5
Skor total          20 dari 30
                    permintaan 3×2 + celah 3×2 + bukti 3 + kapasitas 5
Pilar konten        keuangan
Format konten       Decision Notes

Situasi audiens     Pelanggan bilang harga mahal, padahal tim sudah kewalahan.
Masalah utama       Harga ditetapkan dari HPP saja, tidak mencerminkan
                    kapasitas tim terbatas.
Kedalaman bisnis    Harga, ruang lingkup, dan kapasitas tim perlu diputuskan
                    bersama.
```

Itu satu ide, dibaca dari atas ke bawah tanpa membuka kamus.

## Arti kolom

### Identitas dan keputusan

| Kolom | Isi | Contoh |
|---|---|---|
| `kode_ide` | Kode permanen. Jangan diubah setelah dipakai di brief atau naskah. | `IDEA-009` |
| `judul_kerja` | Judul kerja dari Tahap 1: kalimat yang layak muncul di feed dan jangkarnya sudah ada. Bukan judul final video — yang final dipilih di Tahap 2. | `Pelanggan Bilang Mahal, Tim Sudah Kewalahan` |
| `status` | Posisi ide. Nilainya di tabel "Status" di bawah. | `siap` |
| `skor_total` | 4–30. Dihitung otomatis dari empat skor. Jangan diisi tangan. | `20` |

### Konsep dan isi konten

| Kolom | Isi | Contoh |
|---|---|---|
| `konsep_bisnis` | Konsep yang diajarkan video ini. | `Penetapan harga` |
| `skor_prioritas_konsep` | 1–5. Seberapa fatal kalau audiens salah paham konsep ini. | `5` |
| `pilar_konten` | Pilar positioning. Nilainya di tabel "Pilar" di bawah. | `keuangan` |
| `format_konten` | Kerangka cerita. Nilainya di tabel "Format" di bawah. | `Decision Notes` |
| `situasi_audiens` | Lapisan 1. Situasi yang dikenali tanpa jargon. Bahan judul dan thumbnail. Di SOP disebut *pintu masuk*. | `Pelanggan bilang harga mahal, ...` |
| `masalah_utama` | Lapisan 2. Siapa, mengalami apa, akibatnya apa. | `Harga ditetapkan dari HPP saja, ...` |
| `kedalaman_bisnis` | Lapisan 3. Ukuran, trade-off, atau batas yang membuat topik tetap bernilai bagi operator matang. Di SOP disebut *ketegangan lanjut*. | `Harga, ruang lingkup, dan kapasitas ...` |

### Bukti dan asal ide

| Kolom | Isi | Contoh |
|---|---|---|
| `median_tayangan_10_teratas` | Median tayangan 10 hasil teratas, dari tiga putaran pindai. Bukan total views. | `136495` |
| `celah_pasokan` | Seberapa penuh YouTube Indonesia membahas keputusan ini. | `sedang` |
| `jenis_bukti` | Sumber kekuatan bukti awal. | `riset primer` |
| `skor_permintaan` | 1–5. Dari median, disesuaikan relevansi hasil. | `3` |
| `skor_celah_pasokan` | 0–5. Dari `celah_pasokan`. 0 = tidak ada celah. | `3` |
| `skor_bukti` | 1–5. Dari `jenis_bukti`. | `3` |
| `skor_kapasitas` | 1–5. Dari perkiraan hari kerja. | `5` |
| `perkiraan_hari_kerja` | Perkiraan hari kerja untuk memproduksi. | `2` |
| `asal_ide` | Dari mana ide datang: `pindai-gap`, `pindai-demand`, `global-adopsi`, `audiens`, `pengalaman`, `tren`, `log-keputusan`. | `pindai-gap` |
| `berkas_pindai` | Nama berkas hasil pindai sebagai bukti asal. | `pindai-2026-11-03` |
| `kode_rujukan` | Kode sitasi, dipisah titik koma. Bukan URL. | `Hinterhuber2004;Avlonitis2007` |

### Catatan

| Kolom | Isi | Contoh |
|---|---|---|
| `alasan_keputusan` | Satu kalimat: mengapa ide ini dipilih, ditunda, digabung, atau gugur. | `Kandidat utama putaran ...` |
| `tanggal_masuk` | Tanggal ide masuk database. Format `YYYY-MM-DD`. | `2026-11-02` |

## Arti nilai pilihan

### Pilar konten

| Nilai | Pilar lengkap |
|---|---|
| `keuangan` | Model Bisnis & Keuangan — pricing, margin, unit economics, cash flow. |
| `pertumbuhan` | Sistem Pertumbuhan Pendapatan — akuisisi, funnel, retensi, CAC/LTV. |
| `operasional` | Sistem Operasional & Kepemimpinan — SOP, KPI, delegasi, hiring. |

### Format konten

| Nilai | Struktur |
|---|---|
| `Decision Notes` | Situasi → pilihan → kriteria → keputusan → trade-off. |
| `Operating Playbook` | Masalah → langkah → contoh → ukuran → batas. |

### Status

| Nilai | Artinya |
|---|---|
| `siap` | Lolos gerbang. Boleh masuk Tahap 2 (pengemasan). |
| `perlu perbaikan` | Ide hidup, tetapi satu syarat belum lengkap: kemasan, bukti, atau sudut. |
| `ditunda` | Ide hidup, menunggu bukti atau urutan produksi. Bukan gugur. |
| `gugur` | Tidak diproduksi. Alasan wajib diisi. |
| `digabung` | Isinya masuk ke ide lain. Jangan diproduksi terpisah. |

### Celah pasokan

| Nilai | Artinya | Skor |
|---|---|---|
| `lebar` | Belum ada video Indonesia yang membahas keputusan ini langsung. | 5 |
| `sedang` | Ada yang membahas topiknya, tetapi tanpa keputusan, bukti, atau trade-off. | 3 |
| `sempit` | Sudah dibahas lengkap dan baik. Butuh pembeda kuat, atau gugur. | 0 |

> Berkas pindai lama memakai istilah **Kosong / Dangkal / Dalam**. Artinya sama, arahnya
> terbalik: Kosong = `lebar`, Dangkal = `sedang`, Dalam = `sempit`. Nama lama mudah
> disalahbaca ("celah dalam" terdengar seperti celah besar), karena itu diganti.

### Jenis bukti

| Nilai | Artinya | Skor |
|---|---|---|
| `data sendiri` | Catatan atau angka Fadhil yang aman dibuka. | 5 |
| `riset primer` | Laporan, filing, statistik resmi, jurnal, atau pengukuran yang siap jalan. | 3 |
| `tanpa sumber primer` | Hanya sumber sekunder, opini, atau batas pengalaman tanpa dokumen pendukung. | 1 |

## Rumus dan urutan

```text
skor_total = (skor_permintaan × 2)
           + (skor_celah_pasokan × 2)
           + skor_bukti
           + skor_kapasitas
```

Database yang menghitung `skor_total`. Kalau satu skor diubah, total ikut berubah.
Rentangnya 4–30. Yang tertinggi saat ini 22.

Urutan memakai dua kunci: `skor_prioritas_konsep` dulu, baru `skor_total`. Alasannya,
ide yang mengajarkan hal paling dasar harus tampil lebih dulu walaupun skornya lebih
rendah. Contoh: arus kas skornya 18 dan gugur karena pasokan sudah `sempit`, tetapi
konsepnya tetap paling dasar.

**Skor adalah penilaian, bukan hasil ukur.** Rubriknya ada di
`workflows/produksi/01-ideasi.md`. Kalau `alasan_keputusan` menyebut kendala, skor bisa
lebih rendah daripada angka mentahnya. Contoh: IDEA-009 mediannya 136 ribu tetapi skor
permintaannya 3 karena relevansi hasil hanya parsial.

## Memberi nilai

| Skor | Permintaan | Celah | Bukti | Kapasitas |
|---|---|---|---|---|
| 5 | Median di atas 100.000 | `lebar` | `data sendiri` yang aman dibuka | Siap dalam dua hari kerja |
| 3 | Median 10.000–100.000 | `sedang` | `riset primer` atau pengukuran siap jalan | Empat hari kerja |
| 1 | Di bawah 10.000 atau tidak stabil | `sempit` tanpa pembeda — **skor 0** | `tanpa sumber primer` | Lebih dari satu minggu |

> Celah memakai 0 untuk `sempit`, bukan 1: kalau tidak ada celah, nilainya nol. Tiga kriteria
> lain memakai 1–5. Ini sebabnya rentang `skor_total` dimulai dari 4, bukan 6.

Skor prioritas konsep:

| Skor | Arti |
|---|---|
| 5 | Kalau audiens salah paham, bisnisnya gagal. Contoh: margin per lini, HPP, arus kas, penetapan harga. |
| 4 | Kalau salah, bisnisnya rusak pelan atau berhenti tumbuh. Contoh: churn, retensi, CAC. |
| 3 | Kalau salah, pertumbuhan lambat. Contoh: funnel, peran tim, ukuran produktivitas. |
| 2 | Kalau salah, jalan lebih lambat. |
| 1 | Ini alat atau dokumen, bukan keputusan bisnis. |

## Menambah ide baru

Ide baru masuk lewat berkas JSON, satu hasil pindai sekaligus. Nama kunci JSON = nama
kolom.

```bash
python3 tools/tambah-ide.py ide-baru.json
cat ide.json | python3 tools/tambah-ide.py -
```

Contoh satu ide:

```json
[
  {
    "judul_kerja": "Kalimat yang layak muncul di feed; jangkar sudah ada",
    "situasi_audiens": "Situasi yang dikenali tanpa jargon",
    "masalah_utama": "Siapa, mengalami apa, akibatnya apa",
    "kedalaman_bisnis": "Ukuran atau trade-off untuk operator matang",
    "pilar_konten": "keuangan",
    "format_konten": "Decision Notes",
    "asal_ide": "pindai-gap",
    "berkas_pindai": "pindai-2026-11-03",
    "median_tayangan_10_teratas": 136495,
    "celah_pasokan": "sedang",
    "jenis_bukti": "riset primer",
    "skor_permintaan": 3,
    "skor_celah_pasokan": 3,
    "skor_bukti": 3,
    "skor_kapasitas": 5,
    "perkiraan_hari_kerja": 2,
    "konsep_bisnis": "Penetapan harga",
    "skor_prioritas_konsep": 5,
    "status": "siap",
    "kode_rujukan": "Hinterhuber2004",
    "alasan_keputusan": "Satu kalimat alasan"
  }
]
```

Aturan yang dijaga skrip:

- Baris lama tidak pernah ditimpa. Hanya ada INSERT.
- `kode_ide` dibuat otomatis dari nomor terakhir.
- `skor_total` dihitung database, bukan diisi.
- `tanggal_masuk` diisi tanggal hari ini.
- `judul_kerja` yang sama dilewati, bukan digandakan.
- Kolom atau nilai yang tidak dikenal ditolak, bukan diabaikan diam-diam.
- Ide baru wajib punya `situasi_audiens` dan `kedalaman_bisnis`. Keduanya mencegah
  database berhenti pada nama konsep yang hanya dipahami orang yang sudah belajar bisnis.

## Mengubah satu nilai

```bash
sqlite3 database/database.db \
  "update ide set skor_prioritas_konsep = 4 where kode_ide = 'IDEA-011';"
```

`skor_total` ikut berubah sendiri. Jangan pernah meng-update `skor_total`.

## Mengekspor

```bash
sqlite3 -header -csv database/database.db "select * from ide" > ekspor.csv
sqlite3 -header -csv database/database.db "select * from papan_ide" > papan.csv
```

## Aturan penamaan (best practice)

Dipakai untuk kolom baru, supaya database ini tidak kembali sulit dibaca.

1. **Nama adalah jawaban, bukan teka-teki.** Tulis `skor_permintaan`, bukan `sp` atau
   `pri`. Singkatan hanya boleh untuk istilah yang sudah dipakai audiens: KPI, SOP, CAC.
2. **Satu konsep, satu nama.** Jangan memakai alias di view. `papan_ide` memakai nama
   kolom yang sama dengan tabel.
3. **Nilai pilihan ditulis sebagai kata.** `keuangan`, bukan `1`. `lebar`, bukan
   `Kosong`. Database menolak nilai di luar daftar lewat `CHECK`.
4. **Sertakan satuan di nama.** `median_tayangan_10_teratas`, `perkiraan_hari_kerja`, dan skala
   `1–5` pada kolom skor. Tanpa satuan, angka tidak bisa ditafsirkan.
5. **Pisahkan data mentah dan turunan.** Simpan `median_tayangan_10_teratas` dan
   `perkiraan_hari_kerja`. Hitung `skor_total` di database, jangan disimpan dua kali.
6. **Urutkan kolom sesuai cara membacanya.** Identitas → keputusan → isi → bukti →
   catatan. Jangan menaruh kolom panjang di depan.
7. **Dokumentasi tinggal di sebelah data.** Arti kolom dan nilai ada di README ini dan
   komentar `skema.sql`, bukan di kepala orang.

## Batas yang belum selesai

- Ambang "siap" di skor 18 masih meloloskan 7 dari 8 ide hidup. Ambang itu belum
  menyaring apa pun.
- Rubrik skor hanya memakai nilai 1, 3, dan 5. Jarak antar-ide terlihat lebih tegas
  daripada kenyataannya.
- `data sendiri` belum pernah dipakai, sehingga `skor_bukti` belum pernah 5 dan total
  tertinggi yang wajar adalah 28 dari 30.
- `asal_ide` masih teks bebas. Nilai baru bisa muncul tanpa tercatat di README.
- Tidak ada riwayat perubahan. Kalau skor diubah, nilai lama hilang. Backup manual ada
  di `database/backup/`.
