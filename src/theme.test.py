#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market


import unittest
import theme


class ThemeTests(unittest.TestCase):

    def test_1_connect_cards_to_a_theme(self):
        test_data_cards = [{'ID': 0, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Super Rare', 'SPECIAL' : 'Normal', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0}]
        test_data_theme = {"ID": 0,"NAME": "Super Rare Cards","THEME_TYPE": "RARITY","ARTIST": "","CARD_ID": "","TYPE": "","RARITY": "Super Rare","SPECIAL": "","SET": "","COLOUR": "","GENERAL_ATTRACTION": 3.0}

        
        _test_data_connections = []

        result_connections = [{"CARD_ID": 0, "THEME_ID": 0, "ATTRACTION": 3.0}]
        
        _result_connections = theme.connect_cards_to_a_theme(test_data_cards, test_data_theme, _test_data_connections)

        self.assertEqual(_result_connections, result_connections)

class ThemeTests(unittest.TestCase):

    def test_1_connect_cards_to_a_theme(self):
        test_data_cards = [{'ID': 0, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Super Rare', 'SPECIAL' : 'Normal', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0}]
        test_data_theme = {"ID": 0,"NAME": "Super Rare Cards","THEME_TYPE": "RARITY","ARTIST": "","CARD_ID": "","TYPE": "","RARITY": "Super Rare","SPECIAL": "","SET": "","COLOUR": "","GENERAL_ATTRACTION": 3.0}

        
        _test_data_connections = []

        result_connections = [{"CARD_ID": 0, "THEME_ID": 0, "ATTRACTION": 3.0}]
        
        _result_connections = theme.connect_cards_to_a_theme(test_data_cards, test_data_theme, _test_data_connections)

        self.assertEqual(_result_connections, result_connections)


    def test_2_connect_cards_to_a_theme_one_card_from_multiple(self):
        test_data_cards = [{'ID': 0, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Super Rare', 'SPECIAL' : 'Normal', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0},
                            {'ID': 1, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Super Rare', 'SPECIAL' : 'Normal', 'ARTIST': '123 Baghig', 'DESCRIPTION': 0},
                            {'ID': 2, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Super Rare', 'SPECIAL' : 'Normal', 'ARTIST': '14 Baghig', 'DESCRIPTION': 0},
                            {'ID': 3, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Super Rare', 'SPECIAL' : 'Normal', 'ARTIST': 'Co463rym Baghig', 'DESCRIPTION': 0}]
        test_data_theme = {"ID": 0,"NAME": "Corym Baghig Cards","THEME_TYPE": "ARTIST","ARTIST": "Corym Baghig","CARD_ID": "","TYPE": "","RARITY": "","SPECIAL": "","SET": "","COLOUR": "","GENERAL_ATTRACTION": 3.0}

        
        _test_data_connections = []

        result_connections = [{"CARD_ID": 0, "THEME_ID": 0, "ATTRACTION": 3.0}]
        
        _result_connections = theme.connect_cards_to_a_theme(test_data_cards, test_data_theme, _test_data_connections)

        self.assertEqual(_result_connections, result_connections)


    def test_3_connect_cards_to_a_theme_no_connections(self):
        test_data_cards = [{'ID': 0, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Super Rare', 'SPECIAL' : 'Normal', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0},
                            {'ID': 1, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Super Rare', 'SPECIAL' : 'Normal', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0},
                            {'ID': 2, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Super Rare', 'SPECIAL' : 'Normal', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0},
                            {'ID': 3, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Super Rare', 'SPECIAL' : 'Normal', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0}]
        test_data_theme = {"ID": 0,"NAME": "Corym Baghig Cards","THEME_TYPE": "ARTIST","ARTIST": "Oola Baghig","CARD_ID": "","TYPE": "","RARITY": "","SPECIAL": "","SET": "","COLOUR": "","GENERAL_ATTRACTION": 3.0}
        
        _test_data_connections = []

        result_connections = []
        
        _result_connections = theme.connect_cards_to_a_theme(test_data_cards, test_data_theme, _test_data_connections)

        self.assertEqual(_result_connections, result_connections)


    def test_4_connect_cards_to_a_theme_existing_connections(self):
        test_data_cards = [{'ID': 0, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Super Rare', 'SPECIAL' : 'Hologram', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0},
                            {'ID': 1, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Super Rare', 'SPECIAL' : 'Foil', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0},
                            {'ID': 2, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Super Rare', 'SPECIAL' : 'Normal', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0},
                            {'ID': 3, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Super Rare', 'SPECIAL' : 'Gold', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0}]
        test_data_theme = {"ID": 0,"NAME": "Holograms","THEME_TYPE": "SPECIAL","ARTIST": "","CARD_ID": "","TYPE": "","RARITY": "","SPECIAL": "Hologram","SET": "","COLOUR": "","GENERAL_ATTRACTION": 2.0}
        
        _test_data_connections = [{"CARD_ID": 1, "THEME_ID": 1, "ATTRACTION": 4.0}]

        result_connections = [{"CARD_ID": 1, "THEME_ID": 1, "ATTRACTION": 4.0},{"CARD_ID": 0, "THEME_ID": 0, "ATTRACTION": 2.0}]
        
        _result_connections = theme.connect_cards_to_a_theme(test_data_cards, test_data_theme, _test_data_connections)

        self.assertEqual(_result_connections, result_connections)



if __name__ == '__main__':
    unittest.main()