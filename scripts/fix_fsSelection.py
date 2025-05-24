from pathlib import Path
from fontTools.ttLib import TTFont

FONTS_DIR = Path("fonts")

def set_use_typo_metrics_bit(font):
    os2 = font["OS/2"]
    # Bit 7 (0b10000000) setzen, ohne andere Bits zu verändern
    os2.fsSelection |= (1 << 7)

def fix_font_file(font_path):
    print(f"🔧 Setze fsSelection Bit 7 für {font_path.name}")
    font = TTFont(font_path)
    set_use_typo_metrics_bit(font)
    font.save(font_path)
    print(f"✅ Fertig: {font_path.name}")

def main():
    font_paths = list(FONTS_DIR.glob("*.ttf")) + list(FONTS_DIR.glob("*.otf"))
    if not font_paths:
        print("❌ Keine .ttf oder .otf Dateien im 'fonts/'-Ordner gefunden.")
        return

    for font_path in font_paths:
        try:
            fix_font_file(font_path)
        except Exception as e:
            print(f"❌ Fehler bei {font_path.name}: {e}")

if __name__ == "__main__":
    main()

