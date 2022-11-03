#!/usr/bin/env python3
# Author: Pekka Marjamäki - Suolenkainen
# https://github.com/suolenkainen/market


import unittest
import transactions


class TransactionTests(unittest.TestCase):

    # Testing combination of purchase and sell

    def test_01_combine_purchase_and_sell_orders(self):
        test_purchase_dict = [{'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 10.0, "active": True}]
        test_sales_dict = [{'id': 0, 'idproduct': 0, 'idseller': 0, 'amount': 1, 'priceone': 10.0, "active": True}]
        
        result_matches = [[0,0]]
        result_purchase_dict = [{'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 10.0, "active": False}]
        result_sales_dict = [{'id': 0, 'idproduct': 0, 'idseller': 0, 'amount': 1, 'priceone': 10.0, "active": False}]

        _result_matches, _result_purchase_dict, _result_sales_dict = transactions.combine_purchase_and_sell_orders(test_purchase_dict, test_sales_dict)
        
        self.assertEqual(_result_matches, result_matches)
        self.assertEqual(_result_purchase_dict, result_purchase_dict)
        self.assertEqual(_result_sales_dict, result_sales_dict)


    def test_02_combine_purchase_and_sell_orders_double_data(self):
        test_purchase_dict = [{'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 10.0, "active": True}, 
                               {'id': 1, 'idproduct': 2, 'idpurchaser': 0, 'amount': 1, 'priceone': 10.0, "active": True}]
        test_sales_dict = [{'id': 0, 'idproduct': 0, 'idseller': 0, 'amount': 1, 'priceone': 10.0, "active": True}, 
                            {'id': 1, 'idproduct': 2, 'idseller': 0, 'amount': 1, 'priceone': 10.0, "active": True}]
        
        result_matches = [[0,0], [1,1]]
        result_purchase_dict = [{'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 10.0, "active": False}, 
                               {'id': 1, 'idproduct': 2, 'idpurchaser': 0, 'amount': 1, 'priceone': 10.0, "active": False}]
        result_sales_dict = [{'id': 0, 'idproduct': 0, 'idseller': 0, 'amount': 1, 'priceone': 10.0, "active": False}, 
                            {'id': 1, 'idproduct': 2, 'idseller': 0, 'amount': 1, 'priceone': 10.0, "active": False}]

        _result_matches, _result_purchase_dict, _result_sales_dict = transactions.combine_purchase_and_sell_orders(test_purchase_dict, test_sales_dict)
        
        self.assertEqual(_result_matches, result_matches)
        self.assertEqual(_result_purchase_dict, result_purchase_dict)
        self.assertEqual(_result_sales_dict, result_sales_dict)


    def test_03_orders_price_differs(self):
        test_purchase_dict = [{'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 10.0, "active": True}]
        test_sales_dict = [{'id': 0, 'idproduct': 0, 'idseller': 0, 'amount': 1, 'priceone': 11.0, "active": True}]

        result_matches = [[0,0]]
        result_purchase_dict =  [{'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 11.0, "active": False}]
        result_sales_dict = [{'id': 0, 'idproduct': 0, 'idseller': 0, 'amount': 1, 'priceone': 11.0, "active": False}]

        _result_matches, _result_purchase_dict, _result_sales_dict = transactions.combine_purchase_and_sell_orders(test_purchase_dict, test_sales_dict)
        
        self.assertEqual(_result_matches, result_matches)
        self.assertEqual(_result_purchase_dict, result_purchase_dict)
        self.assertEqual(_result_sales_dict, result_sales_dict)


    def test_04_orders_price_differs_by_much(self):
        test_purchase_dict = [{'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 10.0, "active": True}]
        test_sales_dict = [{'id': 0, 'idproduct': 0, 'idseller': 0, 'amount': 1, 'priceone': 13.0, "active": True}]
        
        result_matches = []
        result_purchase_dict =  [{'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 10.0, "active": True}]
        result_sales_dict = [{'id': 0, 'idproduct': 0, 'idseller': 0, 'amount': 1, 'priceone': 13.0, "active": True}]

        _result_matches, _result_purchase_dict, _result_sales_dict = transactions.combine_purchase_and_sell_orders(test_purchase_dict, test_sales_dict)
        
        self.assertEqual(_result_matches, result_matches)
        self.assertEqual(_result_purchase_dict, result_purchase_dict)
        self.assertEqual(_result_sales_dict, result_sales_dict)


    def test_05_order_amounts_differ(self):
        test_purchase_dict = [{'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 2, 'priceone': 10.0, "active": True}]
        test_sales_dict = [{'id': 0, 'idproduct': 0, 'idseller': 0, 'amount': 1, 'priceone': 10.0, "active": True}]

        result_matches = [[0,0]]
        result_purchase_dict =  [{'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 10.0, "active": False}, 
                                {'id': 1, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 10.0, "active": True}]
        result_sales_dict = [{'id': 0, 'idproduct': 0, 'idseller': 0, 'amount': 1, 'priceone': 10.0, "active": False}]

        _result_matches, _result_purchase_dict, _result_sales_dict = transactions.combine_purchase_and_sell_orders(test_purchase_dict, test_sales_dict)
        
        self.assertEqual(_result_matches, result_matches)
        self.assertEqual(_result_purchase_dict, result_purchase_dict)
        self.assertEqual(_result_sales_dict, result_sales_dict)


    def test_06_check_prices_equal(self):
        test_purchase = {'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 10.0, "active": True}
        test_sales = {'id': 0, 'idproduct': 0, 'idseller': 0, 'amount': 1, 'priceone': 10.0, "active": True}

        result_purchase =  {'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 10.0, "active": True}
        result_sales = {'id': 0, 'idproduct': 0, 'idseller': 0, 'amount': 1, 'priceone': 10.0, "active": True}

        _match, _result_purchase, _result_sales = transactions.check_prices(test_purchase, test_sales)
        
        self.assertEqual(_match, True)
        self.assertEqual(_result_purchase, result_purchase)
        self.assertEqual(_result_sales, result_sales)


    def test_07_check_prices_in_margin(self):
        test_purchase = {'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 10.0, "active": True}
        test_sales = {'id': 0, 'idproduct': 0, 'idseller': 0, 'amount': 1, 'priceone': 11.0, "active": True}

        result_purchase =  {'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 11.0, "active": True}
        result_sales = {'id': 0, 'idproduct': 0, 'idseller': 0, 'amount': 1, 'priceone': 11.0, "active": True}

        _match, _result_purchase, _result_sales = transactions.check_prices(test_purchase, test_sales)
        
        self.assertEqual(_match, True)
        self.assertEqual(_result_purchase, result_purchase)
        self.assertEqual(_result_sales, result_sales)


    def test_08_check_prices_asking_prices_over_margin(self):
        test_purchase = {'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 13.0, "active": True}
        test_sales = {'id': 0, 'idproduct': 0, 'idseller': 0, 'amount': 1, 'priceone': 10.0, "active": True}

        result_purchase =  {'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 13.0, "active": True}
        result_sales = {'id': 0, 'idproduct': 0, 'idseller': 0, 'amount': 1, 'priceone': 10.0, "active": True}

        _match, _result_purchase, _result_sales = transactions.check_prices(test_purchase, test_sales)
        
        self.assertEqual(_match, False)
        self.assertEqual(_result_purchase, result_purchase)
        self.assertEqual(_result_sales, result_sales)


    def test_09_generate_additional_transactions_new_purchase(self):
        test_purchase = {'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 3, 'priceone': 10.0, "active": True}
        test_sales = {'id': 0, 'idproduct': 0, 'idseller': 0, 'amount': 1, 'priceone': 10.0, "active": True}

        result_purchase =  {'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 10.0, "active": False}
        result_sales = {'id': 0, 'idproduct': 0, 'idseller': 0, 'amount': 1, 'priceone': 10.0, "active": False}
        _result_new_purchase = {'id': 1, 'idproduct': 0, 'idseller': 0, 'amount': 2, 'priceone': 10.0, "active": True}

        _result_purchase, _result_new_purchase, _result_sales, _result_new_sales = transactions.generate_additional_transactions(test_purchase, test_sales, 1, 1)
        
        self.assertEqual(_result_purchase, result_purchase)
        self.assertEqual(_result_new_purchase, _result_new_purchase)
        self.assertEqual(_result_sales, result_sales)
        self.assertEqual(_result_new_sales, {})

    
    def test_10_generate_additional_transactions_new_sales(self):
        test_purchase = {'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 10.0, "active": True}
        test_sales = {'id': 0, 'idproduct': 0, 'idseller': 0, 'amount': 4, 'priceone': 10.0, "active": True}

        result_purchase =  {'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 10.0, "active": False}
        result_sales = {'id': 0, 'idproduct': 0, 'idseller': 0, 'amount': 1, 'priceone': 10.0, "active": False}
        _result_new_sales = {'id': 1, 'idproduct': 0, 'idseller': 0, 'amount': 3, 'priceone': 10.0, "active": True}

        _result_purchase, _result_new_purchase, _result_sales, _result_new_sales = transactions.generate_additional_transactions(test_purchase, test_sales, 1, 1)
        
        self.assertEqual(_result_purchase, result_purchase)
        self.assertEqual(_result_new_purchase, {})
        self.assertEqual(_result_sales, result_sales)
        self.assertEqual(_result_new_sales, _result_new_sales)


    def test_11_crete_list_of_orders(self):
        test_purchase_orders = [{'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 10.0, "active": False}]
        test_sales_orders = [{'id': 0, 'idproduct': 0, 'idseller': 0, 'amount': 1, 'priceone': 10.0, "active": False}]
        test_matches = [[0,0]]

        result_producer_transactions =  [{'idproducer': 0, 'idproduct': 0, 'price': 10}]
        result_people_transactions = [{'idperson': 0, 'idproduct': 0, 'amount': 1, 'price': 10}]

        _result_producer_transactions, _result_people_transactions = transactions.crete_list_of_orders(test_matches, test_purchase_orders, test_sales_orders)
        
        self.assertEqual(_result_producer_transactions, result_producer_transactions)
        self.assertEqual(_result_people_transactions, result_people_transactions)


    def test_12_crete_list_of_orders_unmatched_orders(self):
        test_purchase_orders = [{'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 10.0, "active": False}, 
                                {'id': 1, 'idproduct': 1, 'idpurchaser': 0, 'amount': 1, 'priceone': 10.0, "active": True}]
        test_sales_orders = [{'id': 0, 'idproduct': 0, 'idseller': 0, 'amount': 1, 'priceone': 10.0, "active": False}]
        test_matches = [[0,0]]

        result_producer_transactions =  [{'idproducer': 0, 'idproduct': 0, 'price': 10}]
        result_people_transactions = [{'idperson': 0, 'idproduct': 0, 'amount': 1, 'price': 10}]

        _result_producer_transactions, _result_people_transactions = transactions.crete_list_of_orders(test_matches, test_purchase_orders, test_sales_orders)
        
        self.assertEqual(_result_producer_transactions, result_producer_transactions)
        self.assertEqual(_result_people_transactions, result_people_transactions)


    def test_13_crete_list_of_orders_no_matches(self):
        test_purchase_orders = [{'id': 0, 'idproduct': 0, 'idpurchaser': 0, 'amount': 1, 'priceone': 10.0, "active": False}, 
                                {'id': 1, 'idproduct': 1, 'idpurchaser': 0, 'amount': 1, 'priceone': 10.0, "active": True}]
        test_sales_orders = [{'id': 0, 'idproduct': 0, 'idseller': 0, 'amount': 1, 'priceone': 10.0, "active": False}]
        test_matches = []

        result_producer_transactions =  []
        result_people_transactions = []

        _result_producer_transactions, _result_people_transactions = transactions.crete_list_of_orders(test_matches, test_purchase_orders, test_sales_orders)
        
        self.assertEqual(_result_producer_transactions, result_producer_transactions)
        self.assertEqual(_result_people_transactions, result_people_transactions)


if __name__ == '__main__':
    unittest.main()