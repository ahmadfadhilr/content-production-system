#!/usr/bin/env python3
"""Pindai permintaan dan supply YouTube Indonesia untuk satu daftar kueri.

Pakai:
    python3 tools/pindai-youtube.py "cara menghitung margin" "kapan menaikkan harga"

Keluaran: jumlah hasil, tayangan tertinggi, median 10 teratas, jumlah video di atas
100 ribu tayangan, durasi terpanjang, dan lima judul teratas.

Catatan: skrip ini hanya membaca judul, durasi, dan tayangan. Klasifikasi "dangkal"
atau "dalam" tetap butuh menonton video.
"""

import json
import re
import statistics
import subprocess
import sys
import urllib.parse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"


def ambil(kueri):
    url = (
        "https://www.youtube.com/results?search_query="
        + urllib.parse.quote(kueri)
        + "&hl=id&gl=ID"
    )
    html = subprocess.run(
        ["curl", "-sL", "-A", UA, url], capture_output=True, text=True
    ).stdout
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", html, re.S)
    if not m:
        return []
    data = json.loads(m.group(1))
    hasil = []

    def baca(v):
        hasil.append(
            {
                "id": v.get("videoId", ""),
                "judul": "".join(
                    r.get("text", "") for r in v.get("title", {}).get("runs", [])
                ),
                "kanal": "".join(
                    r.get("text", "") for r in v.get("ownerText", {}).get("runs", [])
                ),
                "tayangan": v.get("viewCountText", {}).get("simpleText", ""),
                "durasi": v.get("lengthText", {}).get("simpleText", ""),
                "unggah": v.get("publishedTimeText", {}).get("simpleText", ""),
            }
        )

    # Ambil hanya daftar hasil utama. Penjelajahan seluruh pohon ikut menangkap
    # rak "orang juga menonton" dan video populer, yang membuat median melonjak
    # dan tidak bisa dibandingkan antar putaran.
    utama = []
    try:
        isi = data["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"][
            "sectionListRenderer"
        ]["contents"]
        for bagian in isi:
            if "itemSectionRenderer" in bagian:
                utama.extend(bagian["itemSectionRenderer"].get("contents", []))
    except (KeyError, TypeError):
        utama = []

    if utama:
        for item in utama:
            if isinstance(item, dict) and "videoRenderer" in item:
                baca(item["videoRenderer"])
        return hasil

    def jelajah(o):
        if isinstance(o, dict):
            if "videoRenderer" in o:
                baca(o["videoRenderer"])
            for x in o.values():
                jelajah(x)
        elif isinstance(o, list):
            for x in o:
                jelajah(x)

    jelajah(data)
    return hasil


def angka_tayangan(teks):
    s = teks.lower().replace("x ditonton", "").replace("ditonton", "").strip()
    kali = 1
    if "jt" in s:
        kali, s = 1_000_000, s.replace("jt", "")
    elif "rb" in s:
        kali, s = 1_000, s.replace("rb", "")
    s = s.replace(".", "").replace(",", ".").strip()
    try:
        return int(float(s) * kali)
    except ValueError:
        return None


def detik(durasi):
    """YouTube kadang menulis durasi sebagai '1:19', kadang sebagai '1.19'.

    Titik dipakai sebagai pemisah jam/menit/detik, bukan desimal. Jadi '1.19'
    berarti 1 menit 19 detik, dan '1.02.33' berarti 1 jam 2 menit 33 detik.
    """
    if not durasi:
        return 0
    bersih = durasi.strip().replace(".", ":")
    bagian = []
    for x in bersih.split(":"):
        if not x.isdigit():
            return 0
        bagian.append(int(x))
    if len(bagian) == 1:
        return bagian[0]
    if len(bagian) == 2:
        return bagian[0] * 60 + bagian[1]
    if len(bagian) == 3:
        return bagian[0] * 3600 + bagian[1] * 60 + bagian[2]
    return 0


def ribuan(n):
    return f"{n:,}".replace(",", ".")


def statistik(hasil):
    tayangan = [angka_tayangan(h["tayangan"]) for h in hasil]
    tayangan = [t for t in tayangan if t is not None]
    if not tayangan:
        return None
    atas = sorted(tayangan, reverse=True)[:10]
    return {
        "n": len(hasil),
        "tertinggi": max(tayangan),
        "median": int(statistics.median(atas)),
        "gt100k": sum(1 for t in tayangan if t >= 100_000),
        "terpanjang": max(detik(h["durasi"]) for h in hasil) // 60,
    }


def main(kueri, detail=False, ulang=3):
    for q in kueri:
        putaran = []
        hasil = []
        for _ in range(ulang):
            h = ambil(q)
            s = statistik(h) if h else None
            if s:
                putaran.append(s)
                hasil = h
        if not putaran:
            print(f"\n{q}\n  tidak ada hasil atau gagal parse")
            continue

        median_putaran = [s["median"] for s in putaran]
        median = int(statistics.median(median_putaran))
        rendah, tinggi = min(median_putaran), max(median_putaran)
        rasio = tinggi / rendah if rendah else 0
        akhir = putaran[-1]

        print("\n" + "=" * 72)
        print(q)
        print(f"  median 10 teratas: {ribuan(median)}"
              f"   (rentang {ulang} putaran: {ribuan(rendah)}–{ribuan(tinggi)}"
              f", {rasio:.1f}x)")
        print(f"  hasil: {akhir['n']} | tertinggi: {ribuan(akhir['tertinggi'])}"
              f" | di atas 100 rb: {akhir['gt100k']}"
              f" | durasi terpanjang: {akhir['terpanjang']} menit")
        tampil = hasil if detail else hasil[:5]
        for h in tampil:
            # ID dicetak sebaris dengan judul. Kalau dipisah ke baris sendiri, ID mudah
            # tertukar antar putaran karena urutan hasil pencarian berubah.
            ekor = f"  https://youtu.be/{h['id']}" if detail else ""
            print(
                f"   [{h['durasi']:>6}] {h['tayangan']:<18} "
                f"{h['kanal'][:26]:<26} | {h['judul'][:56]}{ekor}"
            )
            if detail:
                print(f"          ({h['unggah']})")


if __name__ == "__main__":
    arg = sys.argv[1:]
    detail = False
    ulang = 3
    while arg and arg[0].startswith("-"):
        f = arg.pop(0)
        if f in ("-d", "--detail"):
            detail = True
        elif f.startswith("-r"):
            ulang = int(f.lstrip("-r") or 3)
    if not arg:
        print(__doc__)
        sys.exit(1)
    main(arg, detail, ulang)
