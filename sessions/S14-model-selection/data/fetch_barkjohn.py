"""Download the two EPA sensor collocation sets into this folder, and check them.

K. Barkjohn (2021), the US-wide 24 hour collocation set, U.S. EPA Office of Research and
Development, EPA ScienceHub, doi:10.23719/1522388; and K. Barkjohn (2023), the hourly smoke set,
EPA ScienceHub, doi:10.23719/1528138. data/README.md cites the papers they support. The sensor readings in both came from PurpleAir, whose terms do not let
the course copy them into the repository, so each student downloads them once, here, and git
ignores them.

The notebook runs this script in its first section with

    %run data/fetch_barkjohn.py

For each set it downloads the zip from EPA only if the CSV the notebook reads is not already
here, checks the zip's SHA-256 against the value recorded on 2026-09-30, takes that one CSV out
of it into this folder, and deletes the zip. On every run it checks each CSV's SHA-256, so every
student and every grader reads the same bytes. It stops with a RuntimeError, which halts Run All,
if a download fails or a file differs. The two downloads are 4 MB and 72 MB; the two CSVs take
268 MB of disk.
"""

import hashlib
import urllib.request
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SETS = [   # (zip URL, zip SHA-256, the CSV inside it, the CSV's SHA-256)
    ("https://pasteur.epa.gov/uploads/10.23719/1522388/Data_DevelopmentUSPAcorrection_210408.zip",
     "121b6978ac8a926aca710c9d7b5626245f8176cfd04e3b78c4f061b22734d63e",
     "Data_DevelopmentUSPAcorrection_210408/Full24hrdataset.csv",
     "c0027349e693f629596d74fde4900f5318e8556530f58c44c79409aac55ba2c3"),
    ("https://pasteur.epa.gov/uploads/10.23719/1528138/Dataset_PurpleAirSmoke_Barkjohn_3_15_23.zip",
     "f235f42a2d2d8c3e9730c14daffd6c0387977b082b0c0fc948d232d66933b421",
     "Dataset_PurpleAirSmoke_Barkjohn_1_18_23/Finaldataset_correcteddatasetwholding_10_26_22.csv",
     "84edd2527ff5598a0674824aee196036db3602416461982d4322cdb12a0bcd29"),
]
BACKUP = ("We will post the files on Canvas, in the Session 14 module, if the source refuses. "
          f"Download them from there and put them in {HERE}, then run this cell again.")


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


for url, zip_sha, member, csv_sha in SETS:
    csv_path = HERE / member
    if not csv_path.exists():
        zip_path = HERE / url.rsplit("/", 1)[1]
        if not zip_path.exists():
            print(f"Downloading {url}")
            request = urllib.request.Request(url, headers={"User-Agent": "chem427-course-fetch"})
            try:
                with urllib.request.urlopen(request, timeout=120) as response, open(zip_path, "wb") as out:
                    while block := response.read(1 << 20):
                        out.write(block)
            except OSError as err:
                zip_path.unlink(missing_ok=True)
                raise RuntimeError(f"The download failed ({err}).\n{BACKUP}")
        if sha256(zip_path) != zip_sha:
            raise RuntimeError(f"{zip_path.name} is not the file the course recorded. Delete it and run this cell again.\n{BACKUP}")
        with zipfile.ZipFile(zip_path) as z:
            z.extract(member, HERE)
        zip_path.unlink()
    if sha256(csv_path) != csv_sha:
        raise RuntimeError(f"{member} is not the file the course recorded. Delete it and run this cell again.\n{BACKUP}")
    print(f"{member}: {csv_path.stat().st_size:,} bytes, SHA-256 checked")
