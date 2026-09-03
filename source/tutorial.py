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


testSpc = Spacer(shape = 5, color = 'red')
testSsmall = Spacer(shape = 3, color = 'blue')
testBan = Banner('graffiti','red','ASCIItlst')


def banTest():
    """
    Simple test protocol for Banner object
    :return:
    """
    ansi.ansi_print("\n| Test bannière |\n", "red")
    testSpc.print_spacer(40)

    show_palette()

    testSsmall.print_spacer(13)
    usrBanner = Banner(input(askFnt), input(f"{testSsmall.print_spacer(13)}\n{askCol}\n"), input(f"{testSsmall.print_spacer(13)}\n{askTxt}\n"))
    testSsmall.print_spacer(13)
    ansi.ansi_print("| Rendu |", "yellow")
    testSpc.print_spacer(13)
    time.sleep(1)
    usrBanner.printBanner()


def spcTest():
    """
    Simple test protocol for Spacer object
    :return:
    """
    ansi.ansi_print("| Test éspaceur |\n", "red")

    testSpc.print_spacer(40)

    show_shapes()
    testSsmall.print_spacer(13)
    usrSpacer = Spacer(shape = input(askShape), color = input(f"{testSsmall.print_spacer(13)}\n{askCol}\n"))
    length = int(input(f"{testSsmall.print_spacer(13)}\n{askLen}"))
    testSpc.print_spacer(40)
    testSsmall.print_spacer(13)
    ansi.ansi_print(" | Rendu | ", 'yellow')
    testSsmall.print_spacer(13)
    time.sleep(1)
    usrSpacer.print_spacer(length)



def redo() -> bool:
    """
    Interface func ask redo at the end of
    tutorial module
    :rtype: object
    """
    if input(askRedo) == "n":
        return False
    else:
        return True

# FIXED : not stopping when input == 'n'
