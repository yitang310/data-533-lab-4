#!/usr/bin/env python
# coding: utf-8

# In[12]:


class TimeError(Exception):
    pass

def property(ig, ed, md):
    try:
        if ed < md:
            raise TimeError()

        if type(ig) is not str:
            raise TypeError()

        print("main ingredients: {}".format(ig))
        print("expiration date: {}".format(ed))
        print("date of manufacture: {}".format(md))

    except TypeError:
         print("Error: TypeError")

    except TimeError:
        print("Error: expiration date < date of manufacture.")
