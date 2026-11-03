# SOP Tahap 3 — Riset dan Verifikasi Fakta

> **Tahap sebelumnya:** [02-pengemasan.md](./02-pengemasan.md) — judul dan konsep thumbnail
> sudah ada.
> **Tahap sesudahnya:** [04-penulisan-naskah.md](./04-penulisan-naskah.md) — naskah ditulis
> berdasarkan fakta yang sudah diverifikasi.

---

## Tujuan

Mengumpulkan bukti yang mendukung POV, dengan **sumber primer untuk setiap klaim inti**. Setiap
angka harus punya definisi, periode, dan sumber.

Tahap ini punya dua pekerjaan yang berbeda:

1. **Mencari** bukti yang layak dipakai.
2. **Memeriksa** apakah bukti itu benar.

Kebanyakan sistem riset hanya mengerjakan nomor 2. Akibatnya rapi tetapi kosong.

---

## Input

| Input | Sumber | Wajib? |
|---|---|---|
| Brief konten (masalah, POV, format) | `content/briefs/` | ✅ |
| Judul dan konsep thumbnail | Tahap 2 | ✅ |
| Log keputusan | `content/log-keputusan.md` | Opsional. Dibutuhkan kalau memakai jalur 1 di Langkah 5 |
| Pengalaman langsung Fadhil | Wawancara / catatan | Jika relevan |

---

## Output

**Lembar fakta** di `content/briefs/[judul-pendek]-fakta.md`. Setiap butir memuat:

- Klaim atau angka
- Sumber (nama, URL, tanggal/periode)
- Jenis: pengalaman langsung / data publik / ilustrasi
- Reliabilitas: *terverifikasi* / *simpulan* / *tebakan*
- Primer atau sekunder

---

## Tiga Jenis Sumber

| Jenis | Definisi | Contoh | Label |
|---|---|---|---|
| **Pengalaman langsung** | Fakta dari bisnis Fadhil sendiri | "Kami naikkan harga 28%, churn naik 3%." | `[PENGALAMAN]` |
| **Data publik** | Angka dari sumber yang bisa ditelusuri | "Menurut BPS 2024, 63% UMKM..." | `[DATA]` |
| **Ilustrasi** | Contoh buatan untuk menjelaskan konsep | "Bayangkan bisnis jasa dengan margin 40%..." | `[ILUSTRASI]` |

> [!CAUTION]
> Jangan pernah menyajikan ilustrasi sebagai data nyata. Awali dengan "misalnya", "bayangkan",
> atau "ilustrasinya begini".

---

## Tiga Label Reliabilitas

| Label | Artinya | Kapan dipakai |
|---|---|---|
| **Terverifikasi** ✅ | Sumber primer ditemukan, angka sesuai | Laporan resmi, statistik pemerintah, laporan keuangan publik, pengukuran sendiri |
| **Simpulan** ⚠️ | Kesimpulan dari data, bukan data mentahnya | "Dari angka ini bisa disimpulkan..." |
| **Tebakan** ❓ | Belum ada data | "Dugaan saya..." |

**Aturan:**

- Ketiga jenis boleh muncul. Yang dilarang: menyajikan tebakan sebagai terverifikasi.
- Kalau klaim inti hanya didukung tebakan, ubah klaimnya atau cari bukti.
- Sebut tingkat kepastian di naskah: "Data menunjukkan..." vs "Dari pengamatan saya..." vs
  "Dugaan saya...".

---

## Prosedur Langkah demi Langkah

### Langkah 1 — Baca Brief dan Tulis Ulang POV

- **Pintu masuk:** situasi yang dapat dipahami tanpa istilah bisnis.
- **Masalah audiens:** pertanyaan spesifik yang dijawab video ini.
- **POV:** posisi Fadhil.
- **Ketegangan lanjut:** ukuran, trade-off, atau batas yang perlu diuji untuk operator yang lebih matang.
- **Format:** Decision Notes / Business Breakdown / Operating Playbook.

