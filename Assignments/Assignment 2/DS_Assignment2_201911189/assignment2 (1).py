#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#A4 - Linked List (5+1 points)


# #A4-1(1 point)
# singly_linked_list의 경우, x와 y를 swap하는 과정에서 x의 previous node와 y의 previous node를 모두 알아야 한다. 이 과정에서 각각의 previous node를 찾기 위해 O(n) time이 소요된다. 반면 doubly_linked_list의 경우 x와 y의 previous 노트 탐색을 O(1) time에 수행 가능하다.(모든 node가 previous_node_field와 next_node_field를 갖고 있기 때문) 띠라서 singly_linked_list의 작업 소요 시간이 더 길다.

# In[8]:


#A4-2(1 point)
from positional_list import PositionalList 
class personal_PL_2(PositionalList):
    def __reversed__(self):
        cursor = self.last()
        while cursor is not None:
            yield cursor.element()
            cursor = self.before(cursor)


# In[9]:


p = personal_PL()
arr = []
for i in ['a', 'b', 'c', 'd', 'e']:
    p.add_last(i)
for i in p:
    print(i, end = ' ')
print()
reversed_p = reversed(p)
for k in reversed_p:
    print(k, end = ' ')


# In[13]:


#A4-3(1 point)
from positional_list import PositionalList
class personal_PL_3(PositionalList):
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
                self.add_after(before_node, elem) #before_node의 다음 node에 elem 삽입
    
    def display(self, message = ''):
        count = 0
        print(message, end = '')
        node = self._header
        while True:
            if node._element == None:
                count += 1
            if count == 2:
                print(node._element)
                break
            else:
                print(node._element, end=' - ')
                node = node._next


# In[14]:


L = personal_PL()
L.display('initial statement: ')
L.add_first(10)
L.add_first(20)
L.add_first(30)
L.display('addfirst 3times: ')
L.add_last(40)
L.add_last(50)
L.add_last(60)
L.display('addlast 3times: ')
L.add_before(L.first(), 70)
L.add_before(L.last(), 80)
L.display('addbefore 3times: ')


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


# In[29]:


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


# In[30]:


L = personal_PL_5()
for i in [1, 2, 3, 4, 5]:
    L.add_first(i)
print(L.find(5))
print(L.find(3))
print(L.find(1))


# In[25]:


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
                    self.find(self.element())


# In[ ]:


L = personal_PL_B()
for i in [1, 2, 3, 4, 5]:
    L.add_first(i)
print(L.find(5))
print(L.find(3))
print(L.find(1))


# L의 capacity를 n이라 하면, 위 함수는 L에서 elem을 탐색하기 위해 n번의 재귀호출이 필요하다. 이는 새로 생성되는 space가 n번 생성되는 뜻과 상통하고, 따라서 공간복잡도는 O(n)이 된다.

# In[ ]:


#A5 - Trees (7 points)


# #A5-1(1 point)
# 1. /user/rt/courses/
# 2. /user/rt/courses/, cs016/, homeworks/, programs/, cs252/, projects/, papers/, /demos/
# 3. cs016/ has 9 decendants.
# 4. It has only 1 ancestor.(//user/rt/courses/)
# 5. Its sibilings are grades/ and programs/.
# 6. papers/ and demos/
# 7. 3
# 8. 4

# #A5-2 (1 point)
#       E      
#      / \
#     X   N
#    / \
#   A   U
#  / \
# M   F

# In[ ]:


#A5-3 (2 points)
def root():
    for node in T:
        if f(node) == 0:
            return node
        
def is_root(p):
    return f(p) == 0

def parent(p):
    if f(p) % 2 == 0:
        for node in T:
            return T[(f(p))/2-1]
    elif f(p) % 2 == 1:
        for node in T:
            return T[(f(p)-1)/2]
        
def left(p):
    for node in T:
        if node == parent(T[2*f(p)+1]):
            return node
        else:
            return None

def right(p):
    for node in T:
        if node == parent(T[2*f(p)+2]):
            return node
        else:
            return None

def is_leaf(p):
    if left(p) != None or right(p) != None:
        False
    else:
        True


# In[139]:


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


# In[1]:


#A6 - Priority Queues, Heaps (8+2 points)


