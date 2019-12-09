#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
from product.information import price as pr

class TestPrice(unittest.TestCase): # test class
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    def setUp(self):
        print("setUp")
        
    def test_price1(self): # test case 
        self.assertEqual(pr.tax_price(1,'BC'), 1.12) 
        self.assertEqual(pr.tax_price(1,'AB'), 1.05) 
        self.assertEqual(pr.tax_price(1,'ON'), 1.13)
        self.assertEqual(pr.tax_price(1,'NB'), 1.15)
        self.assertEqual(pr.tax_price(1,'MB'), 1.13)
        self.assertEqual(pr.tax_price(1,'NL'), 1.15)
        self.assertEqual(pr.tax_price(1,'SK'), 1.11)

    def test_price2(self): # test case 
        self.assertNotEqual(pr.tax_price(1,'NS'), 1.17) 
        self.assertNotEqual(pr.tax_price(1,'NT'), 1.08) 
        self.assertNotEqual(pr.tax_price(1,'NU'), 1.12)
        self.assertNotEqual(pr.tax_price(1,'PE'), 1.14)
        self.assertNotEqual(pr.tax_price(1,'QC'), 1.15)
        self.assertNotEqual(pr.tax_price(1,'YT'), 1.13)
        
    def tearDown(self):
        print("tearDown")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

