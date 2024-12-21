import time

from source import *

from source.tests.test_all import roll

spc = Spacer(shape = "zebi zeub", color = ["green","red","yellow"])#, random = True)

def main():
    spc.__spc_nfo__()
    print(os.getcwd())
    #print(getFntList())
    spc.print_spacer(17)
    spc.set(cutoff = False, shape = "zeub zebi")
    spc.print_spacer(100)
    spc.set(color="red")
    spc.print_spacer(3)
    print(Colr.Ansi.ansi_comb("BRGYBMCW",
                              ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'],
                              ['white', 'cyan', 'magenta', 'blue', 'yellow', 'green', 'red', 'black']))
    print(spc.__repr__())
    #roll('red', "test")

if __name__ == "__main__":
    main()