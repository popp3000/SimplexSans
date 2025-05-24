from pathlib import Path
from fontTools.ttLib import TTFont

FONTS_DIR = Path("fonts")

def fix_subfamily_to_regular(font):
    name_table = font["name"]
    for platform_id, encoding_id, lang_id in [(3, 1, 1033), (1, 0, 0)]:
        name_table.setName("Regular", 2, platform_id, encoding_id, lang_id)

def fix_font_file(font_path):
    print(f"🔧 SubFamily auf 'Regular' setzen für {font_path.name}")
    font = TTFont(font_path)
    fix_subfamily_to_regular(font)
    font.save(font_path)
    print(f"✅ Gespeichert: {font_path.name}")

def main():
    font_paths = list(FONTS_DIR.glob("*.ttf")) + list(FONTS_DIR.glob("*.otf"))
    if not font_paths:
        print("❌ Keine Font-Dateien gefunden.")
        return

    for font_path in font_paths:
        try:
            fix_font_file(font_path)
        except Exception as e:
            print(f"❌ Fehler bei {font_path.name}: {e}")

if __name__ == "__main__":
    main()

