#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#A4-Bonus(1 point)
from positional_list import PositionalList 
class personal_PL_B(PositionalList):
    walk = self.first()
    def find(self, elem):
        if self.is_empty():
            raise EmptyError('The list is empty')
        else:
            if self.first().element() == elem:
                return self._make_position(walk.element())
            else:
                walk = self.after(walk)
                if walk.element() == elem:
                    return self._make_position(walk)
                else:
                    return self.find(self.element())

