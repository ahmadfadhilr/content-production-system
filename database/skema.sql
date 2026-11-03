-- Skema database ide konten.
-- Satu tabel: ide. Satu baris = satu calon video.
--
-- Membuat dari kosong:
--   sqlite3 database/database.db < database/skema.sql
--
-- Aturan penamaan yang dipakai di sini:
--   1. Nama kolom memakai bahasa Indonesia biasa, bukan singkatan.
--   2. Nama menyebut isi dan satuannya: skor 1-5, hari kerja, tayangan.
--   3. Nilai pilihan disimpan sebagai kata yang bisa dibaca, bukan angka atau kode.
--      Contoh: 'keuangan', bukan 1. 'lebar', bukan 'Kosong'.
--   4. Satu konsep, satu nama. View tidak mengganti nama kolom jadi lebih pendek.
--   5. Kolom turunan dihitung database, bukan diisi tangan.

CREATE TABLE IF NOT EXISTS ide (
    -- Identitas dan keputusan
    kode_ide                    TEXT PRIMARY KEY,  -- IDEA-001
    judul_kerja                 TEXT NOT NULL,     -- judul sementara, bukan judul final video
    status                      TEXT NOT NULL,     -- siap | perlu perbaikan | ditunda | gugur | digabung
    skor_total                  INTEGER GENERATED ALWAYS AS (
                                    skor_permintaan * 2
                                    + skor_celah_pasokan * 2
                                    + skor_bukti
                                    + skor_kapasitas
                                ) VIRTUAL,         -- dihitung otomatis, jangan diisi

    -- Konsep dan isi konten
    konsep_bisnis               TEXT NOT NULL,     -- konsep yang diajarkan, mis. "Penetapan harga"
    skor_prioritas_konsep       INTEGER NOT NULL,  -- 1-5: seberapa fatal kalau konsep ini salah dipahami
    pilar_konten                TEXT NOT NULL,     -- keuangan | pertumbuhan | operasional
    format_konten               TEXT NOT NULL,     -- Decision Notes | Operating Playbook

    -- Tiga lapisan isi, dari yang paling mudah dikenali ke yang paling dalam
    situasi_audiens             TEXT NOT NULL,     -- lapisan 1 (SOP: pintu masuk)
    masalah_utama               TEXT,              -- lapisan 2: siapa, mengalami apa, akibatnya
    kedalaman_bisnis            TEXT NOT NULL,     -- lapisan 3 (SOP: ketegangan lanjut)

    -- Bukti dan asal ide
    median_tayangan_10_teratas  INTEGER,           -- median 10 hasil teratas, tiga putaran
    celah_pasokan               TEXT,              -- lebar | sedang | sempit
    jenis_bukti                 TEXT,              -- data sendiri | riset primer | tanpa sumber primer
    skor_permintaan             INTEGER NOT NULL,  -- 1-5: dari median tayangan
    skor_celah_pasokan          INTEGER NOT NULL,  -- 0-5: dari celah_pasokan; 0 = tidak ada celah
    skor_bukti                  INTEGER NOT NULL,  -- 1-5: dari jenis_bukti
    skor_kapasitas              INTEGER NOT NULL,  -- 1-5: dari perkiraan hari kerja
    perkiraan_hari_kerja        INTEGER,           -- hari kerja untuk memproduksi
    asal_ide                    TEXT NOT NULL,     -- pindai-gap, pindai-demand, audiens, pengalaman, ...
    berkas_pindai               TEXT NOT NULL,     -- nama berkas hasil pindai
    kode_rujukan                TEXT,              -- kode sitasi, dipisah titik koma

    -- Catatan
    alasan_keputusan            TEXT,              -- satu kalimat
    tanggal_masuk               TEXT NOT NULL,     -- YYYY-MM-DD

    CHECK (status IN ('siap', 'perlu perbaikan', 'ditunda', 'gugur', 'digabung')),
    CHECK (pilar_konten IN ('keuangan', 'pertumbuhan', 'operasional')),
    CHECK (format_konten IN ('Decision Notes', 'Operating Playbook')),
    CHECK (celah_pasokan IS NULL OR celah_pasokan IN ('lebar', 'sedang', 'sempit')),
    CHECK (jenis_bukti IS NULL OR jenis_bukti IN ('data sendiri', 'riset primer', 'tanpa sumber primer')),
    CHECK (skor_prioritas_konsep BETWEEN 1 AND 5),
    CHECK (skor_permintaan BETWEEN 1 AND 5),
    CHECK (skor_celah_pasokan BETWEEN 0 AND 5),
    CHECK (skor_bukti BETWEEN 1 AND 5),
    CHECK (skor_kapasitas BETWEEN 1 AND 5)
);

-- Papan baca: hanya ide yang masih hidup, hanya kolom pendek, sudah diurutkan.
-- Untuk membaca satu ide lengkap: python3 tools/lihat-ide.py IDEA-001
DROP VIEW IF EXISTS ide_ringkas;
DROP VIEW IF EXISTS papan_ide;
CREATE VIEW papan_ide AS
SELECT
    kode_ide,
    status,
    skor_total,
    skor_prioritas_konsep,
    judul_kerja,
    konsep_bisnis,
    pilar_konten,
    format_konten,
    median_tayangan_10_teratas,
    celah_pasokan,
    jenis_bukti
FROM ide
WHERE status NOT IN ('gugur', 'digabung')
ORDER BY skor_prioritas_konsep DESC, skor_total DESC, median_tayangan_10_teratas DESC;
