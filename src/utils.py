#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market

from subprocess import check_output
import csv
from re import match as regmatch


def csv_to_dict_converter(filename):
    with open(filename, newline='') as csvfile:
        file_data=csv.reader(csvfile, delimiter='|')
        headers=next(file_data)
        _result_list_dicts = [dict(zip(headers,i)) for i in file_data]
    csvfile.close()

    for _dict in _result_list_dicts:
        for key, value in _dict.items():
            regid = r"id"
            regamount = r"amount"
            if regmatch(regid, value) or regmatch(regamount, value):
                _dict[key] = int(value)
                continue
            if key == "date":
                _dict[key] = str(value)
                continue
            # Converts integers to proper form
            regint = r"^[0-9]"
            if regmatch(regint, value):
                _dict[key] = float(value)
                continue

            # Converts boolean to proper form
            elif value in ["True", "False"]:
                _dict[key] = bool(value)

    return _result_list_dicts
    
    
if __name__ == '__main__':
    check_output("python .\\src\\utils.test.py -v", shell=True)