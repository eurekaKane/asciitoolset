from os import name as os_name
from os import system

class Ansi:
    def __init__(self):
        if os_name == "nt":
            system("color")

        self.RESET = "\x1b[0m"

        self.GRAD = False

        self.COLOR1 = ""
        self.COLOR2 = ""


        class Preset:
            pass



    def rgb_to_ansi(self, rgb_color, background=False):
        r, g, b = rgb_color

        if background:
            return f"\x1b[48;2;{r};{g};{b}m"
        else:
            return f"\x1b[38;2;{r};{g};{b}m"

    def hex_to_ansi(self, hex_color, background=False):
        hex_color = hex_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
        return self.rgb_to_ansi((r, g, b), background)

    def string_to_ansi(self, string, background=False):
        color_map = {
            'black': ('30', '40'),
            'red': ('31', '41'),
            'green': ('32', '42'),
            'yellow': ('33', '43'),
            'blue': ('34', '44'),
            'magenta': ('35', '45'),
            'cyan': ('36', '46'),
            'white': ('37', '47'),
        }

        if string in color_map:
            code = color_map[string][1 if background else 0]
            return f'\033[{code}m'
        else:
            raise ValueError(f"{string} is not a valid color.")

    def process_color(self, color_value, is_background):
        if isinstance(color_value, str):
            if color_value.startswith('#'):
                return self.hex_to_ansi(color_value, is_background)
            else:
                return self.string_to_ansi(color_value, is_background)
        elif isinstance(color_value, tuple):
            return self.rgb_to_ansi(color_value, is_background)
        elif color_value is None:
            return ''
        else:
            raise ValueError(f"{color_value} is not a valid color.")

    def ansi(self, char, color: None|str|int = None, background: None|str|int = None):
        """
        Function to detect either color is hex, rgb or string to use the right converter to ANSI.
        After using converter returns colored string.
        Used in Ansi.ansi_comb() for multi-coloring.


        :param char: single (or multiple characters) to color
        :param color: HEX, RGB or NAME of text color
        :param background: HEX, RGB or NAME of background color
        :return: colored 'char'
        """

        ansi_color = self.process_color(color, False)
        ansi_bg = self.process_color(background, True)

        return f"{ansi_color}{ansi_bg}{char}{self.RESET}"

    def ansi_comb(self, strs: list[str], colors: list[str | tuple], bg_colors: list[str | tuple] | None = None) -> str:
        """
        Combine multiple strings with different colors and background colors.

        :param strs: List of strings to be colored
        :param colors: List of colors (HEX, RGB, or NAME) for text
        :param bg_colors: Optional list of colors for backgrounds
        :return: Combined colored string
        """
        result = ''
        if bg_colors is None:
            bg_colors = [None]

        length = max(len(strs), len(colors), len(bg_colors))
        if self.GRAD:
                if len(colors) < 2:
                    raise ValueError("At least two colors are required for gradient")

                raise "IN DEVELOPMENT"
        else:
            for i in range(length):
                text = strs[i % len(strs)]

                if isinstance(colors, list):
                    color = colors[i % len(colors)]
                else:
                    color = colors

                if isinstance(bg_colors, list):
                    bg_color = bg_colors[i % len(bg_colors)]
                else:
                    bg_color = bg_colors

                result += self.ansi(text, color, bg_color)


        return result