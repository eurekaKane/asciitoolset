# -*- encoding: utf-8 -*-
import os
from types import NoneType

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

# import sys


from pyfiglet import Figlet

from .colr import *
from .utils import *

# COPYRIGHT
__copyright__ = """
The MIT License (MIT)
Copyright © 2023 - 2024
Author: Ernest BECHTOLD-DALBERA <eurekakane@proton.me>
Co-Author: Denis KISLITSYN <denis.kislitsyn@proton.me>
"""

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

class Spacer:
    def __init__(self, **opt):
        """
        A spacer is an object designed to give some space to
        the console output, making it readable, and good-looking.
        :param **opt: Spacer's options
        """

        class SpacerParams:
            def __init__(self, opt_params):
                self.RANDOM = _validate_bool(opt_params.get('random', False), 'random') # Un-fucking-controllable
                self.RANDOM_RANGE = _validate_positive_int(opt_params.get('random_range', 4), 'random_range')

                self.SHAPE = _validate_shape(opt_params.get('shape', 2)) # By default, uses preset 2

                _result = self.SHAPE
                if isinstance(self.SHAPE, int):
                    _result = shapes[self.SHAPE]
                elif self.RANDOM:
                    _result = ''.join(random.choices(chars, k=self.RANDOM_RANGE))

                self.SHAPE = _result

                self.CUTOFF = _validate_bool(opt_params.get('cutoff', True), 'cutoff')

                self.COLOR = _validate_color(opt_params.get('color', 'white'))
                self.CHARS_COLOR = _validate_positive_int(opt_params.get('chars_color', 1), 'chars_color')

                self.BG_COLOR = _validate_color(opt_params.get('bg_color', None))
                self.CHARS_BG_COLOR = _validate_positive_int(opt_params.get('chars_bg_color', 1), 'chars_bg_color')

        self.Params = SpacerParams(opt)

    def set(self, **opt) -> None:
        for param, value in opt.items():
            if hasattr(self.Params, param.upper()):
                setattr(self.Params, param.upper(), value)
            else:
                raise ValueError(f'Spacer.set() has no attribute "{param.upper()}"')

        _result = self.Params.SHAPE
        if isinstance(self.Params.SHAPE, int):
            _result = shapes[self.Params.SHAPE]
        elif self.Params.RANDOM:
            _result = ''.join(random.choices(chars, k=self.Params.RANDOM_RANGE))


        self.Params.SHAPE = _result

        return None

    def string(self, **opt) -> None:
        pass

    def print_spacer(self, len_spc: int) -> None:
        """
        Displays the compiled spacer.

        :param len_spc: spacer length in chars

        :return: None
        """
        # TODO : Add y axis support (ez but too lazy)
        # TODO : Add option to skip \n before and/or after in output

        spc_shape = ""
        spc_temp = self.Params.SHAPE

        if self.Params.CUTOFF:
            for i_char in range(len_spc):
                spc_shape += spc_temp[i_char % len(spc_temp)]
        else:
            while len(spc_shape) < len_spc:
                spc_shape += spc_temp

        print()
        if isinstance(self.Params.COLOR, str):
            print(Colr.Ansi.ansi(spc_shape, self.Params.COLOR, self.Params.BG_COLOR))
        elif isinstance(self.Params.COLOR, list):
            print(Colr.Ansi.ansi_comb(spc_shape, self.Params.COLOR, self.Params.BG_COLOR))
        else:
            raise ValueError(f"Color/BG color must be a list or a string")
        print()

        return None

    def __spc_nfo__(self):
        """
        Getter for Spacer info (shape and color)
        :return: None

        Debug func only
        """
        params = {
            'Shape': self.Params.SHAPE,
            'Cutoff': self.Params.CUTOFF,
            'Color': self.Params.COLOR,
            'CharsColor': self.Params.CHARS_COLOR,
            'Random': self.Params.RANDOM,
            'Random Range': self.Params.RANDOM_RANGE,
        }

        info = f"{self}\n"
        for key, value in params.items():
            info += f"{key:20}: {value}\n"

        tcol.cprint(info, 'yellow')

        return None


class Banner:
    def __init__(self, fnt, col, txt, **opt):
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
        self.width = opt.get('width', None)
        self.banner = self.font.renderText(self.text)

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


    def get_width(self):
        """
        Getter for Banner width
        :return: Banner width
        """

        return self.width

    def setFont(self, fnt):
        """
        Setter for Banner font
        :return: None
        """

        self.font = fnt

        return None

    def setColor(self, col):
        """
        Setter for Banner color
        :return: None
        """
        self.color = col

        return None
    def setTxt(self, txt):
        """
        Setter for Banner text
        :return: None
        """
        self.text = txt

        return None


    def set_width(self, width):
        """
        Setter for Banner width
        :param width:
        :return:
        """
        self.width = width


    def printBanner(self):
        """
        Displays the compiled banner
        :return: None
        """

        tcol.cprint(self.banner, self.color)

        return None


    def saveBanner(self, userdir: str, name: str):
        """
        Saves the rendered banner to a (.txt) file
        :param name: user specified name for the banner
        :return: None
        """
        os.chdir()
        expBan = open(f"{name}.txt", "w")
        expBan.write(self.banner)
        expBan.close()
        return None


    def __banfo(self):
        """
        Getter for Banner info (shape and color)
        :return: None

        Debug func only
        """
        os.mkdir(f'{__local}\\')
        tcol.cprint(f"""

               {self.__repr__()}'s shape is {self.getTxt()}
               {self.__repr__()}'s color is {self.getColor()}
               """, 'yellow')

        return None


# OTHER FEATURES
