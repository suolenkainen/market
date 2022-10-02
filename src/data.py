#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market

import utils
import os

## Global variables
PATH = os.path.abspath(os.getcwd())

people_path = PATH + "\\src\\resources\\people.csv"
products_path = PATH + "\\src\\resources\\products.csv"
people_product_path = PATH + "\\src\\resources\\people-product.csv"
producers_path = PATH + "\\src\\resources\\producers.csv"
storage_path = PATH + "\\src\\resources\\storage.csv"

PEOPLE = utils.csv_to_dict_converter(people_path)
PEOPLE_PRODUCT = utils.csv_to_dict_converter(people_product_path)
PRODUCT = utils.csv_to_dict_converter(products_path)
PRODUCERS = utils.csv_to_dict_converter(producers_path)
STORAGE = utils.csv_to_dict_converter(storage_path)

print()