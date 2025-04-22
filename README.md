# SimplexSans

**SimplexSans** is a modular, grid-based display typeface inspired by the era of manual lettering — a time when type wasn’t designed on screens, but drawn by hand with ruler and compass. 

![Sample Image](documentation/image1.png)

## Concept

SimplexSans was developed as a typographic experiment rooted in analog construction techniques. Every glyph is based on a strict modular system, allowing the shapes to be drawn manually on graph paper using only a ruler and a compass. The result is a display typeface that feels both mechanical and human, rational and playful. 

## Design Characteristics

- Geometric, monolinear construction
- Based on a triospace grid system, no kerning! 
- Normal characters (a, b, n, etc.) are 2 units wide, narrow characters (I, i, l, etc.) 1 are unit wide and wide characters (W, m, etc.) are 3 units wide
- Designed for display use: headlines, signage, editorial experiments
- Trispace font: to allow rhythmic typographic patterns without relying on variable widths or kerning
- No optical corrections — all shapes are purely constructed and follow the logic of the grid
- Special characters are typically drawn with half the stroke width

## Technical Details

- Formats: OTF and WOFF2
- Character set includes:
  - Basic Latin (A–Z, a–z, numerals, punctuation)
  - Essential symbols and selected extended Latin characters
- No kerning — spacing is fully modular

## About

Designed by [Markus Popp](https://github.com/markuspopp)

## Building

Fonts are built automatically by GitHub Actions - take a look in the "Actions" tab for the latest build.

If you want to build fonts manually on your own computer:

* `make build` will produce font files.
* `make test` will run [FontBakery](https://github.com/googlefonts/fontbakery)'s quality assurance tests.
* `make proof` will generate HTML proof files.

The proof files and QA tests are also available automatically via GitHub Actions - look at `https://yourname.github.io/your-font-repository-name`.

## Changelog

When you update your font (new version or new release), please report all notable changes here, with a date.
[Font Versioning](https://github.com/googlefonts/gf-docs/tree/main/Spec#font-versioning) is based on semver. 
Changelog example:

**26 May 2021. Version 2.13**
- MAJOR Font turned to a variable font.
- SIGNIFICANT New Stylistic sets added.

## License

This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is available with a FAQ at https://openfontlicense.org

## Contribution & Feedback

SimplexSans is a personal project but open to feedback, critique, and potential collaboration. Feel free to open an issue or submit a pull request.
