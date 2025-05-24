from pathlib import Path
from fontTools.ttLib import TTFont

FONTS_DIR = Path("fonts")

def fix_fsType(font_path):
    font = TTFont(font_path)
    os2_table = font["OS/2"]
    if os2_table.fsType != 0:
        print(f"🔧 {font_path.name}: fsType {os2_table.fsType} → 0 (Installable Embedding)")
        os2_table.fsType = 0
        font.save(font_path)
        print(f"✅ fsType korrigiert.")
    else:
        print(f"✅ {font_path.name}: fsType ist bereits korrekt (0).")

def main():
    font_paths = list(FONTS_DIR.glob("*.ttf")) + list(FONTS_DIR.glob("*.otf"))
    if not font_paths:
        print("❌ Keine Font-Dateien im 'fonts/'-Ordner gefunden.")
        return

    for path in font_paths:
        try:
            fix_fsType(path)
        except Exception as e:
            print(f"❌ Fehler bei {path.name}: {e}")

if __name__ == "__main__":
    main()

