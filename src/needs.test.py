#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market


import unittest
import needs


class NeedsTests(unittest.TestCase):

    # Testing consuming resources

    def test_01_people_consume_products(self):
        test_people_products = [{'idperson': 0, 'idproduct': 0, 'amount': 2.0}]
        test_needs = [{"idperson": 0, "idproduct": 0, "needs": 1.0, "price": 1.0, "idpriority": 0}]
        
        result_people_products = [{'idperson': 0, 'idproduct': 0, 'amount': 1.0}]
        result_needs = [{"idperson": 0, "idproduct": 0, "needs": 1.0, "price": 1.0, "idpriority": 0}]

        _result_people_products, _result_needs = needs.people_consume_products_and_generate_needs(test_people_products, test_needs)
        
        self.assertEqual(_result_people_products, result_people_products)
        self.assertEqual(_result_needs, result_needs)


    def test_02_people_consume_products_no_need(self):
        test_people_products = [{'idperson': 0, 'idproduct': 0, 'amount': 2.0}]
        test_needs = []
        
        result_people_products = [{'idperson': 0, 'idproduct': 0, 'amount': 2.0}]
        result_needs = []

        _result_people_products, _result_needs = needs.people_consume_products_and_generate_needs(test_people_products, test_needs)
        
        self.assertEqual(_result_people_products, result_people_products)
        self.assertEqual(_result_needs, result_needs)


    def test_03_people_consume_products_too_big_need(self):
        test_people_products = [{'idperson': 0, 'idproduct': 0, 'amount': 2.0}]
        test_needs = [{"idperson": 0, "idproduct": 0, "needs": 3.0, "price": 1.0, "idpriority": 0}]
        
        result_people_products = []
        result_needs = [{"idperson": 0, "idproduct": 0, "needs": 6.0, "price": 1.0, "idpriority": 1}]

        _result_people_products, _result_needs = needs.people_consume_products_and_generate_needs(test_people_products, test_needs)
        
        self.assertEqual(_result_people_products, result_people_products)
        self.assertEqual(_result_needs, result_needs)


    def test_04_people_consume_products_priority1_fulfilled(self):
        test_people_products = [{'idperson': 0, 'idproduct': 0, 'amount': 7.0}]
        test_needs = [{"idperson": 0, "idproduct": 0, "needs": 4.0, "price": 1.0, "idpriority": 1}]
        
        result_people_products = [{'idperson': 0, 'idproduct': 0, 'amount': 3.0}]
        result_needs = [{"idperson": 0, "idproduct": 0, "needs": 2.0, "price": 1.0, "idpriority": 0}]

        _result_people_products, _result_needs = needs.people_consume_products_and_generate_needs(test_people_products, test_needs)
        
        self.assertEqual(_result_people_products, result_people_products)
        self.assertEqual(_result_needs, result_needs)


    def test_05_people_consume_products_increase_priority(self):
        test_people_products = []
        test_needs = [{"idperson": 0, "idproduct": 0, "needs": 4.0, "price": 1.0, "idpriority": 1}]
        
        result_people_products = []
        result_needs = [{"idperson": 0, "idproduct": 0, "needs": 8.0, "price": 1.0, "idpriority": 2}]

        try:
            _result_people_products, _result_needs = needs.people_consume_products_and_generate_needs(test_people_products, test_needs)
        except ValueError:
            pass


    def test_06_people_consume_products_priority2_fulfilled(self):
            test_people_products = [{'idperson': 0, 'idproduct': 0, 'amount': 10.0}]
            test_needs = [{"idperson": 0, "idproduct": 0, "needs": 8.0, "price": 1.0, "idpriority": 2}]
            
            result_people_products = [{'idperson': 0, 'idproduct': 0, 'amount': 2.0}]
            result_needs = [{"idperson": 0, "idproduct": 0, "needs": 2.0, "price": 1.0, "idpriority": 0}]

            _result_people_products, _result_needs = needs.people_consume_products_and_generate_needs(test_people_products, test_needs)
            
            self.assertEqual(_result_people_products, result_people_products)
            self.assertEqual(_result_needs, result_needs)


    def test_07_deactivate_person(self):
            test_people = [{'id': 0, 'name': 'Alpha', 'wealth': 0.0, "active": True}]
            test_needs = [{"idperson": 0, "idproduct": 0, "needs": 8.0, "price": 1.0, "idpriority": 3}]
            
            result_persons = [{'id': 0, 'name': 'Alpha', 'wealth': 0.0, "active": False}]
            result_needs = []

            _result_persons, _result_needs = needs.deactivate_person(test_people, test_needs)
            
            self.assertEqual(_result_persons, result_persons)
            self.assertEqual(_result_needs, result_needs)


    def test_08_deactivate_person_multiple_persons(self):
            test_people = [{'id': 0, 'name': 'Alpha', 'wealth': 7.0, "active": True}, 
                            {'id': 1, 'name': 'Alpha', 'wealth': 7.0, "active": True}]
            test_needs = [{"idperson": 0, "idproduct": 0, "needs": 8.0, "price": 1.0, "idpriority": 3}]
            
            result_persons = [{'id': 0, 'name': 'Alpha', 'wealth': 7.0, "active": False}, 
                                {'id': 1, 'name': 'Alpha', 'wealth': 7.0, "active": True}]
            result_needs = []

            _result_persons, _result_needs = needs.deactivate_person(test_people, test_needs)
            
            self.assertEqual(_result_persons, result_persons)
            self.assertEqual(_result_needs, result_needs)


    def test_09_deactivate_person_multiple_both(self):
            test_people = [{'id': 0, 'name': 'Alpha', 'wealth': 7.0, "active": True}, 
                            {'id': 1, 'name': 'Alpha', 'wealth': 7.0, "active": True}]
            test_needs = [{"idperson": 0, "idproduct": 0, "needs": 8.0, "price": 1.0, "idpriority": 3}, 
                            {"idperson": 0, "idproduct": 0, "needs": 8.0, "price": 1.0, "idpriority": 1}, 
                            {"idperson": 1, "idproduct": 0, "needs": 8.0, "price": 1.0, "idpriority": 2}]
            
            result_persons = [{'id': 0, 'name': 'Alpha', 'wealth': 7.0, "active": False}, {'id': 1, 'name': 'Alpha', 'wealth': 7.0, "active": True}]
            result_needs = [{"idperson": 1, "idproduct": 0, "needs": 8.0, "price": 1.0, "idpriority": 2}]

            _result_persons, _result_needs = needs.deactivate_person(test_people, test_needs)
            
            self.assertEqual(_result_persons, result_persons)
            self.assertEqual(_result_needs, result_needs)


    def test_10_adjust_need_prices(self):
            test_needs = [{"idperson": 0, "idproduct": 0, "needs": 8.0, "price": 1.0, "idpriority": 3}]
            test_orders = [{'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 10, "active": True}]
            
            result_needs = [{"idperson": 0, "idproduct": 0, "needs": 8.0, "price": 1.0, "idpriority": 3}]
            result_orders = [{'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 10, "active": True}]

            _result_needs, _result_orders = needs.adjust_need_prices(test_needs, test_orders)
            
            self.assertEqual(_result_needs, result_needs)
            self.assertEqual(_result_orders, result_orders)


    def test_10_adjust_need_prices(self):
            test_needs = [{"idperson": 0, "idproduct": 0, "needs": 8.0, "price": 10.0, "idpriority": 0}]
            test_purchase_orders = [{'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 11.0, "active": False}]
            
            result_needs = [{"idperson": 0, "idproduct": 0, "needs": 8.0, "price": 10.7, "idpriority": 0}]

            _result_needs = needs.adjust_need_prices(test_needs, test_purchase_orders)
            
            self.assertEqual(_result_needs, result_needs)


    def test_11_adjust_need_prices_no_successfull_purchases(self):
            test_needs = [{"idperson": 0, "idproduct": 0, "needs": 8.0, "price": 10.0, "idpriority": 0}]
            test_purchase_orders = [{'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 11.0, "active": True}]
            
            result_needs = [{"idperson": 0, "idproduct": 0, "needs": 8.0, "price": 10.5, "idpriority": 0}]

            _result_needs = needs.adjust_need_prices(test_needs, test_purchase_orders)
            
            self.assertEqual(_result_needs, result_needs)


    def test_12_adjust_need_prices_higher_priority(self):
            test_needs = [{"idperson": 0, "idproduct": 0, "needs": 8.0, "price": 10.0, "idpriority": 2}]
            test_purchase_orders = [{'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 11.0, "active": True}]
            
            result_needs = [{"idperson": 0, "idproduct": 0, "needs": 8.0, "price": 12.0, "idpriority": 2}]

            _result_needs = needs.adjust_need_prices(test_needs, test_purchase_orders)
            
            self.assertEqual(_result_needs, result_needs)


    def test_13_adjust_need_prices_multiple_each(self):
            test_needs = [{"idperson": 0, "idproduct": 0, "needs": 2.0, "price": 5.0, "idpriority": 0}, 
                            {"idperson": 0, "idproduct": 1, "needs": 2.0, "price": 5.0, "idpriority": 0}, 
                            {"idperson": 1, "idproduct": 1, "needs": 2.0, "price": 10.0, "idpriority": 0}, 
                            {"idperson": 2, "idproduct": 0, "needs": 8.0, "price": 15.0, "idpriority": 2}]
            test_purchase_orders = [{'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 6.0, "active": False},
                                    {'id': 1, 'idproduct': 1, 'idpurchaser': 0, 'amount': 1, 'priceone': 5.0, "active": True},
                                    {'id': 2, 'idproduct': 0, 'idpurchaser': 1, 'amount': 1, 'priceone': 10.0, "active": False},
                                    {'id': 3, 'idproduct': 1, 'idpurchaser': 1, 'amount': 1, 'priceone': 11.0, "active": True}]
            
            result_needs = [{"idperson": 0, "idproduct": 0, "needs": 2.0, "price": 5.8, "idpriority": 0}, 
                            {"idperson": 0, "idproduct": 1, "needs": 2.0, "price": 5.2, "idpriority": 0}, 
                            {"idperson": 1, "idproduct": 1, "needs": 2.0, "price": 10.5, "idpriority": 0}, 
                            {"idperson": 2, "idproduct": 0, "needs": 8.0, "price": 18.0, "idpriority": 2}]

            _result_needs = needs.adjust_need_prices(test_needs, test_purchase_orders)
            
            self.assertEqual(_result_needs, result_needs)


if __name__ == '__main__':
    unittest.main()