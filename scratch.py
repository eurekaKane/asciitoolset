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

# INIT

os.system('color')
colorama.init()

def clr():
    _ = os.system('cls' if os.name == 'nt' else 'clear')
class Spacer:
    # TODO : make a variable that stores the spacer params instead of the whole makeSpacer func
    def __init__(self, sh, col : str):
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
        """"""
        if self.sh == "rand":
            chars = string.printable
            self.shape = ''.join(random.choice(chars) for _ in range(4))
        else:
            self.shape = shapes[int(self.sh)]

    def getShape(self):
        return self.shape

    def getColor(self):
        return self.color

    def getSpcInfo(self):
        print(f"{self}'s shape is {self.shape}/n")
        print(f"{self}'s color is {self.color}")

    def setShape(self, sh):
        self.sh = sh
        self.makeSpacer()

    def setColor(self, col):
        self.color = col
        self.makeSpacer()

    def spPrint(self, le):
        spcShape = self.shape
        for _ in range(le):
            spcShape += self.shape
        tcol.cprint(f"\n{spcShape}\n", self.color)


class Banner:
    def __init__(self, fnt, col, txt):
        self.font = Figlet(font=fnt)
        self.color = col
        self.text = txt
        self.banner = self.font.renderText(self.text)

    def makeBanner(self):
        self.banner = self.font.renderText(self.text)

    def getFont(self):
        return self.fnt

    def getColor(self):
        return self.color

    def getTxt(self):
        return self.text

    def setFont(self, fnt):
        self.font = fnt
        self.makeBanner()

    def setColor(self, col):
        self.color = col
        self.makeBanner()

    def setTxt(self, txt):
        self.text = txt
        self.makeBanner()

    def printBanner(self):
        self.makeBanner()
        tcol.cprint(self.banner, self.color)


def test():
    spc = Spacer('rand', "red")
    myban = Banner('doom', "blue", "DooM")
    while True:
        myban.printBanner()
        spc.spPrint(10)

test()