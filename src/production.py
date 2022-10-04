#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market

from subprocess import check_output

def generate_products_for_producers(producers, storage):

    for _producer in  producers:
        _produced = _producer["speed"]
        _new_goods_required = True
        for _goods in storage:
            if _goods["idproducer"] == _producer["id"]:
                if _goods["amount"] + _produced > _producer["max"]:
                    _diff = _goods["amount"] + _produced - _producer["max"]
                    _goods["amount"] = _producer["max"]
                    _producer["waste"] = _diff
                else:
                    _goods["amount"] += _produced
                    _producer["waste"] = 0.0
                _new_goods_required = False
                break
        if _new_goods_required:
            _new_stock = {'idproducer': _producer["id"], 'idproduct': _producer["idproduct"], 'amount': _produced}
            storage.append(_new_stock)

    return producers, storage


def adjust_product_prices(producers, purchases):
    price_adjusting = 0.05
    for _producer in producers:
        if purchases == []:
            _producer["price"] = round(_producer["price"] / (price_adjusting + 1), 1)
        elif len(purchases) == 1:
            _producer["price"] = round(purchases[0]["price"] * (price_adjusting / 2 + 1), 1)
        else:
            _producer["price"] = round(purchases[0]["price"] * (price_adjusting * len(purchases) + 1), 1)

    return producers


if __name__ == '__main__':

    check_output("python .\\src\\production.py.test -v", shell=True)