Tulis POV dalam satu kalimat. Pastikan bukti dapat menjelaskan pintu masuk tanpa membuatnya
terasa seperti contoh kosong, dan dapat menjawab ketegangan lanjut tanpa menambah jargon. Kalau
tidak bisa, kembali ke Tahap 1.

---

### Langkah 2 — Daftar Klaim yang Butuh Bukti

Untuk setiap klaim, tanya: **"Kalau penonton bilang 'buktinya apa?', apa jawabanku?"**

| Tingkat | Definisi | Syarat bukti |
|---|---|---|
| **Klaim inti** | Mendukung POV utama | Wajib sumber primer |
| **Klaim pendukung** | Memperkaya argumen | Boleh data publik sekunder |
| **Klaim konteks** | Latar belakang umum | Cukup referensi umum |

Contoh:

| # | Klaim | Tingkat | Bukti yang dibutuhkan |
|---|---|---|---|
| 1 | Naikkan harga 20% bisa menaikkan profit lebih dari 20% | Inti | Perhitungan unit economics sendiri |
| 2 | Mayoritas bisnis jasa punya margin bersih di bawah 15% | Pendukung | Survei industri |
| 3 | Churn setelah kenaikan harga lebih rendah dari yang ditakutkan | Inti | Data churn sendiri |
| 4 | Bisnis jasa di Indonesia tumbuh 7% per tahun | Konteks | BPS |

---

### Langkah 3 — Cari Bukti, Mulai dari yang Paling Dekat

Urutannya penting. Jangan mulai dari Google.

> [!IMPORTANT]
> **Urutan mencari berbeda dari urutan menyajikan.** Yang paling kuat untuk meyakinkan bukan yang
> paling enak dibuka. Dua belas video berperforma tertinggi yang saya periksa (2 November 2026)
> tidak satu pun membuka dengan jurnal. Yang muncul di 60 detik pertama: klip pernyataan pejabat,
> pengumuman lembaga, harga beli, omzet yang dibandingkan, rekaman lokasi. Jurnal masuk sebagai
> penopang di tengah. Catatan lengkapnya di `content/analisis/2026-11-02-naskah-rujukan/`.

#### 3a. Data dan Artefak Sendiri

Ini bukti terkuat dan satu-satunya yang tidak bisa ditiru kreator lain.

- Buka `content/log-keputusan.md`.
- Cari baris yang berhubungan dengan klaim.
- Kumpulkan artefaknya: spreadsheet, invoice, dashboard, potongan laporan, tangkapan layar.
- Catat sebagai `[PENGALAMAN]`.

**Yang dihitung bukti sendiri:**

- Angka yang pernah diukur, walaupun kecil sampelnya.
- Keputusan yang sudah diambil, beserta alasannya.
- Dokumen yang benar-benar dipakai: SOP, kontrak, tagihan, rekap penjualan.
- Kesalahan yang pernah terjadi dan biayanya.

**Yang tidak dihitung:**

- Perasaan bahwa "bisnis seperti ini biasanya begini".
- Angka yang dibulatkan tanpa catatan asal.
- Cerita yang tidak pernah terjadi.

> [!IMPORTANT]
> Kalau klaim inti tidak punya bukti sendiri, klaim itu turun tingkat menjadi klaim pendukung.
> POV tidak boleh bergantung pada klaim yang tidak punya bukti sendiri.

#### 3b. Sumber Primer Publik

**Sumber primer** adalah dokumen asli yang memuat angka itu pertama kali:

| Jenis | Contoh |
|---|---|
| Laporan keuangan | Laporan tahunan, prospektus, filing IDX |
| Statistik resmi | BPS, Bank Indonesia, OJK |
| Dokumen kebijakan | Peraturan, siaran pers resmi |
| Penelitian asli | Jurnal dengan metodologi yang bisa dibaca |
| Data perusahaan | Halaman investor relations, laporan tahunan |

