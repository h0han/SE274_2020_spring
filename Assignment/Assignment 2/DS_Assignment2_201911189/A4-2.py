#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#A4-2(1 point)
from positional_list import PositionalList 
class personal_PL_2(PositionalList):
    def __reversed__(self):
        cursor = self.last()
        while cursor is not None:
            yield cursor.element()
            cursor = self.before(cursor)

