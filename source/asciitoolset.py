# -*- encoding: utf-8 -*-
import os


# COPYRIGHT
__copyright__ = """
The MIT License (MIT)
Copyright © 2023 - 2024
Author: Ernest BECHTOLD-DALBERA <eurekakane@proton.me>
Co-Author: Denis KISLITSYN <denis.kislitsyn@proton.me>
"""

# DESCRIPTION

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

import cv2

import sys

import numpy as np

import concurrent.futures

from pyfiglet import Figlet

from .utils import *

#from PIL import Image as PILImage


# ASCIITOOLSET

def grayscale(rgb):
    rgb = rgb
    r = int(rgb[0])
    g = int(rgb[1])
    b = int(rgb[2])
    brightness = (r + g + b) / 3
    return brightness


class Spacer:
    def __init__(self, **opt):
        """
        A spacer is an object designed to give some space to
        the console output, making it readable, and good-looking.
        :param **opt: Spacer's options
        """

        class SpacerParams:
            def __init__(self, opt_params):
                self.RANDOM = utils._validate_bool(opt_params.get('random', False), 'random') # Un-fucking-controllable
                self.RANDOM_RANGE = utils._validate_positive_int(opt_params.get('random_range', 4), 'random_range')

                self.SHAPE = utils._validate_shape(opt_params.get('shape', 2)) # By default, uses preset 2

                _result = self.SHAPE
                if isinstance(self.SHAPE, int):
                    _result = shapes[self.SHAPE]
                elif self.RANDOM:
                    _result = ''.join(random.choices(chars, k=self.RANDOM_RANGE))

                self.SHAPE = _result

                self.CUTOFF = utils._validate_bool(opt_params.get('cutoff', True), 'cutoff')

                self.COLOR = utils._validate_color(opt_params.get('color', 'white'))
                self.CHARS_COLOR = utils._validate_positive_int(opt_params.get('chars_color', 1), 'chars_color')

                self.BG_COLOR = utils._validate_color(opt_params.get('bg_color', None))
                self.CHARS_BG_COLOR = utils._validate_positive_int(opt_params.get('chars_bg_color', 1), 'chars_bg_color')

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
            print(ansi.ansi(spc_shape, self.Params.COLOR, self.Params.BG_COLOR))
        elif isinstance(self.Params.COLOR, list):
            print(ansi.ansi_comb(spc_shape, self.Params.COLOR, self.Params.BG_COLOR))
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

        print(ansi.ansi_comb(info, 'yellow'))

        return None


class Banner:
    def __init__(self, fnt, col, txt, **opt):
        """
        A banner is an object designed to display your program logo or name.

        :param fnt: Figlet font
        :param col: banner color
        :param txt: banner text
        :param **opt: Banner options
        """
        class BannerParams:
            def __init__(self, opt_params):
                self.FONT = utils._validate_string(fnt, 'font')
                self.COLOR = utils._validate_color(col)
                self.TEXT = utils._validate_string(txt, 'text')
                self.WIDTH = opt_params.get('width', None)

        self.Params = BannerParams(opt)
        self.font = Figlet(font=self.Params.FONT)
        self.banner = self.font.renderText(self.Params.TEXT)

    def set(self, **opt) -> None:
        for param, value in opt.items():
            if hasattr(self.Params, param.upper()):
                setattr(self.Params, param.upper(), value)
            else:
                raise ValueError(f'Banner.set() has no attribute "{param.upper()}"')

        self.font = Figlet(font=self.Params.FONT)
        self.banner = self.font.renderText(self.Params.TEXT)

        return None

    def print_banner(self) -> None:
        """
        Displays the compiled banner.
        :return: None
        """
        ansi.ansi_print(self.banner, self.Params.COLOR)
        return None

    def save_banner(self, path, name: str) -> None:
        """
        Saves the rendered banner to a (.txt) file.
        :param name: user specified name for the banner
        :return: None
        """
        #crt_dir('Banners')
        with open(f"{path}/{name}.txt", "w") as expBan:
            expBan.write(self.banner)
        return None

    def __banfo(self) -> None:
        """
        Getter for Banner info (shape and color).
        :return: None

        Debug func only
        """
        ansi.ansi_print(f"""
               {self}'s shape is {self.Params.TEXT}
               {self}'s color is {self.Params.COLOR}
               """, 'yellow')
        return None


