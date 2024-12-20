import time

from source.asciitoolset import *

from source.tests.test_all import roll

spc = Spacer(shape = "zebi zeub", color = ["green","red","yellow"])#, random = True)

def main():
    spc._spcnfo()
    print(os.getcwd())
    #print(getFntList())
    spc.print(17)
    spc.set(cutoff = False, shape = "zeub zebi")
    spc.print(100)
    spc.set(color="red")
    spc.print(3)

    print(spc.__repr__())
    #roll('red', "test")

if __name__ == "__main__":
    main()