from source.asciitoolset import *
from source.tests.test_all import test_fonts, roll, fix_fonts


def main():
    tcol.cprint(getFileSize(), 'red')
    tcol.cprint(getFntList(), 'green')
    test_fonts()

    fix_fonts()
    roll('red', 'Ma bite')
    test_fonts()

if __name__ == '__main__':
    main()