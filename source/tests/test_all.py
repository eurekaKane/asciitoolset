# -*- encoding : utf-8 -*-
from pyfiglet import FontNotFound


# IMPORTS

from source.asciitoolset import *

from source.utils.utils import __local, __tmp



failed_fonts = []
working_fonts = []

def roll(col, txt):
    """
    Roll through every font in the font list and renders a Banner for each with the specified parameters
    :param col: color to display
    :param txt: text to display
    :return: None
    """
    font_list = get_fnt_list()

    spc = Spacer(shape = 2, color ='white')

    for font in font_list:
        roll_ban = Banner(font, col, txt, width = 100)
        print(ansi.ansi_comb(f'{roll_ban.__repr__()}\n', 'green'))
        roll_ban.printBanner()
        spc.print_spacer(175)

    return None


def test_fonts():
    tmp_list = get_fnt_list()

    for font in tmp_list:
        try:
            _ = Figlet(font)
        except FontNotFound:
            failed_fonts.append(font)
            print(ansi.ansi_comb(font, 'red'))
        else:
            working_fonts.append(font)
            print(ansi.ansi_comb(font, 'green'))

    print(ansi.ansi_comb(failed_fonts, 'red'))


def fix_fonts():
    tmp_list = get_fnt_list()
    checked_fonts = []
    with open(__tmp+'\\fontList.txt', 'w') as file:
        file.truncate()
        file.close()

    with open(__tmp+'\\fontList.txt', 'w') as file:
        for font in tmp_list:
            for _ in failed_fonts:
                if font in checked_fonts:
                    pass
                elif font in failed_fonts:
                    checked_fonts.append(font)
                else:
                    file.write(font + '\n')
                    checked_fonts.append(font)
