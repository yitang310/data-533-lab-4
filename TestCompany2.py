#!/usr/bin/env python
# coding: utf-8

# In[68]:


import unittest
from product.company.value_profit import *
class TestCompany2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
    def setUp(self):
        print("setUp")
        
    def teststr(self):
        self.assertIsInstance(value_percentage(1000,10000),str)
        self.assertIsInstance(sales_percentage(200,10000),str)
        self.assertIsInstance(tendency(500,600),str)
        self.assertIs(type(float(value_percentage(1000,10000).strip("%"))),float)
        self.assertIsNot(type(float(sales_percentage(1000,10000).strip("%"))),int)
        
    def testnumber(self):
        self.assertTrue(float(value_percentage(1000,10000).strip("%"))==1000/10000*100)
        self.assertTrue(float(sales_percentage(1000,10000).strip("%"))==1000/10000*100)
        self.assertTrue(float(tendency(500,600).strip("%"))==500/600*100)
        self.assertFalse(float(value_percentage(1234,10000).strip("%"))==1000/10000*100)
        self.assertFalse(float(sales_percentage(1234,10000).strip("%"))==1000/10000*100)
    
    def tearDown(self):
        print("tearDown")
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

