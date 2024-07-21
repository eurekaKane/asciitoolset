# -*- encoding: utf-8 -*-

"""
This is a module meant to facilitate CLI UIs
making. Allowing you to generate save and edit
spacers and banners to make your program
look neater. More feature will be added.
This is a rewrite in OOP
"""

# IMPORTS

import random, string

import re

import colorama

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


def showShapes():
    """
    :return: print each sort of spacers
    """
    for i in range(len(shapes)):
        print(f"{i+1}.'{shapes[i + 1]}'\n")
    return None

# INIT

"""Required to display colors properly on any terminal"""
os.system('color')
colorama.init()


def clr():
    """Clears the console on both Linux and Windows"""
    _ = os.system('cls' if os.name == 'nt' else 'clear')


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

    def __str__(self):
        return str(self.__class__.__name__)

    def makeSpacer(self):
        """Compile Spacer's parameters into a single variable"""
        if self.sh == "rand":
            chars = string.printable
            self.shape = ''.join(random.choice(chars) for _ in range(4))
        else:
            self.shape = shapes[int(self.sh)]

    def getShape(self):
        """Getter for Spacer shape"""
        return self.shape

    def getColor(self):
        """Getter for Spacer color"""
        return self.color

    def getSpcInfo(self):
        """Getter for Spacer info (shape and color)"""
        print(f"{self}'s shape is {self.shape}/n")
        print(f"{self}'s color is {self.color}")

    def setShape(self, sh):
        """Setter for Spacer shape"""
        self.sh = sh
        self.makeSpacer()

    def setColor(self, col):
        """Setter for Spacer color"""
        self.color = col
        self.makeSpacer()

    def spPrint(self, le):
        """Displays the compiled spacer"""
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
        self.color = col
        self.text = txt
        self.banner = self.font.renderText(self.text)

    def makeBanner(self):
        """Compiles the banner using Figlet python port PyFiglet by 'pwaller'"""
        self.banner = self.font.renderText(self.text)

    def getFont(self):
        """Getter for Banner font"""
        return self.font

    def getColor(self):
        """Getter for Banner color"""
        return self.color

    def getTxt(self):
        """Getter for Banner text"""
        return self.text

    def setFont(self, fnt):
        """Setter for Banner font"""
        self.font = fnt
        self.makeBanner()

    def setColor(self, col):
        """Setter for Banner color"""
        self.color = col
        self.makeBanner()

    def setTxt(self, txt):
        """Setter for Banner text"""
        self.text = txt
        self.makeBanner()

    def printBanner(self):
        """Displays the compiled banner"""
        self.makeBanner()
        tcol.cprint(self.banner, self.color)


def test():
    spc = Spacer('rand', "red")
    myBan = Banner('doom', "blue", "DooM")
    while True:
        myBan.printBanner()
        spc.spPrint(10)
