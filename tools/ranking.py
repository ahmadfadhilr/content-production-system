#!/usr/bin/env python3
"""
Baca database/database.db, urutkan, cetak.

Urutan: konsep prioritas lebih dulu, baru skor total. Alasannya, ide yang
mengajarkan hal paling dasar harus tampil lebih dulu walaupun skornya lebih
rendah.

Contoh:
  python3 tools/ranking.py            # ide hidup saja
  python3 tools/ranking.py --semua    # termasuk Gugur dan Digabung
  python3 tools/ranking.py --detail   # tampilkan rincian skor
"""

import os
import sqlite3
import sys

DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(DIR, "database", "database.db")

URUT = "skor_prioritas DESC, total DESC, median_tayangan DESC"


def ambil(semua=False, pilar=None, status=None):
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    sql = "SELECT * FROM ide"
    syarat, nilai = [], []
    if not semua:
        syarat.append("status NOT IN ('Gugur', 'Digabung')")
    if pilar:
        syarat.append("pilar = ?")
        nilai.append(pilar)
    if status:
        syarat.append("status = ?")
        nilai.append(status)
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
    print(f"{'#':>2}  {'Pri':>3}  {'Total':>5}  {'Status':<9}  {'Kode':<9}  Sudut")
    print("-" * 112)
    for i, r in enumerate(baris, 1):
        print(
            f"{i:>2}  {r['skor_prioritas']:>3}  {r['total']:>5}  "
            f"{r['status']:<9}  {r['id']:<9}  {potong(r['sudut'], 64)}"
        )
    print()
    for s in ("Siap", "Perbaiki", "Tunda"):
        kumpulan = [r for r in baris if r["status"] == s]
        if kumpulan:
            print(f"{s} ({len(kumpulan)}):")
            for r in kumpulan:
                print(f"  {r['id']}  {potong(r['sudut'], 60)}")
            print()


def cetak_detail(baris):
    if not baris:
        print("Kosong.")
        return
    print(
        f"{'#':>2}  {'Pri':>3}  {'Tot':>3}  {'perm':>4} {'celah':>5} {'bukti':>5} "
        f"{'kapas':>5}  {'Konsep':<28}  {'Median':>9}  Status"
    )
    print("-" * 108)
    for i, r in enumerate(baris, 1):
        print(
            f"{i:>2}  {r['skor_prioritas']:>3}  {r['total']:>3}  "
            f"{r['skor_permintaan']:>4} {r['skor_celah']:>5} {r['skor_bukti']:>5} "
            f"{r['skor_kapasitas']:>5}  {potong(r['konsep_prioritas'], 28):<28}  "
            f"{ribuan(r['median_tayangan']):>9}  {r['status']}"
        )
    print()
    print("perm = skor permintaan (x2), celah = skor celah (x2).")
    print("Total = (perm x 2) + (celah x 2) + bukti + kapasitas. Maksimum 28.")


if __name__ == "__main__":
    semua = "--semua" in sys.argv
    detail = "--detail" in sys.argv
    pilar = None
    for a in sys.argv:
        if a.startswith("--pilar="):
            pilar = int(a.split("=")[1])
    hasil = ambil(semua=semua, pilar=pilar)
    if detail:
        cetak_detail(hasil)
    else:
        cetak_ringkas(hasil)
