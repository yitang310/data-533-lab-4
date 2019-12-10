class ValuesBrandCompanyError(Exception):
    def __init__(self, value1,value2): 
        self.value1 = value1
        self.value2 = value2

def value_percentage(brand_value,company_value):
    try:
        
        if brand_value>company_value:
             raise ValuesBrandCompanyError(brand_value,company_value)
                
        bcpv=str(brand_value/company_value*100)+"%"
        return bcpv
            
    except ValuesBrandCompanyError as ve:
        print("Brand Value {} should not larger than Company Value {}.".format(ve.value1,ve.value2))
        
    except TypeError:
        print("TypeError")


def sales_percentage(sales_brand,sales_company):
    try:
        if sales_brand>sales_company:
            raise ValuesBrandCompanyError(sales_brand,sales_company)
                
        bcps=str(sales_brand/sales_company*100)+"%"
        return bcps
    
    except ValuesBrandCompanyError as ve2:
        print("Brand Sales {} should not larger than Company Sales {}.".format(ve2.value1,ve2.value2))
        

def tendency(lastyear,thisyear):
    
    ten=str(lastyear/thisyear*100)+"%"
    return ten