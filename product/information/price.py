#!/usr/bin/env python
# coding: utf-8

# In[11]:


class ProvinceError(Exception):
    pass

def tax_price(p, str):
    try:
        pro = ['AB','BC','MB','NB','NL','NS','NT','NU','ON','PE','QC','SK','YT']

        if str not in pro:
            raise ProvinceError()

        if str == 'AB':
            return 1.05 * p
        if str == 'BC':
            return 1.12 * p
        if str == 'MB':
            return 1.13 * p
        if str == 'NB':
            return 1.15 * p
        if str == 'NL':
            return 1.15 * p
        if str == 'NS':
            return 1.15 * p
        if str == 'NT':
            return 1.05 * p
        if str == 'NU':
            return 1.05 * p
        if str == 'ON':
            return 1.13 * p
        if str == 'PE':
            return 1.15 * p
        if str == 'QC':
            return 1.14975 * p
        if str == 'SK':
            return 1.11 * p
        if str == 'YT':
            return 1.05 * p

    except TypeError:
        print("Error: TypeError")

    except ProvinceError:
        print("Error input: please input correct number of provinces.")
