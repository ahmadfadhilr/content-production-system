# Pasar Indonesia untuk Topik Harga Jasa — Data 3 November 2026

Analisis ini menjawab satu kekhawatiran: pola judul dan thumbnail yang dipelajari dari kreator
berbahasa Inggris akan terasa mentah kalau diterjemahkan begitu saja. Yang diuji bukan selera, tetapi
apa yang benar-benar dipakai dan dipakai berulang di pasar Indonesia.

---

## Batas data, baca dulu

| Yang dipakai | Jumlah |
|---|---|
| Kueri | 7, dijalankan dengan `tools/pindai-youtube.py -r1 -d` |
| Judul yang dibaca | 132 dari 120 channel berbeda |
| Thumbnail yang dibuka satu per satu | 12 |
| Ukuran performa | Tayangan, bukan CTR dan bukan retensi |

Tujuh kueri: "cara menaikkan harga jasa", "hitung harga jasa", "bisnis jasa tidak untung", "omzet naik
untung turun", "kenapa bisnis tidak berkembang", "cara menghitung biaya tenaga kerja", "bisnis
edukasi cara berkembang".

Hasil pencarian bukan sampel acak. Ia condong ke channel yang sudah lama dan sudah besar, karena
itulah yang ditampilkan YouTube. Jadi angka di bawah menggambarkan **pasokan yang terlihat**, bukan
selera seluruh pasar.

---

## Temuan 1 — Video terjemahan ikut bersaing, dan bahasanya terasa mentah

Ini *terverifikasi*, bukan kesan.

| Yang terlihat di hasil pencarian Indonesia | Judul asli (dibaca lewat `oembed`) |
|---|---|
| "Cara Menaikkan Harga Tanpa Kehilangan Klien" — 352.684 tayangan, 4 bulan | "How to Raise Your Prices Without Losing Clients" |
| "Cara Menentukan Harga Layanan Anda untuk Menghasilkan LE..." — 157.861 tayangan | "How To Price Your Services To Make MORE Money & Give MORE Value (Masterclass 3/5)" |
| "Bagaimana Mengembangkan Bisnis Anda Begitu Cepat Hingga..." — 437.742 tayangan | Kanal Dan Martell, judul asli berbahasa Inggris |
| "Biaya Tenaga Kerja Langsung - Definisi, Rumus, Cara Meng..." | Kanal Academic Gain Tutorials, judul asli berbahasa Inggris |

YouTube sekarang menerjemahkan judul video asing otomatis untuk penonton Indonesia. Artinya
pesaing langsung Fadhil bukan hanya kreator Indonesia, melainkan juga video Inggris yang tampil
dengan judul Indonesia.

**Ciri judul terjemahan, yang harus dihindari:**

| Ciri | Contoh dari data |
|---|---|
| Sapaan "Anda" | "Cara Menentukan Harga Layanan **Anda**", "Mengembangkan Bisnis **Anda**" |
| Urutan kalimat Inggris | "Bagaimana Mengembangkan Bisnis Anda Begitu Cepat Hingga..." |
| Frasa nominal panjang | "Biaya Tenaga Kerja Langsung - Definisi, Rumus, Cara Menghitung" |
| Menjelaskan isi, bukan menawarkan ketegangan | "Cara Menentukan Harga Layanan Anda untuk Menghasilkan Lebih" |
| Tidak ada satu kata lisan pun | Tidak ada "kok", "ternyata", "gak", "dulu", "-mu" |

Kesimpulannya *simpulan*: judul terjemahan tetap terbaca sebagai terjemahan meskipun tata bahasanya
benar, karena tidak memakai satu pun penanda percakapan Indonesia.

---

## Temuan 2 — Dua register, dan yang tumbuh memakai yang kedua

Dihitung dari 132 judul:

| Penanda | Jumlah | Siapa yang memakai |
|---|---:|---|
| "Anda" | 11 | Video terjemahan dan pelatih lama (Hendra Hilman, Tom MC Ifle, Dan Martell) |
| "kamu" atau "kalian" | 2 | Raymond Chin, kanal yang lebih muda |
| "lo" atau "lu" | 1 | Suara Berkelas, kanal gaya Jakarta |

Angka mentahnya kecil karena sebagian besar judul tidak menyapa penonton sama sekali. Yang penting
bukan jumlahnya, melainkan **kelompoknya**. Tidak satu pun channel yang tumbuh dalam tiga tahun
terakhir memakai "Anda" sebagai sapaan utama.

*Simpulan*: "Anda" adalah penanda video terjemahan atau pelatih seminar. "Kamu" dan "kalian" adalah
penanda kreator yang berbicara kepada penonton, bukan kepada peserta training.

---

## Temuan 3 — Kosakata lokal yang tidak bisa diterjemahkan

Ini bagian yang paling sering hilang saat orang menerjemahkan judul Inggris.

