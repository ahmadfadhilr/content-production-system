#!/usr/bin/env python3
"""
Baca database/database.db, urutkan, cetak.

Urutan: skor_prioritas_konsep lebih dulu, baru skor_total. Alasannya, ide yang
mengajarkan konsep paling dasar harus tampil lebih dulu walaupun skornya lebih
rendah.

Contoh:
  python3 tools/ranking.py                  # ide hidup saja
  python3 tools/ranking.py --semua          # termasuk gugur dan digabung
  python3 tools/ranking.py --detail         # tampilkan rincian empat skor
  python3 tools/ranking.py --pilar=keuangan # hanya pilar keuangan (1/2/3 juga bisa)
"""

import os
import sqlite3
import sys

DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(DIR, "database", "database.db")

URUT = "skor_prioritas_konsep DESC, skor_total DESC, median_tayangan_10_teratas DESC"
PILAR = {"1": "keuangan", "2": "pertumbuhan", "3": "operasional"}


def ambil(semua=False, pilar=None):
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    sql = "SELECT * FROM ide"
    syarat, nilai = [], []
    if not semua:
        syarat.append("status NOT IN ('gugur', 'digabung')")
    if pilar:
        syarat.append("pilar_konten = ?")
        nilai.append(pilar)
    if syarat:
        sql += " WHERE " + " AND ".join(syarat)
    sql += f" ORDER BY {URUT}"
    baris = conn.execute(sql, nilai).fetchall()
    conn.close()
    return baris


def potong(teks, lebar):
    teks = teks or ""
    return teks if len(teks) <= lebar else teks[: lebar - 1] + "…"


def ribuan(nilai):
    return f"{int(nilai or 0):,}".replace(",", ".")


def cetak_ringkas(baris):
    if not baris:
        print("Kosong. Tidak ada ide yang lolos.")
        return
    print(f"{'#':>2}  {'Prioritas':>9}  {'Total':>5}  {'Status':<17}  {'Kode':<9}  Judul kerja")
    print("-" * 118)
    for i, r in enumerate(baris, 1):
        print(
            f"{i:>2}  {r['skor_prioritas_konsep']:>9}  {r['skor_total']:>5}  "
            f"{r['status']:<17}  {r['kode_ide']:<9}  {potong(r['judul_kerja'], 58)}"
        )
    print()
    for s in ("siap", "perlu perbaikan", "ditunda"):
        kumpulan = [r for r in baris if r["status"] == s]
        if kumpulan:
            print(f"{s} ({len(kumpulan)}):")
            for r in kumpulan:
                print(f"  {r['kode_ide']}  {potong(r['judul_kerja'], 60)}")
            print()


def cetak_detail(baris):
    if not baris:
        print("Kosong.")
        return
    print(
        f"{'#':>2}  {'Prior':>5}  {'Total':>5}  {'minta':>5} {'celah':>5} {'bukti':>5} "
        f"{'kapas':>5}  {'Konsep':<28}  {'Median':>9}  Status"
    )
    print("-" * 118)
    for i, r in enumerate(baris, 1):
        print(
            f"{i:>2}  {r['skor_prioritas_konsep']:>5}  {r['skor_total']:>5}  "
            f"{r['skor_permintaan']:>5} {r['skor_celah_pasokan']:>5} {r['skor_bukti']:>5} "
            f"{r['skor_kapasitas']:>5}  {potong(r['konsep_bisnis'], 28):<28}  "
            f"{ribuan(r['median_tayangan_10_teratas']):>9}  {r['status']}"
        )
    print()
    print("minta = skor_permintaan (×2), celah = skor_celah_pasokan (×2).")
    print("Total dihitung database: minta×2 + celah×2 + bukti + kapasitas.")


if __name__ == "__main__":
    semua = "--semua" in sys.argv
    detail = "--detail" in sys.argv
    pilar = None
    for a in sys.argv:
        if a.startswith("--pilar="):
            nilai = a.split("=", 1)[1]
            pilar = PILAR.get(nilai, nilai)
    hasil = ambil(semua=semua, pilar=pilar)
    if detail:
        cetak_detail(hasil)
    else:
        cetak_ringkas(hasil)
