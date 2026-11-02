# Pipeline Analisis — Draf

> **Status:** belum berjalan. Dokumen ini disiapkan supaya tidak ditulis ulang saat video pilot
> pertama terbit. Nilai per tahap baru bisa diisi setelah ada minimal satu video dengan data 7
> hari. Sebelum itu, pertanyaannya berbeda — lihat Aturan 5.

**Tujuan:** setiap minggu, menilai seluruh pipeline produksi dan memilih **satu** perbaikan.

**Kenapa dipisah dari pipeline produksi.** Produksi mengejar terbit; analisis mengejar perubahan
sistem. Kalau dicampur, yang menang selalu terbit — dan sistem yang rusak tidak pernah diperbaiki.
Menulis post-mortem video (Tahap 10) bukan analisis pipeline. Post-mortem menilai satu video;
analisis menilai mesinnya.

---

## Ritme

Sekali seminggu, 30–45 menit, **sebelum** blok produksi (Sabtu pagi). Kalau dilakukan setelah
produksi, keputusannya selalu "nanti saja".

## Input

| Input | Dari mana | Wajib? |
|---|---|---|
| Post-mortem video 7 hari | `content/briefs/` | ✅ |
| Jam kerja per tahap | Diukur manual selama seminggu | ✅ |
| Komentar audiens | Post-mortem | ✅ |
| Log keputusan | `content/log-keputusan.md` | Kalau kosong, itu temuannya |
| Keluhan saat mengerjakan | Catatan pribadi | ✅ |

Kalau salah satu kosong, kosongnya itu sendiri temuan.

---

## Lima Langkah

### 1. Kumpulkan (10 menit)

Buka post-mortem terakhir dan catat lima angka: CTR, AVD, retensi 30 detik, jumlah komentar dari
pemilik bisnis, dan jam kerja total.

### 2. Nilai per tahap (15 menit)

Beri nilai 1–5 dan **satu bukti** per tahap. Nilai tanpa bukti tidak dipakai.

| Tahap | Pertanyaan | Nilai | Bukti |
|---|---|---|---|
| 1 Ideasi | Apakah ide datang tanpa buntu? | | |
| 2 Pengemasan | Apakah judul dan thumbnail bisa dipertahankan? | | |
| 3 Riset | Apakah bukti cukup dalam 90 menit? | | |
| 4 Naskah | Apakah naskah lulus tanpa ditulis ulang? | | |
| 5 Rekaman | Apakah selesai dalam satu sesi tanpa ulang? | | |
| 6 Visual | Apakah artefak cukup dan mudah diambil? | | |
| 7 Editing | Berapa jam, dan bagian mana yang paling lama? | | |
| 8 Penerbitan | Apakah ada yang menunda terbit? | | |
| 9 Distribusi | Apakah klip benar-benar terbit? | | |
| 10 Evaluasi | Apakah pelajaran tercatat dan dipakai? | | |

### 3. Pilih satu hambatan (5 menit)

Aturannya: **yang paling mahal dan paling bisa diperbaiki minggu ini.** Bukan yang paling menarik.
Kalau dua kandidat, pilih yang muncul dua minggu berturut-turut.

### 4. Ubah satu berkas (10 menit)

Satu perubahan, di satu berkas di `workflows/produksi/`. Ganti kalimat lama; jangan menambah
paragraf baru di bawahnya. Berkas panduan yang terus bertambah akan berhenti dibaca.

### 5. Catat (5 menit)

Simpan di `content/analisis/pipeline/YYYY-MM-DD.md` dengan bentuk di bawah. Satu berkas per
minggu, bukan satu berkas panjang yang terus diedit.

```markdown
# Analisis Pipeline — YYYY-MM-DD

**Video yang dinilai:** [judul] · terbit [tanggal]
**Angka:** CTR [ ] · AVD [ ] · retensi 30 dtk [ ] · komentar audiens target [ ]
**Jam kerja:** ideasi [ ] · riset [ ] · naskah [ ] · rekam [ ] · edit [ ] · total [ ]

## Nilai per tahap
[tabel 1–5 + bukti]

## Hambatan utama minggu ini
[satu kalimat]

## Perubahan yang dibuat
[berkas] · [kalimat lama] → [kalimat baru]

## Yang dipantau minggu depan
[satu angka atau satu gejala]

## Yang sengaja tidak diubah
[supaya tidak dibuka ulang]
```

---

## Aturan

1. **Satu perubahan per minggu.** Dua perubahan sekaligus membuat tidak ada yang bisa dinilai.
2. **Data di bawah 7 hari bukan sinyal.** CTR dan AVD hari pertama sangat tidak stabil.
3. **Jangan mengubah dua tahap sekaligus.** Kalau Tahap 3 dan 7 diubah bersamaan, tidak ada cara
   tahu mana yang berpengaruh.
4. **Jangan menambah pilar, format, atau channel** sebelum empat video pilot selesai. Ini sudah
   diputuskan di pipeline produksi.
5. **Kalau belum ada video terbit, pertanyaan analisisnya bukan "apa yang perlu diimprove",**
   melainkan "apa yang menghalangi terbit". Jawabannya biasanya prasyarat, bukan workflow.

---

## Gerbang Keluaran

✅ Satu berkas `content/analisis/pipeline/YYYY-MM-DD.md` ada, berisi satu hambatan dan satu
perubahan yang sudah benar-benar diterapkan ke berkas workflow — bukan rencana perubahan.
