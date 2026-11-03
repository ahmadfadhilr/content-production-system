#!/usr/bin/env python3
"""
Tambah ide baru ke database/database.db. Tidak pernah menimpa baris lama.

Masukan berupa satu berkas JSON berisi daftar ide. Satu hasil pindai biasanya
menghasilkan banyak ide sekaligus, jadi bentuknya daftar.

Contoh:
  python3 tools/tambah-ide.py content/pindai/ide-baru.json
  cat ide.json | python3 tools/tambah-ide.py -

Isi minimal satu ide (nama kunci = nama kolom):

  {
    "judul_kerja": "Judul sementara, bukan judul final",
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
    "konsep_bisnis": "Penetapan harga",
    "skor_prioritas_konsep": 5,
    "status": "siap"
  }

Opsional: perkiraan_hari_kerja, kode_rujukan, alasan_keputusan, masalah_utama.
Dibuat otomatis: kode_ide, skor_total, tanggal_masuk.

Nilai yang diterima:
  pilar_konten   keuangan | pertumbuhan | operasional
  format_konten  Decision Notes | Operating Playbook
  celah_pasokan  lebar | sedang | sempit
  jenis_bukti    data sendiri | riset primer | tanpa sumber primer
  status         siap | perlu perbaikan | ditunda | gugur | digabung
"""

import json
import os
import sqlite3
import sys
from datetime import date

DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(DIR, "database", "database.db")

WAJIB = [
    "judul_kerja", "situasi_audiens", "kedalaman_bisnis", "pilar_konten", "format_konten",
    "asal_ide", "berkas_pindai", "median_tayangan_10_teratas", "celah_pasokan", "jenis_bukti",
    "skor_permintaan", "skor_celah_pasokan", "skor_bukti", "skor_kapasitas",
    "konsep_bisnis", "skor_prioritas_konsep", "status",
]
OPSIONAL = ["masalah_utama", "perkiraan_hari_kerja", "kode_rujukan", "alasan_keputusan"]
DIBUAT_DATABASE = {"kode_ide", "skor_total", "tanggal_masuk"}

PILAR = {"keuangan", "pertumbuhan", "operasional"}
FORMAT = {"Decision Notes", "Operating Playbook"}
CELAH = {"lebar", "sedang", "sempit"}
BUKTI = {"data sendiri", "riset primer", "tanpa sumber primer"}
STATUS = {"siap", "perlu perbaikan", "ditunda", "gugur", "digabung"}

SKOR = {
    "skor_permintaan": (1, 5),
    "skor_celah_pasokan": (0, 5),
    "skor_bukti": (1, 5),
    "skor_kapasitas": (1, 5),
    "skor_prioritas_konsep": (1, 5),
}


