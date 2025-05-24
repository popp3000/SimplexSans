from pathlib import Path
from fontTools.ttLib import TTFont

LICENSE_TEXT = (
    "This Font Software is licensed under the SIL Open Font License, Version 1.1. "
    "This license is available with a FAQ at: https://openfontlicense.org"
)

LICENSE_URL = "https://openfontlicense.org"

FONTS_DIR = Path("fonts")

def fix_license_description(font):
    name_table = font["name"]
    # NameID 13 (LICENSE DESCRIPTION)
    # Windows: platformID=3, platEncID=1, langID=1033
    name_table.setName(LICENSE_TEXT, 13, 3, 1, 1033)
    # Mac: platformID=1, platEncID=0, langID=0
    name_table.setName(LICENSE_TEXT, 13, 1, 0, 0)

    # NameID 14 (LICENSE INFO URL)
    # Windows
    name_table.setName(LICENSE_URL, 14, 3, 1, 1033)
    # Mac
    name_table.setName(LICENSE_URL, 14, 1, 0, 0)

def fix_font_file(font_path):
    print(f"🔧 Lizenztext setzen für {font_path.name}")
    font = TTFont(font_path)
    fix_license_description(font)
    font.save(font_path)
    print(f"✅ Fertig: {font_path.name}")

def main():
    font_paths = list(FONTS_DIR.glob("*.ttf")) + list(FONTS_DIR.glob("*.otf"))
    if not font_paths:
        print("❌ Keine .ttf- oder .otf-Dateien im 'fonts/'-Ordner gefunden.")
        return

    for font_path in font_paths:
        try:
            fix_font_file(font_path)
        except Exception as e:
            print(f"❌ Fehler bei {font_path.name}: {e}")

if __name__ == "__main__":
    main()

