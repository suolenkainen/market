#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market

from subprocess import check_output


def adjust_person_wealth(person, purchases):
    
    for _order in purchases:
        if person["id"] == _order["person"]:
            _price = round(_order["amount"] * _order["price"], 1)
            person["wealth"] = person["wealth"] - _price
            if person["wealth"] < 0:
                person["wealth"] = 0.0
                person["active"] = False

    return person


def add_products_to_people(people_product, orders):

    for _order in orders:
        for _row in people_product:
            if _order["person"] == _row["idperson"] and _order["product"] == _row["idproduct"]:
                _row["amount"] = _row["amount"] + _order["amount"]
                break
            elif _order["person"] == _row["idperson"] and _order["product"] != _row["idproduct"]:
                _new_row = {'idperson': _order["person"], 'idproduct': _order["product"], 'amount': _order["amount"]}
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

    check_output("python .\\src\\people.py.test -v", shell=True)