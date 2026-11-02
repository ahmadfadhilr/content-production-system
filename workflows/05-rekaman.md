# Tahap 5 — Rekaman

## Tujuan

Merekam audio dan video yang cukup jelas dan bersih untuk diedit. Fadhil yang merekam (talking head atau voice over). Dokumen ini menyediakan ceklis, panduan lingkungan, dan aturan produksi agar hasil rekaman konsisten dari sesi ke sesi.

---

## Input

| Input | Sumber | Wajib? |
|---|---|---|
| Naskah atau outline final | `content/scripts/` — output Tahap 4 | ✅ Ya |
| Brief konten | `content/briefs/` | ✅ Ya |
| Konsep thumbnail | Output Tahap 2 | Opsional (untuk referensi framing) |

> [!IMPORTANT]
> Jangan mulai rekam kalau naskah belum final. Revisi di tengah sesi rekaman membuang waktu dan energi.

---

## Prinsip Utama

**Audio lebih penting daripada video.** Audio buruk lebih merusak pengalaman menonton daripada gambar yang sederhana. Penonton bisa menerima visual biasa, tapi tidak bisa mentoleransi suara berdengung, pecah, atau bergema.

**Jangan kejar sempurna saat rekam.** Kesalahan dipotong saat editing. Fokus pada energi dan kejelasan penyampaian.

**Jangan beli peralatan mahal sebelum pilot selesai.** Mulai dengan kamera HP + mikrofon dasar. Upgrade berdasarkan apa yang benar-benar membatasi kualitas setelah empat video pertama selesai.

---

## Urutan Prioritas Audio

Ini urutan yang paling berdampak ke kualitas akhir. Nomor 1 paling penting — tidak ada editing yang bisa memperbaiki ruangan yang bising.

| Prioritas | Faktor | Catatan |
|---|---|---|
| 1 | **Ruangan sunyi** | Matikan AC, kipas, mesin cuci. Tutup jendela. Jauhkan HP dari mikrofon. |
| 2 | **Penempatan mikrofon** | Dalam jarak 30 cm dari mulut. Konsisten sepanjang sesi. |
| 3 | **Level gain yang benar** | Peak di −12 sampai −6 dB. Jangan sampai clipping (lampu merah). |
| 4 | **Kamera dan pencahayaan** | Boleh basic — audio yang menentukan. |

> [!WARNING]
> Clipping (distorsi karena gain terlalu tinggi) tidak bisa diperbaiki di post-production. Lebih baik terlalu pelan sedikit daripada terlalu keras.

---

## Ceklis Sebelum Rekam

Periksa semua ini **sebelum** menekan tombol rekam. Jangan skip — menemukan masalah saat editing jauh lebih menyakitkan.

### Audio

- [ ] Mikrofon bersih dan terpasang dengan benar
- [ ] Tidak ada dengung AC, kipas, kulkas, atau mesin di sekitar
- [ ] Jendela tertutup — tidak ada suara lalu lintas atau hujan masuk
- [ ] HP di-silent dan dijauhkan dari mikrofon (menghindari interferensi sinyal)
- [ ] Test rekam 15 detik → putar ulang dengan headphone → dengarkan noise
- [ ] Gain sudah diatur: peak di −12 sampai −6 dB saat bicara normal

### Video

- [ ] Pencahayaan konsisten — tidak ada flicker, tidak berubah karena awan
- [ ] Latar bersih dan rapi — tidak ada benda yang mengganggu
- [ ] Kamera stabil (tripod atau permukaan datar)
- [ ] Tidak ada jendela terang di belakang subjek (backlight)

### Frame

- [ ] Resolusi 4K jika tersedia (untuk fleksibilitas zoom saat editing)
- [ ] Rasio 16:9
- [ ] Kepala di sepertiga atas frame
- [ ] Kamera sejajar mata atau sedikit di atas

### Persiapan Umum

- [ ] Naskah/outline sudah final dan terbuka di layar (laptop/tablet di samping kamera)
- [ ] Air minum tersedia (suara kering terdengar di mikrofon)
- [ ] Pakaian sudah dipilih (hindari motif garis halus — bisa moire di kamera)
- [ ] **Room tone:** rekam 10 detik keheningan ruangan sebelum mulai bicara

> [!TIP]
> Room tone adalah rekaman keheningan ruangan — suara "kosong" yang khas di ruangan itu. Editor membutuhkan ini untuk noise reduction yang konsisten. Tanpa room tone, noise gate akan terdengar tidak natural.

---

## Pengaturan Lingkungan Rekaman

### Pencahayaan

```
        [KEY LIGHT]
            \  45°
             \
              \
    [KAMERA] ---- [SUBJEK]
              /
             /
            /  45°
     [FILL LIGHT
      atau REFLEKTOR]
```

