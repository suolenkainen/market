#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market

from data import PEOPLE, PURCHASE_ORDERS, SALES_ORDERS, MARKET_PRICES
from data import PEOPLE_ID, PURCHASE_ORDERS_ID, SALES_ORDERS_ID
import transactions, people, needs, production


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


# Add products to people
_people_products = people.add_products_to_people(PEOPLE_PRODUCT, _people_transactions)
print(_people_products)
print()


# Apply needs and deactivate
_people_products, _needs = needs.people_consume_products_and_generate_needs(_people_products, NEEDS)
print(_people_products, _needs)
print()

_people, _needs = needs.deactivate_person(_people, _needs)
print(_people, _needs)
print()


# Adjust needs prices
_needs = needs.adjust_need_prices(_needs, _purchase_dict)
print(_needs)
print()


# Generate products for producers
_producers, _storage = production.generate_products_for_producers(PRODUCERS, STORAGE)
print(_producers, _storage)
print()


# Generate new sales orders based on warehouse and production


# Generate new purchase orders based on needs