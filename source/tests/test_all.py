# -*- encoding : utf-8 -*-
from pyfiglet import FontNotFound

# IMPORTS

from source.asciitoolset import *


def roll(col, txt):
    """
    Roll through every font in the font list and renders a Banner for each with the specified parameters
    :param col: color to display
    :param txt: text to display
    :return: None
    """
    fontList = getFntList()

    spc = Spacer(2, 'white')

    for font in fontList:
        rollBan = Banner(font, col, txt, width = 100)
        tcol.cprint(f'{rollBan.__repr__()}\n', 'green')
        rollBan.printBanner()
        time.sleep(0.5)
        spc.sp_print(25)

    return None


def test_fonts():
    tmp_list = getFntList()
    working = 0
    failed_fonts = []

    for font in tmp_list:
        try:
            _ = Figlet(font)
        except FontNotFound:
            failed_fonts.append(font)
            tcol.cprint(font, 'red')
        else:
            working += 1
            tcol.cprint(font, 'green')

    tcol.cprint(failed_fonts, 'red')


def fix_fonts():
    pass


#def testFonts():
#    fontList = getFntList()
#    passed = 0
#    failed = []
#    status = 'green'
#    for font in fontList:
#        try:
#            _ = Figlet(font)
#        except FigletError:
#            ln_clr()
#            tcol.cprint(f"{font} : Failed !", "red", end=' ', flush=True)
#            tcol.cprint(f"{passed} tests passed / {len(fontList)}", "green" if passed >= len(fontList) / 2 else "red",
#                        end='\r', flush=True)
#            time.sleep(0.05)
#            failed.append(font)
#            status = 'red'
#        else:
#            passed += 1
#            ln_clr()
#            tcol.cprint(f"{font} : OK !", "green", end=' ', flush=True)
#            tcol.cprint(f"{passed} tests passed / {len(fontList)}", status, end='\r', flush=True)
#            time.sleep(0.05)
#
#    tcol.cprint(f"Failed: {failed}", "red")
#    return failed
#
#
#def fixFonts():
#    fntList = getFntList()
#    passedFnt = []
#    failed = testFonts()
#    with open('../files.txt', 'w') as t:
#        t.truncate()
#        t.close()
#
#    with open('../files.txt', 'w') as f:
#        for fonts in fntList:
#            for _ in failed:
#                if fonts in passedFnt:
#                    pass
#                elif fonts in failed:
#                    tcol.cprint(f"{fonts} is not working, it has been deleted !\n", "red")
#                    passedFnt.append(fonts)
#                else:
#                    f.write(fonts + "\n")
#                    tcol.cprint(f"{fonts} is good !\n", "green")
#                    passedFnt.append(fonts)
#        f.close()
#        # TODO : fix fixFonts() haha !
#