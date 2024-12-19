from source.asciitoolset import *
from source.tests.test_all import test_fonts, roll


def main():
    tcol.cprint(getFileSize(), 'red')
    tcol.cprint(getFntList(), 'green')
    test_fonts()
    roll('red', 'Ma bite')


if __name__ == '__main__':
    main()