# -*- encoding: utf-8 -*-

"""
This script is meant to test and get familiar with the different objects of the module
before using it in your scripts
"""


# IMPORTS

from source.asciitoolset import *

from source.utils.utils import *

# COPYRIGHT
__copyright__ = """
The MIT License (MIT)
Copyright © 2023 - 2024
Author: Ernest BECHTOLD-DALBERA <eurekakane@proton.me>
"""

# QUESTIONS

askTxt = "QUE SOUHAITEZ VOUS ÉCRIRE ? :\n"
askFnt = "QUELLE POLICE ? :\n"
askCol = "QUELLE COULEUR ? (en anglais) :\n"
askLen = "QUELLE LONGUEUR ? :\n"
askShape = "QUELLE FORME ? \n"
askRedo = "VOULEZ VOUS RE-TESTER ? (y/n) :\n"


testSpc = Spacer(5, 'red')
testSsmall = Spacer(3, 'blue')
testBan = Banner('graffiti','red','ASCIItlst')


def banTest():
    """
    Simple test protocol for Banner object
    :return:
    """
    tcol.cprint("\n| Test bannière |\n", "red")
    testSpc.spPrint(40)

    showPalette()

    testSsmall.spPrint(13)
    usrBanner = Banner(input(askFnt), input(f"{testSsmall.spPrint(13)}\n{askCol}\n"), input(f"{testSsmall.spPrint(13)}\n{askTxt}\n"))
    testSsmall.spPrint(13)
    tcol.cprint("| Rendu |", "yellow")
    testSpc.spPrint(13)
    time.sleep(1)
    usrBanner.printBanner()


def spcTest():
    """
    Simple test protocol for Spacer object
    :return:
    """
    tcol.cprint("| Test éspaceur |\n", "red")

    testSpc.spPrint(40)

    showShapes()
    testSsmall.spPrint(13)
    usrSpacer = Spacer(input(askShape), input(f"{testSsmall.spPrint(13)}\n{askCol}\n"))
    length = int(input(f"{testSsmall.spPrint(13)}\n{askLen}"))
    testSpc.spPrint(40)
    testSsmall.spPrint(13)
    tcol.cprint(" | Rendu | ", 'yellow')
    testSsmall.spPrint(13)
    time.sleep(1)
    usrSpacer.spPrint(length)


def redo() -> bool:
    """
    Interface func ask redo at the end of
    tutorial module
    :rtype: object
    """
    if input(askRedo) == "n":
        clr()
        return False
    else:
        clr()
        return True

# FIXED : not stopping when input == 'n'
