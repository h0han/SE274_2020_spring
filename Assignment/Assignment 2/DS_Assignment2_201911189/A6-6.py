#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#A6-6 (3 points)
from heap_priority_queue import HeapPriorityQueue 
class heapq(HeapPriorityQueue):
    def heappushpop(self, elem):
        self.add(elem[0], elem[1]) #elem의 key, value쌍 입력
        return self.remove_min() #downheap의 경우 remove_min에서 자동으로 수행
    
    def heapreplace(self, elem):
        show = self.remove_min() #조건에 맞추어 새로운 element가 add되기 전 최솟값을 추출
        self.add(elem[0], elem[1])
        return show

