# -*- encoding: utf-8 -*-

"""
This is a module meant to facilitate CLI scripts readability
making. Allowing you to generate save and edit
spacers and banners to make your program
look neater. More feature will be added.
This is a rewrite in OOP
"""

# IMPORTS

import random

import string

import colorama

import os

# import time

from termcolor import termcolor as tcol

from pyfiglet import Figlet, FigletError

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


def clr():
    """Clears the console on both Linux and Windows"""
    _ = os.system('cls' if os.name == 'nt' else 'clear')


def getFileSize():
    filesize = os.path.getsize(files)
    return filesize


def getFntList():
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


def testFonts():
    fontList = getFntList()
    passed = 0
    failed = []
    for font in fontList:
        try:
            fnt = Figlet(font)
        except FigletError:
            tcol.cprint(f"{font} : Failed !\n", "red")
            failed.append(font)
        else:
            passed += 1
            tcol.cprint(f"{font} : OK !\n", "green")

    tcol.cprint(f"{passed} tests passed / {len(fontList)}", "green" if passed >= len(fontList) / 2 else "red")
    tcol.cprint(f"Failed: {failed}", "red")

    def fixFonts():
        fntList = getFntList()
        passedFnt = []
        with open('files.txt', 'w') as t:
            t.truncate()
            t.close()

        with open('files.txt', 'w') as f:
            for fonts in fntList:
                for _ in failed:
                    if fonts in passedFnt:
                        pass
                    elif fonts in failed:
                        tcol.cprint(f"{fonts} is not working, it has been deleted !\n", "red")
                        passedFnt.append(fonts)
                    else:
                        f.write(fonts + "\n")
                        tcol.cprint(f"{fonts} is good !\n", "green")
                        passedFnt.append(fonts)


        f.close()
        # FIXME : fix fixFonts() haha !
    if len(failed) > 0:
        fixFonts()


def showPalette():
    print("Palette :\n")
    print("-'black'\n")
    for y in range(len(colors)):
        tcol.cprint(f"-(light_)'{colors[y + 1]}'\n", colors[y + 1])
    print("-'white'\n")


def showShapes():
    """Prints out the shape list"""
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
        self.fontName = fnt
        self.color = col
        self.text = txt
        self.banner = self.font.renderText(self.text)

    def __repr__(self):
        return f"Font {self.fontName} in {self.color} tested with '{self.text}'"

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

    def saveBanner(self, userdir: str, name: str):
        os.chdir(userdir)
        expBan = open(f"{name}.txt", "w")
        expBan.write(self.banner)
        expBan.close()


def roll(col, txt):
    fontList = getFntList()
    spc = Spacer(2, 'white')
    for font in fontList:
        rollBan = Banner(font, col, txt)
        tcol.cprint(f'{rollBan.__repr__()}\n', 'green')
        rollBan.printBanner()
        spc.spPrint(25)

def test():
    spc = Spacer('rand', "red")
    myBan = Banner('doom', "blue", "DooM")
    myBan.printBanner()
    spc.spPrint(10)
    try :
        roll('red', 'Test')
    except :
        tcol.cprint("Oops! Smth went wrong run testFonts() to see which font isn't working", "red")
        if input('Do you want to fix the fonts ? (y/n) : ') == 'y':
            testFonts()
    finally:
        tcol.cprint('Everything is working !', 'green')


test()
