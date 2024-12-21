# -*- encoding: utf-8 -*-

import time

from source import *

from source.tests.test_all import roll

spc = Spacer(shape = "zebi zeub", color = ["green","red","yellow"])#, random = True)


def print_palette():
    colors = [
        (255, 0, 0),  # Red
        (255, 128, 0),  # Orange
        (255, 255, 0),  # Yellow
        (128, 255, 0),  # Lime Green
        (0, 255, 0),  # Green
        (0, 255, 128),  # Spring Green
        (0, 255, 255),  # Cyan
        (0, 128, 255),  # Sky Blue
        (0, 0, 255),  # Blue
        (128, 0, 255),  # Violet
        (255, 0, 255),  # Magenta
        (255, 0, 128)  # Pink
    ]


    # Number of steps in the gradient
    steps = 32


    gradient_colors = ansi.gradient(steps, *colors)

    print("Gradient Palette:")

    # Print each color block in a single line
    for color in gradient_colors:
        color_block = ansi.rgb_to_ansi(color, background=True) + "   " + ansi.RESET
        print(color_block, end="")

    print()


def main():
    spc.__spc_nfo__()
    cwd = os.getcwd()
    print(cwd)
    ansi.ansi_print(get_file_size(cwd), 'red')
    #print(getFntList())
    spc.print_spacer(17)
    spc.set(cutoff = False, shape = "zeub zebi")
    spc.print_spacer(100)
    spc.set(color="red")
    spc.print_spacer(3)

    preset = ansi.Preset('red', 'blue', 'italic')
    preset.apply("zeubizetion")

    print("\nColr tests:")
    print(ansi.ansi_comb("BRGYBMCW",
                              ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'],
                              ['white', 'cyan', 'magenta', 'blue', 'yellow', 'green', 'red', 'black']))

    print(ansi.ansi_comb("WCMBYGRB",
                              ['white', 'cyan', 'magenta', 'blue', 'yellow', 'green', 'red', 'black'],
                              ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']))

    grad_text = ansi.gradient(4, (255,0,0), (0,255,0), (0,0,255))
    grad_bg = ansi.gradient(4, (0, 0, 255), (0, 255, 0), (255, 0, 0))

    print(ansi.ansi_comb("0"*len(grad_text), grad_text, grad_bg))

    print(spc.__repr__())
    #roll('red', "test")

    print_palette()

if __name__ == "__main__":
    main()