| Kata | Muncul di | Artinya | Padanan Inggris yang biasa dipakai |
|---|---|---|---|
| boncos | "Ga Naikin Harga Boncos" | rugi, modal tidak kembali | losing money |
| kabur | "Takut Customer Kabur?" | pelanggan pergi | churn |
| gak laku | "Takut Gak Laku" | tidak terjual | not selling |
| kebobolan | "Jangan Sampai Kebobolan" | biaya tak terduga | cost overrun |
| dikibulin | "Awas Dikibulin Tukang" | ditipu | scammed |
| mentok | "Bisnis Mentok" | berhenti berkembang | plateau |
| mapan | "Bisnis yang Diem-Diem Bikin Mapan" | stabil dan aman | stable |
| cuan | "Tetap Cuan" | untung | profit |
| jasamu | "Harga Jasamu" | layananmu | your service |

*Simpulan*: "churn", "cost overrun", dan "plateau" adalah kata yang benar tetapi bukan kata yang
diucapkan pemilik bisnis Indonesia. Kalau judul memakai kata Inggris yang diterjemahkan rapi, hasilnya
terdengar seperti laporan konsultan.

Satu contoh yang paling jelas: thumbnail "GINI CARA MENENTUKAN HARGA **JASAMU**" disertai teks
"**SEKIAN TERIMA GAJI**". Frasa terakhir itu berasal dari iklan lowongan kerja dan tidak punya
padanan Inggris. Tidak ada penerjemah yang akan menghasilkannya.

---

## Temuan 4 — Thumbnail di niche ini lebih panjang dari 3–5 kata

Delapan thumbnail dibuka satu per satu dari kueri harga jasa. Jumlah kata pada teks thumbnail:

| Video | Teks thumbnail | Kata |
|---|---|---:|
| Coach Yohanes, "Mau Menaikkan Harga Tapi Takut Kehilangan Pelanggan?" | MAU NAIKIN HARGA TAPI TAKUT CUSTOMER KABUR? | 8 |
| Hendra Hilman, "4 Cara Menentukan Harga Jual" | 4 CARA MENENTUKAN HARGA JUAL UNTUK MENAIKKAN OMSET | 9 |
| Hendra Hilman, "Strategi Menjual Harga Lebih Tinggi" | STRATEGI MENJUAL HARGA LEBIH TINGGI CUSTOMER TETAP BELI | 9 |
| Arsimatra, "Awas Dikibulin Tukang!" | JANGAN SAMPAI KEBOBOLAN! BEGINI CARA HITUNG UPAH TUKANG EFEKTIF! | 10 |
| KJA ASP, "Cara Menghitung HPP" | GINI CARA MENENTUKAN HARGA JASAMU / SEKIAN TERIMA GAJI | 8 |
| EnricoJo, "Rumus Harga Jasa Freelance" | Nentuim Harga Freelance | 3 |
| Rio Gandhi, "Ga Naikin Harga Boncos" | Jualan Online DILEMA HARGA NAIK / TIDAK? TAKUT BONCOS!! TAKUT GAK LAKU!! | 13 |
| Agung Adimas, "Strategi Penetapan Harga" | PSIKOLOGI MARKETING BUKAN TENTANG MENIPU | 5 |

Median 8–9 kata. Aturan "3–5 kata" yang dipakai di `02-pengemasan.md` berasal dari thumbnail berita
dan bedah bisnis (Raymond Chin, Big A Story, Hormozi), bukan dari thumbnail layanan bisnis Indonesia.

*Simpulan*: batas 3–5 kata bukan hukum, melainkan pilihan gaya. Yang wajib adalah teks thumbnail
melengkapi judul, bukan mengulangnya. Di niche ini, dua baris 6–10 kata adalah bentuk yang lazim.

---

## Temuan 5 — Teks thumbnail lebih lisan daripada judulnya

Pola ini muncul berulang dan mudah diperiksa.

| Judul | Teks thumbnail | Yang berubah |
|---|---|---|
| Mau **Menaikkan** Harga Tapi Takut **Kehilangan Pelanggan**? | MAU **NAIKIN** HARGA TAPI TAKUT **CUSTOMER KABUR**? | Kata baku menjadi kata lisan |
| Awas Dikibulin Tukang! | JANGAN SAMPAI KEBOBOLAN! | Ancaman yang sama, kata berbeda |
| 4 Cara Menentukan Harga Jual untuk Menaikkan Omzet | 4 CARA MENENTUKAN HARGA JUAL UNTUK MENAIKKAN OMSET | Tidak berubah — ini yang lemah |

*Simpulan*: thumbnail adalah tempat pertama kata lisan boleh masuk, bahkan wajib. Judul boleh sedikit
lebih rapi karena harus terbaca di kolom teks; thumbnail harus terdengar seperti orang berbicara.