def periksa(ide, nomor):
    tak_dikenal = set(ide) - set(WAJIB) - set(OPSIONAL) - DIBUAT_DATABASE
    if tak_dikenal:
        raise ValueError(
            f"ide ke-{nomor}: kolom tidak dikenal {', '.join(sorted(tak_dikenal))}. "
            f"Lihat daftar kunci di docstring skrip ini."
        )
    dipakai = [k for k in DIBUAT_DATABASE if k in ide]
    if dipakai:
        raise ValueError(
            f"ide ke-{nomor}: {', '.join(sorted(dipakai))} dibuat otomatis, jangan diisi."
        )
    kurang = [k for k in WAJIB if k not in ide or ide[k] in (None, "")]
    if kurang:
        raise ValueError(f"ide ke-{nomor}: kolom wajib kosong {', '.join(kurang)}")

    if ide["pilar_konten"] not in PILAR:
        raise ValueError(
            f"ide ke-{nomor}: pilar_konten harus salah satu dari {', '.join(sorted(PILAR))}"
        )
    if ide["format_konten"] not in FORMAT:
        raise ValueError(
            f"ide ke-{nomor}: format_konten harus salah satu dari {', '.join(sorted(FORMAT))}"
        )
    if ide["celah_pasokan"] not in CELAH:
        raise ValueError(
            f"ide ke-{nomor}: celah_pasokan harus salah satu dari {', '.join(sorted(CELAH))}"
        )
    if ide["jenis_bukti"] not in BUKTI:
        raise ValueError(
            f"ide ke-{nomor}: jenis_bukti harus salah satu dari {', '.join(sorted(BUKTI))}"
        )
    if ide["status"] not in STATUS:
        raise ValueError(
            f"ide ke-{nomor}: status harus salah satu dari {', '.join(sorted(STATUS))}"
        )
    for nama, (bawah, atas) in SKOR.items():
        if not bawah <= int(ide[nama]) <= atas:
            raise ValueError(f"ide ke-{nomor}: {nama} harus {bawah} sampai {atas}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1

    sumber = sys.argv[1]
    teks = sys.stdin.read() if sumber == "-" else open(sumber).read()
    daftar = json.loads(teks)
    if isinstance(daftar, dict):
        daftar = [daftar]

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    nomor_akhir = conn.execute(
        "SELECT COALESCE(MAX(CAST(SUBSTR(kode_ide, 6) AS INTEGER)), 0) FROM ide"
    ).fetchone()[0]

    ditambah, dilewati = 0, []
    for i, ide in enumerate(daftar, 1):
        periksa(ide, i)
        kembar = conn.execute(
            "SELECT kode_ide FROM ide WHERE LOWER(TRIM(judul_kerja)) = LOWER(TRIM(?))",
            (ide["judul_kerja"],),
        ).fetchone()
        if kembar:
            dilewati.append(f"{ide['judul_kerja']} (sudah ada sebagai {kembar['kode_ide']})")
            continue

        nomor_akhir += 1
        kode = f"IDEA-{nomor_akhir:03d}"
        conn.execute(
            """INSERT INTO ide (
                   kode_ide, judul_kerja, status,
                   konsep_bisnis, skor_prioritas_konsep, pilar_konten, format_konten,
                   situasi_audiens, masalah_utama, kedalaman_bisnis,
                   median_tayangan_10_teratas, celah_pasokan, jenis_bukti,
                   skor_permintaan, skor_celah_pasokan, skor_bukti, skor_kapasitas,
                   perkiraan_hari_kerja, asal_ide, berkas_pindai, kode_rujukan,
                   alasan_keputusan, tanggal_masuk
               ) VALUES (
                   :kode_ide, :judul_kerja, :status,
                   :konsep_bisnis, :skor_prioritas_konsep, :pilar_konten, :format_konten,
                   :situasi_audiens, :masalah_utama, :kedalaman_bisnis,
                   :median_tayangan_10_teratas, :celah_pasokan, :jenis_bukti,
                   :skor_permintaan, :skor_celah_pasokan, :skor_bukti, :skor_kapasitas,
                   :perkiraan_hari_kerja, :asal_ide, :berkas_pindai, :kode_rujukan,
                   :alasan_keputusan, :tanggal_masuk
               )""",
            {
                "kode_ide": kode,
                "judul_kerja": ide["judul_kerja"].strip(),
                "status": ide["status"],
                "konsep_bisnis": ide["konsep_bisnis"].strip(),
                "skor_prioritas_konsep": int(ide["skor_prioritas_konsep"]),
                "pilar_konten": ide["pilar_konten"],
                "format_konten": ide["format_konten"],
                "situasi_audiens": ide["situasi_audiens"].strip(),
                "masalah_utama": (ide.get("masalah_utama") or "").strip(),
                "kedalaman_bisnis": ide["kedalaman_bisnis"].strip(),
                "median_tayangan_10_teratas": int(ide["median_tayangan_10_teratas"]),
                "celah_pasokan": ide["celah_pasokan"],
                "jenis_bukti": ide["jenis_bukti"],
                "skor_permintaan": int(ide["skor_permintaan"]),
                "skor_celah_pasokan": int(ide["skor_celah_pasokan"]),
                "skor_bukti": int(ide["skor_bukti"]),
                "skor_kapasitas": int(ide["skor_kapasitas"]),
                "perkiraan_hari_kerja": ide.get("perkiraan_hari_kerja"),
                "asal_ide": ide["asal_ide"],
                "berkas_pindai": ide["berkas_pindai"],
                "kode_rujukan": (ide.get("kode_rujukan") or "").strip(),
                "alasan_keputusan": (ide.get("alasan_keputusan") or "").strip(),
                "tanggal_masuk": date.today().isoformat(),
            },
        )
        total = conn.execute(
            "SELECT skor_total FROM ide WHERE kode_ide = ?", (kode,)
        ).fetchone()[0]
        print(f"ditambah: {kode} (skor total {total}) — {ide['judul_kerja'].strip()}")
        ditambah += 1

    conn.commit()
    print(f"selesai: {ditambah} ide ditambah")
    for s in dilewati:
        print(f"dilewati: {s}")
    conn.close()
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, json.JSONDecodeError, OSError) as masalah:
        print(f"gagal: {masalah}")
        sys.exit(1)
