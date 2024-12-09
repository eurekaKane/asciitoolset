<h1 align="center">===========ASCII-Toolset===========</h1>



<h2>This is a module that allows you to manipulate characters 
to make clean terminal-based programs UIs</h2>

<h1 align="center">WARNING !</h1>
<h2>Don't clone my repo nothing works, like seriously i need to make a setup.py file else you are going to need and fix everything by hand to make it work it's terrible !</h2>
<h2>Like the mess it is in terms of dependencies and like shit you need to know to make it work is awful. GOD ! This repo is a construction site. Fixing my stuff ASAP :)</h2>

## Changelog

Global changes :
-
* Added an '__ _init_ __.py' file (it's empty for the moment)
* Added a copy of 'files.txt' to /source for test purposes (path to original one will be added in master soon)

Specific changes :
-
* Few experimental features for testing the fonts : testFonts() --> fixFonts() (the two of them will be splited) ; getFileSize(), getFontList
* New roll() func, it basically renders out a banner for each font name in 'files.txt'
* Opening an experimental branch

Future changes :
-
* 
* fill
* fill


## Supported
* Every device with Python3 and pip installed

## Guide
<details>
<summary>Guide for beginners</summary>

1. <details><summary>Cloning GitHub repo</summary>
   
   1. fill
   2. fill
   3. fill
   
   </details>

2. <details><summary>Downloading .zip archive on GitHub</summary>

   1. fill
   2. fill
   3. fill

   </details>

</details>

<details><summary>Guide for advanced people</summary>

1. fill 
2. fill
3. fill

</details>

## Modules used
[requirements.txt](requirements.txt)
* [setuptools](https://pypi.org/project/setuptools/)
* [colorama](https://pypi.org/project/colorama/)
* [termcolor](https://pypi.org/project/termcolor/)
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
