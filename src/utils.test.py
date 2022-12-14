#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market


import unittest
import utils
import os

PATH = os.path.abspath(os.getcwd())


class UtilsTests(unittest.TestCase):

    # Testing csv converter
    def test_1_csv_to_dict_converter(self):
        _test_data_text = "id|name|wealth|active\n0|Alpha|1|True"
        _test_result_dict = [{'id': 0, 'name': 'Alpha', 'wealth': 1, 'active': True}]
        _filename = 'csv_to_dict.csv'

        _file = open(_filename, "w")
        _file.write(_test_data_text)
        _file.close()

        _result_dict = utils.csv_to_dict_converter(PATH + "\\" + _filename)

        if os.path.exists(_filename):
            os.remove(_filename)
        
        self.assertEqual(_result_dict, _test_result_dict)


    # Testing csv converter
    def test_2_csv_to_dict_converter(self):
        _test_data_text = 'ID|SET_ID|SET|COLOUR|NAME|TYPE|ATTRIBUTE|RARITY|ARTIST|DESCRIPTION|NORMAL_AMOUNT|FOIL_AMOUNT|HOLOGRAM_AMOUNT|GOLD_AMOUNT\n222|P1-001|Promo pack 1: Pride Month|Green|Forest|Mana|Mana source|Common|Corym Baghig|0|40|10|4|0'
        _test_result_dict = [{'ID': 222, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0, 'NORMAL_AMOUNT': 40, 'FOIL_AMOUNT': 10, 'HOLOGRAM_AMOUNT': 4, 'GOLD_AMOUNT': 0}]
        _filename = 'csv_to_dict.csv'

        _file = open(_filename, "w")
        _file.write(_test_data_text)
        _file.close()

        _result_dict = utils.csv_to_dict_converter(PATH + "\\" + _filename)

        if os.path.exists(_filename):
            os.remove(_filename)
        
        
        self.assertEqual(_result_dict, _test_result_dict)


if __name__ == '__main__':
    unittest.main()