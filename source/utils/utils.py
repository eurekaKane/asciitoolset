# -*- encoding: utf-8 -*-

# IMPORTS

import importlib.resources

import os

import string

import time

from types import NoneType

#from unittest import installHandler

from pyfiglet import FigletError, FontNotFound

from source.colr import *


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

colrs: dict[int, str] = {
    1: "red",
    2: "green",
    3: "yellow",
    4: "blue",
    5: "magenta",
    6: "cyan",
}



# CONST

#SHARED_DIRECTORY = os.path.join(os.environ["APPDATA"])

__local = os.getcwd()

path_to_fnts = importlib.resources.files('pyfiglet.fonts')

FILES = f"{path_to_fnts}\\files.txt"

__tmp = f"{__local}\\tmp"

chars = string.printable


# INIT

os.system('color')


def fibonacci(max_numbers : int, color : str, bg : str):
    """
    Useless function that calculates fibonacci number
    and displays it in the console
    :return: fib -> str
    """
    fib = [0,1]

    for i in range(max_numbers - 1):
        fib.append(fib[i] + fib[i+1])

    ansi.ansi_print(f"{fib}", color, bg)


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
                os.remove(f"{__tmp}\\{files[i]}")

            os.removedirs(__tmp)

        except FileNotFoundError:
            pass

    elif handler_input not in ('clean', 'make'):

        raise Exception("Not a valid input")

    return None


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
    #os.system('cls' if os.name == 'nt' else 'clear')
    # Old clr, works too btw (fuck denis)

    os.system('cls' if os.name == 'nt' else 'clear')#print("\033[3J", end="", flush=True)

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

    with open(f'{__tmp}\\fontList.txt', 'w') as t:
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

    for y in range(1, len(colrs)+1):
        ansi.ansi_print(f"-(light_)'{colrs[y]}'\n", colrs[y])


    print("-'white'\n")

    return None

def show_fonts():
    """
    Shows the font list
    :return:
    """
    tmp_list = get_fnt_list()
    ansi.ansi_print("Voici la liste des police utilisables\n", "cyan")

    x = 1

    for i in range(len(tmp_list)//6):
        for j in range(6):
            print('|', end = '')
            ansi.ansi_print(f"{tmp_list[x-1]}   |   {tmp_list[x]}   |   {tmp_list[x+1]}   |   {tmp_list[x+2]}   |   {tmp_list[x+3]}   |   {tmp_list[x+4]}", 'green')
            x += 6

#TODO : Fix that shit and make fit nicely in the terminal

def show_shapes():
    """
    Prints out shape list to choose from
    :return: None
    """

    for i in range(1, len(shapes)+1):
        print(f"{i}.'{shapes[i]}'\n")

    return None


def _validate_shape(value):
    if not isinstance(value, (int, str)):
        raise ValueError("Shape must be an integer or a string")
    if isinstance(value, int) and value < 1:
        raise ValueError("Shape integer must be positive")
    return value


def _validate_color(value):
    if not isinstance(value, (list, str, NoneType)):
        raise ValueError("Color must be a list or a string")
    return value


def _validate_string(value, param_name):
    if not isinstance(value, str):
        raise ValueError(f"{param_name} must be a string")
    return value


def _validate_bool(value, param_name):
    if not isinstance(value, bool):
        raise ValueError(f"{param_name} must be a boolean")
    return value


def _validate_positive_int(value, param_name):
    if not isinstance(value, int) or value < 1:
        raise ValueError(f"{param_name} must be an integer bigger than 0")
    return value

