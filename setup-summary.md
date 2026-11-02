# Setup Content Production System — Ringkasan

## Apa yang sudah dibuat

Sistem produksi konten end-to-end untuk personal brand Fadhil sebagai Business Builder. Semua file sudah lengkap dan siap dipakai.

---

## Struktur Proyek (17 file + 6 folder)

```
content-production-system/
├── AGENTS.md                         ← Panduan utama AI (635 baris)
├── Personal Brand Plan.docx          ← Riset audiens dan positioning (sudah ada)
├── ref-AGENTS.md                     ← Rujukan dari Salam Cendekia (sudah ada)
│
├── workflows/                        ← 13 SOP
│   ├── 01-ideasi.md                  ← Cari masalah audiens, validasi ide
│   ├── 02-pengemasan.md              ← Judul + thumbnail SEBELUM naskah
│   ├── 03-riset-dan-fakta.md         ← Kumpulkan bukti, label terverifikasi/simpulan/tebakan
│   ├── 04-penulisan-naskah.md        ← Outline/naskah dengan hook, PAS, open loop
│   ├── 05-rekaman.md                 ← Ceklis rekaman, batch recording
│   ├── 06-riset-visual.md            ← B-roll, grafis data, peta visual
│   ├── 07-penyuntingan.md            ← Editing 3 lapis (rough → fine → polish)
│   ├── 08-penerbitan.md              ← Upload, metadata, SEO YouTube Indonesia
│   ├── 09-distribusi-ulang.md        ← 1 video → 3-6 klip Reels/Shorts/TikTok
│   ├── 10-evaluasi.md                ← Post-mortem 48 jam, 7 hari, bulanan
│   ├── content-bank.md               ← 40 ide konten (3 pilar × 3 format)
│   ├── brand-guidelines.md           ← Identitas visual, aturan thumbnail
│   └── prinsip-editorial.md          ← 7 prinsip + rubrik terbit
│
├── templates/                        ← 2 templat
│   ├── brief-konten.md               ← Brief per video (masalah → POV → bukti → visual)
│   └── post-mortem.md                ← Evaluasi per video (metrik → retensi → pelajaran)
│
├── tools/                            ← Skrip otomasi (kosong, diisi sesuai kebutuhan)
├── content/briefs/                   ← Brief yang sudah diisi per video
├── content/scripts/                  ← Naskah per video
├── content/assets/                   ← Aset visual per video
├── content/exports/                  ← File jadi (video, thumbnail, klip)
└── brand_assets/                     ← Logo, font, palet warna
```

---

## Pipeline Produksi — 10 Tahap

Setiap tahap punya **gerbang keluaran** yang harus lulus sebelum lanjut ke tahap berikutnya.

```
Ideasi → Pengemasan → Riset → Naskah → Rekam → Visual → Edit → Terbit → Distribusi → Evaluasi
                                                                                        ↓
                                                                              Umpan balik ke Ideasi
```

---

## Sumber Referensi yang Sudah Diriset

### Kreator rujukan (pola yang diadopsi)
| Kreator | Tautan | Pola utama yang diambil |
|---|---|---|
| **Alex Hormozi** | `https://www.youtube.com/@AlexHormozi` | Hook tanpa basa-basi, jump cut, punch zoom 4K, kinetic captions, batch recording |
| **Raymond Chin** | `https://www.youtube.com/@RaymondChins` | Business Breakdown berbasis data, motion graphics, editing dinamis |
| **Ferry Irwandi** | `https://www.youtube.com/@ferryirwandi` | Gaya investigatif mini-dokumenter, sound design sinematik |
| **Big A Story** | `https://www.youtube.com/@WeAreBigAStory` | Judul pertanyaan dengan entitas dan taruhan uang. Channel bisnis sepak bola, bukan channel bisnis umum. |
| **Moon** | `https://www.youtube.com/@Moon-Real` | Video esai panjang berbahasa Inggris dengan produksi tim. Contoh hasil, bukan contoh proses. |

Daftar video terbaru tiap channel bisa dibaca tanpa login dengan
`python3 tools/ambil-daftar-video.py Moon-Real WeAreBigAStory`. Jangan mencari nama tampilan di
mesin pencari, karena hasilnya channel lain dengan nama mirip.

### Best practice yang diadopsi
- Packaging-first: judul + thumbnail dirancang **sebelum** naskah
- Hook 3–5 detik tanpa sapaan
- Editing 3 lapis: rough cut → fine cut → polish
- Audio: −14 LUFS, HP 80 Hz, musik −20 s/d −25 dB
- SEO Indonesia: long-tail keyword, format "Cara.../Kenapa.../Tips..."
- 1 video YouTube → 3–6 klip pendek (Reels/Shorts)
- Post-mortem di 48 jam dan 7 hari

---

## Langkah Selanjutnya

> [!IMPORTANT]
> Empat hal yang perlu dilakukan sebelum produksi video pertama:

1. **Finalisasi palet warna dan aset brand** — Warna, font, dan templat thumbnail belum ditetapkan (lihat `workflows/brand-guidelines.md`). Buat di Canva/Figma dan simpan di `brand_assets/`.

2. **Pilih empat brief pilot** — Jadwal pilot dari Personal Brand Plan sudah ada. Isi brief menggunakan `templates/brief-konten.md` untuk empat video pertama.

3. **Audit izin data Salam Cendekia** — Tentukan angka dan cerita mana yang aman untuk dibagikan dan mana yang harus disamarkan.

4. **Siapkan channel YouTube** — Buat channel, tulis deskripsi, pasang banner dan foto profil.
