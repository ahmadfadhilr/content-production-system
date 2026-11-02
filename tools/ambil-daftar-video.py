#!/usr/bin/env python3
"""Ambil daftar video terbaru dari channel YouTube tanpa login.

Pakai:
    python3 tools/ambil-daftar-video.py Moon-Real
    python3 tools/ambil-daftar-video.py AlexHormozi RaymondChins ferryirwandi Moon-Real WeAreBigAStory

Yang dicetak: durasi, tayangan, waktu unggah, dan judul. Semua dari halaman /videos publik.

Jebakan yang sudah terbukti:
- Feed RSS `youtube.com/feeds/videos.xml?channel_id=...` mengembalikan 404 atau 500 untuk
  beberapa channel. Jangan pakai jalur itu.
- Mencari nama tampilan di mesin pencari menemukan channel lain dengan nama mirip. Pakai handle.
- `videoRenderer` sudah tidak dipakai di halaman /videos. Yang dipakai `lockupViewModel`.
"""

import json
import re
import subprocess
import sys

URL = "https://www.youtube.com/@{handle}/videos"
HEADER = "Accept-Language: id-ID,id;q=0.9,en;q=0.8"


def ambil(handle):
    html = subprocess.run(
        ["curl", "-sL", URL.format(handle=handle), "-H", HEADER],
        capture_output=True,
        text=True,
    ).stdout

    cocok = re.search(r"var ytInitialData = (\{.*?\});</script>", html, re.S)
    if not cocok:
        print(f"@{handle}: ytInitialData tidak ditemukan ({len(html)} byte).")
        return

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

    sub = re.search(r'"content":"([0-9][^"]*subscriber)"', html)
    print(f"=== @{handle} | {sub.group(1) if sub else '?'} | {len(lockups)} video ===")

    for lockup in lockups:
        meta = lockup.get("metadata", {}).get("lockupMetadataViewModel", {})
        judul = meta.get("title", {}).get("content", "")
        baris = (
            meta.get("metadata", {})
            .get("contentMetadataViewModel", {})
            .get("metadataRows", [])
        )
        info = " | ".join(
            bagian.get("text", {}).get("content", "")
            for baris_meta in baris
            for bagian in baris_meta.get("metadataParts", [])
        )
        durasi = ""
        try:
            badge = lockup["contentImage"]["thumbnailViewModel"]["overlays"][0][
                "thumbnailBottomOverlayViewModel"
            ]["badges"]
            durasi = badge[0]["thumbnailBadgeViewModel"]["text"]
        except (KeyError, IndexError, TypeError):
            pass
        print(f"{durasi:>8} | {info:<26} | {judul}")
    print()


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        ambil(arg)
