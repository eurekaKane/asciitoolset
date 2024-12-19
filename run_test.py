# -*- encoding : utf-8 -*-

# IMPORTS

from source.tests.test_all import *


def main():
    """
    Test script for asciitoolset
    :return:
    """

    # INTRO

    spc = Spacer('1', "red")
    myBan = Banner('doom', "blue", "DooM")
    tcol.cprint(f'DEBUG : {os.getcwd()}', 'yellow')
    myBan.printBanner()
    spc.spPrint(10)

    try:
        roll('red', 'DoxBin for Kislitsyn :)')
    except FigletError:
        spc.setColor('green')
        tcol.cprint("Oops! Smth went wrong running testFonts() to see which font isn't working", "red")
        spc.spPrint(10)
        testFonts()
        if input('Do you want to fix the fonts ? (y/n) : ') == 'y':
            fixFonts()
    finally:
        tcol.cprint('Everything is working !', 'green')
    clr()
    testFonts()


if __name__ == '__main__':
    main()
