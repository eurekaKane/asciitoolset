# -*- encoding: utf-8 -*-

"""
This is the standalone test version of a project that allows you
to manipulate characters to make clean terminal based programs
"""

# IMPORTS
from asciitoolset import showShapes, Spacer, Banner, clr
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


def showPalette():
    print("Palette :\n")
    print("-'black'\n")
    for y in range(len(colors)):
        tcol.cprint(f"-(light_)'{colors[y + 1]}'\n", colors[y + 1])
    print("-'white'\n")


spacer1 = Spacer(1, "blue")
banner1 = Banner('slant', 'red', 'asciiTest')


def main():
    """
    Interactive set of tests for the main functions of
    the "asciitoolset" module
    """
    clr()
    while True:
        # HEAD / INTRO
        banner1.printBanner()
        spacer1.spPrint(50)
        tcol.cprint("Ceci est un module de test destiné à tester asciitoolset.py", "green")
        spacer1.spPrint(50)
        # TEST makeBanner()
        tcol.cprint("\n| Test bannière |\n", "red")
        spacer1.spPrint(50)

        showPalette()

        usrBanner = Banner(input(askFnt), input(askCol), input(askTxt))
        usrBanner.printBanner()

        spacer1.spPrint(50)

        # TEST makeSpacer()

        tcol.cprint("| Test éspaceur |\n", "red")
        spacer1.spPrint(50)
        showShapes()
        usrSpacer = Spacer(input(askShape), input(askCol))
        usrSpacer.spPrint(int(input(askLen)))
        spacer1.spPrint(50)
        # RE TEST
        if input(askRedo) == "n":
            return False
        else:
            clr()


if __name__ == "__main__":
    main()
