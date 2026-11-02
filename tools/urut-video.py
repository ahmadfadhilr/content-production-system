#!/usr/bin/env python3
"""Urutkan video satu channel berdasarkan tayangan, beserta ID dan kelipatan median.

Pakai:
    python3 tools/urut-video.py SepulangSekolah
    python3 tools/urut-video.py AlexHormozi RaymondChins --top=5

Yang dicetak: ID, tayangan, durasi, kelipatan terhadap median channel, judul.

Kenapa ada alat ini: `yt-dlp --flat-playlist --print "%(view_count)s"` pada halaman channel
mengembalikan angka yang salah. "984 rb tayangan" terbaca 984, bukan 984.000. Tayangan dan durasi
di halaman /videos berupa teks, jadi harus diurai sendiri.

Yang tetap tidak bisa didapat dari halaman publik: jumlah share, jumlah save, dan average view
duration. Tiga angka itu hanya ada di YouTube Studio pemilik channel. Jangan mengarangnya.
"""

import json
import re
import statistics
import subprocess
import sys

URL = "https://www.youtube.com/@{handle}/videos"
HEADER = "Accept-Language: id-ID,id;q=0.9,en;q=0.8"


def urai_tayangan(teks):
    """'1,2 jt tayangan' -> 1_200_000. '984 rb' -> 984_000. '12.345' -> 12_345."""
    if not teks:
        return None
    t = teks.lower().replace(".", "").replace(",", ".")
    m = re.search(r"([\d.]+)\s*(jt|rb|k|m)?", t)
    if not m:
        return None
    angka = float(m.group(1))
    satuan = m.group(2)
    if satuan in ("jt", "m"):
        angka *= 1_000_000
    elif satuan in ("rb", "k"):
        angka *= 1_000
    return int(angka)


def urai_durasi(teks):
    """'1:02:03' -> 3723 detik. '12:34' -> 754. Di locale Indonesia: '16.10' -> 970."""
    if not teks or not re.search(r"[:.]", teks):
        return 0
    bagian = [int(x) for x in re.findall(r"\d+", teks)]
    while len(bagian) < 3:
        bagian.insert(0, 0)
    jam, menit, detik = bagian[-3:]
    return jam * 3600 + menit * 60 + detik


def ambil(handle):
    html = subprocess.run(
        ["curl", "-sL", URL.format(handle=handle), "-H", HEADER],
        capture_output=True,
        text=True,
    ).stdout

    cocok = re.search(r"var ytInitialData = (\{.*?\});</script>", html, re.S)
    if not cocok:
        print(f"@{handle}: ytInitialData tidak ditemukan ({len(html)} byte).")
        return []

    data = json.loads(cocok.group(1))
    lockups = []

    def jelajah(o):
        if isinstance(o, dict):
            if "lockupViewModel" in o:
                lockups.append(o["lockupViewModel"])
            for nilai in o.values():
                jelajah(nilai)
        elif isinstance(o, list):
            for nilai in o:
                jelajah(nilai)

    jelajah(data)

    hasil = []
    for lockup in lockups:
        vid = lockup.get("contentId", "")
        meta = lockup.get("metadata", {}).get("lockupMetadataViewModel", {})
        judul = meta.get("title", {}).get("content", "")
        baris = (
            meta.get("metadata", {})
            .get("contentMetadataViewModel", {})
            .get("metadataRows", [])
        )
        info = [
            bagian.get("text", {}).get("content", "")
            for baris_meta in baris
            for bagian in baris_meta.get("metadataParts", [])
        ]
        # Di halaman channel, bagian pertama berisi tayangan mentah: "79 rb", "1,2 jt".
        tayangan = None
        for bagian in info:
            if "lalu" in bagian or "yang lalu" in bagian:
                continue
            angka = urai_tayangan(bagian)
            if angka:
                tayangan = angka
                break

        # Durasi ada di badge thumbnail, kedalamannya berubah-ubah. Cari rekursif.
        durasi = ""

        def cari_durasi(o):
            nonlocal durasi
            if isinstance(o, dict):
                if "thumbnailBadgeViewModel" in o:
                    teks = o["thumbnailBadgeViewModel"].get("text", "")
                    if re.search(r"[:.]", teks):
                        durasi = teks
                for v in o.values():
                    cari_durasi(v)
            elif isinstance(o, list):
                for v in o:
                    cari_durasi(v)

        cari_durasi(lockup)
        hasil.append(
            {
                "id": vid,
                "judul": judul,
                "tayangan": tayangan,
                "detik": urai_durasi(durasi),
                "mentah": " | ".join(info),
            }
        )
    return hasil


def main():
    arg = [a for a in sys.argv[1:] if not a.startswith("--")]
    top = 5
    for a in sys.argv[1:]:
        if a.startswith("--top="):
            top = int(a.split("=", 1)[1])
    if not arg:
        print(__doc__)
        return

    for handle in arg:
        hasil = [h for h in ambil(handle) if h["tayangan"]]
        if not hasil:
            continue
        median = statistics.median([h["tayangan"] for h in hasil])
        print(f"=== @{handle} | {len(hasil)} video | median tayangan {int(median):,} ===")
        print(f"{'ID':<12} {'tayangan':>10} {'x':>5} {'durasi':>7}  judul")
        for h in sorted(hasil, key=lambda x: -x["tayangan"])[:top]:
            print(
                f"{h['id']:<12} {h['tayangan']:>10,} {h['tayangan']/median:>5.1f} "
                f"{h['detik']//60:>4}m{h['detik']%60:02d}  {h['judul'][:64]}"
            )
        print()


if __name__ == "__main__":
    main()
