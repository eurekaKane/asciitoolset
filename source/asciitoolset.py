# -*- encoding: utf-8 -*-
from os import getcwd
from platform import system

long_des = """
This is a module meant to facilitate CLI scripts making process and readability.
Allowing you to generate save and edit spacers, banners (and many others)
to make your program look neater.
More feature will be added.
This is a rewrite in OOP (check the OG commit to see the mess it was in functional programming).
I decided to change paradigm simply because I was working with what could be interpreted as objects, thus it was
far more optimized coding in OOP :)
"""

# IMPORTS

import random

import string

import colorama

import os

import sys

import time

from termcolor import termcolor as tcol

from pyfiglet import Figlet, FigletError

# COPYRIGHT
__copyright__ = """
The MIT License (MIT)
Copyright © 2023 - 2024
Author: Ernest BECHTOLD-DALBERA <eurekakane@proton.me>
"""

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

# COLORS

colors: dict[int, str] = {
    1: "red",
    2: "green",
    3: "yellow",
    4: "blue",
    5: "magenta",
    6: "cyan",
}

files = 'files.txt'

# INIT
# Required to display colors properly on any terminal

os.system('color')
colorama.init()


def ln_clr():
    """
    Clears current line
    makes sys.stdout.flush() work without any ghosting
    :return:
    """
    print("\033[1G\033[2K", end="", flush=True)
    return None


def clr():
    """
    Clears the console context on both Linux and Windows
    :return: None
    """
    _ = os.system('cls' if os.name == 'nt' else 'clear')
    return None


def getFileSize():
    """
    Gets the size of files.txt
    for truncate purposes
    :return: filesize -> float
    """
    filesize = os.path.getsize(files)
    return filesize


def getFntList():
    """
    Gets all Figlet fonts present in files.txt
    :return: fntList -> list
    """
    fntList = []
    with open('fontList.txt', 'w') as t:
        with open(files, 'r') as f:
            for line in f:
                font = line.strip('\n')
                fntList.append(font)
                t.write(font + '\n')
        f.close()
    t.close()
    return fntList


def showPalette():
    """
    Displays termcolor's palette
    :return: None
    """
    print("Palette :\n\n")
    print("-'black'\n")
    for y in range(len(colors)):
        tcol.cprint(f"-(light_)'{colors[y + 1]}'\n", colors[y + 1])
    print("-'white'\n")
    return None

def showShapes():
    """
    Prints out the shape list
    :return: None
    """
    for i in range(len(shapes)):
        print(f"{i + 1}.'{shapes[i + 1]}'\n")
    return None


class Spacer:
    # TODO : make a variable that stores the spacer params instead of the whole makeSpacer func
    def __init__(self, sh, col):
        """
        A spacer is an object designed to give some space to
        the console output, make it readable, and good-looking
        :param sh: shape of spacer
        :param col: color of spacer
        """
        self.sh = sh
        self.color = col
        self.shape = None
        if self.sh == "rand":
            chars = string.printable
            self.shape = ''.join(random.choice(chars) for _ in range(4))
        else:
            self.shape = shapes[int(self.sh)]

    def __repr__(self):
        """
        __repr__ method for Spacer
        :return: a string representation of Spacer object
        """
        return f"Object : Spacer ; Shape : n°{self.sh} ; Color : {self.color}"

    def makeSpacer(self):
        """
        Compile Spacer's parameters into a single variable
        :return: None
        """
        if self.sh == "rand":
            chars = string.printable
            self.shape = ''.join(random.choice(chars) for _ in range(4))
        else:
            self.shape = shapes[int(self.sh)]


    def getShape(self):
        """
        Getter for Spacer's shape parameter
        :return: spacer's shape
        """
        return self.shape

    def getColor(self):
        """
        Getter for Spacer's color parameter
        :return: spacer's color
        """
        return self.color

    def getSpcInfo(self):
        """
        Getter for Spacer info (shape and color)
        :return: None
        """
        print(f"{self}'s shape is {self.shape}/n")
        print(f"{self}'s color is {self.color}")

    def setShape(self, sh):
        """
        Setter for Spacer shape
        :return: None
        """
        self.sh = sh
        self.makeSpacer()

    def setColor(self, col):
        """
        Setter for Spacer color
        :return: None
        """
        self.color = col
        self.makeSpacer()

    def spPrint(self, le):
        """
        Displays the compiled spacer with a supplementary argument
        :param le: spacer length
        :return: None
        """
        spcShape = self.shape

        for _ in range(le):
            spcShape += self.shape

        tcol.cprint(f"\n{spcShape}\n", self.color)


class Banner:
    def __init__(self, fnt, col, txt):
        """
        A banner is an object designed to display your program logo or name
        :param fnt: Figlet font
        :param col: banner color
        :param txt: banner text
        """
        self.font = Figlet(font=fnt)
        self.fontName = fnt
        self.color = col
        self.text = txt
        self.banner = self.font.renderText(self.text)

    def __repr__(self):
        """
        __repr__ method for Banner
        :return: f-string representation of Banner object
        """
        return f"Object[ Banner ] ; Font[ {self.fontName} ] ; Color[ {self.color} ] ; Text[ '{self.text}' ]"

    def makeBanner(self):
        """
        Compiles the banner using Figlet python port PyFiglet
        :return: Banner object
        """
        self.banner = self.font.renderText(self.text)
        return self.banner

    def getFont(self):
        """
        Getter for Banner font
        :return: Figlet font object
        """
        return self.font

    def getColor(self):
        """
        Getter for Banner color
        :return: Banner color
        """
        return self.color

    def getTxt(self):
        """
        Getter for Banner text
        :return: Banner text
        """
        return self.text

    def setFont(self, fnt):
        """
        Setter for Banner font
        :return: None
        """
        self.font = fnt
        self.makeBanner()

    def setColor(self, col):
        """
        Setter for Banner color
        :return: None
        """
        self.color = col
        self.makeBanner()

    def setTxt(self, txt):
        """
        Setter for Banner text
        :return: None
        """
        self.text = txt
        self.makeBanner()

    def printBanner(self):
        """
        Displays the compiled banner
        :return: None
        """
        self.makeBanner()
        tcol.cprint(self.banner, self.color)

    def saveBanner(self, userdir: str, name: str):
        """
        Saves the rendered banner to a (.txt) file
        :param userdir: user specified directory
        :param name: user specified name for the banner
        :return: None
        """
        os.chdir(userdir)
        expBan = open(f"{name}.txt", "w")
        expBan.write(self.banner)
        expBan.close()


# OTHER FEATURES


def roll(col, txt):
    """
    Roll through every font in the font list and renders a Banner for each with the specified parameters
    :param col: color to display
    :param txt: text to display
    :return: None
    """
    fontList = getFntList()
    spc = Spacer(2, 'white')
    for font in fontList:
        rollBan = Banner(font, col, txt)
        tcol.cprint(f'{rollBan.__repr__()}\n', 'green')
        rollBan.printBanner()
        spc.spPrint(25)


def debug():
    """
    :return: Debug string
    """
    cwd = getcwd()
    return cwd


print(debug())