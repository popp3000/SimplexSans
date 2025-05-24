from pathlib import Path
from fontTools.ttLib import TTFont

FONTS_DIR = Path("fonts")

def fix_typo_ascender(font):
    os2 = font["OS/2"]
    hhea = font["hhea"]
    if os2.sTypoAscender != hhea.ascent:
        print(f"  🔧 sTypoAscender war {os2.sTypoAscender}, wird auf hhea.ascent ({hhea.ascent}) gesetzt.")
        os2.sTypoAscender = hhea.ascent
    else:
        print("  ✅ sTypoAscender stimmt bereits mit hhea.ascent überein.")

def fix_font_file(font_path):
    print(f"→ Bearbeite {font_path.name}")
    font = TTFont(font_path)
    fix_typo_ascender(font)
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

