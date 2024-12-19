import time

from source.asciitoolset import *

from source.tests.test_all import roll

spc = Spacer(shape = "skibidi", color = ["green","red","yellow"])#, random = True)

def main():
    spc.__spc_nfo__()
    print(os.getcwd())
    #print(getFntList())
    spc.sp_print(17)
    spc.set(shape = "zob")
    spc.set(cutoff = True)
    spc.sp_print(100)
    print(spc.__repr__())
    spc.set(color="red")
    spc.sp_print(3)
    #roll('red', "test")

if __name__ == "__main__":
    main()