**Bukan sumber primer:**

- Artikel berita yang mengutip laporan.
- Blog yang merangkum penelitian.
- Utas media sosial.
- Video YouTube lain, termasuk video kreator rujukan.

Kalau hanya menemukan artikel, cari dokumen yang dikutip artikel itu. Kalau tidak ketemu,
tandai "sumber primer belum ditemukan" dan turunkan reliabilitasnya.

#### 3c. Studi Kasus Perusahaan Lain

- Prioritaskan yang bisa ditelusuri publik.
- Catat konteks geografis dan skala bisnis.
- Jangan menyamakan startup Silicon Valley dengan UMKM Indonesia tanpa penjelasan.

#### 3d. Pendapat Ahli

- Atribusi jelas: siapa, kapan, di mana.
- Jangan melepas kutipan dari konteksnya.

#### 3e. Pilih Satu Bukti Pembuka yang Dikenali Penonton

Setelah semua bukti terkumpul, tentukan satu yang akan muncul di 60 detik pertama. Syaratnya bukan
"paling ilmiah", tetapi **bisa dikenali tanpa penjelasan**:

| Layak jadi pembuka | Tidak layak jadi pembuka |
|---|---|
| Klip atau kutipan pejabat, pengumuman lembaga, siaran pers | Jurnal akademik |
| Harga, omzet, atau biaya yang bisa dibandingkan | Angka tanpa pembanding |
| Dokumen yang bisa ditampilkan di layar | Ringkasan artikel yang mengutip dokumen |
| Rekaman lokasi atau layar kerja | Framework atau definisi |

Studi akademik tetap dipakai, tetapi sebagai **penopang argumen di tengah**, bukan pintu masuk.
Kalau satu-satunya bukti yang ada adalah jurnal, itu tanda Tahap 3 belum selesai, bukan tanda
jurnalnya tidak layak.

Yang perlu disiapkan untuk Tahap 4: satu angka spesifik untuk menit pertama, dan satu kalimat yang
menjelaskan apa yang sedang dilihat penonton.

---

### Langkah 4 — Verifikasi Setiap Bukti

- [ ] **Definisi jelas.** "Conversion rate" — dari apa ke apa?
- [ ] **Periode jelas.** Tahun berapa? Kuartal mana?
- [ ] **Sumber bisa ditelusuri.** Ada nama, URL, atau publikasi.
- [ ] **Sumber primer ditemukan.** Kalau tidak, catat bahwa belum.
- [ ] **Konteks geografis dan industri sesuai.**
- [ ] **Tidak ada konflik kepentingan.** Data dari vendor yang menjual solusi perlu dicatat
      biasnya.

> [!WARNING]
> Sumber sekunder sering salah. "70% bisnis gagal dalam 5 tahun" — dari mana, negara mana,
> definisi gagal apa? Selalu cari dokumen aslinya.

---

### Langkah 5 — Pilih Satu Bukti yang Tidak Bisa Ditiru dari Riset

Setiap video harus memuat satu hal yang tidak bisa disalin kreator lain hanya dengan membaca
sumber yang sama. Tanpa itu, video menjadi rangkuman dua jurnal, dan tidak ada alasan menonton
Anda alih-alih membaca sumbernya.

Syarat ini **tidak wajib berupa data historis milik sendiri.** Ada tiga bentuk, pilih salah satu.
Bentuk 1 paling kuat. Bentuk 3 paling longgar, tetapi tetap jujur.

| Jalur | Syarat | Yang ditampilkan di layar |
|---|---|---|
| **1. Catatan sendiri** | Angka dari `content/log-keputusan.md`, spreadsheet, invoice, atau dashboard yang sudah ada. Boleh angka yang merugikan. | Dokumen aslinya |
| **2. Pengukuran untuk video ini** | Ukur satu hal minggu ini. Catat caranya, tampilkan hasilnya, sebut yang tidak berjalan sesuai dugaan. | Hasil ukur dan cara mengukurnya |
| **3. Batas pengalaman** | Sebut terang-terangan apa yang belum pernah Anda jalankan, dan bagian mana yang karena itu dibatasi. | Teks di layar atau ucapan langsung |

