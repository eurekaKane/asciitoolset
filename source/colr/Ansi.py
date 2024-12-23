# -*- encoding: utf-8 -*-

from os import name as os_name
from os import system

class Ansi:

    def __init__(self):
        """
        Ansi is a class that provides methods for coloring and styling text in the terminal.
        Styles are not supported on most command lines.
        """
        if os_name == "nt":
            system("color")

        self.RESET = "\x1b[0m"
        self.DEFAULT = "\x1b[39m"

        self.color_map = {
            # Reset
            'default': ('39', '49'),

            # Standard colors
            'black': ('30', '40'),
            'red': ('31', '41'),
            'green': ('32', '42'),
            'yellow': ('33', '43'),
            'blue': ('34', '44'),
            'magenta': ('35', '45'),
            'cyan': ('36', '46'),
            'white': ('37', '47'),

            # Bright colors
            'gray': ('90', '100'), # bright black? no, gray
            'bright_red': ('91', '101'),
            'bright_green': ('92', '102'),
            'bright_yellow': ('93', '103'),
            'bright_blue': ('94', '104'),
            'bright_magenta': ('95', '105'),
            'bright_cyan': ('96', '106'),
            'bright_white': ('97', '107'),
        }

        self.styles_map = {# All styles except 'reverse' won't work on Windows CMD.
            'reset': '0',
            'bold': '1',
            'italic': '3',
            'underline': '4',
            'reverse': '7',
            'strikethrough': '9'
        }

        class Preset:
            def __init__(self, color=None, background=None, styles: list = None):
                """
                Presets builder for Ansi class
                """
                self.color = color
                self.background = background
                self.styles = styles

            def apply(self, text):
                """
                Apply preset styles to text.
                """
                return Ansi().ansi(text, self.color, self.background, self.styles)

        # Attach Preset class to Ansi class
        self.Preset = Preset


    def rgb_to_ansi(self, rgb_color, background=False):
        r, g, b = rgb_color

        if background :
            return f"\x1b[48;2;{r};{g};{b}m"
        else:
            return f"\x1b[38;2;{r};{g};{b}m"


    def hex_to_ansi(self, hex_color, background=False):
        hex_color = hex_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
        return self.rgb_to_ansi((r, g, b), background)


    def string_to_ansi(self, string, background=False):

        if string in self.color_map:
            code = self.color_map[string][1 if background else 0]
            return f'\033[{code}m'
        else:
            raise ValueError(f"{string} is not a valid color.")


    def process_ansi(self, color_value, is_background):
        if color_value is None:
            return ''
        elif isinstance(color_value, str):
            if color_value.startswith('#'):
                return self.hex_to_ansi(color_value, is_background)
            else:
                return self.string_to_ansi(color_value, is_background)
        elif isinstance(color_value, tuple):
            return self.rgb_to_ansi(color_value, is_background)
        elif isinstance(color_value, bool):
            return self.rgb_to_ansi(color_value, is_background)
        else:
            raise ValueError(f"{color_value} is not a valid ANSI value.")

    def process_styles(self, styles):
        """
        Process the styles and return the corresponding ANSI codes.

        :param styles: String or list of strings representing text styles
        :return: ANSI codes for the specified styles
        """
        if isinstance(styles, str):
            styles = [styles]

        style_codes = []
        for style in styles:
            if style in self.styles_map:
                style_code = self.styles_map[style]
                if style_code:
                    style_codes.append(style_code)

        return '\033[' + ';'.join(style_codes) + 'm' if style_codes else ''

    def ansi(self, char, color: str|int = 'default', background: str|int = 'default', styles: list|None = None):
        """
        Function to detect either color is hex, rgb or string to use the right converter to ANSI.
        After using converter returns colored string.
        Used in Ansi.ansi_comb() for multi-coloring.



        :param char: single (or multiple characters) to color
        :param color: HEX, RGB or NAME of text color
        :param background: HEX, RGB or NAME of background color
        :param styles: A list of styles

        :return: 'char' with ANSI encoding
        """

        if color is None:
            raise ValueError('Should at least have one color')

        ansi_color = self.process_ansi(color, False)
        ansi_bg = self.process_ansi(background, True)
        ansi_styles = self.process_styles(styles) if styles else ''

        return f"{ansi_bg}{ansi_color}{ansi_styles}{char}{self.RESET}"

    def gradient(self, step, color1, color2, *colors):
        all_colors = [color1, color2] + list(colors)
        total_colors = len(all_colors)

        if total_colors < 2:
            raise ValueError("Must have at least 2 colors")

        result = []

        for i in range(total_colors-1):
            start_color = all_colors[i]
            end_color = all_colors[i+1]

            for j in range(step):
                t = j / (step -1)

                result.append((int(start_color[0] * (1-t) + end_color[0] * t),int(start_color[1] * (1-t) + end_color[1] * t),int(start_color[2] * (1-t) + end_color[2] * t)))

        return result



    def ansi_comb(self, strs: list[str], colors: list[str] | str= "default", bg_colors: list[str] | str = "default", *styles) -> str:
        """
        Combine multiple strings with different colors and background colors.

        :param strs: List of strings to be colored
        :param colors: List of colors (HEX, RGB, or NAME) for text
        :param bg_colors: Optional list of colors for backgrounds
        :return: Combined colored string
        """
        result = ''



        # String type support (optional):
        if bg_colors is None:
            bg_colors = [None]
        if not isinstance(bg_colors, list):
            bg_colors = [bg_colors]
        if not isinstance(colors, list):
            colors = [colors]

        length = max(len(strs), len(colors), len(bg_colors))

        for i in range(length):
            text = strs[i % len(strs)]

            color = colors[i % len(colors)]
            bg_color = bg_colors[i % len(bg_colors)]

            result += self.ansi(text, color, bg_color, styles)

        return result

    def ansi_print(self, strs: list[str], colors: list[str | tuple], bg_colors: list[str | tuple] | None = None) -> str:
        print(self.ansi_comb(strs, colors, bg_colors)) # the most useless function fr

