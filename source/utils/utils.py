# -*- encoding: utf-8 -*-

# IMPORTS

from source.asciitoolset import *


files = f"{os.getcwd()}\\source\\files.txt"


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
    filesize = os.path.getsize(files)

    return filesize


def getFntList():
    """
    Gets all Figlet fonts present in files.txt
    :return: fntList -> list
    """
    fntList = []

    with open('source\\fontList.txt', 'w') as t:
        with open(files, 'r') as f:
            for line in f:
                font = line.strip('\n')
                fntList.append(font)
                t.write(font + '\n')

        f.close()

    t.close()

    return fntList