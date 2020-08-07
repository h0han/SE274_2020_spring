#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#A4-3(1 point)
from positional_list import PositionalList
class personal_PL(PositionalList):
    def add_last(self, elem):
        if self.is_empty() == True: #리스트가 비어있으면
            return self.add_first(elem) #header 노드 뒤에 elem 삽입
        else:
            last = self.last()
            return self.add_after(last, elem)
        
    def add_before(self, pos, elem):
        if self.is_empty() == True:
            return self.add_first(elem)
        else:
            before_node = self.before(pos) #pos 이전 node를 before_node에 할당
            if before_node == None:
                return self.add_first(elem)
            else:
                return self.add_after(before_node, elem) #before_node의 다음 node에 elem 삽입

