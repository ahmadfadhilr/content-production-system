#!/usr/bin/env python3
"""
Baca database/ide.tsv, urutkan, cetak ranking.

Contoh:
  python3 tools/ranking.py          # ranking ide aktif (tidak Gugur/Digabung)
  python3 tools/ranking.py --semua  # semua ide termasuk gugur
  python3 tools/ranking.py --detail # tampilkan breakdown skor
"""

import csv
import os

DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TSV = os.path.join(DIR, "database", "ide.tsv")


def baca():
    with open(TSV) as f:
        for row in csv.DictReader(f, delimiter="\t"):
            row["total"] = int(row["total"])
            yield row


def ranking(rows, semua=False):
    if not semua:
        rows = [r for r in rows if r["status"] not in ("Gugur", "Digabung")]
    return sorted(rows, key=lambda r: -r["total"])


def cetak_simple(rows):
    if not rows:
        print("Kosong. Tidak ada ide yang lolos.")
        return
    print(f"{'#':>3} | {'Sudut':<58} | {'P':>1} | {'Total':>5} | {'Status':>9}")
    print("-" * 88)
    for i, r in enumerate(rows, 1):
        print(
            f"{i:>3} | {r['sudut'][:56]:<58} | {r['pilar']:>1} | {r['total']:>5} | {r['status']:>9}"
        )
    print()
    siap = [r for r in rows if r["status"] == "Siap"]
    if siap:
        print(f"Siap diproduksi ({len(siap)}):")
        for r in siap:
            print(f"  {r['id']} — {r['sudut'][:50]}")


def cetak_detail(rows):
    if not rows:
        print("Kosong.")
        return
    print(
        f"{'#':>3} | {'Sudut':<50} | {'Pilar':>1} | {'Tot':>3} | {'p':>1} {'g':>1} {'b':>1} {'k':>1} | {'bp':>2} {'bg':>2} | {'Format':>4} | {'Trigger':>12} | {'Status':>9}"
    )
    print("-" * 125)
    for i, r in enumerate(rows, 1):
        print(
            f"{i:>3} | {r['sudut'][:48]:<50} | {r['pilar']:>1} | {r['total']:>3} | "
            f"{r['p']:>1} {r['g']:>1} {r['b']:>1} {r['k']:>1} | "
            f"{r['bp']:>2} {r['bg']:>2} | {r['format']:>4} | {r['trigger']:>12} | {r['status']:>9}"
        )
    print()


if __name__ == "__main__":
    import sys
    semua = "--semua" in sys.argv
    detail = "--detail" in sys.argv
    data = list(baca())
    hasil = ranking(data, semua)
    if detail:
        cetak_detail(hasil)
    else:
        cetak_simple(hasil)