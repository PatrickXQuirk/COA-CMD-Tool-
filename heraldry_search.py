#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IRISH HERALDRY SEARCH TOOL
ASCII Coat of Arms Display System

Search for your Irish surname and display its authentic coat of arms
"""

import os
import sys
import time
from heraldry_database_real import IRISH_HERALDRY
from coat_of_arms_art_real import COAT_OF_ARMS_ART

# Set UTF-8 encoding for Windows console
if os.name == 'nt':
    os.system('chcp 65001 >nul 2>&1')
    os.system('')
    # Force UTF-8 encoding for stdout
    import sys
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# ANSI Color Codes
class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    GOLD = '\033[93m'
    SILVER = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

# ASCII Art Title
TITLE_ART = """
        ═══════════════════════════════════════════════════
            ██╗██████╗ ██╗███████╗██╗  ██╗
            ██║██╔══██╗██║██╔════╝██║  ██║
            ██║██████╔╝██║███████╗███████║
            ██║██╔══██╗██║╚════██║██╔══██║
            ██║██║  ██║██║███████║██║  ██║
            ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝

    ██╗  ██╗███████╗██████╗  █████╗ ██╗     ██████╗ ██████╗ ██╗   ██╗
    ██║  ██║██╔════╝██╔══██╗██╔══██╗██║     ██╔══██╗██╔══██╗╚██╗ ██╔╝
    ███████║█████╗  ██████╔╝███████║██║     ██║  ██║██████╔╝ ╚████╔╝
    ██╔══██║██╔══╝  ██╔══██╗██╔══██║██║     ██║  ██║██╔══██╗  ╚██╔╝
    ██║  ██║███████╗██║  ██║██║  ██║███████╗██████╔╝██║  ██║   ██║
    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝   ╚═╝

            <<< ANCIENT GAELIC HERALDRY TOME >>>
        ═══════════════════════════════════════════════════
"""

CELTIC_BORDER = """
    ─────────────────────────────────────────────────────────
        AUTHENTIC IRISH FAMILY HERALDRY DATABASE

        The Guild of Heraldic Arts & Research
                  Nonprofit 501(c)(3)
    ─────────────────────────────────────────────────────────
