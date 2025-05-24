# scripts/fix_fsselection_use_typo_metrics.py

from fontTools.ttLib import TTFont
from pathlib import Path

FONTS_DIR = Path("fonts")

def set_bit_7(fsSelection):
    return fsSelection | (1 << 7)

def fix_use_typo_metrics(font_path):
    font = TTFont(font_path)
    os2_table = font["OS/2"]

    old_value = os2_table.fsSelection
    new_value = set_bit_7(old_value)

    if old_value != new_value:
        os2_table.fsSelection = new_value
        font.save(font_path)
        print(f"✅ Bit 7 gesetzt in: {font_path.name}")
    else:
        print(f"✔️ Bit 7 bereits gesetzt in: {font_path.name}")

def main():
    fonts = list(FONTS_DIR.glob("*.ttf")) + list(FONTS_DIR.glob("*.otf"))
    for font_path in fonts:
        try:
            fix_use_typo_metrics(font_path)
        except Exception as e:
            print(f"❌ Fehler bei {font_path.name}: {e}")

if __name__ == "__main__":
    main()

