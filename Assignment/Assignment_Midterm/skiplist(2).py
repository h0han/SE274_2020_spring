from collections.abc import MutableMapping
import math, random

class SkipList(MutableMapping):
    __slots__ = '_head', '_tail', '_n', '_height'

    #------------------------------- nested _Node class -------------------------------
    class _Node:
        __slots__ = '_key', '_value', '_next'

        """Lightweight composite to store key-value pairs as map items."""
        def __init__(self, k, v, height):
            self._key = k
            self._value = v
            self._next = [None] * (height)

        def __eq__(self, other): #other 값에 value 삽입              
            if other == None:
                return False
            return self._key == other._key   # compare items based on their keys

        def __ne__(self, other):
            return not (self == other)       # opposite of __eq__

        def __lt__(self, other):               
            return self._key < other._key    # compare items based on their keys

    # 수정됨
    def __init__(self, height=1):
        """Create an empty map."""
        self._head = self._Node(-math.inf, None, height)   # Head: the first node in a skip list
        self._tail = self._Node(math.inf, None, height)    # Tail: the last node in a skip list

        for i in range(0, height):
            self._head._next[i] = self._tail             # Initially, there's no item -> head is directly linked to the tail

        self._n = 0                                  # Initially, there's no item, so _n = 0
        self._height = height                        # Initially, the height of a skip list is 1
  
    def __getitem__(self, k: int, update=None):
        """Return value associated with key k (raise KeyError if not found)."""
        h = self._height - 1
        current_node = self._head._next[0]

        while current_node != self._tail and h >= 0:
            if current_node._key == k:
                return current_node

            next_node = current_node._next[h]           

            if next_node._key > k:
                h -= 1
            else:
                current_node = current_node._next[h]

        raise KeyError

    def __setitem__(self, k: int, v: object) -> None:
        """Assign value v to key k, overwriting existing value if present."""
        
        try:
            target_node = self.__getitem__(k)
            target_node._value = v
        except KeyError:
            new_node = self._Node(k, v, self._height)
            current_node = self._head
            
            while self._n == 0 or (self._n >= 0 and current_node != self._tail):
                next_node = current_node._next[0]

                if current_node._key < k < next_node._key:
                    # 여기 짜야됨
                    
                    break

                current_node = next_node

            self._n += 1

    def __delitem__(self, k):
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
                
                print(print_val, end ='\t')
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

    def print_tree2(self):
        pass


if __name__ == '__main__':
    my_list = SkipList(5)

    my_list.__setitem__(1, 'a')
    my_list.__setitem__(2, 'b')
    #my_list.__setitem__(3, 'b')
    #my_list.__setitem__(4, 'd')
    #my_list.__setitem__(5, 'e')

    my_list.print_tree()