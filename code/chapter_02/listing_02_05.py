# Listing 2.5: Reading and writing text files safely
from pathlib import Path

folder = Path("data")
folder.mkdir(exist_ok=True)
(folder / "comments.txt").write_text(
    "Excelente servicio\nTrès bon produit\nVery helpful staff\n",
    encoding="utf-8")

with open(folder / "comments.txt", encoding="utf-8") as f:
    for line_no, line in enumerate(f, start=1):
        print(line_no, line.rstrip())

raw = (folder / "comments.txt").read_bytes()
print(len(raw), "bytes on disk")
