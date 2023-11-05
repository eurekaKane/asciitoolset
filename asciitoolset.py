# -*- encoding: utf-8 -*-

"""
This is a complete module that allows you
to manipulate characters to make clean
terminal-based programs UIs
"""
# IMPORTS

import random, string

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

fonts = os.listdir("C:/Users/mynam/AppData/Local/Programs/Python/Python39/Lib/site-packages/pyfiglet/fonts")


def makeBanner(txt, fnt, col):
    """
    :param txt: string you want
    :param fnt: chosen font
    :param col: color of banner
    :return: ascii banner
    """
    ban = Figlet(font=fnt)
    myban = ban.renderText(txt)
    tcol.cprint(myban, col)
    return None


def makeSpacer(sh, le, col):
    """
    :param sh: shape of spacer
    :param le: length of spacer
    :param col: color of spacer
    :return:
    """
    if sh == "rand":
        chars = string.printable
        shape = ''.join(random.choice(chars) for i in range(4))
        shape1 = shape
        for _ in range(le):
            shape1 += shape
        tcol.cprint(f"\n{shape1}\n", col)
    else:
        shape = shapes[int(sh)]
        shape1 = shape
        for _ in range(le):
            shape1 += shape
        tcol.cprint(f"\n{shape1}\n", col)
    return None


# FIXME : fixme please
def strip(lis, foo):
    """
    :param lis: the list you want to strip the string(s) out of
    :param foo: string(s) that you want to strip
    :return: returns a list with the specific string removed
    """
    ls = []
    rem = [foo]
    for y in range(len(lis)):
        for i in range(len(rem)):
            strp = re.compile(f'(\\S*){rem[i-1]}(\\S*)')
            ls.append(strp.sub('\\1\\2', lis[i]))

    return ls

# s1, s2 = foo
# strip1 = re.compile(f'(\\S*){s1}(\\S*)')
# strip2 = re.compile(f'(\\S*){s2}(\\S*)')


def showFonts():
    # TODO : take args like family, alpha ord, spec string
    """
    :return: Print all pyfiglet font using the string 'test'
    """
    fontss = []
    stp = re.compile('(\\s*).flf(\\s*)')
    for i in range(len(fonts)-2):
        fontss.append(stp.sub('\\1\\2', fonts[i]))
        font = Figlet(font=fontss[i])
        ban = font.renderText('test')
        print(f"{i}.'{fonts[i]}'\n\n{ban}\n")
        makeSpacer(5, 50, "red")


def showShapes():
    """
    :return: print each sort of spacers
    """
    e = 0
    for i in range(len(shapes)):
        e += 1
        print(f"{i+1}.'{shapes[i + 1]}'\n")
    print(f"{e+1}.'rand'\n")
    return None

# TODO : "help" function in python or with argparse
# def help():
#    print("")

# TODO (UI) : cleaner way of enumerating things
