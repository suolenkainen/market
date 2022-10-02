#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market

from subprocess import check_output

def generate_products_for_producers(producer, storage):

    _produced = producer["speed"]
    _new_goods_required = True
    for _goods in storage:
        if _goods["idproducer"] == producer["id"]:
            if _goods["amount"] + _produced > producer["max"]:
                _diff = _goods["amount"] + _produced - producer["max"]
                _goods["amount"] = producer["max"]
                producer["waste"] = _diff
            else:
                _goods["amount"] += _produced
                producer["waste"] = 0.0
            _new_goods_required = False
            break
    if _new_goods_required:
        _new_stock = {'idproducer': producer["id"], 'idproduct': producer["idproduct"], 'amount': _produced}
        storage.append(_new_stock)

    return producer, storage


def adjust_product_prices(producer, purchases):
    price_adjusting = 0.05

    if purchases == []:
        producer["price"] = round(producer["price"] / (price_adjusting + 1), 1)
    elif len(purchases) == 1:
        producer["price"] = round(purchases[0]["price"] * (price_adjusting / 2 + 1), 1)
    else:
        producer["price"] = round(purchases[0]["price"] * (price_adjusting * len(purchases) + 1), 1)

    return producer


if __name__ == '__main__':

    check_output("python .\\src\\production.py.test -v", shell=True)