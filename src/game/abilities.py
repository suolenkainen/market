#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market

from subprocess import check_output


if __name__ == '__main__':
    check_output("python .\\src\\game\\abilities.test.py -v", shell=True)