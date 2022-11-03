#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market

from data import PEOPLE, PURCHASE_ORDERS, SALES_ORDERS, MARKET_PRICES
from data import PEOPLE_ID, PURCHASE_ORDERS_ID, SALES_ORDERS_ID
import transactions, people, needs


# Handle transactions -> matches, and purchases and sales in dict form
_matching_orders, _purchase_dict, _sales_dict = transactions.combine_purchase_and_sell_orders(PURCHASE_ORDERS, SALES_ORDERS)
print(_matching_orders, _purchase_dict, _sales_dict)
print()

_producer_transactions, _people_transactions = transactions.crete_list_of_orders(_matching_orders, _purchase_dict, _sales_dict)
print(_producer_transactions, _people_transactions)
print()

# Give money to producers


# Take money from people
_people = people.adjust_person_wealth(PEOPLE, _people_transactions)
print(_people)
print()
