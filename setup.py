# -*- encoding: utf-8 -*-

"""
Setup file :
Install required packages and dependencies for asciitoolset
First ensure that pip is installed and then pull every package from requirements.txt
to install them
"""

# IMPORTS

import os


# INSTALL

os.system("python.exe -m pip install --upgrade pip")
os.system("python -m pip install -r requirements.txt")
