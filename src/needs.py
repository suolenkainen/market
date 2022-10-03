#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market

from subprocess import check_output


def deactivate_person(persons, needs):

    deactive_list = []

    for _need in needs:
        if _need["priority"] == 3:
            for _person in persons:
                if _need["idperson"] == _person["id"]:
                    _person["active"] = False
                    deactive_list.append(_person["id"])
                    break
        if _need["idperson"] in deactive_list:
            _need["idperson"] = -1
            
    needs[:] = [d for d in needs if d.get("idperson") != -1]

    return persons, needs

    
def people_consume_products_and_generate_needs(people_products, needs):

    if people_products == []:
        raise ValueError('people_products == []')

    for _resource in people_products:
        for _need in needs:
            if _need["idperson"] == _resource["idperson"] and _need["idproduct"] == _resource["idproduct"]:
                _resource["amount"] = _resource["amount"] - _need["needs"]
                if _resource["amount"] <= 0:
                    _need["priority"] += 1
                    _need["needs"] = _need["needs"] * 2
                    _resource["amount"] = 0
                    continue
                if _need["priority"] != 0:
                    _need["needs"] = _need["needs"] / (_need["priority"] * 2)
                _need["priority"] = 0

    people_products[:] = [d for d in people_products if d.get("amount") != 0]

    return people_products, needs


def adjust_need_prices(needs, purchase_orders):
    price_adjusting = 0.05

    for _need in needs:
        for _order in purchase_orders:
            if _need["priority"] != 0:
                _need["price"] = round(_need["price"] * (1 + _need["priority"] * price_adjusting * 2), 1)
                break
            elif _need["idperson"] == _order["idpurchaser"] and _need["idproduct"] == _order["idproduct"] and _order["active"]:
                _need["price"] = round(_order["priceone"] * (1 - price_adjusting / 2), 1)
                break
            elif _need["idperson"] == _order["idpurchaser"] and _need["idproduct"] == _order["idproduct"] and not _order["active"]:
                _need["price"] = round(_need["price"] * (1 + price_adjusting), 1)
                break

    return needs

if __name__ == '__main__':

    check_output("python .\\src\\needs.py.test -v", shell=True)