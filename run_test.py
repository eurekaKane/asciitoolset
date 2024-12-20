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
    spc.sp_print(10)

    try:
        roll('red', 'Ct une VANNE !')

    except FigletError:

        spc.set_color('green')
        tcol.cprint("Oops! Smth went wrong running testFonts() to see which font isn't working", "red")
        spc.sp_print(10)
        test_fonts()

        if input('Do you want to fix the fonts ? (y/n) : ') == 'y':
            fix_fonts()

    finally:

        tcol.cprint('Everything is working !', 'green')

    clr()
    test_fonts()

    os.removedirs()


if __name__ == '__main__':
    main()
