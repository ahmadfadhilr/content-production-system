# Database Ide Konten

Satu berkas: `database.db`. Isinya satu tabel, `ide`. Skemanya ada di `skema.sql`
karena berkas `.db` tidak bisa dibaca langsung.

## Cara membaca

```bash
python3 tools/ranking.py            # ide hidup, urut prioritas lalu skor
python3 tools/ranking.py --detail   # tambah rincian skor
python3 tools/ranking.py --semua    # ikutkan yang Gugur dan Digabung
python3 tools/ranking.py --pilar=1  # hanya pilar keuangan
```

Atau buka langsung:

```bash
sqlite3 database/database.db "select * from ide_ringkas;"
```

## Arti kolom

| Kolom | Isi |
|---|---|
| `id` | Kode baris. IDEA-001, IDEA-002, dan seterusnya. |
| `sudut` | Judul kerja, satu kalimat. Bukan judul final video. |
| `pilar` | 1 keuangan, 2 pertumbuhan, 3 operasional. |
| `format` | DN Decision Notes, OP Operating Playbook. |
| `sumber_ide` | Dari mana ide datang: pindai-gap, pindai-demand, global-adopsi, audiens, pengalaman, tren, log-keputusan. |
| `pindai` | Nama berkas hasil pindai sebagai bukti asal. |
| `masalah` | Satu kalimat: siapa, mengalami apa, akibatnya apa. |
| `median_tayangan` | Median tayangan 10 hasil teratas, dari tiga putaran. |
| `celah` | Kosong, Dangkal, atau Dalam. |
| `jenis_bukti` | A data sendiri, B riset primer, C opini. |
| `rujukan` | Kode sumber, dipisah titik koma. |
| `hari_produksi` | Perkiraan hari kerja. |
| `skor_permintaan` | 1–5, dari median tayangan. |
| `skor_celah` | 1–5, dari kelas celah. |
| `skor_bukti` | 1–5, dari jenis bukti. |
| `skor_kapasitas` | 1–5, dari hari produksi. |
| `konsep_prioritas` | Nama konsep bisnis yang dibahas. |
| `skor_prioritas` | 1–5. Seberapa fatal kalau audiens salah paham konsep ini. |
| `total` | Rumus di bawah. |
| `status` | Siap, Perbaiki, Tunda, Gugur, Digabung. |
| `alasan` | Satu kalimat keputusan. |
| `dibuat` | Tanggal masuk database. |

## Rumus

```
total = (skor_permintaan × 2) + (skor_celah × 2) + skor_bukti + skor_kapasitas
```

Nilai tertinggi 28, bukan 30, karena `skor_bukti` belum pernah mencapai 5.
Nilai 5 hanya diberikan untuk bukti tipe A, dan `content/log-keputusan.md` belum
punya satu baris data nyata.

## Cara mengurutkan

Urutan memakai dua kunci: `skor_prioritas` dulu, baru `total`.

Alasannya, ide yang mengajarkan hal paling dasar harus tampil lebih dulu walaupun
skornya lebih rendah. Contohnya arus kas: skornya 18 dan gugur karena pasokan
sudah dalam, tetapi konsepnya tetap paling dasar.

## Arti skor prioritas

| Skor | Arti |
|---|---|
| 5 | Kalau audiens salah paham, bisnisnya gagal. Contoh: margin per lini, HPP, arus kas, penetapan harga. |
| 4 | Kalau salah, bisnisnya rusak pelan atau berhenti tumbuh. Contoh: churn, retensi, CAC. |
| 3 | Kalau salah, pertumbuhan lambat. Contoh: funnel, peran tim, ukuran produktivitas. |
| 2 | Kalau salah, jalan lebih lambat. |
| 1 | Ini alat atau dokumen, bukan keputusan bisnis. |

Skor 1–5 ini penilaian, bukan hasil ukur. Kalau Anda menilai beda, ubah satu baris:

```bash
sqlite3 database/database.db "update ide set skor_prioritas = 4 where id = 'IDEA-011';"
```

## Menambah ide baru

Ide baru masuk lewat berkas JSON, satu hasil pindai sekaligus:

```bash
python3 tools/tambah-ide.py ide-baru.json
```

Aturan yang dijaga skrip ini:

- Baris lama tidak pernah ditimpa. Hanya ada INSERT.
- `id` dibuat otomatis dari nomor terakhir.
- `total` dihitung dari empat skor, tidak diisi tangan.
- Sudut yang sama dilewati, bukan digandakan.
- Nilai di luar rentang ditolak. Pilar harus 1–3, skor harus 1–5, celah harus
  Kosong/Dangkal/Dalam, bukti harus A/B/C.

## Mengekspor

```bash
sqlite3 -header -csv database/database.db "select * from ide" > ekspor.csv
```

## Batas yang belum selesai

- Ambang "Siap" di angka 18 meloloskan 11 dari 13 baris. Ambang itu belum
  menyaring apa pun.
- Rubrik hanya memakai skor 5, 3, dan 1. Nilai 2 dan 4 tidak pernah dipakai,
  jadi jarak antar-ide terlihat lebih tegas daripada kenyataannya.
- Bukti tipe A masih nol, sehingga `total` maksimum yang mungkin adalah 28.
  IDEA-001 duduk tepat di batas itu.
