#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#A4-5(1 point)
from positional_list import PositionalList 
class personal_PL_5(PositionalList):
    def find(self, elem):
        iterator = iter(self)
        for i in iterator:
            if elem == i:
                return self._make_position(i)
            else:
                return None

