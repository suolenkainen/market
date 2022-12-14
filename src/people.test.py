#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market


import unittest
import people


class PeopleTests(unittest.TestCase):

    # Testing combination of purchase and sell

    def test_01_adjust_person_wealth(self):
        test_people = [{'id': 0, 'name': 'Alpha', 'wealth': 10.0, "active": True}]
        test_people_transactions = [{'idperson': 0, 'idproduct': 0, 'amount': 1, 'price': 5.0}]
        
        result_people = [{'id': 0, 'name': 'Alpha', 'wealth': 5.0, "active": True}]

        _result_people = people.adjust_person_wealth(test_people, test_people_transactions)
        
        self.assertEqual(_result_people, result_people)


    def test_02_adjust_person_wealth_multiple_purchases(self):
        test_people = [{'id': 0, 'name': 'Alpha', 'wealth': 10.0, "active": True}]
        test_people_transactions = [{'idperson': 0, 'idproduct': 0, 'amount': 1, 'price': 2.0}, 
                        {'idperson': 0, 'idproduct': 2, 'amount': 3, 'price': 2.0}]
        
        result_people = [{'id': 0, 'name': 'Alpha', 'wealth': 2.0, "active": True}]

        _result_people = people.adjust_person_wealth(test_people, test_people_transactions)
        
        self.assertEqual(_result_people, result_people)


    def test_03_adjust_person_wealth_bankrupt(self):
        test_people = [{'id': 0, 'name': 'Alpha', 'wealth': 7.0, "active": True}]
        test_people_transactions = [{'idperson': 0, 'idproduct': 0, 'amount': 1, 'price': 2.0}, 
                        {'idperson': 0, 'idproduct': 2, 'amount': 3, 'price': 2.0}]
        
        result_people = [{'id': 0, 'name': 'Alpha', 'wealth': 0.0, "active": False}]

        _result_people = people.adjust_person_wealth(test_people, test_people_transactions)
        
        self.assertEqual(_result_people, result_people)


    def test_04_adjust_person_wealth_no_purchase(self):
        test_people = [{'id': 0, 'name': 'Alpha', 'wealth': 10.0, "active": True}]
        test_people_transactions = []
        
        result_people = [{'id': 0, 'name': 'Alpha', 'wealth': 10.0, "active": True}]

        _result_people = people.adjust_person_wealth(test_people, test_people_transactions)
        
        self.assertEqual(_result_people, result_people)


    def test_05_add_products_to_people(self):
        test_people_product = [{'idperson': 0, 'idproduct': 0, 'amount': 1.0}]
        test_people_transactions = [{'idperson': 0, 'idproduct': 0, 'amount': 1.0, 'price': 5.0}]
        
        result_people_product = [{'idperson': 0, 'idproduct': 0, 'amount': 2.0}]

        _result_people_product = people.add_products_to_people(test_people_product, test_people_transactions)
        
        self.assertEqual(_result_people_product, result_people_product)


    def test_06_add_products_to_people_no_orders(self):
        test_people_product = [{'idperson': 0, 'idproduct': 0, 'amount': 2.0}]
        test_people_transactions = []
        
        result_people_product = [{'idperson': 0, 'idproduct': 0, 'amount': 2.0}]

        _result_people_product = people.add_products_to_people(test_people_product, test_people_transactions)
        
        self.assertEqual(_result_people_product, result_people_product)


    def test_07_add_products_to_people_new_order(self):
        test_people_product = [{'idperson': 0, 'idproduct': 0, 'amount': 2.0}]
        test_people_transactions = [{'idperson': 0, 'idproduct': 1, 'amount': 1.0, 'price': 5.0}]
        
        result_people_product = [{'idperson': 0, 'idproduct': 0, 'amount': 2.0}, 
                                {'idperson': 0, 'idproduct': 1, 'amount': 1.0}]

        _result_people_product = people.add_products_to_people(test_people_product, test_people_transactions)
        
        self.assertEqual(_result_people_product, result_people_product)


    def test_08_add_products_to_people_two_orders(self):
        test_people_product = [{'idperson': 0, 'idproduct': 0, 'amount': 2.0}]
        test_people_transactions = [{'idperson': 0, 'idproduct': 0, 'amount': 1.0, 'price': 5.0}, 
                        {'idperson': 0, 'idproduct': 1, 'amount': 1.0, 'price': 5.0}]
        
        result_people_product = [{'idperson': 0, 'idproduct': 0, 'amount': 3.0}, 
                                {'idperson': 0, 'idproduct': 1, 'amount': 1.0}]

        _result_people_product = people.add_products_to_people(test_people_product, test_people_transactions)
        
        self.assertEqual(_result_people_product, result_people_product)


    def test_09_add_products_to_people_two_people_two_orders(self):
        test_people_product = [{'idperson': 0, 'idproduct': 0, 'amount': 2.0}, 
                                {'idperson': 1, 'idproduct': 2, 'amount': 2.0}]
        test_people_transactions = [{'idperson': 0, 'idproduct': 0, 'amount': 1.0, 'price': 5.0}, 
                        {'idperson': 1, 'idproduct': 2, 'amount': 1.0, 'price': 5.0}]
        
        result_people_product = [{'idperson': 0, 'idproduct': 0, 'amount': 3.0}, 
                                {'idperson': 1, 'idproduct': 2, 'amount': 3.0}]

        _result_people_product = people.add_products_to_people(test_people_product, test_people_transactions)
        
        self.assertEqual(_result_people_product, result_people_product)


    def test_10_add_products_to_people_two_people_one_new_order(self):
        test_people_product = [{'idperson': 0, 'idproduct': 0, 'amount': 2.0}, 
                                {'idperson': 1, 'idproduct': 2, 'amount': 2.0}]
        test_people_transactions = [{'idperson': 0, 'idproduct': 2, 'amount': 1.0, 'price': 5.0}]
        
        result_people_product = [{'idperson': 0, 'idproduct': 0, 'amount': 2.0}, 
                                {'idperson': 1, 'idproduct': 2, 'amount': 2.0}, 
                                {'idperson': 0, 'idproduct': 2, 'amount': 1.0}]

        _result_people_product = people.add_products_to_people(test_people_product, test_people_transactions)
        
        self.assertEqual(_result_people_product, result_people_product)



    def test_11_connect_card_to_person_add_new_to_empty(self):
        test_data_card = {'ID': 0, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'SPECIAL' : 'Normal', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0}
        test_data_person = {'ID': 0, 'NAME': 'Forest Gump', 'WEALTH': 500, 'INCREASE_MONTHLY': 0, 'GAME_ABILITY': 'Normal'}
        test_data_card_person = []
        test_data_transfer_data = {'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2}

        result_card_person = [{'CARD_ID': 0, 'PERSON_ID': 0, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2}]
        
        _result_card_person = people.connect_card_to_person(test_data_card, test_data_person, test_data_card_person, test_data_transfer_data)

        self.assertEqual(_result_card_person, result_card_person)


    def test_12_connect_card_to_person_add_new_to_list(self):
        test_data_card = {'ID': 0, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'SPECIAL' : 'Normal', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0}
        test_data_person = {'ID': 0, 'NAME': 'Forest Gump', 'WEALTH': 500, 'INCREASE_MONTHLY': 0, 'GAME_ABILITY': 'Normal'}
        test_data_card_person = [{'CARD_ID': 7, 'PERSON_ID': 3, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2}]
        test_data_transfer_data = {'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2}

        result_card_person = [{'CARD_ID': 7, 'PERSON_ID': 3, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2}, {'CARD_ID': 0, 'PERSON_ID': 0, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2}]
        
        _result_card_person = people.connect_card_to_person(test_data_card, test_data_person, test_data_card_person, test_data_transfer_data)

        self.assertEqual(_result_card_person, result_card_person)


    def test_13_connect_card_to_person_duplicate(self):
        test_data_card = {'ID': 0, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'SPECIAL' : 'Normal', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0}
        test_data_person = {'ID': 0, 'NAME': 'Forest Gump', 'WEALTH': 500, 'INCREASE_MONTHLY': 0, 'GAME_ABILITY': 'Normal'}
        test_data_card_person = [{'CARD_ID': 0, 'PERSON_ID': 0, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2}]
        test_data_transfer_data = {'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2}

        result_card_person = [{'CARD_ID': 0, 'PERSON_ID': 0, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2}]
        
        _result_card_person = people.connect_card_to_person(test_data_card, test_data_person, test_data_card_person, test_data_transfer_data)

        self.assertEqual(_result_card_person, result_card_person)


    def test_14_connect_card_to_person_update_existing(self):
        test_data_card = {'ID': 0, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'SPECIAL' : 'Normal', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0}
        test_data_person = {'ID': 0, 'NAME': 'Forest Gump', 'WEALTH': 500, 'INCREASE_MONTHLY': 0, 'GAME_ABILITY': 'Normal'}
        test_data_card_person = [{'CARD_ID': 0, 'PERSON_ID': 4, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2}]
        test_data_transfer_data = {'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2}

        result_card_person = [{'CARD_ID': 0, 'PERSON_ID': 0, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2}]
        
        _result_card_person = people.connect_card_to_person(test_data_card, test_data_person, test_data_card_person, test_data_transfer_data)

        self.assertEqual(_result_card_person, result_card_person)


    def test_15_connect_card_to_person_update_existing_mass(self):
        test_data_card = {'ID': 0, 'SET_ID': 'P1-001', 'SET': 'Promo pack 1: Pride Month', 'COLOUR': 'Green', 'NAME': 'Forest', 'TYPE': 'Mana', 'ATTRIBUTE': 'Mana source', 'RARITY': 'Common', 'SPECIAL' : 'Normal', 'ARTIST': 'Corym Baghig', 'DESCRIPTION': 0}
        test_data_person = {'ID': 0, 'NAME': 'Forest Gump', 'WEALTH': 500, 'INCREASE_MONTHLY': 0, 'GAME_ABILITY': 'Normal'}
        test_data_card_person = [{'CARD_ID': 2, 'PERSON_ID': 4, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2},
                                {'CARD_ID': 1, 'PERSON_ID': 4, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2},
                                {'CARD_ID': 4, 'PERSON_ID': 4, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2},
                                {'CARD_ID': 3, 'PERSON_ID': 4, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2},
                                {'CARD_ID': 5, 'PERSON_ID': 4, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2},
                                {'CARD_ID': 6, 'PERSON_ID': 4, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2},
                                {'CARD_ID': 7, 'PERSON_ID': 4, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2},
                                {'CARD_ID': 8, 'PERSON_ID': 4, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2},
                                {'CARD_ID': 0, 'PERSON_ID': 4, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2}]
        test_data_transfer_data = {'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2}

        result_card_person = [{'CARD_ID': 2, 'PERSON_ID': 4, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2}, 
                            {'CARD_ID': 1, 'PERSON_ID': 4, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2},
                            {'CARD_ID': 4, 'PERSON_ID': 4, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2},
                            {'CARD_ID': 3, 'PERSON_ID': 4, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2},
                            {'CARD_ID': 5, 'PERSON_ID': 4, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2},
                            {'CARD_ID': 6, 'PERSON_ID': 4, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2},
                            {'CARD_ID': 7, 'PERSON_ID': 4, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2},
                            {'CARD_ID': 8, 'PERSON_ID': 4, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2},
                            {'CARD_ID': 0, 'PERSON_ID': 0, 'DATE': '01/01/2000', 'DESIRABILITY': 0, 'PRICE': 0, 'PREVIOUS_OWNER': 2}]
        
        _result_card_person = people.connect_card_to_person(test_data_card, test_data_person, test_data_card_person, test_data_transfer_data)

        self.assertEqual(_result_card_person, result_card_person)


if __name__ == '__main__':
    unittest.main()