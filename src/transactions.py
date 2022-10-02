#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market

import os
from subprocess import check_output

PATH = os.path.abspath(os.getcwd())

def combine_purchase_and_sell_orders(purchase_dict, sales_dict):
    _matching_orders = []
    
    # Sort lists from lowest price to highest
    purchase_dict = sorted(purchase_dict, key=lambda d: d['priceone']) 
    sales_dict = sorted(sales_dict, key=lambda d: d['priceone']) 

    for _purchase in purchase_dict:
        if _purchase["active"] == "False":
            continue
        for _sales in sales_dict:
            if _sales["active"] == "False":
                continue
            if _purchase["product"] == _sales["product"]:
                print(_purchase["product"], _purchase, _sales)
                _purchase["active"] = "False"
                _sales["active"] = "False"
                match, _purchase, _sales = check_prices(_purchase, _sales)
                if not match:
                    continue
                _matching_orders.append([_purchase["id"], _sales["id"]])


    return _matching_orders, purchase_dict, sales_dict

def check_prices(purchase, sales):
    if purchase["priceone"] == sales["priceone"]:
        match = True
    
    return match, purchase, sales

if __name__ == '__main__':
    #check_output("python .\\src\\transactions.py.test -v", shell=True)
    _test_purchase_dict = [{'id': '0', 'product': '0', 'purchaser': '0', 'amount': '1', 'priceone': '11', "active": "True"}, {'id': '1', 'product': '2', 'purchaser': '0', 'amount': '1', 'priceone': '10', "active": "True"}]
    _test_sales_dict = [{'id': '0', 'product': '0', 'seller': '0', 'amount': '1', 'priceone': '11', "active": "True"}, {'id': '1', 'product': '2', 'seller': '0', 'amount': '1', 'priceone': '10', "active": "True"}]
    combine_purchase_and_sell_orders(_test_purchase_dict,_test_sales_dict)