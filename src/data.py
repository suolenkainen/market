#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market

import utils
import os

## Global variables
PATH = os.path.abspath(os.getcwd())

people_path = PATH + "\\src\\resources\\people.csv"
purchase_path = PATH + "\\src\\resources\\purchase-order.csv"
sales_path = PATH + "\\src\\resources\\sales-order.csv"
market_path = PATH + "\\src\\resources\\market-prices.csv"

PEOPLE = utils.csv_to_dict_converter(people_path)
PEOPLE_ID = len(PEOPLE)

PURCHASE_ORDERS = utils.csv_to_dict_converter(purchase_path)
PURCHASE_ORDERS_ID = len(PURCHASE_ORDERS)

SALES_ORDERS = utils.csv_to_dict_converter(sales_path)
SALES_ORDERS_ID = len(SALES_ORDERS)

MARKET_PRICES = utils.csv_to_dict_converter(market_path)

print()