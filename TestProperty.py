#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
from product.information import property as pr2

class TestProperty(unittest.TestCase): # test class
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    def setUp(self):
        print("setUp")
        
    def test_property1(self): # test case 
        self.assertIsNone(pr2.property('water','2020-08-08','2019-08-08'))
        self.assertIsNone(pr2.property('alcohol','2020-02-02','2019-02-02')) 
        self.assertIsNone(pr2.property('beeswax','2020-09-09','2019-09-09'))
        self.assertIsNone(pr2.property('olive oil','2020-07-07','2019-07-07'))
        self.assertIsNone(pr2.property('cocoa butter','2020-03-03','2019-03-03'))

    def test_property2(self): # test case 
        self.assertNotIsInstance(pr2.property('water','2020-08-08','2019-08-08'),str)
        self.assertNotIsInstance(pr2.property('alcohol','2020-02-02','2019-02-02'),str) 
        self.assertNotIsInstance(pr2.property('beeswax','2020-09-09','2019-09-09'),str)
        self.assertNotIsInstance(pr2.property('olive oil','2020-07-07','2019-07-07'),str)
        self.assertNotIsInstance(pr2.property('cocoa butter','2020-03-03','2019-03-03'),str)
        
    def tearDown(self):
        print("tearDown")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

