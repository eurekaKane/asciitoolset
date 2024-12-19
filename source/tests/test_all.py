# -*- encoding : utf-8 -*-

# IMPORTS

from source.asciitoolset import *

from source.utils.utils import *


def testFonts():
    fontList = getFntList()
    passed = 0
    failed = []
    status = 'green'
    for font in fontList:
        try:
            _ = Figlet(font)
        except FigletError:
            ln_clr()
            tcol.cprint(f"{font} : Failed !", "red", end=' ', flush=True)
            tcol.cprint(f"{passed} tests passed / {len(fontList)}", "green" if passed >= len(fontList) / 2 else "red",
                        end='\r', flush=True)
            # time.sleep(0.05)
            failed.append(font)
            status = 'red'
        else:
            passed += 1
            ln_clr()
            tcol.cprint(f"{font} : OK !", "green", end=' ', flush=True)
            tcol.cprint(f"{passed} tests passed / {len(fontList)}", status, end='\r', flush=True)
            # time.sleep(0.05)

    tcol.cprint(f"Failed: {failed}", "red")
    return failed


def fixFonts():
    fntList = getFntList()
    passedFnt = []
    failed = testFonts()
    with open('../files.txt', 'w') as t:
        t.truncate()
        t.close()

    with open('../files.txt', 'w') as f:
        for fonts in fntList:
            for _ in failed:
                if fonts in passedFnt:
                    pass
                elif fonts in failed:
                    tcol.cprint(f"{fonts} is not working, it has been deleted !\n", "red")
                    passedFnt.append(fonts)
                else:
                    f.write(fonts + "\n")
                    tcol.cprint(f"{fonts} is good !\n", "green")
                    passedFnt.append(fonts)
        f.close()
        # DONE : fix fixFonts() haha !