Jalur 3 dipakai kalau dua jalur di atas belum tersedia. Contohnya: "Saya belum pernah menjalankan
bisnis dengan 100 karyawan, jadi bagian ini saya batasi pada bisnis dengan tim di bawah 10 orang."

Yang membuat jalur 3 tetap sah: batas itu disebut di dalam video, bukan disembunyikan. Yang membuat
jalur 3 tidak sah: dipakai terus-menerus tanpa pernah naik ke jalur 1 atau 2.

**Kalau memakai jalur 1, angka yang merugikan tetap dianjurkan.** Alex Hormozi menyebutnya "the
whole truth": ceritakan bagian yang merugikan, bukan hanya bagian yang menguntungkan.
*Terverifikasi* dari transkrip di `reference/`.

**Bentuk angka merugikan yang sah:**

- Kerugian yang pernah terjadi, beserta nominalnya.
- Keputusan yang ternyata salah, dan biayanya.
- Perkiraan awal yang meleset dari hasil akhir.
- Hasil pengukuran jalur 2 yang tidak sesuai dugaan.

**Bentuk yang tidak sah:**

- Kegagalan kecil yang dipakai untuk membangun kredibilitas palsu.
- "Saya juga pernah salah" tanpa angka dan tanpa konsekuensi.
- Kerugian yang sebenarnya bukan kerugian.
- Jalur 3 yang dipakai tanpa menyebut batasnya secara eksplisit.

> [!CAUTION]
> Angka yang merugikan tetap tunduk pada audit izin data. Kalau tidak boleh dibuka, ganti dengan
> kerugian lain yang boleh. Jangan mengarang.

---

### Langkah 6 — Aturan Khusus Data Salam Cendekia

**Prosedur wajib:**

1. **Buat daftar data yang dibutuhkan.** Data apa, periode kapan, untuk klaim apa.
2. **Minta izin Fadhil.** Tanyakan: aman dibagikan? Bagian mana yang harus disamarkan? Tim
   internal sudah tahu?
3. **Samarkan jika diizinkan.**
   - Angka spesifik jadi rentang: "Rp127 juta" → "sekitar Rp100–150 juta"
   - Hapus nama klien, tutor, mitra
   - Bulatkan persentase: "37,4%" → "sekitar 35–40%"
   - Hapus detail identifikasi: lokasi, nama produk, jumlah karyawan
   - Ubah timeline jika sensitif
4. **Beri label.** `[PENGALAMAN]` plus catatan internal "data SC — sudah diizinkan dan
   disamarkan".

> [!CAUTION]
> **Jangan pernah membuka tanpa izin:** data keuangan detail, data pelanggan, data tutor atau
> karyawan, informasi kontrak dan harga ke klien, strategi internal yang belum publik.

---

### Langkah 7 — Buat Ilustrasi yang Jujur

1. **Label eksplisit.** "Misalnya", "bayangkan", "ini contoh hipotetis".
2. **Asumsi terbuka.** Jangan sembunyikan asumsi di balik angka.
3. **Angka masuk akal.** Jangan pakai Rp10 miliar untuk menggambarkan UMKM.
4. **Jangan terlalu banyak.** Data nyata harus lebih banyak daripada ilustrasi.
5. **Tandai di fact sheet.** Reliabilitas: *tebakan*.

---

### Langkah 8 — Susun Lembar Fakta

