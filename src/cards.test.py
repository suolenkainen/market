#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market


import unittest
import cards


class CardsTests(unittest.TestCase):


    def test_1_generate_list_of_cards_from_source_data(self):
        test_data_dictionary = [{'ID': 222, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0, 'NORMAL_AMOUNT': 2, 'FOIL_AMOUNT': 1, 'HOLOGRAM_AMOUNT': 1, 'GOLD_AMOUNT': 1},
                                {'ID': 223, 'SET_ID': 'P1-002', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Island', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0, 'NORMAL_AMOUNT': 1, 'FOIL_AMOUNT': 1, 'HOLOGRAM_AMOUNT': 0, 'GOLD_AMOUNT': 0}]
        test_result_dict = [{'ID': 0, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'SPECIAL' : 'Normal', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0},
                            {'ID': 1, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'SPECIAL' : 'Normal', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0},
                            {'ID': 2, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'SPECIAL' : 'Foil', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0},
                            {'ID': 3, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'SPECIAL' : 'Hologram', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0},
                            {'ID': 4, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'SPECIAL' : 'Gold', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0},
                            {'ID': 5, 'SET_ID': 'P1-002', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Island', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'SPECIAL' : 'Normal', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0},
                            {'ID': 6, 'SET_ID': 'P1-002', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Island', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'SPECIAL' : 'Foil', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0}]

        _result_dict = cards.generate_list_of_cards_from_source_data(test_data_dictionary)

        self.assertEqual(_result_dict, test_result_dict)


if __name__ == '__main__':
    unittest.main()