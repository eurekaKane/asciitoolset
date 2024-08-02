# -*- encoding: utf-8 -*-

"""
This script is meant to test and get familiar with the different objects of the module
before using it in your scripts
"""

# IMPORTS

from source.test_func import*


def main():
    while True:
        # HEAD / INTRO
        clr()
        testBan.printBanner()
        testSpc.spPrint(50)
        tcol.cprint("Ceci est un module de test destiné à tester asciitoolset.py", "green")
        testSpc.spPrint(50)
        banTest()
        testSpc.spPrint(50)
        spcTest()
        testSpc.spPrint(50)
        return redo()



if __name__ == '__main__':
    main()
