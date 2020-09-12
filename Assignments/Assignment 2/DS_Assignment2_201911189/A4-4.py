#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#A4-4(1 point)
from positional_list import PositionalList
class personal_PL_4(PositionalList):
    def max(self):
        k = 0
        iterator = iter(self)
        for i in iterator:
            if type(i) != int or type(i) != float:
                raise TypeError('Check your element type')
            else:
                if k < i:
                    k = i
        return k