- **Key light** (cahaya utama): di sisi kiri atau kanan, 45 derajat dari wajah. Ini sumber cahaya dominan.
- **Fill light** (cahaya pengisi): di sisi berlawanan. Bisa pakai reflektor putih (styrofoam/karton putih) untuk memantulkan key light. Tujuannya mengurangi bayangan keras di wajah.
- **Fase pilot:** Cahaya jendela bisa jadi key light. Duduk menghadap jendela, bukan membelakanginya. Rekam di jam yang sama setiap sesi agar konsistensi cahaya terjaga.
- **Hindari:** Lampu langit-langit sebagai satu-satunya sumber (membuat bayangan mata). Campuran warna cahaya (daylight + tungsten).

### Latar Belakang

- Bersih dan sederhana. Rak buku, tanaman, atau dinding polos bekerja dengan baik.
- Hindari latar yang terlalu ramai — perhatian penonton terpecah.
- Hindari jendela terang di belakang — kamera akan mengekspos jendela dan wajah jadi gelap.
- Jarak subjek dari latar: minimal 1 meter. Ini membuat latar sedikit blur (depth of field) dan mengurangi echo.

### Kamera

- **Posisi:** Sejajar mata atau sedikit di atas. Jangan dari bawah (kesan tidak profesional).
- **Framing:** Kepala di sepertiga atas. Sedikit ruang di atas kepala (headroom). Mata di garis sepertiga atas frame.
- **Lensa:** Jika pakai HP, gunakan lensa utama (1x), bukan ultrawide.
- **Stabilitas:** Tripod atau tumpukan buku yang stabil. Jangan handheld untuk talking head.

### Mikrofon

| Tipe | Kapan pakai | Jarak ideal |
|---|---|---|
| **Lavalier (clip-on)** | Talking head, banyak gerak | 15–20 cm dari mulut, di kerah baju |
| **Shotgun** | Talking head, di luar frame | 30–50 cm dari mulut, di atas atau di bawah frame |
| **USB condenser** | Voice over, duduk di meja | 15–30 cm dari mulut, pakai pop filter |

- Jarak subjek dari dinding: minimal 1 meter untuk mengurangi echo ruangan.
- Jika ruangan bergema, tambahkan bahan penyerap: selimut, bantal, gorden tebal, atau foam di belakang mikrofon.

---

## Prosedur Rekaman

### Langkah 1 — Siapkan Ruangan (15 menit)

1. Matikan semua sumber suara: AC, kipan, kulkas (jika dekat), notifikasi HP.
2. Atur pencahayaan sesuai panduan di atas.
3. Pasang kamera dan atur framing.
4. Pasang mikrofon dan hubungkan ke perekam/kamera.
5. Buka naskah di layar yang mudah dilihat tanpa menoleh jauh dari kamera.

### Langkah 2 — Test Audio dan Video (5 menit)

1. Rekam 30 detik sambil bicara dengan volume normal.
2. Putar ulang dengan **headphone** (bukan speaker laptop). Dengarkan:
   - Ada dengung atau noise? → Cari sumbernya dan matikan.
   - Suara bergema? → Pindah posisi atau tambah penyerap.
   - Volume terlalu pelan atau terlalu keras? → Atur gain.
3. Periksa video: pencahayaan rata? Framing benar? Fokus tajam?
4. Kalau semua oke, lanjut ke room tone.

### Langkah 3 — Rekam Room Tone (15 detik)

1. Tekan rekam.
2. Diam total selama 10–15 detik. Jangan bergerak, jangan bicara.
3. Stop.
4. Simpan file ini terpisah sebagai `room-tone.wav` atau tandai di awal rekaman.

### Langkah 4 — Rekam per Bagian

1. Rekam sesuai urutan naskah: Hook → Konteks → Isi Utama → Kesimpulan.
2. Untuk setiap bagian utama, lakukan **2–3 take**. Pilih yang energinya paling baik saat editing.
3. Jangan berhenti merekam di antara take — terus rolling dan tandai kesalahan (lihat di bawah).
4. Bicara ke kamera seolah bicara ke satu orang — bukan ke audiens massal.
5. Setelah setiap bagian selesai, periksa sekilas: audio masih oke? Framing tidak bergeser?

### Langkah 5 — Menandai Kesalahan

Ketika salah bicara atau ingin mengulang:

1. **Berhenti bicara** — jeda 2 detik.
2. **Tepuk tangan sekali** dengan keras — ini membuat spike yang mudah dilihat di waveform audio.
3. **Ulangi dari awal kalimat** yang salah.
4. Jangan buang waktu minta maaf ke kamera — langsung ulang.

```
Waveform audio:
───────██───────────────────── ← Tepuk tangan = spike = penanda kesalahan
       ↑
    Potong di sini saat editing
```

