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
purchase_path = PATH + "\\src\\resources\\purchase-order.csv"
sales_path = PATH + "\\src\\resources\\sales-order.csv"

PEOPLE = utils.csv_to_dict_converter(people_path)
PEOPLE_ID = len(PEOPLE)

PEOPLE_PRODUCT = utils.csv_to_dict_converter(people_product_path)

PRODUCT = utils.csv_to_dict_converter(products_path)
PRODUCT_ID = len(PRODUCT)

PRODUCERS = utils.csv_to_dict_converter(producers_path)
PRODUCERS_ID = len(PRODUCERS)

STORAGE = utils.csv_to_dict_converter(storage_path)

PURCHASE_ORDERS = utils.csv_to_dict_converter(purchase_path)
PURCHASE_ORDERS_ID = len(PURCHASE_ORDERS)

SALES_ORDERS = utils.csv_to_dict_converter(sales_path)
SALES_ORDERS_ID = len(SALES_ORDERS)

print()