# #A6-1 (1 point)
# heap에서의 remove_min 실행의 시간복잡도는 O(log(n))이다. 그런데, 문제에서 removing smallest elements의 횟수를 log(n)이라 지정하였으므로, 총 시간복잡도는 O((log(n))^2)이다.

# In[ ]:


#A6-2 (1 point)
1. remove_min()
In PQ: [(1, D), (4, B), (5, A), (7, F)] -> (1, D)
2. remove_min()
In PQ: [(3, j), (4, B), (5, A), (6, L), (7, F)] -> (3, j)
3. remove_min()
In PQ: [(4, B), (5, A), (6, L), (7, F)] -> (4, B)
4. remove_min()
In PQ: [(5, A), (6, L), (7, F), (8, G)] -> (5, A)
5. remove_min()
In PQ: [(2, H), (6, L), (7, F), (8, G)] -> (2, H)
6. remove_min()
In PQ: [(6, L), (7, F), (8, G)] -> (6, L)

Result: (1, D), (3, j), (4, B), (5, A), (2, H), (6, L)


# #A6-3 (1 point)
# Priority Queue
# future event를 추가하고, time stamp가 가장 낮은 것부터 extract 해야한다. 따라서 key값의 우선순위를 비교하여 pop하는 priority queue의 구조와 흡사하다.

# #A6-4 (1 point)
# <Selection sort>
# Input: Sequence: (22, 15, 36, 44, 10, 3, 9, 13, 29, 25) Queue: ()
# Phase1
# a. S: (15, 36, 44, 10, 3, 9, 13, 29, 25) Q: (22)
# b. S: (36, 44, 10, 3, 9, 13, 29, 25) Q: (22, 15)
# ...
# j. S: () Q: (22, 15, 36, 44, 10, 3, 9, 13, 29, 25)
# 
# Phase2
# a. S: (3) Q: (22, 15, 36, 44, 10, 9, 13, 29, 25)
# b. S: (3, 9) Q: (22, 15, 36, 44, 10, 13, 29, 25)
# c. S: (3, 9, 10) Q: (22, 15, 36, 44, 13, 29, 25)
# d. S: (3, 9, 10, 13) Q: (22, 15, 36, 44, 29, 25)
# e. S: (3, 9, 10, 13, 15) Q: (22, 36, 44, 29, 25)
# f. S: (3, 9, 10, 13, 15, 22) Q: (36, 44, 29, 25)
# g. S: (3, 9, 10, 13, 15, 22, 25) Q: (36, 44, 29)
# h. S: (3, 9, 10, 13, 15, 22, 25, 29) Q: (36, 44)
# i. S: (3, 9, 10, 13, 15, 22, 25, 29, 36) Q: (44)
# j. S: (3, 9, 10, 13, 15, 22, 25, 29, 36, 44) Q: ()

# #A6-5 (1 point)
# <Insertino sort>
# Input: Sequence: (22, 15, 36, 44, 10, 3, 9, 13, 29, 25)	Priority Queue: ()
# Phase1
# a. S: (15, 36, 44, 10, 3, 9, 13, 29, 25) Q: (22)
# b. S: (36, 44, 10, 3, 9, 13, 29, 25) Q: (15, 22) 
# c. S: (44, 10, 3, 9, 13, 29, 25) Q: (15, 22, 36)
# d. S: (10, 3, 9, 13, 29, 25) Q: (15, 22, 36, 44)
# e. S: (3, 9, 13, 29, 25) Q: (10, 15, 22, 36, 44)
# f. S: (9, 13, 29, 25) Q: (3, 10, 15, 22, 36, 44)
# g. S: (13, 29, 25) Q: (3, 9, 10, 15, 22, 36, 44)
# h. S: (29, 25) Q: (3, 9, 10, 13, 15, 22, 36, 44)
# i. S: (25) Q: (3, 9, 10, 13, 15, 22, 29, 36, 44)
# j. S: () Q: (3, 9, 10, 13, 15, 22, 25, 29, 35, 44)
# 
# Phadse2
# a. S: (3) Q: (9, 10, 13, 15, 22, 25, 29, 35, 44)
# b. S: (3, 9) Q: (10, 13, 15, 22, 25, 29, 35, 44)
# …
# j. S: (3, 9, 10, 13, 15, 22, 25, 29, 35, 44) Q: ()

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