### Langkah 6 — Simpan dan Backup

1. Segera setelah sesi selesai, **pindahkan file ke komputer**.
2. Simpan di folder yang benar:
   ```
   content/assets/[YYYY-MM-DD]-[judul-pendek]/
   ```
3. Jangan menunda — memory card penuh atau corrupt bisa menghilangkan footage.
4. Buat file `notes.md` (lihat konvensi penamaan di bawah).

---

## Aturan Rekaman Batch

Rekam 2–4 naskah per sesi untuk efisiensi. Satu kali setup, beberapa video.

| Aturan | Alasan |
|---|---|
| Ganti baju di antara video | Variasi visual — penonton tidak sadar video direkam hari yang sama |
| Istirahat setiap 30–45 menit | Energi menurun → delivery datar → retensi penonton turun |
| Jangan kejar sempurna | Kesalahan dipotong saat edit. Fokus pada energi, bukan kesempurnaan |
| Rekam video yang paling membutuhkan energi duluan | Energi paling tinggi di awal sesi |
| Minum air di setiap jeda | Suara kering terdengar di mikrofon dan mengganggu penonton |

> [!TIP]
> Rekam hook (5 detik pertama) di akhir sesi setelah sudah "warm up". Hook butuh energi tertinggi — lebih mudah setelah kamu sudah nyaman di depan kamera.

---

## Panduan Khusus Voice Over

Jika format video tidak pakai talking head (misalnya screen recording + narasi):

1. **Ruangan:** Pilih ruangan kecil dengan banyak bahan lunak (kasur, bantal, gorden). Ruangan besar dan kosong = echo.
2. **Jarak mikrofon:** Konsisten sepanjang rekaman. Tandai posisi mulut relatif terhadap mikrofon. Perubahan jarak = perubahan volume dan karakter suara.
3. **Energi suara:** Baca dengan semangat. Delivery datar membunuh retensi. Bayangkan kamu sedang menjelaskan ke teman, bukan membaca dokumen.
4. **Multiple takes:** Lakukan 2–3 take untuk setiap bagian. Pilih yang energinya paling hidup.
5. **Pop filter:** Gunakan pop filter atau posisikan mikrofon sedikit di samping mulut (off-axis) untuk menghindari suara "p" dan "b" yang meledak.
6. **Postur:** Berdiri saat voice over jika memungkinkan. Suara lebih bertenaga dibanding duduk membungkuk.

---

## Konvensi Penamaan File

```
content/assets/2026-11-01-margin-vs-omzet/
├── raw-take-01.mov          # Take pertama, full session
├── raw-take-02.mov          # Take kedua (jika rekam terpisah)
├── room-tone.wav            # 10-15 detik keheningan ruangan
└── notes.md                 # Catatan rekaman
```

### Format `notes.md`

```markdown
# Catatan Rekaman — [Judul Video]

**Tanggal:** YYYY-MM-DD
**Durasi sesi:** ± X jam
**Peralatan:** [kamera, mikrofon, pencahayaan]

## Take yang Bagus

- raw-take-01.mov
  - 00:00–02:15 — Hook dan konteks (take 2 lebih baik dari take 1)
  - 03:30–07:45 — Isi utama bagian 1 (oke, energi tinggi)
  - 08:00–08:45 — Isi utama bagian 2 (ulang di take 02)
  - 10:00–11:30 — Kesimpulan (oke)

- raw-take-02.mov
  - 00:00–01:20 — Isi utama bagian 2 (lebih baik dari take 01)
  - 02:00–02:30 — Hook alternatif (coba versi pertanyaan)

## Masalah Teknis

- AC bunyi di menit 05:00–05:30 take 01 — perlu dipotong
- Pencahayaan berubah di menit 09:00 karena awan — color correct saat edit

## Catatan untuk Editor

- Gunakan hook dari take 02 (lebih tajam)
- Bagian tentang unit economics perlu grafis overlay
```

---

## Pengaturan Peralatan Pilot

Peralatan minimum untuk empat video pertama. Jangan beli lebih dari ini sebelum pilot selesai.

| Peralatan | Rekomendasi pilot | Catatan |
|---|---|---|
| **Kamera** | HP dengan kamera 4K (iPhone/Samsung flagship) | Cukup untuk pilot. Upgrade ke mirrorless jika depth of field jadi masalah. |
| **Mikrofon** | Lavalier wireless budget (Boya, Rode Wireless Go) atau USB condenser (Samson Q2U, Audio-Technica ATR2100x) | Investasi terpenting. Audio buruk langsung terasa. |
| **Pencahayaan** | Cahaya jendela + reflektor karton putih | Gratis. Upgrade ke ring light atau LED panel jika inkonsisten. |
| **Tripod** | Tripod HP atau tripod kamera dasar | Harus stabil. Jangan handheld. |
| **Pop filter** | Stoking di frame kawat atau pop filter murah | Untuk voice over. Talking head dengan lavalier tidak perlu. |

