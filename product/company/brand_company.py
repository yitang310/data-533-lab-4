#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class company:
    def __init__(self,companyname=None,companyyear=None,headquarter=None):
        self.companyname=companyname
        self.companyyear=companyyear
        self.headquarter=headquarter
        
    def set_companyname(self,companyname):
        self.companyname=companyname
    
    def set_companyyear(self,companyyear):
        self.companyyear=companyyear
    
    def set_headquarter(self,headquarter):
        self.headquarter=headquarter

    def display(self):
        print("Company name: {} Found year: {} Head quarter: {} ".format(self.companyname,self.companyyear,self.headquarter))

class brand(company):
    def __init__(self,brandname=None,brandyear=None, brandcountry=None,belongyear=None,companyname=None,companyyear=None,headquarter=None):
        company.__init__(self,companyname,companyyear,headquarter)
        self.brandname=brandname
        self.brandyear=brandyear
        self.brandcountry=brandcountry
        self.belongyear=belongyear
    
    def set_brandname(self,brandname):
        self.brandname=brandname
    
    def set_brandyear(self,brandyear):
        self.brandyear=brandyear
    
    def set_brandcountry(self,brandcountry):
        self.brandcountry=brandcountry
    
    def set_belongyear(self,belongyear):
        self.belongyear=belongyear
    
    def display(self):
        company.display(self)
        print("Brand name: {} Found year: {} Brand Country: {} Belong Year: {} ".format(self.brandname,self.brandyear,self.brandcountry,self.belongyear))

