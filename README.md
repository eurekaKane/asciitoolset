<h1 align="center">===========ASCII-Toolset===========</h1>



<h2>This is a module that allows you to manipulate characters 
to make clean terminal-based programs UIs</h2>

<h1 align="center">WARNING !</h1>
<h2>Don't clone my repo UNLESS you have some experience and can work around it !</h2>
<h2>Like the mess it is in terms of dependencies and like shit you need to know to make it work is awful. GOD ! This repo is a construction site. Fixing my stuff ASAP :)</h2>

## Changelog

Global changes :
-
* Added a <code>setup.py</code> file
* Fragmented every script in separate folders :

    +   ``` txt
        /asciitoolset
        │
        ├──/source
        │  │
        │  ├─── /utils
        │  │    ├─── __init__.py
        │  │    └─── utils.py
        │  ├─── /test
        │  │    ├─── __init__.py
        │  │    └─── test_all.py
        │  │
        │  ├─── __init__.py
        │  ├─── asciitoolset.py
        │  ├─── test_all.py
        │  └─── tutorial.py
        │
        ├─── run_test.py
        ├─── run_tutorial.py
        └─── setup.py  
        ```
     


Specific changes :
-
* Deleted the fonts folder
* HUGE <code>README.md</code> upgrade
* I honestly don't remember the other changes

Future changes :
-
* Other objects like loading bars, buttons, boxes... will be added
* Other languages support for the tutorial like English or Russian
* Error handling


## Supported
* Every device with Python3 and pip installed

## Guide
<details>
   <summary>Guide for beginners</summary>

   Since the projects is not yet on PyPi you can't use pip

   1. <details><summary>Cloning GitHub repo</summary>
   
      1. Make sure you have [git](https://git-scm.com/downloads) installed on your computer

         + On Windows 11/10 you'll have to install it manually.
         + On MacOS you can just type in <code>git</code> and a pop-up should ask you if you want to install it.
         + On Linux it's built-in

      2. Once it's done there are two options
   
         + You can navigate to your local python package folder and clone it there
         + Or if you are on a virtual environment clone in your projects local .venv packages folder

      3. Then go to the folder of asciitoolset you just cloned and run <code>python setup.py</code>
   
         + If you don't have <code>pip</code> installed, make sure you re/install it by running <code>py -m ensurepip --upgrade</code>. And re-run <code>setup.py</code>
         + Else you should be good to go
      </details>

   2. <details><summary>Downloading .zip archive on GitHub</summary>

      1. Go to the [repo page](https://github.com/eurekakane/asciitoolset) on GitHub and select the branch you want
      2. Then click on the [<>Code](https://github.com/eurekaKane/asciitoolset/archive/refs/heads/experimental.zip) button and .zip
      3. Extract the archive in your python package folder
      4. You are good to go 

      </details>

</details>

<details><summary>Guide for advanced people</summary>

1. Follow the beginners tutorial 🧍‍♂️

</details>

## Modules used
[requirements.txt](requirements.txt)
* [pyfiglet](https://pypi.org/project/pyfiglet/)

## Bugs
No known bugs just no error handling

# Licence

[MIT License
Copyright (c) 2024 eurekaKane](LICENSE)

## Authors

- [@eurekaKane](https://www.github.com/eurekaKane)

## Description

This module uses mainly pyFiglet a port of Figlet to python made by [@pwaller](https://github.com/pwaller) and [many other](https://github.com/pwaller/pyfiglet/graphs/contributors).
I had the idea of making it after realizing that I had been struggling making CLI UIs for each program I made.
What I usually did was a spacer function and generate a Figlet banner online then copy it in my code. So to spare me the 
pain I decided to write a module simple of use that automates (kinda) all the process. I'm planning on adding a bunch of other features, making this 
projects kinda of a big wrapper for all cool cli-UI programs. 

:) enjoy !

## Usage/Examples

```python
import source.asciitoolset as ascc

myBan = ascc.Banner('myFont','myColor','myText')

mySpc = ascc.Spacer('myShape', 'myColor')

def myfunc():
    myBan.printBanner()
    myBan.setColor('light_blue')
    mySpc.spPrint('myLenght')
    myBan.printBanner()
```
## Output

```pycon
>>> from myScript import myBan, mySpc, myfunc
>>> myfunc()
   __            __ 
  / /____  _____/ /_
 / __/ _ \/ ___/ __/
/ /_/  __(__  ) /_  
\__/\___/____/\__/  
                    
==============================================

   __            __ 
  / /____  _____/ /_
 / __/ _ \/ ___/ __/
/ /_/  __(__  ) /_  
\__/\___/____/\__/  

>>>
```
