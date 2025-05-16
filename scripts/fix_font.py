from pathlib import Path
from fontTools.ttLib import TTFont
import subprocess

FONTS_DIR = Path("fonts")

def fix_os2_metrics(font):
    os2 = font["OS/2"]
    hhea = font["hhea"]

    os2.sTypoLineGap = 0
    os2.sTypoAscender = hhea.ascent
    os2.sTypoDescender = hhea.descent

    # fsSelection bit 7 setzen
    os2.fsSelection |= 1 << 7

    # usWeightClass für 'Medium' = 500
    name = font["name"].getName(17, 3, 1, 1033)
    if name and name.toUnicode() == "Medium":
        os2.usWeightClass = 500

def fix_fsType(font):
    font["OS/2"].fsType = 0

def fix_name_table(font):
    name_table = font["name"]
    
    copyright_string = (
        "Copyright 2025 The SimplexSans Project Authors (https://github.com/popp3000/SimplexSans)"
    )
    license_desc = (
        "This Font Software is licensed under the SIL Open Font License, "
        "Version 1.1. This license is available with a FAQ at: https://openfontlicense.org"
    )

    name_table.setName(copyright_string, 0, 3, 1, 1033)
    name_table.setName(license_desc, 13, 3, 1, 1033)

def apply_autohint(font_path):
    temp_path = font_path.with_name(font_path.stem + "-fix.ttf")
    subprocess.run(["gftools", "fix-nonhinting", str(font_path), str(temp_path)], check=True)
    temp_path.replace(font_path)

def fix_font_file(font_path):
    print(f"→ Fixing {font_path.name}")
    font = TTFont(font_path)
    fix_os2_metrics(font)
    fix_fsType(font)
    fix_name_table(font)
    font.save(font_path)
    apply_autohint(font_path)

def main():
    font_paths = list(FONTS_DIR.glob("*.ttf"))
    if not font_paths:
        print("❌ Keine .ttf-Dateien im 'fonts/'-Ordner gefunden.")
        return

    for font_path in font_paths:
        try:
            fix_font_file(font_path)
            print(f"✅✅ {font_path.name} fertig\n")
        except Exception as e:
            print(f"❌ Fehler bei {font_path.name}: {e}")

if __name__ == "__main__":
    main()

