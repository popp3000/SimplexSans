from pathlib import Path
from fontTools.ttLib import TTFont

# Mapping von Subfamily-Namen zu empfohlenen usWeightClass-Werten
WEIGHT_MAPPING = {
    "Thin": 100,
    "ExtraLight": 200,
    "UltraLight": 200,
    "Light": 300,
    "Regular": 400,
    "Normal": 400,
    "Medium": 500,
    "SemiBold": 600,
    "DemiBold": 600,
    "Bold": 700,
    "ExtraBold": 800,
    "UltraBold": 800,
    "Black": 900,
    "Heavy": 900
}

FONTS_DIR = Path("fonts")

def fix_weight_class(font_path):
    font = TTFont(font_path)
    name_table = font["name"]
    
    # Lese Subfamily (NameID 2), bevorzugt Plattform 3, Windows
    subfamily_name = name_table.getName(2, 3, 1, 1033)
    if not subfamily_name:
        print(f"⚠️ Kein Subfamily-Name in {font_path.name}, übersprungen.")
        return
    
    subfamily = subfamily_name.toUnicode().replace(" ", "")
    expected_weight = WEIGHT_MAPPING.get(subfamily)

    if expected_weight is None:
        print(f"⚠️ Kein Gewicht für Subfamily '{subfamily}' definiert in {font_path.name}")
        return

    os2_table = font["OS/2"]
    if os2_table.usWeightClass != expected_weight:
        print(f"🔧 {font_path.name}: usWeightClass {os2_table.usWeightClass} → {expected_weight} (für '{subfamily}')")
        os2_table.usWeightClass = expected_weight
        font.save(font_path)
        print(f"✅ Gewichts-Korrektur gespeichert.")
    else:
        print(f"✅ {font_path.name}: Gewichtsklasse korrekt.")

def main():
    font_paths = list(FONTS_DIR.glob("*.ttf")) + list(FONTS_DIR.glob("*.otf"))
    if not font_paths:
        print("❌ Keine Font-Dateien in 'fonts/' gefunden.")
        return

    for path in font_paths:
        try:
            fix_weight_class(path)
        except Exception as e:
            print(f"❌ Fehler bei {path.name}: {e}")

if __name__ == "__main__":
    main()

