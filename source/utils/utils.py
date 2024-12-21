# -*- encoding: utf-8 -*-

# IMPORTS

import importlib.resources

import os

#from unittest import installHandler

from pyfiglet import FigletError, FontNotFound

from source.colr import *

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

path_to_fnts = importlib.resources.files('pyfiglet.fonts')

FILES = f"{path_to_fnts}\\files.txt"

__tmp = f"{__local}\\tmp"

chars = string.printable


# INIT

os.system('color')


def crt_dir(new_dir : str):
    os.chdir(__local)
    os.mkdir(f"{new_dir}")


def tmp_handler(handler_input : str):

    if handler_input == 'make':

        try:
            crt_dir('tmp')

        except FileExistsError:
            pass

    elif handler_input == 'clean':

        try:
            files = os.listdir(__tmp)
            os.chmod(__tmp, 0o777)

            for i in range(len(files)):
                os.chmod(f'{__tmp}\\{files[i]}', 0o777)
                os.remove(f"{__tmp}\\{files[i]}")

            os.removedirs(__tmp)

        except FileNotFoundError:
            pass

        else:
            raise Exception("Not a valid input")

# del_tmp()


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


def get_file_size(file):
    """
    Gets the size of files.txt
    for truncate purposes
    :return: filesize -> float
    """
    filesize = os.path.getsize(file)

    return filesize


def get_fnt_list():
    """
    Gets all Figlet fonts present in files.txt
    :return: fntList -> list
    """
    fnt_list = []

    time.sleep(5)
    tmp_handler('make')

    with open(f'{__local}\\tmp\\fontList.txt', 'w') as t:
        with open(FILES, 'r') as f:

            for line in f:
                font = line.strip('\n')
                fnt_list.append(font)
                t.write(font + '\n')

        f.close()

    t.close()

    return fnt_list


def show_palette():
    """
    Displays module's color palette
    :return: None
    """
    print("Palette :\n\n")
    print("-'black'\n")

    for y in range(1, len(colors)+1):
        ansi.ansi_print(f"-(light_)'{colors[y]}'\n", colors[y])


    print("-'white'\n")

    return None

def show_shapes():
    """
    Prints out shape list to choose from
    :return: None
    """

    for i in range(1, len(shapes)+1):
        print(f"{i}.'{shapes[i]}'\n")

    return None
