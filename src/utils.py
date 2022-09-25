#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market

from subprocess import check_output
import random
import csv


def random_item_from_list(list):
    _random_item = random.choice(list)
    return _random_item + 1


def csv_to_dict_converter(filename):
    with open(filename, newline='') as csvfile:
        file_data=csv.reader(csvfile)
        headers=next(file_data)
        _result_dict = [dict(zip(headers,i)) for i in file_data]
    return _result_dict
    

if __name__ == '__main__':
    check_output("python .\\src\\utils.py.test -v", shell=True)