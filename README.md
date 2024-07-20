<h1 align="center">========ASCII-Toolset===========</h1>

<h2>This is a complete module that allows you to manipulate characters 
to make clean terminal-based programs UIs</h2>



## Authors

- [@eurekaKane](https://www.github.com/eurekaKane)

## Description

<p align="center"> This module is mainly using a Figlet port to Python (pyFiglet)</p>

## Usage/Examples

```python
import ascc from asciitoolset

def myfunc():
    myban = ascc.Banner("myText","myFont","myColor")
    myban.prntBan()
    myban.setBan(color("lightBlue"))