> [!CAUTION]
> Jebakan umum: membeli peralatan mahal sebelum tahu format mana yang bekerja. Selesaikan empat video pilot dulu. Lihat apa yang benar-benar membatasi kualitas. Baru upgrade peralatan yang relevan.

---

## Kesalahan Umum

| Kesalahan | Dampak | Pencegahan |
|---|---|---|
| Tidak cek audio sebelum rekam | Dengung AC baru ketahuan saat editing — semua take kena | Selalu test rekam 30 detik + dengarkan pakai headphone |
| Tidak merekam room tone | Noise reduction tidak konsisten, suara "pumping" | Rekam 10–15 detik keheningan di awal setiap sesi |
| Hanya satu take per bagian | Tidak ada pilihan saat editing — terpaksa pakai take yang kurang bagus | Minimal 2 take untuk setiap bagian utama, 2–3 untuk hook |
| Lupa ganti baju saat batch | Semua video terlihat direkam hari yang sama — kurang variasi | Siapkan 2–4 set pakaian sebelum mulai sesi |
| Tidak langsung simpan file | Memory card penuh, corrupt, atau tertimpa — footage hilang | Transfer ke komputer segera setelah sesi selesai |
| Beli peralatan mahal sebelum pilot | Uang terbuang jika format berubah — belum tahu kebutuhan nyata | Pakai peralatan minimum dulu. Upgrade setelah pilot selesai |
| Delivery datar / membaca naskah | Penonton bisa merasakan ketika presenter membaca — retensi turun | Hafal poin utama, bukan kalimat per kalimat. Bicara, jangan baca |
| Merekam terlalu lama tanpa istirahat | Energi drop drastis — take terakhir jauh lebih buruk dari take pertama | Istirahat 5–10 menit setiap 30–45 menit rekaman |

---

## Gerbang Keluaran

Rekaman **lulus** dan boleh lanjut ke Tahap 6 (Riset Visual) jika:

- [ ] File audio/video jelas dan cukup bersih untuk diedit
- [ ] Tidak ada noise atau dengung yang mendominasi di seluruh rekaman
- [ ] Room tone sudah direkam
- [ ] Semua bagian naskah sudah direkam (minimal 2 take per bagian utama)
- [ ] File sudah disimpan di `content/assets/[YYYY-MM-DD]-[judul-pendek]/`
- [ ] Backup tersimpan (hard drive atau cloud)
- [ ] File `notes.md` sudah dibuat dengan timestamp take yang bagus

> [!WARNING]
> Jangan lanjut ke editing jika audio bermasalah. Lebih baik rekam ulang di sesi berikutnya daripada menghabiskan berjam-jam mencoba memperbaiki audio buruk di post-production.

---

## Output

| Output | Lokasi |
|---|---|
| File rekaman mentah (video/audio) | `content/assets/[YYYY-MM-DD]-[judul-pendek]/` |
| File room tone | `content/assets/[YYYY-MM-DD]-[judul-pendek]/room-tone.wav` |
| Catatan rekaman dengan timestamp | `content/assets/[YYYY-MM-DD]-[judul-pendek]/notes.md` |

---

## Alat Bantu

| Alat | Kegunaan |
|---|---|
| Kamera HP / mirrorless | Merekam video |
| Mikrofon lavalier / USB condenser | Merekam audio |
| Headphone | Monitoring audio saat test dan review |
| Tripod | Stabilitas kamera |
| Reflektor / ring light | Pencahayaan |
| Aplikasi kamera (Filmic Pro, Protake) | Kontrol manual exposure dan focus |
| Audio meter di kamera/perekam | Memastikan level gain benar (peak −12 sampai −6 dB) |

---

## Referensi Terkait

- **Sebelum rekam:** Baca naskah final di [`04-penulisan-naskah.md`](file:///Users/ahmadfadhilramadhan/Documents/Personal%20Works/content-production-system/workflows/04-penulisan-naskah.md)
- **Setelah rekam:** Lanjut ke [`06-riset-visual.md`](file:///Users/ahmadfadhilramadhan/Documents/Personal%20Works/content-production-system/workflows/06-riset-visual.md) untuk mengumpulkan aset visual
- **Standar editing audio:** Lihat [`07-penyuntingan.md`](file:///Users/ahmadfadhilramadhan/Documents/Personal%20Works/content-production-system/workflows/07-penyuntingan.md) untuk standar teknis loudness dan mixing
- **Prinsip kualitas:** Lihat [`prinsip-editorial.md`](file:///Users/ahmadfadhilramadhan/Documents/Personal%20Works/content-production-system/workflows/prinsip-editorial.md)
