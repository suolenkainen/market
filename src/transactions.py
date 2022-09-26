#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market

import os
from subprocess import check_output

PATH = os.path.abspath(os.getcwd())

def combine_purchase_and_sell_orders(_purchase_dict, _sales_dict):
    return []


if __name__ == '__main__':
    check_output("python .\\src\\transactions.py.test -v", shell=True)