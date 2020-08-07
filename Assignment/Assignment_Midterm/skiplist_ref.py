import math
from collections import MutableMapping
from random import randint


class SkipList(MutableMapping):
    __slots__ = '_head', '_tail', '_n', '_height'

    # ------------------------------- nested _Node class -------------------------------
    class _Node:
        __slots__ = '_key', '_value', '_next'

        """Lightweight composite to store key-value pairs as map items."""

        def __init__(self, k, v, height):
            self._key = k
            self._value = v
            self._next = [None] * (height)

        def __eq__(self, other):
            if other == None:
                return False
            return self._key == other._key  # compare items based on their keys

        def __ne__(self, other):
            return not (self == other)  # opposite of __eq__

        def __lt__(self, other):
            return self._key < other._key  # compare items based on their keys

    def __init__(self):
        """Create an empty map."""
        self._head = self._Node(-math.inf, None, 1)  # Head: the first node in a skip list
        self._tail = self._Node(math.inf, None, 1)  # Tail: the last node in a skip list
        self._head._next[0] = self._tail  # Initially, there's no item -> head is directly linked to the tail
        self._n = 0  # Initially, there's no item, so _n = 0
        self._height = 1  # Initially, the height of a skip list is 1

    def __getitem__(self, k, update=None):
        node = self._head
        for i in range(self._height-1, -1, -1):  # 위에서 부터 찾음
            while node._next[i]._key <= k:  # 다음값이 k보다 작으면
                node = node._next[i]  # 다음값으로 이동
        if k == node._key:  # 찾은 노드가 key값이 같으면 리턴
            return node._value
        else:  # 아니면 에러
            return KeyError
        """Return value associated with key k (raise KeyError if not found)."""

    def __setitem__(self, k, v):
        node = self._head
        for i in range(self._height-1, -1, -1):
            while node._next[i]._key <= k:
                node = node._next[i]   # getitem과 같은 방식으로 찾음
        if node._key == k:
            node._value = v  # 같으면 덮어쓰기
        else:  # 다르면
            self._n += 1   #크기를 한칸 늘림
            nodeheight = -1
            while True:
                nodeheight += 1
                if randint(1, 2) == 1:
                    break  # 우선 동전 던지기로 새로운 노드의 높이를 정함
            if nodeheight+2 >= self._height:  # 높이가 기존 높이보다 크면
                for i in range(self._height, nodeheight + 2):
                    self._head._next.append(self._tail)  # 키운 만큼 head의 다음 값을 tail로 지정
                    self._tail._next.append(None)  #tail의 다음 값을 None으로 지정
                self._height = nodeheight+2  # 높이 새로 지정

                tnode = self._head  # 높이 맞춰주는 작업
                while tnode._next[0] != self._tail:
                    while len(tnode._next) +1 <= self._height:
                        tnode._next.append(None)
                    tnode = tnode._next[0]
                while len(tnode._next) +1 <= self._height:
                    tnode._next.append(None)
            node = self._head
            newnode = self._Node(k, v, self._height)  # 새노드 선언
            for i in range(self._height-1, -1, -1):  # getitem과 같은 방식으로 찾아서
                while node._next[i]._key <= k:
                    node = node._next[i]
                if i<=nodeheight:             #찾은 높이가 새 노드의 높이까지 내려오면
                    newnode._next[i]=node._next[i]  # 새 노드의 다음값을 바로 전 노드의 다음값으로 바꾸고
                    node._next[i] = newnode  # 전 노드의 다음값을 새 노드로 연결해서 새 노드 삽입


        """Assign value v to key k, overwriting existing value if present."""

    def __delitem__(self, k):
        node = self._head
        check=0
        for i in range(self._height - 1, -1, -1):  # 위에서 부터 찾음
            while node._next[i]._key <= k:
                if node._next[i]._key==k:          #다음 값이 키라면
                    node._next[i]=node._next[i]._next[i]   #현재값의 다음값을 다다음 값으로 바꿈
                    check=1 #check에 표시해줌
                    if(self._head._next[self._height-2]==self._tail):   #지웠는데 제일 꼭대기 아래도 head다음 값이 tail이라면
                        self._height-=1                              #높이를 한칸 줄임
                    break #while문 탈출
                else:
                    node = node._next[i]  # 아니면 다음값으로 이동
        if check==0:
            return KeyError #k값을 찾은적이 없으면 error
        else:
            self._n -= 1
        """Remove item associated with key k (raise KeyError if not found)."""

    def __len__(self):
        """Return number of items in the map."""
        return self._n

    def __iter__(self):
        """Generate iteration of the map's keys."""
        # iterate over the base height (=> height = 0)
        node = self._head._next[0]
        while not node is self._tail:
            yield node._key
            node = node._next[0]

    def print_tree(self):
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^')
        node = self._head
        while node != None:
            print('#', end='\t')
            for i in range(self._height):
                lnk = node._next[i]
                if node is self._tail:
                    print_val = '+'
                elif lnk == None:
                    print_val = '.'
                elif node._key == -math.inf:
                    print_val = '-'
                elif node._key == math.inf:
                    print_val = '+'
                else:
                    print_val = node._key

                print(print_val, end='\t')
            print()
            node = node._next[0]

        for h in reversed(range(self._height)):
            print(f"At height #{h}, ", end='')
            node = self._head
            while node != None:
                print(node._key, end=' -> ')
                node = node._next[h]
            print()
        print('vvvvvvvvvvvvvvvvvvvvvvvvvv')