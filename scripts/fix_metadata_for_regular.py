# scripts/fix_metadata_for_regular.py

from pathlib import Path
from fontTools.ttLib import TTFont

FONTS_DIR = Path("fonts")
TARGET_STYLE = "Regular"
TARGET_WEIGHT = 400

def fix_font_metadata(font_path):
    font = TTFont(font_path)
    name_table = font["name"]

    # Style-Namen (NameIDs 2, 17)
    name_table.setName(TARGET_STYLE, 2, 3, 1, 1033)  # Windows
    name_table.setName(TARGET_STYLE, 2, 1, 0, 0)     # Mac
    name_table.setName(TARGET_STYLE, 17, 3, 1, 1033)  # Typographic Subfamily name
    name_table.setName(TARGET_STYLE, 17, 1, 0, 0)

    # fsSelection-Bits: Setze "Regular" (Bit 6)
    os2 = font["OS/2"]
    os2.usWeightClass = TARGET_WEIGHT
    os2.fsSelection |= 0b01000000  # Regular Bit setzen
    os2.fsSelection &= ~(  # Alle anderen Stilbits ausschalten
        0b00000001 |  # Italic
        0b00000010 |  # Underscore
        0b00000100 |  # Negative
        0b00001000 |  # Outlined
        0b00010000 |  # Strikeout
        0b00100000 |  # Bold
        0b10000000    # Use_Typo_Metrics (lassen wir deaktiviert)
    )

    # hhea ascent an usTypoAscender angleichen (optional, falls du Konsistenz willst)
    font["hhea"].ascent = os2.sTypoAscender
    font["hhea"].descent = os2.sTypoDescender

    font.save(font_path)
    print(f"✅ Metadaten korrigiert für: {font_path.name}")

def main():
    font_paths = list(FONTS_DIR.glob("*.ttf")) + list(FONTS_DIR.glob("*.otf"))
    if not font_paths:
        print("❌ Keine Fonts gefunden in fonts/")
        return
    for font_path in font_paths:
        try:
            fix_font_metadata(font_path)
        except Exception as e:
            print(f"❌ Fehler bei {font_path.name}: {e}")

if __name__ == "__main__":
    main()

