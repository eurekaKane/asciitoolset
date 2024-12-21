# -*- encoding: utf-8 -*-

from os import name as os_name
from os import system

class Ansi:

    def __init__(self):
        if os_name == "nt":
            system("color")

        self.RESET = "\x1b[0m"

        self.color_map = {
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

            # Reset
            'reset': ('0', ''),
            'default': ('39', '49') # Unsupported on most CMDs
        }

        self.styles_map = {
            'bold': ('1', ''),
            'italic': ('3', ''),
            'underline': ('4', ''),
            'reverse': ('7', ''),
            'strikethrough': ('9', '')
        }

        class Preset:
            def __init__(self, color=None, background=None, grad=None, *styles):
                """
                Presets builder for Ansi class
                """
                self.color = color
                self.background = background
                self.grad = grad
                self.styles = styles

            def apply(self, text):
                """
                Apply preset styles to text.
                """
                print(Ansi().ansi(text, self.color, self.background, self.styles))

        # Attach Preset class to Ansi class
        self.Preset = Preset


    def rgb_to_ansi(self, rgb_color, background=False):
        r, g, b = rgb_color

        if background :
            return f"\x1b[48;2;{r};{g};{b}m"
        elif rgb_color == (0, 0, 0):
            return None
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
                style_code = self.styles_map[style][0]
                if style_code:
                    style_codes.append(style_code)

        return '\033[' + ';'.join(style_codes) + 'm' if style_codes else ''

    def ansi(self, char, color: None|str|int = None, background: None|str|int = None, styles: list|None = None):
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
        ansi_bg = self.process_ansi(background, True) if background is not None else ''
        ansi_styles = self.process_styles(styles) if styles is not None else ''

        return f"{ansi_color}{ansi_bg}{ansi_styles}{char}{self.RESET}"


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

                r = int(start_color[0] * (1-t) + end_color[0] * t)
                g = int(start_color[1] * (1-t) + end_color[1] * t)
                b = int(start_color[2] * (1-t) + end_color[2] * t)

                result.append((r,g,b))

        return result



    def ansi_comb(self, strs: list[str], colors: list[str], bg_colors: list[str] | None = None, *styles) -> str:
        """
        Combine multiple strings with different colors and background colors.

        :param strs: List of strings to be colored
        :param colors: List of colors (HEX, RGB, or NAME) for text
        :param bg_colors: Optional list of colors for backgrounds
        :return: Combined colored string
        """
        result = ''

        strs = str(strs)

        # String type support (optional):
        if bg_colors is None:
            bg_colors = [None]
        if isinstance(bg_colors, str) or isinstance(bg_colors, tuple):
            bg_colors = [bg_colors]
        if isinstance(colors, str)or isinstance(colors, tuple):
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

