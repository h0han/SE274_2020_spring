#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#A5-4 (3 points)
from linked_binary_tree import LinkedBinaryTree 
class personal_LBP(LinkedBinaryTree):
    def _delete_subtree(self, p):
        if self.num_children(p) != 0:
            for child in self.children(p):
                self._delete_subtree(child)
            return self._delete(child)
        else:
            return self._delete(p)

running time의 경우, O(n) time이 소요된다.