```markdown
# Lembar Fakta — [Judul Video]

**Tanggal riset:** YYYY-MM-DD
**Brief:** [link]

## POV Utama
[satu kalimat]

## Artefak Utama
[angka atau dokumen yang akan terlihat di layar]

## Angka yang Merugikan
[angka atau keputusan yang membuat Fadhil terlihat buruk]

## Klaim Inti

### Klaim 1: [klaim]
- **Bukti:** [angka / fakta]
- **Definisi:** [apa yang diukur]
- **Periode:** [kapan]
- **Sumber:** [nama] — [URL]
- **Primer/Sekunder:** [Primer / Sekunder — kalau sekunder, sumber primernya apa?]
- **Jenis:** [Pengalaman / Data Publik / Ilustrasi]
- **Reliabilitas:** [Terverifikasi ✅ / Simpulan ⚠️ / Tebakan ❓]
- **Catatan:** [keterbatasan, bias]

## Klaim Pendukung
...

## Klaim Konteks
...

## Ilustrasi
### Ilustrasi 1
- **Asumsi:** [...]
- **Tujuan:** [...]

## Sumber yang Tidak Dipakai
[...]

## Catatan Izin Data Internal
- [ ] Data SC yang dipakai: [...]
- [ ] Izin Fadhil: [sudah / belum]
- [ ] Sudah disamarkan: [sudah / belum]
```

---

### Langkah 9 — Berhenti di 90 Menit

Riset bisa memenuhi jam kerja sebanyak apa pun yang disediakan. Batasi.

**Aturan:**

- Total riset per video: **90 menit**.
- Kalau klaim inti belum punya sumber primer setelah 90 menit, **ganti klaimnya**. Jangan
  menambah waktu.
- Kalau seluruh POV bergantung pada klaim yang belum terbukti, kembali ke Tahap 1 dan pilih ide
  lain. Itu keputusan yang benar, bukan kegagalan.

**Pembagian waktu:**

| Pekerjaan | Waktu |
|---|---|
| Baca brief, daftar klaim | 15 menit |
| Kumpulkan artefak sendiri | 20 menit |
| Cari sumber primer | 40 menit |
| Verifikasi dan susun fact sheet | 15 menit |

---

## Alat Bantu Riset

| Alat | Fungsi |
|---|---|
| `content/log-keputusan.md` | Sumber bukti utama |
| BPS (bps.go.id) | Statistik resmi Indonesia |
| IDX / investor relations | Laporan keuangan perusahaan publik |
| Google Scholar | Penelitian asli |
| Wayback Machine | Arsip halaman yang berubah |
| Google Trends | Validasi permintaan, bukan bukti klaim |

> [!NOTE]
> Statista dan laporan konsultan boleh dipakai untuk klaim pendukung. Untuk klaim inti, cari
> dokumen aslinya. Laporan konsultan sering merangkum data pihak lain tanpa menyebut metodologi.

---

## Gerbang Keluaran

- [ ] Lembar fakta tersusun di `content/briefs/`
- [ ] Setiap klaim inti punya sumber **primer**
- [ ] Setiap angka punya definisi, periode, sumber
- [ ] Setiap butir punya label reliabilitas
- [ ] Setiap butir punya label jenis
- [ ] Ada minimal satu artefak yang bisa ditampilkan di layar: dokumen sendiri, hasil pengukuran,
      atau dokumen publik primer
- [ ] Sudah dipilih satu bukti pembuka yang dikenali penonton tanpa penjelasan (Langkah 3e), plus
      satu angka spesifik untuk menit pertama
- [ ] Bukti tidak bisa ditiru dari riset sudah dipilih lewat salah satu dari tiga jalur di Langkah 5
- [ ] Data Salam Cendekia: izin didapat, sudah disamarkan
- [ ] Ilustrasi berlabel dan asumsinya terbuka
- [ ] Riset selesai dalam 90 menit

> [!IMPORTANT]
> Kalau klaim inti tidak bisa didukung sumber primer, jangan paksakan. Ubah klaim menjadi lebih
> tentatif, cari sudut lain, atau tunda video.

