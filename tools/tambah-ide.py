#!/usr/bin/env python3
"""
Tambah ide baru ke database/database.db. Tidak pernah menimpa baris lama.

Masukan berupa satu berkas JSON berisi daftar ide. Satu hasil pindai biasanya
menghasilkan banyak ide sekaligus, jadi bentuknya daftar.

Contoh:
  python3 tools/tambah-ide.py content/pindai/ide-baru.json
  cat ide.json | python3 tools/tambah-ide.py -

Setiap ide wajib punya: sudut, pilar, format, sumber_ide, pindai, median_tayangan,
celah, jenis_bukti, skor_permintaan, skor_celah, skor_bukti, skor_kapasitas,
konsep_prioritas, skor_prioritas, status.
Opsional: masalah, rujukan, hari_produksi, alasan.
"""

import json
import os
import sqlite3
import sys
from datetime import date

DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(DIR, "database", "database.db")

WAJIB = [
    "sudut", "pilar", "format", "sumber_ide", "pindai", "median_tayangan",
    "celah", "jenis_bukti", "skor_permintaan", "skor_celah", "skor_bukti",
    "skor_kapasitas", "konsep_prioritas", "skor_prioritas", "status",
]
PILAR = {1, 2, 3}
FORMAT = {"DN", "OP"}
CELAH = {"Kosong", "Dangkal", "Dalam"}
BUKTI = {"A", "B", "C"}
STATUS = {"Siap", "Perbaiki", "Tunda", "Gugur", "Digabung"}


def periksa(ide, nomor):
    kurang = [k for k in WAJIB if k not in ide or ide[k] in (None, "")]
    if kurang:
        raise ValueError(f"ide ke-{nomor}: kolom kosong {', '.join(kurang)}")
    if ide["pilar"] not in PILAR:
        raise ValueError(f"ide ke-{nomor}: pilar harus 1, 2, atau 3")
    if ide["format"] not in FORMAT:
        raise ValueError(f"ide ke-{nomor}: format harus DN atau OP")
    if ide["celah"] not in CELAH:
        raise ValueError(f"ide ke-{nomor}: celah harus Kosong, Dangkal, atau Dalam")
    if ide["jenis_bukti"] not in BUKTI:
        raise ValueError(f"ide ke-{nomor}: jenis_bukti harus A, B, atau C")
    if ide["status"] not in STATUS:
        raise ValueError(f"ide ke-{nomor}: status harus {', '.join(sorted(STATUS))}")
    for k in ("skor_permintaan", "skor_celah", "skor_bukti", "skor_kapasitas", "skor_prioritas"):
        if not 1 <= int(ide[k]) <= 5:
            raise ValueError(f"ide ke-{nomor}: {k} harus 1 sampai 5")


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
        "SELECT COALESCE(MAX(CAST(SUBSTR(id, 6) AS INTEGER)), 0) FROM ide"
    ).fetchone()[0]

    ditambah, dilewati = 0, []
    for i, ide in enumerate(daftar, 1):
        periksa(ide, i)
        kembar = conn.execute(
            "SELECT id FROM ide WHERE LOWER(TRIM(sudut)) = LOWER(TRIM(?))", (ide["sudut"],)
        ).fetchone()
        if kembar:
            dilewati.append(f"{ide['sudut']} (sudah ada sebagai {kembar['id']})")
            continue

        nomor_akhir += 1
        total = (
            int(ide["skor_permintaan"]) * 2
            + int(ide["skor_celah"]) * 2
            + int(ide["skor_bukti"])
            + int(ide["skor_kapasitas"])
        )
        conn.execute(
            """INSERT INTO ide (
                   id, sudut, pilar, format, sumber_ide, pindai, masalah,
                   median_tayangan, celah, jenis_bukti, rujukan, hari_produksi,
                   skor_permintaan, skor_celah, skor_bukti, skor_kapasitas,
                   konsep_prioritas, skor_prioritas, total, status, alasan, dibuat
               ) VALUES (
                   :id, :sudut, :pilar, :format, :sumber_ide, :pindai, :masalah,
                   :median_tayangan, :celah, :jenis_bukti, :rujukan, :hari_produksi,
                   :skor_permintaan, :skor_celah, :skor_bukti, :skor_kapasitas,
                   :konsep_prioritas, :skor_prioritas, :total, :status, :alasan, :dibuat
               )""",
            {
                "id": f"IDEA-{nomor_akhir:03d}",
                "sudut": ide["sudut"].strip(),
                "pilar": int(ide["pilar"]),
                "format": ide["format"],
                "sumber_ide": ide["sumber_ide"],
                "pindai": ide["pindai"],
                "masalah": ide.get("masalah", ""),
                "median_tayangan": int(ide["median_tayangan"]),
                "celah": ide["celah"],
                "jenis_bukti": ide["jenis_bukti"],
                "rujukan": ide.get("rujukan", ""),
                "hari_produksi": ide.get("hari_produksi"),
                "skor_permintaan": int(ide["skor_permintaan"]),
                "skor_celah": int(ide["skor_celah"]),
                "skor_bukti": int(ide["skor_bukti"]),
                "skor_kapasitas": int(ide["skor_kapasitas"]),
                "konsep_prioritas": ide["konsep_prioritas"],
                "skor_prioritas": int(ide["skor_prioritas"]),
                "total": total,
                "status": ide["status"],
                "alasan": ide.get("alasan", ""),
                "dibuat": date.today().isoformat(),
            },
        )
        ditambah += 1

    conn.commit()
    print(f"ditambah: {ditambah}")
    for s in dilewati:
        print(f"dilewati: {s}")
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
