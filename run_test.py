# -*- encoding : utf-8 -*-

# IMPORTS

from source.tests.test_all import *


def main():
    """
    Test script for asciitoolset
    :return:
    """

    # INTRO

    spc = Spacer(shape = '1', color = "red")
    myBan = Banner('doom', "blue", "DooM")
    ansi.ansi_print(f'DEBUG : {os.getcwd()}', 'yellow')
    myBan.printBanner()
    spc.print_spacer(10)

    try:
        roll('red', 'Ct une VANNE !')

    except FigletError:

        spc.set(color = 'green')
        ansi.ansi_print("Oops! Smth went wrong running testFonts() to see which font isn't working", "red")
        spc.print_spacer(10)
        test_fonts()

        if input('Do you want to fix the fonts ? (y/n) : ') == 'y':
            fix_fonts()

    finally:

        ansi.ansi_print('Everything is working !', 'green')

    clr()
    test_fonts()

    os.removedirs()


if __name__ == '__main__':
    main()
