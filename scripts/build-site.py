from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"

if SITE.exists():
    shutil.rmtree(SITE)
SITE.mkdir()
shutil.copy2(ROOT / "index.html", SITE / "index.html")

for version, destination in (
    ("Front_Portfolio", SITE),
    ("Unity_Portfolio", SITE / "Unity_Portfolio"),
):
    for folder, stylesheet in (
        ("web-starter", "styles.css"),
        ("portfolio-ppt", "portfolio-ppt.css"),
    ):
        source = ROOT / version / folder
        target = destination / folder
        target.mkdir(parents=True)
        for name in ("index.html", stylesheet):
            shutil.copy2(source / name, target / name)
        shutil.copytree(source / "assets", target / "assets")
        if folder == "portfolio-ppt":
            (target / "output").mkdir()
            for pdf in (source / "output").glob("*.pdf"):
                shutil.copy2(pdf, target / "output" / pdf.name)

shutil.copy2(ROOT / "Unity_Portfolio/index.html", SITE / "Unity_Portfolio/index.html")
print(f"배포 파일 준비 완료: {SITE}")
