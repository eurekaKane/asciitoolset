# -*- encoding : utf-8 -*-


# IMPORTS

from source.asciitoolset import *

from source.utils import utils

from source.utils.utils import __tmp, __local


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
        print(ansi.ansi_comb(f'{font}\n', 'green'))
        roll_ban.print_banner()
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

    if len(failed_fonts) == 0:
        print(ansi.ansi_comb(failed_fonts, 'red'))
    elif len(failed_fonts) < 0:
        print(ansi.ansi_comb("No problems w/ the font register :)", 'green'))


def fix_fonts():
    tmp_list = get_fnt_list()
    with open(utils.FILES, 'w') as file:
        for font in tmp_list:
            if font not in failed_fonts:
                file.write(font + '\n')
