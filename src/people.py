#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market

from subprocess import check_output


def adjust_person_wealth(people, purchases):

    for _person in people:
        for _order in purchases:
            if _person["id"] == _order["idperson"]:
                _price = round(_order["amount"] * _order["price"], 1)
                _person["wealth"] = _person["wealth"] - _price
                if _person["wealth"] < 0:
                    _person["wealth"] = 0.0
                    _person["active"] = False

    return people


def add_products_to_people(people_product, purchase_orders):

    for _order in purchase_orders:
        for _row in people_product:
            if _order["idperson"] == _row["idperson"] and _order["idproduct"] == _row["idproduct"]:
                _row["amount"] = _row["amount"] + _order["amount"]
                break
            elif _order["idperson"] == _row["idperson"] and _order["idproduct"] != _row["idproduct"]:
                _new_row = {'idperson': _order["idperson"], 'idproduct': _order["idproduct"], 'amount': _order["amount"]}
                people_product.append(_new_row)
                break

    return people_product


def connect_card_to_person(card, person, card_person_connection, transfer_data):
    _person_id = person["ID"]
    _card_id = card["ID"]
    
    for _connection in card_person_connection:
        if _connection['CARD_ID'] == _card_id:
            _connection['PERSON_ID'] = _person_id
            return card_person_connection
    
    _new_connection = transfer_data
    _new_connection['CARD_ID'] = _card_id
    _new_connection['PERSON_ID'] = _person_id
    card_person_connection.append(_new_connection)

    return card_person_connection


if __name__ == '__main__':

    check_output("python .\\src\\people.test.py -v", shell=True)