class Image:
    def __init__(self, img_bytes, size=(60, 60)):
        """
        An image is an object designed to display an image in the console.
        :param img_bytes: image byte array
        :param size: image size (x, y)
        """

        self.size = size
        self.image = self.load_image(img_bytes, size)

    def load_image(self, img_bytes, size):
        """
        Load and resize the image.
        :param img_bytes: image byte array
        :param size: image size (width, height)
        :return: numpy array of the image
        """
        img_array = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        img_resized = cv2.resize(img, size, interpolation=cv2.INTER_AREA)

        return img_resized

    def process_image(self, image):
        """
        Process the image to apply ANSI colors using '▀' character.
        :return: processed image as text
        """
        img_bgr = image[:, :, ::-1]  # Convert RGB to BGR
        height, width = img_bgr.shape[:2]

        processed_image = []
        for y in range(0, height, 2):
            for x in range(width):
                upper_pixel = tuple(img_bgr[y, x])
                lower_pixel = tuple(img_bgr[min(y + 1, height - 1), x])
                processed_image.append(ansi.ansi_comb(['▀'], [upper_pixel], [lower_pixel]))
                # Faster to put upper_pixel and lower_pixel in a list bcs it avoids if checks in ansi_comb
            processed_image.append('\n')

        return ''.join(processed_image)

    def print_image(self):
        """
        Displays the processed image as text.
        :return: None
        """
        text_image = self.process_image(self.image)
        print(text_image)

    def set(self, **opt):
        """
        Setter for Image object
        :param **opt: Image options
        :return: None
        """
        for param, value in opt.items():
            if hasattr(self, param):
                setattr(self, param, value)
            else:
                raise ValueError(f'Image.set() has no attribute "{param}"')
        return None


class Video:
    def __init__(self, path, fps=None, size=(60, 60)):
        """
        A video is an object designed to display a video in the console.
        :param path: video path
        :param fps: frames per second
        :param size: frame size (width, height)
        """
        self.path = path
        self.cap = cv2.VideoCapture(self.path)
        self.fps = fps if fps else int(self.get_video_fps())
        self.size = size

    def get_video_fps(self):
        if not self.cap.isOpened():
            raise ValueError(f"Can't open video at: {self.path}")
        return self.cap.get(cv2.CAP_PROP_FPS)

    def load_video(self):
        # open the video file
        if not self.cap.isOpened():
            raise ValueError(f"Can't open video at: {self.path}")
        if not self.fps:
            self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        return self.cap

    def get_video_frame(self):
        ret, frame = self.cap.read()
        return frame if ret else None

    def process_frames(self):
        def _proc_frame(frame, index):
            _, img_bytes = cv2.imencode('.bmp', frame)
            image = Image(img_bytes.tobytes(), self.size)
            ansi_frame = image.process_image(image.image)
            return index, ansi_frame

        max_workers = min(32, (os.cpu_count() or 1) + 4)  # Limit number of threads to not burn the family house down
        processed_frames = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            frame_index = 0
            while True:
                frame = self.get_video_frame()
                if frame is None:
                    break
                futures.append(executor.submit(_proc_frame, frame, frame_index))
                frame_index += 1

            for future in sorted(concurrent.futures.as_completed(futures), key=lambda f: f.result()[0]):
                _, processed_frame = future.result()
                processed_frames.append(processed_frame)

        return processed_frames

    def play(self):
        self.cap = self.load_video()
        utils.clr()

        sys.stdout.write('Converting video to console output...\n')
        sys.stdout.flush()

        processed_frames = self.process_frames()

        input("Done! Press Enter to play the video.")
        utils.clr()

        frame_time = 1 / self.fps
        total_frames = len(processed_frames)-1

        i = 0
        start_time = time.time()
        while i < total_frames:
            current_time = time.time()
            elapsed_time = current_time - start_time

            # Calculate the ideal frame number based on elapsed time
            ideal_frame = int(elapsed_time * self.fps)

            # Skip frames if we're behind
            if ideal_frame > i:
                frames_to_skip = ideal_frame - i
                i += frames_to_skip
                if i >= total_frames:
                    break

            # Display the current frame
            frame_start_time = time.time()
            sys.stdout.write('\033[H')
            sys.stdout.write(processed_frames[i])
            sys.stdout.write(f"Frame: {i}/{total_frames}")
            sys.stdout.flush()
            frame_end_time = time.time()

            # Calculate how long to wait until the next frame
            frame_duration = frame_end_time - frame_start_time
            wait_time = max(0, frame_time - frame_duration)

            time.sleep(wait_time)
            i += 1

        sys.stdout.write("\nPlayback finished.")



class Clickable:
    """
    Empty
    """
    def __init__(self):
        """
        Empty
        """

# TODO : Implement clickable elements

class Window:
    """
    Empty
    """
    def __init__(self):
        """
        Empty
        """

# TODO : Implement windows that can contains smaller ones and clickable