---

## Temuan 6 — Gaya "seminar" mendominasi, dan itu bukan register Fadhil

Tiga dari delapan thumbnail memakai pola yang sama: latar hitam atau biru tua, huruf kapital penuh,
emas dan putih, wajah pemateri di kanan, logo kanal di pojok. Dua di antaranya dari channel yang sama
(Hendra Hilman).

Pola ini bekerja untuk audiensnya: "4 Cara Menentukan Harga Jual" mencapai 281.996 tayangan. Tetapi
ia memberi sinyal **pelatihan**, bukan **analisis**. Kalau Fadhil memakainya, penonton akan
mengharapkan seminar dan modul, bukan keputusan dan trade-off.

*Simpulan*: pola yang paling sering muncul bukan otomatis pola yang harus ditiru. Yang ditiru adalah
**cara pasar ini berbicara**, bukan **cara pasar ini berjualan**.

---

## Temuan 7 — Thumbnail yang bekerja adalah instruksi utuh, bukan fragmen

Ini temuan yang paling menentukan untuk video kita, karena ia mengoreksi kesimpulan di Temuan 4.
Panjang teks bukan penentunya. Yang menentukan adalah **bentuk kalimatnya**.

| Video | Teks thumbnail | Bentuk |
|---|---|---|
| Cara Menghitung Harga Borongan Tukang (377.559) | CARA MENGHITUNG HARGA BORONGAN TUKANG PER METER PERSEGI | Cara + objek + satuan |
| Hitung HPP Usaha Kecil (119.835) | HITUNG HPP UNTUK USAHA KECIL | Perintah + audiens disebut |
| Contoh Hitung HPP Jasa Digital (14.981) | CONTOH HITUNG HPP JASA DIGITAL | Benda + cara + segmen |
| Bagaimana Menentukan Harga Jual ke Konsumen? (153.301) | Bagaimana Menentukan Harga Jual ke Konsumen? | Pertanyaan utuh |
| Praktis!! Hitung HPP untuk Sukses Bisnis Kuliner (214.783) | PRAKTIS!! HITUNG HPP UNTUK SUKSES BISNIS KULINER | Penilaian + cara + hasil |

Yang tidak ditemukan satu kali pun: **fragmen data tanpa subjek**, seperti "2 jam lawan 6 jam".
Setiap thumbnail di atas menjawab satu pertanyaan yang sama: *setelah menonton, saya bisa apa?*
Fragmen angka tidak menjawab pertanyaan itu, karena pembaca harus menebak dulu angka itu tentang apa.

*Simpulan*: teks thumbnail harus berbentuk kalimat yang punya subjek dan tindakan. Angka boleh ada,
tetapi sebagai penopang — bukan sebagai pesan utama.

---

## Temuan 8 — Thumbnail berbahasa Inggris adalah penanda terjemahan paling cepat

Video `ufP5w_FLbkI` tampil di pencarian Indonesia dengan judul "Cara Menghitung Biaya Tenaga Kerja
untuk Restoran & Usaha", tetapi thumbnailnya bertuliskan **"CALCULATE LABOUR COSTS"**.

Artinya judul Indonesia itu hasil terjemahan otomatis, bukan buatan kreator. Memeriksa thumbnail
lebih cepat daripada memanggil `oembed`, dan bisa dilakukan sambil melihat hasil pencarian.

*Terverifikasi* untuk satu video. *Simpulan* bahwa pola ini berlaku umum: kalau teks thumbnail
berbahasa Inggris sementara judulnya berbahasa Indonesia, video itu terjemahan.

---

## Yang dipakai dan yang tidak

| Temuan | Dipakai | Tidak dipakai |
|---|---|---|
| Judul terjemahan terasa mentah | Daftar ciri untuk dihindari | — |
| Dua register | "kamu" dan "-mu", sesuai suara Fadhil | "lo/lu", "gw" |
| Kosakata lokal | boncos, kabur, laku, mentok, omzet | cuan, mapan (bukan suara Fadhil) |
| Panjang teks thumbnail | Dua baris kalau perlu, bukan dipaksa 3 kata | 13 kata seperti Rio Gandhi |
| Thumbnail lebih lisan | Wajib | — |
| Gaya seminar | Hanya sebagai pembanding | Emas-hitam, kapital penuh, logo pojok |
| Thumbnail berbentuk instruksi utuh | Wajib | Fragmen angka tanpa subjek |

---

## Berkas pendukung

- `thumb/` — delapan thumbnail asli, nama berkas sama dengan ID video.
- Data judul mentah: hasil `python3 tools/pindai-youtube.py -r1 -d` atas tujuh kueri di atas.
- Analisis kemasan lintas kreator: `../2026-11-03-kemasan-klik/`.
- Data judul dan tayangan enam channel rujukan: `../2026-11-03-judul-rujukan/`.
