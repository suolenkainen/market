#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market

from subprocess import check_output
from copy import copy


def combine_purchase_and_sell_orders(purchase_dict, sales_dict):
    matching_orders = []
    
    # Sort lists from lowest price to highest
    purchase_dict = sorted(purchase_dict, key=lambda d: d['priceone']) 
    sales_dict = sorted(sales_dict, key=lambda d: d['priceone']) 

    for _purchase in purchase_dict:
        if _purchase["active"] == False:
            continue
        for _sales in sales_dict:
            if _sales["active"] == False:
                continue
            if _purchase["product"] == _sales["product"]:
                match, _purchase, _sales = check_prices(_purchase, _sales)
                if not match:
                    continue
                
                if _purchase["amount"] == _sales["amount"]:
                    _purchase["active"] = False
                    _sales["active"] = False
                    matching_orders.append([_purchase["id"], _sales["id"]])
                else:
                    _purchase, _new_purchase, _sales, _new_sales = generate_additional_transactions(_purchase, _sales, len(purchase_dict), len(sales_dict))
                    if _new_purchase != {}:
                        purchase_dict.append(_new_purchase)
                    if _new_sales != {}:
                        sales_dict.append(_new_sales)
                    matching_orders.append([_purchase["id"], _sales["id"]])

    return matching_orders, purchase_dict, sales_dict


def check_prices(purchase, sales):
    margin = 1.1

    # Check that prices are within margin
    if purchase["priceone"] == sales["priceone"]:
        match = True
    elif purchase["priceone"] < sales["priceone"] and sales["priceone"] <= purchase["priceone"] * margin:
        match = True
        purchase["priceone"] = max([sales["priceone"], purchase["priceone"]])
        sales["priceone"] = max([sales["priceone"], purchase["priceone"]])
    else:
        match = False

    return match, purchase, sales


def generate_additional_transactions(purchase, sales, len_purch, len_sales):
    new_purchase = {}
    new_sales = {}

    if purchase["amount"] > sales["amount"]:
        _diff = purchase["amount"] - sales["amount"]
        new_purchase = copy(purchase)
        new_purchase["amount"] = _diff
        new_purchase["id"] = len_purch
        purchase["amount"] -= _diff

    if purchase["amount"] < sales["amount"]:
        _diff = sales["amount"] - purchase["amount"]
        new_sales = copy(sales)
        new_sales["amount"] = _diff
        new_sales["id"] = len_sales
        sales["amount"] -= _diff

    purchase["active"] = False
    sales["active"] = False

    return purchase, new_purchase, sales, new_sales


def crete_list_of_orders(purchase_orders, sales_orders, matches):
    producer_transactions = []
    people_transactions = []
    
    for _match in matches:
        for _purchase_order in purchase_orders:
            if _purchase_order["id"] == _match[0]:
                _producer_transaction = {'producer': _purchase_order["id"], 'product': _purchase_order["product"], 
                                        'price': _purchase_order["priceone"]}
                producer_transactions.append(_producer_transaction)
                break
        for _sales_order in sales_orders:
            if _sales_order["id"] == _match[1]:
                _person_transaction = {'person': _purchase_order["id"], 'product': _purchase_order["product"], 'amount': _sales_order["amount"], 'price': _purchase_order["priceone"]}
                people_transactions.append(_person_transaction)
                break

    return producer_transactions, people_transactions

if __name__ == '__main__':
    # _test_purchase_dict = [{'id': 0, 'product': 0, 'purchaser': 0, 'amount': 1, 'priceone': 11, "active": True}, {'id': 1, 'product': 2, 'purchaser': 0, 'amount': 1, 'priceone': 10, "active": True}]
    # _test_sales_dict = [{'id': 0, 'product': 0, 'seller': 0, 'amount': 1, 'priceone': 11, "active": True}, {'id': 1, 'product': 2, 'seller': 0, 'amount': 1, 'priceone': 10, "active": True}]
    # combine_purchase_and_sell_orders(_test_purchase_dict,_test_sales_dict)

    check_output("python .\\src\\transactions.py.test -v", shell=True)