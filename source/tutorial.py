# -*- encoding: utf-8 -*-

"""
This script is meant to test and get familiar with the different objects of the module
before using it in your scripts
"""


# IMPORTS

from source.asciitoolset import clr, showPalette, showShapes, Spacer, Banner
from termcolor import termcolor as tcol

# QUESTIONS

askTxt = "QUE SOUHAITEZ VOUS ÉCRIRE ? :\n"
askFnt = "QUELLE POLICE ? :\n"
askCol = "QUELLE COULEUR ? (en anglais) :\n"
askLen = "QUELLE LONGUEUR ? :\n"
askShape = "QUELLE FORME ? \n"
askRedo = "VOULEZ VOUS RE-TESTER ? (y/n) :\n"


testSpc = Spacer(5, 'red')
testBan = Banner('graffiti','red','ASCIItlst')


def banTest():
    tcol.cprint("\n| Test bannière |\n", "red")
    testSpc.spPrint(50)

    showPalette()

    usrBanner = Banner(input(askFnt), input(askCol), input(askTxt))
    usrBanner.printBanner()


def spcTest():
    tcol.cprint("| Test éspaceur |\n", "red")

    testSpc.spPrint(50)

    showShapes()

    usrSpacer = Spacer(input(askShape), input(askCol))
    testSpc.spPrint(50)
    usrSpacer.spPrint(int(input(askLen)))


def redo() -> bool:
    """

    :rtype: object
    """
    if input(askRedo) == "n":
        clr()
        return False
    else:
        clr()

# FIXED : not stopping when input == 'n'
