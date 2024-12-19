import time

from source.asciitoolset import *

from source.tests.test_all import roll

spc = Spacer(shape = "skibidi", color = ["green","red","yellow"])#, random = True)

def main():
    spc._spcnfo()
    print(os.getcwd())
    #print(getFntList())
    spc.sp_print(17)
    print(spc.__repr__())
    spc.set(color="red")
    spc.sp_print(3)
    #roll('red', "test")

if __name__ == "__main__":
    main()