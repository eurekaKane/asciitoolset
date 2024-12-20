# -*- encoding: utf-8 -*-
import os

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

from source.utils.utils import *

from source.utils.utils import __local

# COPYRIGHT
__copyright__ = """
The MIT License (MIT)
Copyright © 2023 - 2024
Author: Ernest BECHTOLD-DALBERA <eurekakane@proton.me>
Co-Author: Denis KISLITSYN <denis.kislitsyn@proton.me>
"""


class Spacer:
    # TODO : multicolor spacer

    def __init__(self, **opt):
        """
        A spacer is an object designed to give some space to
        the console output, making it readable, and good-looking
        :param sh: shape of spacer
        :param **opt: spacer's options
        """

        class SpacerParams:
            def __init__(self, opt_params):
                self.SH = opt_params.get('shape', 2)

                self.CUTOFF = opt_params.get('cutoff', True)

                self.COLOR = opt_params.get('color', 'white')
                self.CHARS_PER_COLOR = opt_params.get('chars_per_color', 1)

                self.RANDOM = opt_params.get('random', False)
                self.RANDOM_RANGE = opt_params.get('random_range', 4)

        self.Params = SpacerParams(opt)

        # Shape handler
        if isinstance(self.Params.SH, int):
            _result = shapes[self.Params.SH]
        elif self.Params.RANDOM:
            _result = ''.join(random.choice(chars) for _ in range(self.Params.RANDOM_RANGE))
        else:
            _result = self.Params.SH

        self.shape = _result

    def set(self, **opt):
        self.Params.CUTOFF = opt.get('cutoff', self.Params.CUTOFF)

        self.Params.COLOR = opt.get('color', self.Params.COLOR)
        self.Params.CHARS_PER_COLOR = opt.get('chars_per_color', self.Params.CHARS_PER_COLOR)

        self.Params.RANDOM = opt.get('random', self.Params.RANDOM)
        self.Params.RANDOM_RANGE = opt.get('random_range', self.Params.RANDOM_RANGE)

        sh_tmp = opt.get('shape', self.shape)
        if self.Params.RANDOM:
            _result = ''.join(random.choice(chars) for _ in range(self.Params.RANDOM_RANGE))
        else:
            _result = sh_tmp

        self.shape = _result

    def get_shape(self):
        """
        Getter for Spacer shape
        :return: spacer's shape
        """
        return self.shape

    def get_color(self):
        """
        Getter for Spacer color
        :return: spacer's color
        """
        return self.Params.COLOR

    def sp_print(self, len_spc):
        """
        Displays the compiled spacer.
        Fuck this shit for real man, I spent 1h trying to fix it and in the end I got where i started.

        :param len_spc: spacer length in chars

        :return: None
        """

        spc_shape = ""
        spc_temp = self.shape

        if self.Params.CUTOFF:
            for i in range(len_spc):
                spc_shape += spc_temp[i % len(spc_temp)]
        else:
            for spc_char in spc_temp:
                spc_shape += spc_char


        if isinstance(self.Params.COLOR, str):
            tcol.cprint(f"\n{spc_shape}\n", self.Params.COLOR)
        elif isinstance(self.Params.COLOR, list):
            tcol.cprint(f"\n")
            for i_char in range(len(spc_shape)):
                tcol.cprint(f"{spc_shape[i_char]}", self.Params.COLOR[i_char%len(self.Params.COLOR)], end="")
            tcol.cprint(f"\n")

        return None

    def __spc_nfo__(self):
        """
        Getter for Spacer info (shape and color)
        :return: None

        Debug func only
        """

        tcol.cprint(f"""
                
               {self}'s shape is {self.shape}
               {self}'s color is {self.Params.COLOR}
               """, 'yellow')

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


    def __repr__(self):
        """
        __repr__ method for Banner
        :return: a string representation of Banner object
        """
        return f"Object[ Banner ] ; Font[ {self.fontName} ] ; Color[ {self.color} ] ; Text[ '{self.text}' ]"


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
