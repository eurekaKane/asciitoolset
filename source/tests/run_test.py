# -*- encoding : utf-8 -*-
import time

# IMPORTS

from source.tests.test_all import *


spc = Spacer(shape = '1', color = "red")
myBan = Banner('doom', "blue", "DooM")


def main():
    """
    Test script for asciitoolset
    :return:
    """

    # INTRO
    ansi.ansi_print(f'DEBUG : {os.getcwd()}', 'yellow')
    myBan.print_banner()
    spc.print_spacer(10)


    utils.fibonacci(20, 'black', 'white')


    spc.print_spacer(10)

    try:
        roll('red', 'Ct une vanne')

    except FigletError:

        spc.set(color = 'green')
        ansi.ansi_print("Oops! Smth went wrong running testFonts() to see which font isn't working", "red")
        spc.print_spacer(10)
        test_fonts()

        if input('Do you want to fix the fonts ? (y/n) : ') == 'y':
            fix_fonts()

    finally:

        if len(failed_fonts) == 0:
            ansi.ansi_print('Everything is working !', 'green')
            if input('Do you want to see the fonts again ? (y/n) : ') == 'y':
                roll('red', 'Ct une vanne')
        else:
            if input("Do you want to see what's wrong ? (y/n) : ") == 'y':
                test_fonts()

    utils.tmp_handler('clean')

if __name__ == '__main__':
    main()
