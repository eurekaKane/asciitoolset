# -*- encoding: utf-8 -*-

"""
This script is meant to test and get familiar with the different objects of the module
before using it in your scripts
"""

# IMPORTS

from source.tutorial import *

# COPYRIGHT
__copyright__ = """
The MIT License (MIT)
Copyright © 2023 - 2024
Author: Ernest BECHTOLD-DALBERA <eurekakane@proton.me>
"""


def main():
    while True:
        # HEAD / INTRO
        clr()
        testBan.printBanner()
        testSsmall.print_spacer(13)
        ansi.ansi_print(__copyright__, 'yellow')
        ansi.ansi_print(long_des, (119,0,143))
        testSsmall.print_spacer(13)
        testSpc.print_spacer(40)
        ansi.ansi_print("Bienvenue sur ce petit tutoriel visant a montrer les principales fonctionnalités du module "
                    "asciitoolset", "green")
        testSpc.print_spacer(40)
        banTest()
        testSpc.print_spacer(40)
        spcTest()
        testSpc.print_spacer(40)
        redo()


if __name__ == '__main__':
    main()
