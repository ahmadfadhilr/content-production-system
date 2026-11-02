-- Skema database ide konten.
-- Jalankan sekali: sqlite3 database/database.db < database/skema.sql
-- Setiap kolom diberi nama biasa supaya bisa dibaca tanpa membuka dokumentasi.

CREATE TABLE IF NOT EXISTS ide (
    id                TEXT PRIMARY KEY,  -- IDEA-001, IDEA-002, ...
    sudut             TEXT NOT NULL,     -- judul kerja, satu kalimat
    pilar             INTEGER NOT NULL,  -- 1 keuangan, 2 pertumbuhan, 3 operasional
    format            TEXT NOT NULL,     -- DN (Decision Notes) atau OP (Operating Playbook)

    sumber_ide        TEXT NOT NULL,     -- dari mana ide ini datang
    pindai            TEXT NOT NULL,     -- nama berkas hasil pindai
    masalah           TEXT,              -- satu kalimat: siapa, apa, akibatnya

    median_tayangan   INTEGER,           -- median 10 hasil teratas, tiga putaran
    celah             TEXT,              -- Kosong, Dangkal, Dalam
    jenis_bukti       TEXT,              -- A data sendiri, B riset primer, C opini
    rujukan           TEXT,              -- kode sumber, dipisah titik koma
    hari_produksi     INTEGER,           -- perkiraan hari kerja untuk memproduksi

    skor_permintaan   INTEGER NOT NULL,  -- 1-5, dari median tayangan
    skor_celah        INTEGER NOT NULL,  -- 1-5, dari kelas celah
    skor_bukti        INTEGER NOT NULL,  -- 1-5, dari jenis bukti
    skor_kapasitas    INTEGER NOT NULL,  -- 1-5, dari hari produksi

    konsep_prioritas  TEXT,              -- nama konsep bisnis yang dibahas
    skor_prioritas    INTEGER NOT NULL,  -- 1-5, fatal atau tidak kalau audiens salah paham

    total             INTEGER NOT NULL,  -- (permintaan x 2) + (celah x 2) + bukti + kapasitas
    status            TEXT NOT NULL,     -- Siap, Perbaiki, Tunda, Gugur, Digabung
    alasan            TEXT,              -- satu kalimat keputusan
    dibuat            TEXT NOT NULL      -- tanggal masuk database, YYYY-MM-DD
);

-- Tampilan baca: semua kolom panjang digabung supaya muat di layar lebar.
DROP VIEW IF EXISTS ide_ringkas;
CREATE VIEW ide_ringkas AS
SELECT
    id,
    total,
    skor_prioritas                        AS pri,
    konsep_prioritas                      AS konsep,
    sudut,
    pilar                                 AS pil,
    format                                AS fmt,
    status,
    median_tayangan                       AS median,
    celah,
    jenis_bukti                           AS bukti
FROM ide
ORDER BY skor_prioritas DESC, total DESC;
