from pathlib import Path
from fontTools.ttLib import TTFont

FONTS_DIR = Path("fonts")

def fix_typo_line_gap(font):
    os2 = font["OS/2"]
    if os2.sTypoLineGap != 0:
        print(f"  🔧 sTypoLineGap war {os2.sTypoLineGap}, wird auf 0 gesetzt.")
        os2.sTypoLineGap = 0
    else:
        print("  ✅ sTypoLineGap ist bereits 0.")

def fix_font_file(font_path):
    print(f"→ Bearbeite {font_path.name}")
    font = TTFont(font_path)
    fix_typo_line_gap(font)
    font.save(font_path)
    print(f"✅ Fertig: {font_path.name}\n")

def main():
    font_paths = list(FONTS_DIR.glob("*.ttf")) + list(FONTS_DIR.glob("*.otf"))
    if not font_paths:
        print("❌ Keine Font-Dateien im 'fonts/'-Ordner gefunden.")
        return

    for font_path in font_paths:
        try:
            fix_font_file(font_path)
        except Exception as e:
            print(f"❌ Fehler bei {font_path.name}: {e}")

if __name__ == "__main__":
    main()

