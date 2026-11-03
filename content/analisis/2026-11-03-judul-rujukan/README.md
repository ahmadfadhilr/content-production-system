# Judul Kreator Rujukan — Data 3 November 2026

Enam channel, 178 video, diambil dengan `tools/ambil-daftar-video.py`. Tujuannya satu: menguji
apakah "judul yang memuat angka atau orang pertama lebih menarik klik" punya dasar di data, atau
hanya perasaan.

---

## Batas data ini, baca dulu

| Yang dicari | Bisa didapat? |
|---|---|
| Tayangan per video | Ya, dari halaman channel |
| Median channel | Ya, dari 30 video terakhir |
| **CTR** | **Tidak.** Hanya ada di YouTube Studio pemilik channel |
| **Retensi / AVD** | **Tidak** |
| **Sumber traffic** | **Tidak** |

Jadi yang diukur di sini adalah **tayangan relatif terhadap median channel sendiri**. Itu bukan
CTR. Judul yang menarik klik dan judul yang dibagikan luas sama-sama menghasilkan tayangan tinggi,
dan data ini tidak bisa membedakan keduanya.

Satu lagi: 30 video terakhir bercampur usia. Video baru punya waktu tayang lebih pendek, jadi
kelipatannya bias turun. Angka di bawah adalah *terverifikasi* sebagai hasil hitung; pola yang
ditarik dari situ adalah *simpulan*, bukan sebab-akibat.

---

## Hasil

Median kelipatan tayangan per channel, lalu digabung. "Ya" berarti judul memuat ciri itu.

| Ciri judul | Jumlah | Median kelipatan | Tanpa ciri | Median kelipatan |
|---|---:|---:|---:|---:|
| Ada angka | 44 | **1,25×** | 134 | 0,94× |
| Ada orang pertama ("saya", "aku", "I", "my") | 14 | **1,27×** | 164 | 1,00× |
| Berbentuk pertanyaan | 74 | 1,06× | 104 | 0,93× |

Pembacaan yang jujur:

- **Angka dan orang pertama berasosiasi dengan tayangan lebih tinggi.** Selisihnya sekitar 25–27
  persen di median. Itu cukup besar untuk diperhatikan, dan cukup kecil untuk bukan bukti.
- **Pertanyaan saja hampir tidak membedakan.** "Kenapa..." tanpa angka atau entitas bukan alat.
  Ini konsisten dengan catatan di `02-pengemasan.md` bahwa rasa penasaran tanpa jangkar konkret
  berperforma di bawah median.
- **Contohnya bukan pola, tapi arah.** Di Big A Story, tiga judul dengan angka punya median 2,5×;
  di Raymond, judul dengan angka justru 0,8×. Arahnya tidak konsisten antar channel.

## Lima judul teratas per channel

| Channel | Judul | × |
|---|---|---:|
| Alex Hormozi | Can I Save This Failing Theme Park in 90 Days? | 5,1 |
| Alex Hormozi | How I Would Build a $10M Service Business (If I Had to Start Over) | 4,2 |
| Raymond Chin | Selamat, Purbaya Dipecat. | 3,7 |
| Ferry Irwandi | Memburu Titik Api di Kebakaran Hutan Kalimantan [4K] | 8,2 |
| Moon | Adobe Is Completely F*cked. | 3,3 |
| Big A Story | Bagaimana Como Bisa Membuat Klub di Seluruh Dunia Membutuhkan Como? | 20,7 |
| SepulangSekolah | BAHTERA NABI NUH DITEMUKAN? "100% Buatan Manusia!" | 3,6 |

Yang dimiliki lima teratas dan tidak dimiliki judul kita:

1. **Entitas atau angka yang bisa disebut.** Klub, perusahaan, harga, nominal, tenggat.
2. **Taruhan yang bisa gagal.** "in 90 Days", "kalau harus mulai dari nol".
3. **Pertentangan yang terbaca tanpa konteks.** "Selamat" + "Dipecat".

## Artinya untuk Tahap 1

Judul kerja yang ada sekarang — "Harga Jasa Terlihat Untung, Tetapi Tim Terus Kehabisan Waktu" —
tidak punya satu pun dari tiga hal di atas. Ia menjelaskan topik, bukan menawarkan ketegangan. Itu
sebabnya terasa tidak layak diklik.

Tapi kesimpulannya bukan "tambahkan angka". Kita belum punya angka milik Fadhil, dan mengarang
angka di judul melanggar aturan Tahap 1. Yang bisa dipakai sekarang hanya **jangkar situasi**.
Karena itu judul baru di Tahap 1 memakai situasi yang spesifik dan pertentangan yang terbaca,
bukan angka.

Begitu ada satu angka nyata (harga, jam, jumlah klien), pola berangka ini yang diuji lebih dulu.
Itu pekerjaan 04.1 dan Tahap 2 ulang, bukan pekerjaan hari ini.

---

*Data mentah: `daftar-video-mentah.txt`. Ringkasan terstruktur: `ringkasan.json`.*
