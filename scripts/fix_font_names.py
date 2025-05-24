# scripts/fix_font_names.py

from fontTools.ttLib import TTFont
from pathlib import Path

FONTS_DIR = Path("fonts")
TARGET_FAMILY = "Simplex Sans"
TARGET_SUBFAMILY = "Regular"

def fix_names(font_path):
    font = TTFont(font_path)
    name_table = font["name"]

    # Hilfsfunktionen
    def set_name(nameID, string):
        name_table.setName(string, nameID, 3, 1, 1033)  # Windows
        name_table.setName(string, nameID, 1, 0, 0)     # Mac

    # Setze die geforderten Werte
    set_name(1, TARGET_FAMILY)                              # Family Name
    set_name(2, TARGET_SUBFAMILY)                           # Subfamily Name
    set_name(4, f"{TARGET_FAMILY} {TARGET_SUBFAMILY}")      # Full Name
    set_name(6, f"{TARGET_FAMILY.replace(' ', '')}-{TARGET_SUBFAMILY}")  # PostScript Name

    # Entferne nameIDs 16 & 17 (Typographic names)
    name_table.names = [n for n in name_table.names if n.nameID not in (16, 17)]

    font.save(font_path)
    print(f"✅ Namen korrigiert für: {font_path.name}")

def main():
    fonts = list(FONTS_DIR.glob("*.ttf")) + list(FONTS_DIR.glob("*.otf"))
    for font in fonts:
        try:
            fix_names(font)
        except Exception as e:
            print(f"❌ Fehler bei {font.name}: {e}")

if __name__ == "__main__":
    main()

