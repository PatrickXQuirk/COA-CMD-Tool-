# Irish Heraldry Search Tool

A command-line application for searching and viewing authentic Irish family coat of arms and heraldic records.

## Features

- 🔍 **Search Irish surnames** and view their authentic coat of arms
- 🎨 **ASCII art representations** of heraldic shields and crests
- 📜 **Complete motto information** with English translations and language attribution
- 🏛️ **Historical origin data** (Milesian vs Norman heritage)
- 📊 **Multiple coat of arms** comparison for surnames with several variants
- 📚 **Browse all surnames** in the database
- 🎯 **Smart search** with Mc/Mac name normalization

## Database Statistics

- **622 total heraldic entries**
- **566 unique Irish surnames**
- **~94% complete translations** (579 of 619 mottos translated)
- **558 entries** with historical origin data
- Includes both **Crests** and **Insignias** from authentic sources

### Historical Origins
- **Milesian**: 551 entries (native Gaelic Irish families)
- **Norman**: 7 entries (Anglo-Norman families)

## Requirements

- Python 3.7 or higher
- Windows console with UTF-8 support (for best display)
- Cross-platform compatible (Linux/Mac/Windows)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/irish-heraldry-search.git
cd irish-heraldry-search
```

2. No additional dependencies required - uses Python standard library only

## Usage

### Windows
Double-click `RUN_HERALDRY.bat` or run from command line:
```bash
RUN_HERALDRY.bat
```

### All Platforms
```bash
python heraldry_search.py
```

### Quick Commands
- Type `menu` at any prompt to jump to main menu
- Type `zoltar` to skip directly to search

## Example Searches

The database includes surnames such as:
- **O'Brien** - Ancient High Kings of Ireland
- **Kennedy** - Milesian lineage from County Clare
- **Burke** - Norman family, Earls of Clanricarde
- **McCarthy** - Kings of Desmond
- **O'Neill** - Kings of Ulster
- And 560+ more...

## Database Structure

### Entry Format
Each heraldic entry contains:
- **Surname**: Family name
- **Crest Code**: Reference identifier (Crest/Insignia number and plate)
- **Page**: Source document page number
- **Motto**: Original motto text (Latin, Old Irish, French, etc.)
- **Motto Translation**: English translation
- **Motto Language**: Language of the motto
- **Origin**: Milesian (Gaelic) or Norman heritage

## Files

- `heraldry_search.py` - Main application
- `heraldry_database_real.py` - Complete database of 622 Irish heraldic entries
- `coat_of_arms_art_real.py` - ASCII art for coat of arms displays
- `RUN_HERALDRY.bat` - Windows launcher
- `README.md` - This file

## Data Sources

All heraldic data is compiled from authentic historical records. The database includes:
- Crest and plate references
- Original motto texts in Latin, Old Irish, French, and other languages
- Professional English translations
- Historical family origin classifications

## About The Guild

Created for **The Guild of Heraldic Arts & Research**, a nonprofit 501(c)(3) organization dedicated to:
- Preserving heraldic traditions
- Documenting family coat of arms
- Providing public access to authentic heraldic knowledge
- Building the world's most comprehensive heraldic library

## Easter Eggs

The application includes special responses for certain non-Irish surnames. Try searching for:
- Hodges (Scottish)
- Charbonneau (French)

## Contributing

This project contains authentic historical data. Contributions should:
- Include verified historical sources
- Maintain data authenticity
- Follow the existing database format

## License

Educational and historical preservation purposes.

## Version History

### v2.0 (Current)
- Added 4 new surname entries (BEGLEY, BRODY, CAREY, CARR)
- Imported 441 motto translations from source CSV
- Added 441 language attributions
- Added Origin field (Milesian/Norman) to 558 entries
- Improved Mc/Mac surname normalization
- Database now 94% complete with translations

### v1.0
- Initial release with 618 entries
- ASCII art coat of arms display
- Interactive search functionality

---

**Note**: This is a historical research tool. Coat of arms are traditionally granted to individuals, not surnames. The entries in this database represent historical armorial bearings associated with Irish family names from various sources and periods.
