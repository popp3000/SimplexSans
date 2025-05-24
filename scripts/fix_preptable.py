import subprocess
from pathlib import Path

FONTS_DIR = Path("fonts")

def fix_nonhinting(font_path):
    if font_path.suffix.lower() != ".ttf":
        print(f"⏩ Überspringe {font_path.name} (nicht .ttf)")
        return

    temp_path = font_path.with_name(font_path.stem + "-fix.ttf")
    try:
        print(f"→ Behebe Non-Hinting für {font_path.name}")
        subprocess.run([
            "gftools",
            "fix-nonhinting",
            str(font_path),
            str(temp_path)
        ], check=True)

        # Original ersetzen
        font_path.unlink()
        temp_path.rename(font_path)
        print(f"✅ Fertig: {font_path.name}\n")
    except subprocess.CalledProcessError as e:
        print(f"❌ Fehler bei {font_path.name}: {e}")

def main():
    font_paths = list(FONTS_DIR.glob("*.ttf")) + list(FONTS_DIR.glob("*.otf"))
    if not font_paths:
        print("❌ Keine Font-Dateien im 'fonts/'-Ordner gefunden.")
        return

    for font_path in font_paths:
        fix_nonhinting(font_path)

if __name__ == "__main__":
    main()

