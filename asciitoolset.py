# -*- encoding: utf-8 -*-

"""
This is a complete module that allows you
to manipulate characters to make clean
terminal-based programs UIs
"""
# IMPORTS

import re

import os

from termcolor import termcolor as tcol

from pyfiglet import Figlet


# SHAPES
shapes = {
    1: "|-|_",
    2: "####",
    3: "/-/-",
    4: "~~~~",
    5: "====",
    6: "=+=+",
    7: "$%$%",
    8: "/*/*",
    9: "////",
    10: ">>>>",
    11: "--->"
}


def makeBanner(txt, fnt, col):
    """
        Precond : Takes 3 args : text, font, color
        :return: print(banner)
    """
    ban = Figlet(font=fnt)
    myban = ban.renderText(txt)
    tcol.cprint(myban, col)
    return None


def makeSpacer(sh, le, col):
    """
    Precond : Takes 3 args : shape, size, color
    :return: print(spacer)
    """
    shape = shapes[sh]
    shape1 = shape
    for _ in range(le):
        shape1 += shape
    tcol.cprint(f"\n{shape1}\n", col)
    return None


def showFonts():
    # TODO : take args like family, alpha ord, spec string
    """
    :return: Print all pyfiglet font using the string 'test'
    """
    fonts = os.listdir("C:/Users/mynam/AppData/Local/Programs/Python/Python312/Lib/site-packages/pyfiglet/fonts")
    strip = re.compile('(\\S*).flf(\\S*)')
    fontss = []
    for i in range(len(fonts)-2):
        fontss.append(strip.sub('\\1\\2', fonts[i]))
        font = Figlet(font=fontss[i])
        ban = font.renderText('test')
        print(f"{i}.'{fontss[i]}'\n\n{ban}\n")
        makeSpacer(5, 50, "red")


def showShapes():
    """
    :return: print each sort of spacers
    """
    for i in range(len(shapes)):
        print(f"{i+1}.'{shapes[i + 1]}'\n")
    return None

# TODO "help" function in python or with argparse
# def help():
#    print("")

# TODO cleaner way of enumerating things
