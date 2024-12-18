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
        testSsmall.spPrint(13)
        tcol.cprint(__copyright__, 'yellow')
        tcol.cprint(long_des, 'light_magenta')
        testSsmall.spPrint(13)
        testSpc.spPrint(40)
        tcol.cprint("Bienvenue sur ce petit tutoriel visant a montrer les principales fonctionnalités du module "
                    "asciitoolset", "green")
        testSpc.spPrint(40)
        banTest()
        testSpc.spPrint(40)
        spcTest()
        testSpc.spPrint(40)
        redo()


if __name__ == '__main__':
    main()
