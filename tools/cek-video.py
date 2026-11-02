#!/usr/bin/env python3
"""Periksa kedalaman satu video YouTube tanpa menonton: deskripsi dan chapter.

Pakai:
    python3 tools/cek-video.py VIDEO_ID [VIDEO_ID ...]
    python3 tools/cek-video.py https://youtu.be/VIDEO_ID

Keluaran: judul, kanal, durasi, daftar chapter, dan 1.500 karakter pertama deskripsi.

Ini bukan pengganti menonton. Chapter dan deskripsi menunjukkan apakah video
menjanjikan angka, kerangka, atau hanya pengantar. Kalau tidak ada chapter dan
deskripsinya hanya kalimat promosi, kemungkinan besar isinya dangkal. Itu
simpulan, bukan hasil menonton.
"""

import json
import re
import subprocess
import sys

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"


def id_dari(arg):
    m = re.search(r"(?:v=|youtu\.be/|shorts/|embed/)([A-Za-z0-9_-]{11})", arg)
    return m.group(1) if m else arg


def ambil(vid):
    url = f"https://www.youtube.com/watch?v={vid}&hl=id&gl=ID"
    html = subprocess.run(
        ["curl", "-sL", "-A", UA, url], capture_output=True, text=True
    ).stdout
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", html, re.S)
    if not m:
        return None
    return json.loads(m.group(1))


def cari_kunci(o, kunci, hasil):
    if isinstance(o, dict):
        if kunci in o:
            hasil.append(o[kunci])
        for v in o.values():
            cari_kunci(v, kunci, hasil)
    elif isinstance(o, list):
        for v in o:
            cari_kunci(v, kunci, hasil)


def teks_dari(o):
    if isinstance(o, str):
        return o
    if isinstance(o, dict):
        if "simpleText" in o:
            return o["simpleText"]
        if "runs" in o:
            return "".join(r.get("text", "") for r in o["runs"])
        if "content" in o:
            return o["content"]
    return ""


def main(ids):
    for arg in ids:
        vid = id_dari(arg)
        data = ambil(vid)
        print("\n" + "=" * 72)
        print(f"https://youtu.be/{vid}")
        if not data:
            print("  gagal membaca halaman")
            continue

        judul, kanal, durasi = [], [], []
        cari_kunci(data, "videoPrimaryInfoRenderer", judul)
        cari_kunci(data, "videoOwnerRenderer", kanal)
        cari_kunci(data, "lengthText", durasi)

        if judul:
            print("  JUDUL :", teks_dari(judul[0].get("title", {})))
        if kanal:
            print("  KANAL :", teks_dari(kanal[0].get("title", {})))
        if durasi:
            print("  DURASI:", teks_dari(durasi[0]))

        chapter = []
        cari_kunci(data, "chapterRenderer", chapter)
        if chapter:
            print(f"  CHAPTER ({len(chapter)}):")
            for c in chapter:
                print(
                    f"    {teks_dari(c.get('timeRangeStartMillis', 0))} "
                    f"{teks_dari(c.get('title', {}))}"
                )
        else:
            print("  CHAPTER: tidak ada")

        desk = []
        cari_kunci(data, "attributedDescription", desk)
        if not desk:
            cari_kunci(data, "description", desk)
        isi = teks_dari(desk[0]) if desk else ""
        print(f"  DESKRIPSI ({len(isi)} karakter):")
        for baris in isi[:1500].split("\n"):
            if baris.strip():
                print("   ", baris.strip()[:110])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    main(sys.argv[1:])
