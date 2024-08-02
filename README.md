<h1 align="center">===========ASCII-Toolset===========</h1>

<h2>This is a module that allows you to manipulate characters 
to make clean terminal-based programs UIs</h2>



## Authors

- [@eurekaKane](https://www.github.com/eurekaKane)

## Description

This module uses mainly pyFiglet a port of Figlet to python made by pwaller(INSERT HREF)
I had the idea of making it after realizing that I had been strugling making CLI UIs for each program I made.
What I usually did was a spacer function and generate a Figlet banner online then copy it in my code. So to spare me the 
pain I decided to write a module simple of use that automates all the process 

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
