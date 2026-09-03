# -*- encoding: utf-8 -*-

from source.asciitoolset import *
from source.tests.test_all import test_fonts, roll, fix_fonts


def main():
    print(get_file_size(FILES))

    print(get_fnt_list())
    #test_fonts()
    #
    #fix_fonts()
    #roll('red', 'Ma bite')
    #test_fonts()

if __name__ == '__main__':
    main()