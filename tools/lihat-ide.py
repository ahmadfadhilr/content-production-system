#!/usr/bin/env python3
"""
Baca satu ide lengkap dengan label, atau daftar ide yang masih hidup.

Contoh:
  python3 tools/lihat-ide.py                 # daftar ide hidup, urut prioritas
  python3 tools/lihat-ide.py IDEA-009        # kartu lengkap satu ide
  python3 tools/lihat-ide.py --semua         # daftar termasuk yang gugur/digabung
"""

import os
import sqlite3
import sys
import textwrap

DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(DIR, "database", "database.db")

LEBAR = 78
LABEL = 20


def sambung():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


def angka(nilai):
    if nilai is None:
        return "—"
    return f"{int(nilai):,}".replace(",", ".")


def baris(label, nilai):
    teks = "—" if nilai in (None, "") else str(nilai)
    potongan = textwrap.wrap(teks, width=LEBAR - LABEL) or [""]
    print(f"{label:<{LABEL}}{potongan[0]}")
    for lanjutan in potongan[1:]:
        print(" " * LABEL + lanjutan)


def kartu(ide):
    print(f"{ide['kode_ide']} · {ide['status']}")
    print(ide["judul_kerja"])
    print()

    baris("Konsep bisnis", ide["konsep_bisnis"])
    baris("Prioritas konsep", f"{ide['skor_prioritas_konsep']} dari 5")
    baris("Skor total", f"{ide['skor_total']} dari 30")
    print(
        f"{'':<{LABEL}}permintaan {ide['skor_permintaan']}×2"
        f" + celah {ide['skor_celah_pasokan']}×2"
        f" + bukti {ide['skor_bukti']}"
        f" + kapasitas {ide['skor_kapasitas']}"
    )
    baris("Pilar konten", ide["pilar_konten"])
    baris("Format konten", ide["format_konten"])
    print()

    baris("Situasi audiens", ide["situasi_audiens"])
    baris("Masalah utama", ide["masalah_utama"])
    baris("Kedalaman bisnis", ide["kedalaman_bisnis"])
    print()

    baris("Median tayangan", f"{angka(ide['median_tayangan_10_teratas'])} (10 hasil teratas)")
    catatan_celah = " (tidak ada celah)" if ide["skor_celah_pasokan"] == 0 else ""
    baris("Celah pasokan", f"{ide['celah_pasokan']} — skor {ide['skor_celah_pasokan']} dari 5{catatan_celah}")
    baris("Jenis bukti", f"{ide['jenis_bukti']} — skor {ide['skor_bukti']} dari 5")
    hari = ide["perkiraan_hari_kerja"]
    baris("Perkiraan kerja", f"{hari} hari kerja" if hari is not None else "—")
    baris("Asal ide", ide["asal_ide"])
    baris("Berkas pindai", ide["berkas_pindai"])
    baris("Kode rujukan", ide["kode_rujukan"])
    print()

    baris("Alasan keputusan", ide["alasan_keputusan"])
    baris("Tanggal masuk", ide["tanggal_masuk"])


def daftar(semua):
    conn = sambung()
    if semua:
        sql = """SELECT kode_ide, status, skor_total, judul_kerja FROM ide
                 ORDER BY skor_prioritas_konsep DESC, skor_total DESC,
                          median_tayangan_10_teratas DESC"""
        judul = "Semua ide"
    else:
        sql = "SELECT kode_ide, status, skor_total, judul_kerja FROM papan_ide"
        judul = "Ide hidup"
    baris_ide = conn.execute(sql).fetchall()
    conn.close()

    print(f"{judul} ({len(baris_ide)})")
    print(f"{'Kode':<10}{'Status':<17}{'Total':>5}  Judul kerja")
    print("-" * LEBAR)
    for r in baris_ide:
        print(f"{r['kode_ide']:<10}{r['status']:<17}{r['skor_total']:>5}  {r['judul_kerja']}")


def main():
    if len(sys.argv) == 1:
        daftar(semua=False)
        return 0

    arg = sys.argv[1]
    if arg == "--semua":
        daftar(semua=True)
        return 0

    conn = sambung()
    ide = conn.execute("SELECT * FROM ide WHERE kode_ide = ?", (arg.upper(),)).fetchone()
    conn.close()
    if ide is None:
        print(f"Kode {arg} tidak ada. Daftar kode: python3 tools/lihat-ide.py --semua")
        return 1

    kartu(ide)
    return 0


if __name__ == "__main__":
    sys.exit(main())
