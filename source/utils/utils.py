# -*- encoding: utf-8 -*-

# IMPORTS

import importlib.resources

import os

import colorama

from pyfiglet import SHARED_DIRECTORY, FigletError

from termcolor import termcolor as tcol

import string

import time

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



# CONST

__local = os.getcwd()

#SHARED_DIRECTORY = os.path.join(os.environ["APPDATA"])

path = importlib.resources.files('pyfiglet.fonts')

FILES = f"{path}\\files.txt"

__tmp = f"{__local}\\tmp"

chars = string.printable


# INIT

os.system('color')

colorama.init()


def del_tmp():
    if os.path.exists(__tmp):
        os.chmod(__tmp, 0o777)
        os.remove(f"{__tmp}\\fontList.txt")
        os.removedirs(__tmp)

del_tmp()

def ln_clr():
    """
    Clears current line
    sys.stdout.flush() but without any ghosting
    :return:
    """
    print("\033[1G\033[2K", end="", flush=True)

    return None


def clr():
    """
    Clears the console on both Linux and Windows
    :return: None
    """
    # _ = os.system('cls' if os.name == 'nt' else 'clear')
    # Old clr, works too btw (fuck denis)

    print("\033[3J", end="", flush=True)

    return None


def getFileSize():
    """
    Gets the size of files.txt
    for truncate purposes
    :return: filesize -> float
    """
    filesize = os.path.getsize(FILES)
    print(path)

    return filesize


def getFntList():
    """
    Gets all Figlet fonts present in files.txt
    :return: fntList -> list
    """
    fntList = []

    del_tmp()

    os.mkdir(f"{__local}\\tmp")

    with open(f'{__local}\\tmp\\fontList.txt', 'w') as t:
        with open(FILES, 'r') as f:
            for line in f:
                font = line.strip('\n')
                fntList.append(font)
                t.write(font + '\n')

        f.close()

    t.close()

    return fntList


def showPalette():
    """
    Displays module's color palette
    :return: None
    """
    print("Palette :\n\n")
    print("-'black'\n")
    for y in range(1, len(colors)+1):
        tcol.cprint(f"-(light_)'{colors[y]}'\n", colors[y])

    print("-'white'\n")

    return None

def showShapes():
    """
    Prints out shape list to choose from
    :return: None
    """
    for i in range(1, len(shapes)+1):
        print(f"{i}.'{shapes[i]}'\n")
    return None
