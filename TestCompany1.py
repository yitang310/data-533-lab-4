#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
from product.company.brand_company import *
class TestCompany1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
    def setUp(self):
        print("setUp")
        self.c1 = company("LOreal")
        self.b1 = brand("Lancome")
    def test_company(self):
        self.c1.set_companyname("LOréal") 
        self.c1.set_companyname("L'Oréal")  
        self.c1.set_companyyear(1909) 
        self.c1.set_headquarter("Clichy, France")
        
        self.assertNotEqual(self.c1.companyname,"LOréal")
        self.assertEqual(self.c1.companyname,"L'Oréal")
        self.assertEqual(self.c1.companyyear,1909)
        self.assertEqual(self.c1.headquarter,"Clichy, France")
        self.assertIsNone(self.c1.display())
        
    def test_brand(self):
        self.b1.set_brandname("Lancôme") 
        self.b1.set_brandyear(1935)  
        self.b1.set_brandcountry("France") 
        self.b1.set_belongyear(1964) 
        self.b1.set_companyname("L'Oréal")  
        self.b1.set_companyyear(1909) 
        self.b1.set_headquarter("Clichy, France")
        
        self.assertEqual(self.b1.brandname,"Lancôme") 
        self.assertEqual(self.b1.brandyear,1935)  
        self.assertEqual(self.b1.brandcountry,"France") 
        self.assertEqual(self.b1.belongyear,1964)
        self.assertIsNone(self.b1.display())
        
    def tearDown(self):
        print("tearDown")
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")


# In[ ]:




