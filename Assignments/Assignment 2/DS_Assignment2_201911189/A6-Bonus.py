#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#A6-Bonus (2 points)
from heap_priority_queue import HeapPriorityQueue
class personal_HPQ(HeapPriorityQueue):
    def upheap(self, i): #upheap과 downheap을 문제 조건에 맞게 재구성
        parent = self._parent(i)
        if i > 0 and self._data[i] > self._data[parent]:
            self._swap(i, parent)
            self._upheap(parent)
            
    def downheap(self, j):
        if self._has_left(j):
            left = self.left(j)
            big_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] > self._data[left]:
                    big_child = right
            if self._data[big_child] > self._data[j]:
                self.swap(j, big_child)
                self.dowmheap(big_child)
    
    def heapsort(a):
        heap = personal_HPQ()
        for key in a:
            heap.add(key, 'value')
        for i in range(len(a)):
            return self.remove_min()