---

## Kesalahan Umum

### 1. Menyajikan ilustrasi sebagai data

❌ "Bisnis jasa rata-rata punya margin 40%."
✅ "Misalnya, kalau bisnis jasa punya margin 40% — angka ini ilustrasi..."

### 2. Mengutip artikel, bukan dokumen aslinya

❌ "Menurut artikel di Kompas, 70% startup gagal."
✅ "Data US Bureau of Labor Statistics 2023 menunjukkan 50% bisnis baru di Amerika bertahan
melewati 5 tahun. Konteks: ini data AS, bukan Indonesia."

### 3. Tidak memberi label reliabilitas

Semua fakta dicampur. Saat menulis naskah, penulis tidak tahu mana yang bisa diklaim tegas.

### 4. Membuka data Salam Cendekia tanpa izin

❌ "Di Salam Cendekia, revenue kami naik 45%."
✅ "Di bisnis edukasi yang saya jalankan, pendapatan naik sekitar 40–50%." (diizinkan dan
disamarkan)

### 5. Angka tanpa definisi

❌ "Conversion rate kami 12%."
✅ "Conversion rate dari pengunjung website ke pembelian pertama adalah 12%, Januari–Maret 2025."

### 6. Data dari konteks berbeda tanpa catatan

Data AS dipakai untuk menyimpulkan Indonesia. Selalu catat konteksnya.

### 7. Terlalu banyak ilustrasi

Kalau fact sheet lebih banyak ilustrasi daripada data nyata, video belum siap.

### 8. Riset tanpa batas waktu

Riset yang berjalan berhari-hari adalah cara menunda terbit tanpa terlihat menunda.

---

## Tips

> [!TIP]
> **Mulai dari pengalaman Fadhil.** Bukti terkuat untuk personal brand adalah pengalaman
> langsung. Data publik memperkuat, bukan menggantikan.

> [!TIP]
> **Catat sumber yang tidak dipakai.** Bisa berguna untuk video berikutnya.

> [!TIP]
> **Simpan snapshot.** Untuk sumber penting, simpan di web.archive.org.

---

## Hubungan dengan Tahap Lain

| Tahap | Hubungan |
|---|---|
| **Tahap 1 — Ideasi** | Artefak utama sudah dipilih di sana |
| **Tahap 2 — Pengemasan** | Judul menentukan janji yang harus dibuktikan |
| **Tahap 4 — Naskah** | Fact sheet adalah satu-satunya sumber angka |
| **Tahap 6 — Visual** | Artefak dari fact sheet menjadi visual utama |
| **Tahap 10 — Evaluasi** | Komentar yang mempertanyakan data dicatat untuk riset berikutnya |

---

## Contoh Alur Singkat

**Video:** "Kapan Produk Konten Perlu Ditambah Layanan?"

1. **POV:** menambah layanan pada waktu yang tepat menaikkan LTV tanpa menaikkan biaya akuisisi.
2. **Klaim inti:** menambah layanan menaikkan LTV; timing salah menggerus margin.
3. **Bukti sendiri:** data LTV per murid sebelum dan sesudah layanan tutoring ditambahkan.
4. **Sumber primer publik:** laporan tahunan perusahaan edukasi publik untuk pembanding.
5. **Angka merugikan:** layanan yang ditambahkan terlalu cepat dan menurunkan margin.
6. **Fact sheet** disimpan di `content/briefs/produk-konten-layanan-fakta.md`.
7. **Cek gerbang.** Lulus → Tahap 4.

---

## Rujukan

- [`workflows/produksi/prinsip-editorial.md`](./prinsip-editorial.md) — prinsip #4 dan #7.
- Rubrik terbit, bagian ⭐ **Bukti**.
- [`AGENTS.md`](../../AGENTS.md) — Tahap 3 dan Batas Penggunaan AI.

---

*Terakhir diperbarui: 2 November 2026*
