# -*- encoding: utf-8 -*-

"""
This is the standalone test version of a project that allows you
to manipulate characters to make clean terminal based programs
"""

# IMPORTS
from asciitoolset import makeBanner, makeSpacer, showShapes, clr
from termcolor import termcolor as tcol

# QUESTIONS
askTxt = "QUE SOUHAITEZ VOUS ÉCRIRE ? :\n"
askFnt = "QUELLE POLICE ? :\n"
askCol = "QUELLE COULEUR ? (en anglais) :\n"
askLen = "QUELLE LONGUEUR ? :\n"
askShape = "QUELLE FORME ? \n"
askRedo = "VOULEZ VOUS RE-TESTER ? (y/n) :\n"

# SHAPES
shapes = {
    1: "|-|_",
    2: "####",
    3: "/-/-",
    4: "~~~~",
    5: "====",
    6: "=+=+",
    7: "$%$%",
    8: "/*/*",
    9: "////",
    10: ">>>>"
}

# COLORS
colors = {
    1: "red",
    2: "green",
    3: "yellow",
    4: "blue",
    5: "magenta",
    6: "cyan",
}


def main():
    """
    Interactive set of tests for the main functions of
    the "asciitoolset" module
    """
    clr()
    while True:
        # HEAD / INTRO
        makeBanner("asciiTest", "slant", "red")
        makeSpacer(1, 100, "blue")
        tcol.cprint("Ceci est un module de test destiné à tester asciitoolset.py", "green")
        makeSpacer(1, 100, 'blue')

        while True:
            # TEST makeBanner()
            tcol.cprint("\n| Test bannière |\n", "red")
            makeSpacer(1, 100, "blue")

            print("Palette :\n")
            print("-'black'\n")
            for y in range(len(colors)):
                tcol.cprint(f"-(light_)'{colors[y + 1]}'\n", colors[y + 1])
            print("-'white'\n")

            makeBanner(input(askTxt), input(askFnt), input(askCol))
            makeSpacer(1, 100, "blue")
            # TEST makeSpacer()
            tcol.cprint("| Test éspaceur |\n", "red")
            makeSpacer(1, 100, "blue")

            print("Palette :\n")
            print("-'black'\n")
            for y in range(len(colors)):
                tcol.cprint(f"-(light_)'{colors[y + 1]}'\n", colors[y + 1])
            print("-'white'\n")
            makeSpacer(1, 100, "blue")

            showShapes()
            makeSpacer(input(askShape), int(input(askLen)), input(askCol))
            makeSpacer(1, 100, "blue")
            # RE TEST
            if input(askRedo) == "n":
                return False


if __name__ == "__main__":
    main()
