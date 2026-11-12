"""Download the Southwest Research Institute diesel spectra into this folder, and check them.

S. Hutzler, Southwest Research Institute (2004), "NIR Spectra of Diesel Fuels" and "Properties
of Diesel Fuels", distributed by Eigenvector Research as SWRI_Diesel_NIR_CSV.zip on its data
sets page, https://eigenvector.com/resources/data-sets/. The page states no licence, so the
course does not copy the files into the repository: each student downloads them once, here,
and git ignores them.

The notebook runs this script in its first section with

    %run data/fetch_diesel.py

It downloads the zip only if the two CSVs the notebook reads are not already here, checks the
zip's SHA-256 against the value recorded on 2026-11-10, takes diesel_spec.csv and
diesel_prop.csv out of it into this folder, and deletes the zip. On every run it checks each
CSV's SHA-256, so every student and every grader reads the same bytes. It stops with a
RuntimeError, which halts Run All, if the download fails or a file differs. The download is
1.0 MB; the two CSVs take 2.8 MB of disk.
"""

import hashlib
import urllib.request
import zipfile
from pathlib import Path

URL = "https://eigenvector.com/wp-content/uploads/2019/06/SWRI_Diesel_NIR_CSV.zip"
ZIP_SHA256 = "c5eb0f7f5aacba47c40e2dbbbc81db944bedf568f1d3e7c6c8e381f610563c7a"   # 1,029,110 bytes, 2026-11-10
CSV_SHA256 = {
    "diesel_spec.csv": "f0ba1ee6f4147ea8920bf106f1e22c4292601f4be12551b3317c466cd796027b",   # 2,787,595 bytes
    "diesel_prop.csv": "6086ffeb42f93b61fb184e72a294735d74f4f0e2ef301a5e4ee5c191610bb983",   # 32,362 bytes
}
HERE = Path(__file__).resolve().parent
BACKUP = ("We will post the files on Canvas, in the Session 17 module, if the source refuses. "
          f"Download them from there and put them in {HERE}, then run this cell again.")


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


if not all((HERE / name).exists() for name in CSV_SHA256):
    zip_path = HERE / URL.rsplit("/", 1)[1]
    if not zip_path.exists():
        print(f"Downloading {URL}")
        request = urllib.request.Request(URL, headers={"User-Agent": "chem427-course-fetch"})
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                zip_path.write_bytes(response.read())
        except OSError as err:
            zip_path.unlink(missing_ok=True)
            raise RuntimeError(f"The download failed ({err}).\n{BACKUP}")
    digest = sha256(zip_path)
    if digest != ZIP_SHA256:
        raise RuntimeError(f"{zip_path.name} is not the file the course recorded (SHA-256 {digest[:12]}..., "
                           f"expected {ZIP_SHA256[:12]}...). Delete it and run this cell again.\n{BACKUP}")
    with zipfile.ZipFile(zip_path) as z:
        for name in CSV_SHA256:
            z.extract(name, HERE)
    zip_path.unlink()

for name, expected in CSV_SHA256.items():
    digest = sha256(HERE / name)
    if digest != expected:
        raise RuntimeError(f"{name} is not the file the course recorded (SHA-256 {digest[:12]}..., "
                           f"expected {expected[:12]}...). Delete it and run this cell again.\n{BACKUP}")
    print(f"{name}: {(HERE / name).stat().st_size:,} bytes, SHA-256 checked")
