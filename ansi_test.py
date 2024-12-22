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


    gradient = ansi.gradient(12, *colors)
    ansi.ansi_print(" ", gradient, gradient)

    print()

def print_all_colors():
    colors = [
        "#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF",
        "#800000", "#808000", "#008000", "#800080", "#008080", "#000080",
        "#C0C0C0", "#808080", "#FFFFFF", "#000000"
    ]

    print("Terminal Color Palette")

    for i in range(0, len(colors), 4):
        row_colors = colors[i:i + 4]
        for color in row_colors:
            block = ansi.ansi("   ", 'default', background=color)
            print(f"{block} {color}", end="   ")
        print(ansi.RESET)


def main():
    print("\n\nAnsi colors:")
    ansi_colors = []
    for i in ansi.color_map:
        ansi.ansi_print(i, i)
        ansi_colors.append(i)

    ansi_colors = ansi_colors[1:]

    print("\nColr tests:")
    ansi.ansi_print("▐"*len(ansi_colors), ansi_colors, ansi_colors[::-1])
    ansi.ansi_print("▐" * len(ansi_colors), ansi_colors[::-1], ansi_colors)

    grad_text = ansi.gradient(8, (255,0,0), (0,255,0), (0,0,255))
    grad_bg = ansi.gradient(8, (0, 0, 255), (0, 255, 0), (255, 0, 0))

    ansi.ansi_print("0"*len(grad_text), grad_text, grad_bg)

    preset = ansi.Preset('cyan', 'bright_red', styles=['italic', 'bold', 'underline', 'reverse', 'strikethrough'])
    preset_var = preset.apply("Preset test")
    print(preset_var)

    #roll('red', "test")

    print_palette()
    print_all_colors()

if __name__ == "__main__":
    main()
