"""Download the Flint water study's lead results into this folder, and check the file.

FlintWaterStudy.org (2015), "Lead Results from Tap Water Sampling in Flint, MI during the
Flint Water Crisis", Virginia Tech, file Flint-Samples-FINAL.xlsx. The site states no
licence, so the course does not copy the file into the repository: each student downloads
it once, here, and git ignores it.

The notebook runs this script in its first section with

    %run data/fetch_flint.py

It downloads the file only if it is not already here, then checks its SHA-256 against the
value recorded on 2026-10-10, so every student and every grader reads the same bytes. It
stops with a RuntimeError, which halts Run All, if the download fails or the file differs.
"""

import hashlib
import urllib.request
from pathlib import Path

URL = "https://flintwaterstudy.org/wp-content/uploads/2015/12/Flint-Samples-FINAL.xlsx"
SHA256 = "96b00f626011b97193ed24d8b97f51a22643c05e95d79dafd50900e7af0c81fb"  # 33,202 bytes, 2026-10-10
FLINT_XLSX = Path(__file__).resolve().parent / "Flint-Samples-FINAL.xlsx"
BACKUP = ("We will post the file on Canvas, in the Session 9 module, if the source refuses. "
          f"Download it from there and put it in {FLINT_XLSX.parent}, then run this cell again.")

if not FLINT_XLSX.exists():
    print(f"Downloading {URL}")
    # The site refuses Python's default user agent with 403 Forbidden, so the request names itself.
    request = urllib.request.Request(URL, headers={"User-Agent": "chem427-course-fetch"})
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            FLINT_XLSX.write_bytes(response.read())
    except OSError as err:
        raise RuntimeError(f"The download failed ({err}).\n{BACKUP}")

digest = hashlib.sha256(FLINT_XLSX.read_bytes()).hexdigest()
if digest != SHA256:
    raise RuntimeError(f"{FLINT_XLSX.name} is not the file the course recorded (SHA-256 {digest[:12]}..., "
                       f"expected {SHA256[:12]}...). Delete it and run this cell again.\n{BACKUP}")
print(f"{FLINT_XLSX.name}: {FLINT_XLSX.stat().st_size:,} bytes, SHA-256 checked")
