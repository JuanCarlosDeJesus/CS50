"""
 the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font,
 the program should exit via sys.exit with an error message.
"""

from pyfiglet import Figlet
import sys

figlet = Figlet()
figlet.getFonts()

def get_input():
    return input("Input: ").strip()

if len(sys.argv) > 1:
    # s = input("Input: ").strip()
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in figlet.getFonts():
            figlet.setFont(font=sys.argv[2])
            print(f"Output: {figlet.renderText(get_input())}")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    sys.exit("Invalid usage")
else:
    print(f"Output: {figlet.renderText(get_input())}")