"""

class IrishHeraldrySearch:
    def __init__(self):
        self.current_surname = None
        self.search_history = []
        self.skip_to_menu = False
        self.skip_to_search = False

    def check_menu_shortcut(self, user_input):
        """Check if input is the menu shortcut command"""
        if user_input.lower().strip() == 'menu':
            self.skip_to_menu = True
            return True
        return False

    def check_zoltar(self, user_input):
        """Check if input is the secret zoltar command to skip to search"""
        if user_input.lower().strip() == 'zoltar':
            self.skip_to_search = True
            return True
        return False

    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_slow(self, text, delay=0.03, color=Color.WHITE):
        """Print text with typewriter effect"""
        for char in text:
            sys.stdout.write(color + char + Color.RESET)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def print_centered(self, text, width=80):
        """Print text centered"""
        lines = text.split('\n')
        for line in lines:
            print(line.center(width))

    def display_title(self):
        """Display the application title"""
        self.clear_screen()
        print(Color.GREEN + Color.BOLD + TITLE_ART + Color.RESET)
        print(Color.CYAN + CELTIC_BORDER + Color.RESET)
        print()
        input(Color.YELLOW + "Press ENTER to continue...".center(80) + Color.RESET)
        self.clear_screen()
        print(Color.GREEN + Color.BOLD + TITLE_ART + Color.RESET)
        print(Color.CYAN + CELTIC_BORDER + Color.RESET)
        print()

    def ask_if_irish(self):
        """Ask user if they are of Irish descent"""
        print(Color.YELLOW + "    ╔═══════════════════════════════════════════════════════════╗")
        print(Color.YELLOW + "    ║                                                           ║")
        print(Color.YELLOW + "    ║           SEEKER OF ANCIENT LINEAGE                       ║")
        print(Color.YELLOW + "    ║                                                           ║")
        print(Color.YELLOW + "    ║     Do you carry the blood of the Emerald Isle?           ║")
        print(Color.YELLOW + "    ║     Does Irish heritage flow through your veins?          ║")
        print(Color.YELLOW + "    ║                                                           ║")
        print(Color.YELLOW + "    ╚═══════════════════════════════════════════════════════════╝" + Color.RESET)
        print("\n\n\n")

        while True:
            response = input(Color.WHITE + "  Your answer (yes/no): " + Color.RESET).strip().lower()
            # Secret shortcuts
            if self.check_menu_shortcut(response):
                return 'menu'
            elif self.check_zoltar(response):
                return 'zoltar'
            elif response in ['yes', 'y', 'yeah', 'aye']:
                print()
                self.print_slow("    >> Wonderful! Let's discover your family's heraldic heritage...", 0.02, Color.GREEN)
                time.sleep(1)
                return True
            elif response in ['no', 'n', 'nah']:
                print()
                self.print_slow("    >> No problem! You can still explore Irish heraldry...", 0.02, Color.CYAN)
                time.sleep(1)
                return False
            else:
                print(Color.RED + "    Please answer 'yes' or 'no'" + Color.RESET)

    def normalize_surname(self, surname):
        """Normalize surname for matching"""
        return surname.upper().strip().replace("'", "").replace(" ", "")

    def hodges_easter_egg(self):
        """Easter egg for when someone searches 'Hodges' (Scottish surname)"""
        import random

        # Matrix code crash effect - scrolling effect
        matrix_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%^&*()_+-=[]{}|;:,.<>?/"

        # Create scrolling matrix effect by repeatedly clearing and redrawing
        for frame in range(6):
            self.clear_screen()
            print(Color.GREEN, end='')
            for _ in range(30):  # 30 lines of matrix
                line = ""
                for _ in range(80):
                    line += random.choice(matrix_chars)
                print(line)
            print(Color.RESET, end='')
            sys.stdout.flush()
            time.sleep(0.06)

        # Flash effect
        for _ in range(3):
            self.clear_screen()
            time.sleep(0.1)
            print(Color.GREEN)
            for _ in range(30):
                line = ""
                for _ in range(80):
                    line += random.choice(matrix_chars)
                print(line)
            print(Color.RESET)
            sys.stdout.flush()
            time.sleep(0.1)

        # Transition to glitchy text
        time.sleep(0.3)
        self.clear_screen()

        # Glitchy text effect
        glitch_messages = [
            "ERRO̴R̷:̶ ̸D̴A̷T̸A̴B̶A̴S̷E̸ ̶C̷O̸R̴R̶U̴P̷T̸I̴O̷N̸ ̶D̴E̷T̸E̴C̶T̸E̷D̸",
            "W̷A̸R̶N̴I̷N̸G̶:̴ ̷N̸O̶N̴-̷I̸R̶I̴S̷H̸ ̶S̴U̷R̸N̶A̴M̷E̸ ̶D̴E̷T̸E̶C̴T̷E̸D̶",
            "S̷Y̸S̶T̴E̷M̸ ̶F̴A̷I̸L̶U̴R̷E̸ ̶I̴M̷M̸I̶N̴E̷N̸T̶.̴.̷.̸"
        ]

        for msg in glitch_messages:
            print(Color.RED + Color.BOLD + "\n\n" + msg.center(80) + Color.RESET)
            sys.stdout.flush()
            time.sleep(0.6)

        time.sleep(0.8)
        self.clear_screen()

        # Final warning screen
        print(Color.RED + Color.BOLD)
        print("\n" + "=" * 80)
        print("  ██████╗ ██████╗ ██╗████████╗██╗ ██████╗ █████╗ ██╗         ███████╗██████╗ ██████╗  ██████╗ ██████╗ ")
        print(" ██╔════╝██╔══██╗██║╚══██╔══╝██║██╔════╝██╔══██╗██║         ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗")
        print(" ██║     ██████╔╝██║   ██║   ██║██║     ███████║██║         █████╗  ██████╔╝██████╔╝██║   ██║██████╔╝")
        print(" ██║     ██╔══██╗██║   ██║   ██║██║     ██╔══██║██║         ██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗")
        print(" ╚██████╗██║  ██║██║   ██║   ██║╚██████╗██║  ██║███████╗    ███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║")
        print("  ╚═════╝╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝")
        print("=" * 80)
        print(Color.RESET)

        print(Color.YELLOW + "\n  ╔══════════════════════════════════════════════════════════════════════════╗")
        print(Color.YELLOW + "  ║                      ⚠️  ALERT: NON-IRISH SURNAME DETECTED  ⚠️            ║")
        print(Color.YELLOW + "  ╚══════════════════════════════════════════════════════════════════════════╝" + Color.RESET)

        print(Color.WHITE + "\n  The surname " + Color.BOLD + Color.RED + "HODGES" + Color.RESET + Color.WHITE + " is of SCOTTISH origin, not Irish!")
        print()
        print(Color.CYAN + "  According to historical records:")
        print(Color.WHITE + "  • Origin: Scottish/English")
        print(Color.WHITE + "  • Meaning: 'Son of Hodge' (a medieval form of Roger)")
        print(Color.WHITE + "  • First found: County Fife, Scotland")
        print()
        print(Color.YELLOW + "  This surname does not appear in authentic Irish heraldic records.")
        print(Color.YELLOW + "  You may want to consult Scottish heraldic authorities instead." + Color.RESET)

        print(Color.RED + "\n  ════════════════════════════════════════════════════════════════════════" + Color.RESET)
        print()

        input(Color.CYAN + "  Press ENTER to return to the tome..." + Color.RESET)

        return None

    def find_surname(self, input_surname):
        """Find all entries for a surname in database"""
        normalized_input = self.normalize_surname(input_surname)

        matches = []
        for key, data in IRISH_HERALDRY.items():
            # Check main surname
            if self.normalize_surname(data['surname']) == normalized_input:
                matches.append(key)

        return matches if matches else None

    def search_surname(self):
        """Search for a surname"""
        self.clear_screen()
        print(Color.CYAN + "\n    ╔═══════════════════════════════════════════════════════╗")
        print("    ║                                                       ║")
        print("    ║        ANCIENT GAELIC HERALDRY TOME                   ║")
        print("    ║                                                       ║")
        print("    ╚═══════════════════════════════════════════════════════╝" + Color.RESET)
        print()

        # Typewriter effect for the prompt
        print()
        for char in "    >> Speak your family name, traveler...":
            sys.stdout.write(Color.YELLOW + char + Color.RESET)
            sys.stdout.flush()
            time.sleep(0.05)
        print()
        surname_input = input(Color.YELLOW + "    >> " + Color.RESET).strip()

        # Secret shortcuts
        if self.check_menu_shortcut(surname_input):
            return 'menu'
        elif self.check_zoltar(surname_input):
            return 'zoltar'

        if not surname_input:
            print(Color.RED + "\n    >> The ancient tome requires a name to reveal its secrets!" + Color.RESET)
            time.sleep(1.5)
            return None

        # Easter egg for Hodges (Scottish surname)
        if self.normalize_surname(surname_input) == "HODGES":
            return self.hodges_easter_egg()

        # Search database
        print()
        self.print_slow("    >> Consulting the ancient heraldic records...", 0.02, Color.CYAN)
        self.print_slow("    >> Searching through centuries of Irish lineage...", 0.02, Color.GREEN)

        found_keys = self.find_surname(surname_input)

        if found_keys:
            print(Color.GREEN + "\n    >> The ancient tome glows with recognition!" + Color.RESET)

            if len(found_keys) > 1:
                print(Color.YELLOW + f"    >> Found {len(found_keys)} heraldic entries for this surname!" + Color.RESET)
            else:
                print(Color.YELLOW + "    >> Your noble lineage has been found!" + Color.RESET)

            time.sleep(1.5)
            self.current_surname = found_keys
            self.search_history.append(surname_input)
            return found_keys
        else:
            print(Color.RED + "\n    >> The ancient scrolls hold no record of this name..." + Color.RESET)
            print(Color.YELLOW + "    >> Try searching the complete surname list (option 3)" + Color.RESET)
            time.sleep(2)
            return None

    def celebration_animation(self):
        """Display celebration animation for multiple entries"""
        frames = [
            {
                "color": Color.YELLOW,
                "lines": [
                    "",
                    "        ════════════════════════════════════════════════════════════",
                    "        ██╗███╗   ██╗ ██████╗██████╗ ███████╗██████╗ ██╗██████╗ ██╗     ███████╗",
                    "        ██║████╗  ██║██╔════╝██╔══██╗██╔════╝██╔══██╗██║██╔══██╗██║     ██╔════╝",
                    "        ██║██╔██╗ ██║██║     ██████╔╝█████╗  ██║  ██║██║██████╔╝██║     █████╗",
                    "        ██║██║╚██╗██║██║     ██╔══██╗██╔══╝  ██║  ██║██║██╔══██╗██║     ██╔══╝",
                    "        ██║██║ ╚████║╚██████╗██║  ██║███████╗██████╔╝██║██████╔╝███████╗███████╗",
                    "        ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝╚═════╝ ╚══════╝╚══════╝",
                    "",
                    "                    *** INCREDIBLE DISCOVERY! ***",
                    "        ════════════════════════════════════════════════════════════",
                    ""
                ]
            },
            {
                "color": Color.CYAN,
                "lines": [
                    "",
                    "",
                    "",
                    "         █████╗ ███╗   ███╗ █████╗ ███████╗██╗███╗   ██╗ ██████╗ ",
                    "        ██╔══██╗████╗ ████║██╔══██╗╚══███╔╝██║████╗  ██║██╔════╝ ",
                    "        ███████║██╔████╔██║███████║  ███╔╝ ██║██╔██╗ ██║██║  ███╗",
                    "        ██╔══██║██║╚██╔╝██║██╔══██║ ███╔╝  ██║██║╚██╗██║██║   ██║",
                    "        ██║  ██║██║ ╚═╝ ██║██║  ██║███████╗██║██║ ╚████║╚██████╔╝",
                    "        ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ",
                    "",
                    "",
                    "",
                    ""
                ]
            },
            {
                "color": Color.MAGENTA,
                "lines": [
                    "",
                    "",
                    "",
                    "        ██╗    ██╗ ██████╗ ██╗    ██╗██╗██╗██╗██╗██╗██╗",
                    "        ██║    ██║██╔═══██╗██║    ██║██║██║██║██║██║██║",
                    "        ██║ █╗ ██║██║   ██║██║ █╗ ██║██║██║██║██║██║██║",
                    "        ██║███╗██║██║   ██║██║███╗██║╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝",
                    "        ╚███╔███╔╝╚██████╔╝╚███╔███╔╝██╗██╗██╗██╗██╗██╗",
                    "         ╚══╝╚══╝  ╚═════╝  ╚══╝╚══╝ ╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝",
                    "",
                    "              +++ ASTONISHING FIND! +++",
                    "",
                    ""
                ]
            },
            {
                "color": Color.GREEN,
                "lines": [
                    "",
                    "",
                    "",
                    "        ███╗   ███╗██╗   ██╗██╗  ████████╗██╗██████╗ ██╗     ███████╗",
                    "        ████╗ ████║██║   ██║██║  ╚══██╔══╝██║██╔══██╗██║     ██╔════╝",
                    "        ██╔████╔██║██║   ██║██║     ██║   ██║██████╔╝██║     █████╗",
                    "        ██║╚██╔╝██║██║   ██║██║     ██║   ██║██╔═══╝ ██║     ██╔══╝",
                    "        ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║██║     ███████╗███████╗",
                    "        ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═╝     ╚══════╝╚══════╝",
                    "",
                    "        ███████╗███╗   ██╗████████╗██████╗ ██╗███████╗███████╗",
                    "        ██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██║██╔════╝██╔════╝",
                    "        █████╗  ██╔██╗ ██║   ██║   ██████╔╝██║█████╗  ███████╗",
                    "        ██╔══╝  ██║╚██╗██║   ██║   ██╔══██╗██║██╔══╝  ╚════██║",
                    "        ███████╗██║ ╚████║   ██║   ██║  ██║██║███████╗███████║",
                    "        ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝",
                    ""
                ]
            },
            {
                "color": Color.BLUE,
                "lines": [
                    "",
                    "",
                    "",
                    "        ████████╗██╗  ██╗██╗███████╗    ██╗███████╗",
                    "        ╚══██╔══╝██║  ██║██║██╔════╝    ██║██╔════╝",
                    "           ██║   ███████║██║███████╗    ██║███████╗",
                    "           ██║   ██╔══██║██║╚════██║    ██║╚════██║",
                    "           ██║   ██║  ██║██║███████║    ██║███████║",
                    "           ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝    ╚═╝╚══════╝",
                    "",
                    "           ██████╗  █████╗ ██████╗ ███████╗██╗",
                    "           ██╔══██╗██╔══██╗██╔══██╗██╔════╝██║",
                    "           ██████╔╝███████║██████╔╝█████╗  ██║",
                    "           ██╔══██╗██╔══██║██╔══██╗██╔══╝  ╚═╝",
                    "           ██║  ██║██║  ██║██║  ██║███████╗██╗",
                    "           ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝",
                    "",
                    ""
                ]
            }
        ]

        for frame in frames:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n\n")
            for line in frame["lines"]:
                print(frame["color"] + Color.BOLD + line + Color.RESET)
            sys.stdout.flush()
            time.sleep(0.6)

        time.sleep(0.4)

    def display_multiple_options(self, surname_keys):
        """Display options when multiple entries exist"""
        # Show celebration animation
        self.celebration_animation()

        self.clear_screen()

        print(Color.CYAN + "\n  ══════════════════════════════════════════════════════════" + Color.RESET)
        print(Color.YELLOW + Color.BOLD + "  MULTIPLE HERALDIC ENTRIES FOUND" + Color.RESET)
        print(Color.CYAN + "  ══════════════════════════════════════════════════════════" + Color.RESET)
        print()

        # Get surname from first entry
        surname = IRISH_HERALDRY[surname_keys[0]]['surname']
        print(Color.WHITE + f"  The surname {Color.BOLD}{surname}{Color.RESET}{Color.WHITE} appears in {len(surname_keys)} entries:" + Color.RESET)
        print()

        # Display disclaimer about multiple coats of arms
        print(Color.CYAN + "  ┌──────────────────────────────────────────────────────────┐" + Color.RESET)
        print(Color.YELLOW + "  │ " + Color.WHITE + "Why Multiple Coats of Arms?" + Color.YELLOW + "                             │" + Color.RESET)
        print(Color.CYAN + "  ├──────────────────────────────────────────────────────────┤" + Color.RESET)
        print(Color.WHITE + "  │ Under Irish heraldic tradition, every family branch      │")
        print("  │ (sept) that bore the same surname could have its own     │")
        print("  │ coat of arms. Unlike the English system, Irish heraldry  │")
        print("  │ treated arms as shared heirlooms of the wider family    │")
        print("  │ name. Each entry below represents a distinct lineage.   │")
        print(Color.CYAN + "  └──────────────────────────────────────────────────────────┘" + Color.RESET)
        print()

        # Display all options
        for idx, key in enumerate(surname_keys, 1):
            data = IRISH_HERALDRY[key]
            crest_type = "COAT OF ARMS" if "CREST" in data['crest_code'].upper() and "insignia" not in data['crest_code'].lower() else "INSIGNIA"

            print(Color.GREEN + f"  [{idx}] " + Color.YELLOW + f"{crest_type}" + Color.RESET)
            print(Color.WHITE + f"      {data['crest_code']}" + Color.RESET)
            print(Color.CYAN + f"      Page {data['page']}" + Color.RESET)
            print()

        print(Color.CYAN + "  ══════════════════════════════════════════════════════════" + Color.RESET)
        print()

        while True:
            choice = input(Color.YELLOW + f"  Select entry (1-{len(surname_keys)}), 'all' for comparison, or 0 to skip: " + Color.RESET).strip()

            if self.check_menu_shortcut(choice):
                return 'menu'
            elif self.check_zoltar(choice):
                return 'zoltar'
            elif choice == '0':
                return None
            elif choice.lower() == 'all':
                return 'all'

            try:
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(surname_keys):
                    return surname_keys[choice_idx]
                else:
                    print(Color.RED + f"  Please enter a number between 1 and {len(surname_keys)}, 'all', or 0" + Color.RESET)
            except ValueError:
                print(Color.RED + "  Please enter a valid number, 'all', or 0" + Color.RESET)

    def wrap_text(self, text, width):
        """Wrap text to fit within specified width"""
        if len(text) <= width:
            return [text]

        words = text.split()
        lines = []
        current_line = []
        current_length = 0

        for word in words:
            if current_length + len(word) + len(current_line) <= width:
                current_line.append(word)
                current_length += len(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)

        if current_line:
            lines.append(' '.join(current_line))

        return lines

    def display_all_comparison(self, surname_keys):
        """Display all entries side-by-side for comparison"""
        self.clear_screen()
        print('\033[H', end='')

        surname = IRISH_HERALDRY[surname_keys[0]]['surname']

        print(Color.YELLOW + "\n  ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
        print(f"  ║  COMPARISON VIEW: {surname.upper():^137}  ║")
        print("  ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝" + Color.RESET)
        print()

        # Display all entries with full information
        for i, key in enumerate(surname_keys, 1):
            data = IRISH_HERALDRY[key]
            art = COAT_OF_ARMS_ART.get(key, None)
            crest_type = "COAT OF ARMS" if "CREST" in data['crest_code'].upper() and "insignia" not in data['crest_code'].lower() else "INSIGNIA"

            # Display entry header
            print(Color.YELLOW + Color.BOLD + f"  [{i}] {crest_type}" + Color.RESET)
            print(Color.CYAN + f"  Crest Code: " + Color.WHITE + f"{data['crest_code']}" + Color.RESET)
            print(Color.CYAN + f"  Page: " + Color.WHITE + f"{data['page']}" + Color.RESET)
            print()

            # Display coat of arms ASCII art if available
            if art:
                print(Color.SILVER + art + Color.RESET)
            else:
                print(Color.MAGENTA + "  [ASCII art not yet digitized for this entry]" + Color.RESET)
                print()

            # Display motto information with wrapping
            if data.get('motto'):
                motto_lines = self.wrap_text(data['motto'], 140)
                print(Color.YELLOW + f"  Motto: " + Color.WHITE + motto_lines[0] + Color.RESET)
                for line in motto_lines[1:]:
                    print(Color.WHITE + f"         {line}" + Color.RESET)
            else:
                print(Color.YELLOW + f"  Motto: " + Color.RED + "[No motto recorded]" + Color.RESET)

            if data.get('motto_language'):
                print(Color.YELLOW + f"  Language: " + Color.WHITE + f"{data['motto_language']}" + Color.RESET)
            else:
                print(Color.YELLOW + f"  Language: " + Color.RED + "[Translation research needed]" + Color.RESET)

            if data.get('motto_translation'):
                trans_lines = self.wrap_text(data['motto_translation'], 140)
                print(Color.YELLOW + f"  Translation: " + Color.WHITE + trans_lines[0] + Color.RESET)
                for line in trans_lines[1:]:
                    print(Color.WHITE + f"               {line}" + Color.RESET)
            else:
                print(Color.YELLOW + f"  Translation: " + Color.RED + "[Translation research needed]" + Color.RESET)

            # Separator between entries
            print(Color.CYAN + "\n  " + "─" * 145 + Color.RESET)
            print()

        print(Color.GREEN + "  >> All {0} heraldic records for this surname displayed above".format(len(surname_keys)) + Color.RESET)
        print()

        # Allow selection of individual entries for detailed view
        while True:
            print(Color.YELLOW + f"  >> Enter entry number (1-{len(surname_keys)}) to view full coat of arms,")
            print(f"     'all' to view this comparison again, or 'menu' to return to main menu" + Color.RESET)
            print()

            choice = input(Color.YELLOW + "  ▸ Your choice: " + Color.RESET).strip().lower()

            if self.check_menu_shortcut(choice):
                return
            elif self.check_zoltar(choice):
                # Navigate to search
                self.skip_to_search = True
                return
            elif choice == 'menu':
                return
            elif choice == 'all':
                self.display_all_comparison(surname_keys)
                return
            else:
                try:
                    choice_idx = int(choice) - 1
                    if 0 <= choice_idx < len(surname_keys):
                        # Inner loop to allow cycling through entries
                        current_idx = choice_idx
                        while True:
                            self.display_coat_of_arms(surname_keys[current_idx])
                            # After viewing, ask what to do next
                            print()
                            print(Color.CYAN + "  ─" * 65 + Color.RESET)
                            print(Color.YELLOW + "\n  >> What would you like to do next?" + Color.RESET)
                            print(Color.CYAN + "     [1-" + str(len(surname_keys)) + "]" + Color.WHITE + " View another entry" + Color.RESET)
                            print(Color.CYAN + "     [all]" + Color.WHITE + " Return to comparison view" + Color.RESET)
                            print(Color.CYAN + "     [menu]" + Color.WHITE + " Return to main menu" + Color.RESET)
                            print()
                            next_choice = input(Color.YELLOW + "  ▸ Your choice: " + Color.RESET).strip().lower()

                            if self.check_menu_shortcut(next_choice):
                                return
                            elif self.check_zoltar(next_choice):
                                self.skip_to_search = True
                                return
                            elif next_choice == 'menu':
                                return
                            elif next_choice == 'all':
                                self.display_all_comparison(surname_keys)
                                return
                            else:
                                try:
                                    next_idx = int(next_choice) - 1
                                    if 0 <= next_idx < len(surname_keys):
                                        # Update current index and loop to display new entry
                                        current_idx = next_idx
                                        continue
                                except ValueError:
                                    pass
                                # If invalid, show comparison view again
                                self.clear_screen()
                                self.display_all_comparison(surname_keys)
                                return
                    else:
                        print(Color.RED + f"  Please enter a number between 1 and {len(surname_keys)}, 'all', or 'menu'" + Color.RESET)
                except ValueError:
                    print(Color.RED + "  Please enter a valid number, 'all', or 'menu'" + Color.RESET)

    def display_coat_of_arms(self, surname_key):
        """Display the coat of arms for the surname"""
        self.clear_screen()
        # Move cursor to top of screen
        print('\033[H', end='')

        data = IRISH_HERALDRY[surname_key]
        art = COAT_OF_ARMS_ART.get(surname_key, "ASCII art not available")

        # Display ornate title (start at top, no extra newlines)
        surname_text = f"THE NOBLE HOUSE OF {data['surname'].upper()}"
        print(Color.YELLOW + "\n" + "  ╔═══════════════════════════════════════════════════════════════╗")
        print("  ║                                                               ║")
        print(Color.BOLD + f"  ║  {surname_text:^59}  ║" + Color.RESET + Color.YELLOW)
        print("  ║                                                               ║")
        print("  ╚═══════════════════════════════════════════════════════════════╝" + Color.RESET)

        # Display coat of arms with decorative borders
        print(Color.CYAN + "\n  ┌───────────────────────────────────────────────────────────────┐" + Color.RESET)
        print(Color.SILVER + art + Color.RESET)
        print(Color.CYAN + "  └───────────────────────────────────────────────────────────────┘" + Color.RESET)

        # Display Motto Information
        print(Color.CYAN + "\n  ┌─────────────────────────────────────────────────────────────┐")
        print("  │                    MOTTO INFORMATION                        │")
        print("  └─────────────────────────────────────────────────────────────┘" + Color.RESET)
        print()

        if data.get('motto'):
            print(Color.YELLOW + f"  Motto: " + Color.WHITE + f"{data['motto']}" + Color.RESET)
        else:
            print(Color.YELLOW + f"  Motto: " + Color.RED + "[No motto recorded]" + Color.RESET)

        if data.get('motto_language'):
            print(Color.YELLOW + f"  Language: " + Color.WHITE + f"{data['motto_language']}" + Color.RESET)
        else:
            print(Color.YELLOW + f"  Language: " + Color.RED + "[Translation research needed]" + Color.RESET)

        if data.get('motto_translation'):
            print(Color.YELLOW + f"  Translation: " + Color.WHITE + f"{data['motto_translation']}" + Color.RESET)
        else:
            print(Color.YELLOW + f"  Translation: " + Color.RED + "[Translation research needed]" + Color.RESET)

        # Guild Reference Section (for staff use)
        print(Color.MAGENTA + "\n  ┌─────────────────────────────────────────────────────────────┐")
        print("  │         GUILD REFERENCE - For Research Assistance           │")
        print("  ├─────────────────────────────────────────────────────────────┤")
        print(Color.WHITE + f"  │  Crest Code: {data['crest_code']:<45} │" + Color.MAGENTA)
        print(Color.WHITE + f"  │  Page Number: {str(data['page']):<44} │" + Color.MAGENTA)
        print("  └─────────────────────────────────────────────────────────────┘" + Color.RESET)
        print()

    def show_menu(self):
        """Show main menu"""
        print()
        print(Color.YELLOW + "  ╔═══════════════════════════════════════╗" + Color.RESET)
        print(Color.YELLOW + "  ║          WHAT WOULD YOU LIKE?         ║" + Color.RESET)
        print(Color.YELLOW + "  ╚═══════════════════════════════════════╝" + Color.RESET)
        print()
        print(Color.CYAN + "  [1]" + Color.WHITE + " Search another surname" + Color.RESET)
        print(Color.CYAN + "  [2]" + Color.WHITE + " View search history" + Color.RESET)
        print(Color.CYAN + "  [3]" + Color.WHITE + " List all available surnames" + Color.RESET)
        print(Color.CYAN + "  [4]" + Color.WHITE + " About The Guild" + Color.RESET)
        print(Color.CYAN + "  [5]" + Color.WHITE + " Exit" + Color.RESET)
        print()

        choice = input(Color.YELLOW + "  ▸ Your choice: " + Color.RESET).strip()

        # Check for shortcuts
        if self.check_menu_shortcut(choice):
            return choice  # Stay in menu
        elif self.check_zoltar(choice):
            return '1'  # Go to search

        return choice

    def show_available_surnames(self):
        """Show all surnames in database"""
        self.clear_screen()
        print(Color.CYAN + "\n  ══════════════════════════════════════════════════════════" + Color.RESET)
        print(Color.YELLOW + Color.BOLD + "  AVAILABLE IRISH SURNAMES IN DATABASE" + Color.RESET)
        print(Color.CYAN + "  ══════════════════════════════════════════════════════════" + Color.RESET)
        print()

        # Get unique surnames with their page numbers
        surnames_dict = {}
        for key, data in IRISH_HERALDRY.items():
            surname = data['surname']
            page = data['page']
            # Only add if not already in dict, or if it's the first occurrence
            if surname not in surnames_dict:
                surnames_dict[surname] = page

        # Sort alphabetically
        surnames_list = sorted(surnames_dict.items(), key=lambda x: x[0])

        for surname, page in surnames_list:
            print(Color.GREEN + f"  ▸ {surname}" + Color.WHITE + f" (Page {page})" + Color.RESET)

        print(Color.CYAN + f"\n  Total: {len(surnames_list)} unique surnames" + Color.RESET)
        print(Color.YELLOW + f"  Note: Some surnames have multiple coats of arms" + Color.RESET)
        input(Color.YELLOW + "\n  Press ENTER to continue..." + Color.RESET)

    def show_search_history(self):
        """Show search history"""
        self.clear_screen()
        print(Color.CYAN + "\n  ══════════════════════════════════════════════════════════" + Color.RESET)
        print(Color.YELLOW + Color.BOLD + "  YOUR SEARCH HISTORY" + Color.RESET)
        print(Color.CYAN + "  ══════════════════════════════════════════════════════════" + Color.RESET)
        print()

        if not self.search_history:
            print(Color.RED + "  No searches yet." + Color.RESET)
        else:
            for i, surname in enumerate(self.search_history, 1):
                print(Color.GREEN + f"  {i}. " + Color.WHITE + surname + Color.RESET)

        print()
        input(Color.YELLOW + "  Press ENTER to continue..." + Color.RESET)

    def show_about(self):
        """Show information about The Guild"""
        self.clear_screen()
        print(Color.YELLOW + "\n  ╔═══════════════════════════════════════════════════════════════╗")
        print("  ║                                                               ║")
        print(Color.BOLD + "  ║          THE GUILD OF HERALDIC ARTS & RESEARCH                ║" + Color.RESET + Color.YELLOW)
        print("  ║                    Nonprofit 501(c)(3)                        ║")
        print("  ║                                                               ║")
        print("  ╚═══════════════════════════════════════════════════════════════╝" + Color.RESET)
        print()
        print(Color.CYAN + "  ══════════════════════════════════════════════════════════════" + Color.RESET)
        print(Color.WHITE + "\n  The Guild of Heraldic Arts & Research is a nonprofit")
        print("  organization dedicated to the preservation, documentation,")
        print("  and education of heraldry and its associated arts.")
        print()
        print("  Our mission is to build the world's most comprehensive")
        print("  heraldic library, digitize rare and historical records, and")
        print("  provide public access to authentic heraldic knowledge.")
        print()
        print("  Through research, archival work, and educational outreach,")
        print("  we aim to safeguard the cultural heritage embedded in coats")
        print("  of arms, family crests, and armorial traditions worldwide.")
        print(Color.RESET)
        print(Color.CYAN + "  ══════════════════════════════════════════════════════════════" + Color.RESET)
        print(Color.GREEN + "\n  For more information about your heraldic heritage,")
        print("  contact The Guild of Heraldic Arts & Research." + Color.RESET)
        print(Color.CYAN + "  ══════════════════════════════════════════════════════════════" + Color.RESET)
        print()
        input(Color.YELLOW + "  Press ENTER to continue..." + Color.RESET)

    def run(self):
        """Main application loop"""
        self.display_title()

        # Ask if Irish (unless shortcuts were used)
        if not self.skip_to_menu and not self.skip_to_search:
            is_irish = self.ask_if_irish()
            if is_irish == 'menu':
                self.skip_to_menu = True
            elif is_irish == 'zoltar':
                self.skip_to_search = True
            else:
                time.sleep(1)

        # If menu shortcut was used, skip to menu
        if self.skip_to_menu:
            self.clear_screen()

        while True:
            # Search for surname (unless menu shortcut was used)
            if not self.skip_to_menu:
                result = self.search_surname()

                if result == 'menu':
                    self.skip_to_menu = True
                elif result == 'zoltar':
                    self.skip_to_search = True
                    continue
                elif result and result not in ['menu', 'zoltar']:
                    # If multiple entries, let user choose
                    if isinstance(result, list) and len(result) > 1:
                        selected_key = self.display_multiple_options(result)
                        if selected_key == 'menu':
                            self.skip_to_menu = True
                        elif selected_key == 'zoltar':
                            self.skip_to_search = True
                            continue
                        elif selected_key == 'all':
                            self.display_all_comparison(result)
                        elif selected_key:
                            self.display_coat_of_arms(selected_key)
                    elif isinstance(result, list) and len(result) == 1:
                        self.display_coat_of_arms(result[0])
                    else:
                        # Single result (old format compatibility)
                        self.display_coat_of_arms(result)

            # Reset skip flags after first use
            self.skip_to_menu = False
            self.skip_to_search = False

            # Show menu
            choice = self.show_menu()

            if choice == '1':
                continue
            elif choice == '2':
                self.show_search_history()
            elif choice == '3':
                self.show_available_surnames()
            elif choice == '4':
                self.show_about()
            elif choice == '5':
                self.clear_screen()
                print()
                print(Color.GREEN + "  ╔════════════════════════════════════════════════════╗")
                print("  ║                                                    ║")
                print("  ║    Thank you for exploring Irish Heraldry!         ║")
                print("  ║                                                    ║")
                print("  ║         " + Color.CYAN + "Slán go fóill! (Goodbye!)" + Color.GREEN + "                ║")
                print("  ║                                                    ║")
                print("  ╚════════════════════════════════════════════════════╝" + Color.RESET)
                print()
                break
            else:
                print(Color.RED + "  Invalid choice. Please try again." + Color.RESET)
                time.sleep(1)

def main():
    """Entry point"""
    try:
        app = IrishHeraldrySearch()
        app.run()
    except KeyboardInterrupt:
        print(Color.YELLOW + "\n\n  Program interrupted. Slán!" + Color.RESET)
        sys.exit(0)

if __name__ == "__main__":
    main()
