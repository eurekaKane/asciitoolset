# -*- encoding : utf-8 -*-
from pyfiglet import FontNotFound

# IMPORTS

from source.asciitoolset import *

from source.utils.utils import __local, __tmp

failed_fonts = []
working_fonts = []

def roll(col, txt):
    """
    Roll through every font in the font list and renders a Banner for each with the specified parameters
    :param col: color to display
    :param txt: text to display
    :return: None
    """
    fontList = getFntList()

    spc = Spacer(shape = 2, color ='white')

    for font in fontList:
        roll_ban = Banner(font, col, txt, width = 100)
        tcol.cprint(f'{roll_ban.__repr__()}\n', 'green')
        roll_ban.printBanner()
        time.sleep(0.1)
        spc.sp_print(175)

    return None


def test_fonts():
    tmp_list = getFntList()

    for font in tmp_list:
        try:
            _ = Figlet(font)
        except FontNotFound:
            failed_fonts.append(font)
            tcol.cprint(font, 'red')
        else:
            working_fonts.append(font)
            tcol.cprint(font, 'green')

    tcol.cprint(failed_fonts, 'red')


def fix_fonts():
    tmp_list = getFntList()
    checked_fonts = []
    with open(__tmp+'\\fontList.txt', 'w') as file:
        file.truncate()
        file.close()

    with open(__tmp+'\\fontList.txt', 'w') as file:
        for font in tmp_list:
            for _ in failed_fonts:
                if font in checked_fonts:
                    pass
                elif font in failed_fonts:
                    checked_fonts.append(font)
                else:
                    file.write(font + '\n')
                    checked_fonts.append(font)



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