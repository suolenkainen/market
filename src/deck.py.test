#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market


import unittest
import deck

class DeckTests(unittest.TestCase):


    def test_1_connect_cards_to_decks(self):
        test_data_cards = [{'ID': 0, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'SPECIAL' : 'Normal', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0},
                            {'ID': 6, 'SET_ID': 'P1-002', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Island', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'SPECIAL' : 'Foil', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0}]
        
        test_data_decks = [{"ID": 0,"NAME": "Promotional Package 1: Pride Month Booster",
                            "SET": "Promotional Package 1: Pride Month","RELEASE_DATE": "06/06/2022","TYPE": "Booster","PRICE":4.99,"ACTIVE": True}]
        test_data_connections = []

        result_card_deck_connections = [{"CARD_ID": 0, "DECK_ID": 0}, {"CARD_ID": 6, "DECK_ID": 0}]
        
        _result_card_deck_connections = deck.connect_cards_to_decks(test_data_cards, test_data_decks, test_data_connections)

        self.assertEqual(_result_card_deck_connections, result_card_deck_connections)


    def test_2_connect_cards_to_decks_duplicate(self):
        test_data_cards = [{'ID': 0, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'SPECIAL' : 'Normal', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0},
                            {'ID': 6, 'SET_ID': 'P1-002', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Island', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'SPECIAL' : 'Foil', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0}]
        
        test_data_decks = [{"ID": 0,"NAME": "Promotional Package 1: Pride Month Booster",
                            "SET": "Promotional Package 1: Pride Month","RELEASE_DATE": "06/06/2022","TYPE": "Booster","PRICE":4.99,"ACTIVE": True}]
        test_data_connections = [{"CARD_ID": 0, "DECK_ID": 0}]

        result_card_deck_connections = [{"CARD_ID": 0, "DECK_ID": 0}, {"CARD_ID": 6, "DECK_ID": 0}]
        
        _result_card_deck_connections = deck.connect_cards_to_decks(test_data_cards, test_data_decks, test_data_connections)

        self.assertEqual(_result_card_deck_connections, result_card_deck_connections)

    
    def test_3_connect_cards_to_decks_multiple_decks(self):
        test_data_cards = [{'ID': 0, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'SPECIAL' : 'Normal', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0},
                            {'ID': 6, 'SET_ID': 'P1-002', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Island', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'SPECIAL' : 'Foil', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0}]
        
        test_data_decks = [{"ID": 0,"NAME": "Promotional Package 1","SET": "Pride Month","RELEASE_DATE": "06/06/2022","TYPE": "Booster","PRICE":4.99 ,"ACTIVE": True},
                            {"ID": 1,"NAME": "Promotional Package 1","SET": "Pride Month","RELEASE_DATE": "06/06/2022","TYPE": "Starter Set","PRICE":4.99,"ACTIVE": True},
                            {"ID": 2,"NAME": "Promotional Package 1","SET": "Pride Month","RELEASE_DATE": "06/06/2022","TYPE": "Booster","PRICE":4.99,"ACTIVE": True}]
        test_data_connections = []

        result_card_deck_connections = [{"CARD_ID": 0, "DECK_ID": 0}, {"CARD_ID": 0, "DECK_ID": 1}, {"CARD_ID": 0, "DECK_ID": 2},
                                {"CARD_ID": 6, "DECK_ID": 0}, {"CARD_ID": 6, "DECK_ID": 1}, {"CARD_ID": 6, "DECK_ID": 2}]
        
        _result_card_deck_connections = deck.connect_cards_to_decks(test_data_cards, test_data_decks, test_data_connections)

        self.assertEqual(_result_card_deck_connections, result_card_deck_connections)

    
    def test_4_connect_cards_to_decks_inactive_decks(self):
        test_data_cards = [{'ID': 0, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'SPECIAL' : 'Normal', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0},
                            {'ID': 6, 'SET_ID': 'P1-002', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Island', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'SPECIAL' : 'Foil', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0}]
        
        test_data_decks = [{"ID": 0,"NAME": "Promotional Package 1","SET": "Pride Month","RELEASE_DATE": "06/06/2022","TYPE": "Booster","PRICE":4.99 ,"ACTIVE": True},
                            {"ID": 1,"NAME": "Promotional Package 1","SET": "Pride Month","RELEASE_DATE": "06/06/2022","TYPE": "Starter Set","PRICE":4.99,"ACTIVE": False},
                            {"ID": 2,"NAME": "Promotional Package 1","SET": "Pride Month","RELEASE_DATE": "06/06/2022","TYPE": "Booster","PRICE":4.99,"ACTIVE": True}]
        test_data_connections = []

        result_card_deck_connections = [{"CARD_ID": 0, "DECK_ID": 0}, {"CARD_ID": 0, "DECK_ID": 2},
                                {"CARD_ID": 6, "DECK_ID": 0}, {"CARD_ID": 6, "DECK_ID": 2}]
        
        _result_card_deck_connections = deck.connect_cards_to_decks(test_data_cards, test_data_decks, test_data_connections)

        self.assertEqual(_result_card_deck_connections, result_card_deck_connections)

    
    def test_5_remove_card_deck_connection(self):
        test_data_cards = [{'ID': 0, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'SPECIAL' : 'Normal', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0},
                            {'ID': 6, 'SET_ID': 'P1-002', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Island', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'SPECIAL' : 'Foil', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0}]
        
        test_data_decks = [{"ID": 0,"NAME": "Promotional Package 1","SET": "Pride Month","RELEASE_DATE": "06/06/2022","TYPE": "Booster","PRICE":4.99,"ACTIVE": True}]
        test_data_connections = [{"CARD_ID": 0, "DECK_ID": 0}, {"CARD_ID": 6, "DECK_ID": 0}]

        result_card_deck_connections = []
        
        _result_card_deck_connections = deck.remove_card_deck_connection(test_data_cards, test_data_decks, test_data_connections)

        self.assertEqual(_result_card_deck_connections, result_card_deck_connections)

    
    def test_6_remove_card_deck_connection_extra_connections(self):
        test_data_cards = [{'ID': 0, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'SPECIAL' : 'Normal', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0},
                            {'ID': 6, 'SET_ID': 'P1-002', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Island', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'SPECIAL' : 'Foil', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0}]
        
        test_data_decks = [{"ID": 0,"NAME": "Promotional Package 1","SET": "Pride Month","RELEASE_DATE": "06/06/2022","TYPE": "Booster","PRICE":4.99,"ACTIVE": True}]
        test_data_connections = [{"CARD_ID": 0, "DECK_ID": 0}, {"CARD_ID": 6, "DECK_ID": 0}, {"CARD_ID": 6, "DECK_ID": 4}, {"CARD_ID": 6, "DECK_ID": 3}]

        result_card_deck_connections = [{"CARD_ID": 6, "DECK_ID": 4}, {"CARD_ID": 6, "DECK_ID": 3}]
        
        _result_card_deck_connections = deck.remove_card_deck_connection(test_data_cards, test_data_decks, test_data_connections)

        self.assertEqual(_result_card_deck_connections, result_card_deck_connections)


    def test_7_release_deck(self):
        test_data_deck = {"ID": 0,"NAME": "Promotional Package 1","SET": "Pride Month","RELEASE_DATE": "","TYPE": "Booster","PRICE":4.99, "ACTIVE": False}
        test_data_date = "06/06/2022"
        
        result_deck = {"ID": 0,"NAME": "Promotional Package 1","SET": "Pride Month","RELEASE_DATE": "06/06/2022","TYPE": "Booster","PRICE":4.99, "ACTIVE": True}
        
        _result_deck = deck.release_deck(test_data_deck, test_data_date)

        self.assertEqual(_result_deck, result_deck)
    
if __name__ == '__main__':
    unittest.main()