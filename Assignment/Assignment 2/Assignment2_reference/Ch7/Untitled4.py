#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#A4-2(1 point)
from positional_list import PositionalList 
class personal_PL(PositionalList):
    def __reversed__(self):
        cursor = self.last()
        while cursor is not None:
            yield cursor.element()
            cursor = self.before(cursor)
p = PositionalList()
for i in ['a', 'b', 'c', 'd']:
    p.add_last(i)
for i in p:
    print(i, end = ' ')
print()
reversed_p = self.__reversed__(p)
print(reversed_p)

