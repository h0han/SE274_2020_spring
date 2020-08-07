from collections import MutableMapping
import math
import random


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

        def __eq__(self, other):
            if other == None:
                return False
            return self._key == other._key   # compare items based on their keys

        def __ne__(self, other):
            return not (self == other)       # opposite of __eq__

        def __lt__(self, other):
            return self._key < other._key    # compare items based on their keys

        def __repr__(self):
            return str(self._value)

    def __init__(self):
        """Create an empty map."""
        self._head = self._Node(-math.inf, 'head',
                                1)   # Head: the first node in a skip list
        # Tail: the last node in a skip list
        self._tail = self._Node(math.inf, 'tail', 1)
        # Initially, there's no item -> head is directly linked to the tail
        self._head._next[0] = self._tail
        self._n = 0                              # Initially, there's no item, so _n = 0
        self._height = 1                         # Initially, the height of a skip list is 1

    def __getitem__(self, k, update=None):
        """Return value associated with key k (raise KeyError if not found)."""
        node, _ = self.do_find(k)
        if node is None:
            raise KeyError(f'{k} not found')
        return node

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        node, update = self.do_find(k)
        if node:
            node._value = v
            return

        new_height = self.get_random_height()
        height = self._height

        update.extend([self._head for _ in range(height, new_height)])
        self._head._next.extend(
            [self._tail for _ in range(height, new_height)])
        self._tail._next.extend([None for _ in range(height, new_height)])

        self._height = max(self._height, new_height)

        new_node = self._Node(k, v, new_height)
        new_node._next = [update[level]._next[level]
                          for level in range(new_height)]
        for level in range(new_height):
            update[level]._next[level] = new_node

        self._n += 1

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        node, update = self.do_find(k)
        if not node:
            raise KeyError(f'{k} not found')
        for i in reversed(range(len(node._next))):
            update[i]._next[i] = node._next[i]
            if len(self._head._next) > 1 and self._head._next[i] == self._tail:
                self._height -= 1
                head = self._head._next.pop()
                del head
        self._n -= 1
        del node

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

    def get_random_height(self):
        height = 1
        while random.choice([True, False]):
            height += 1
        return height

    def do_find(self, k: int):
        height = self._height
        update = [self._head] * height
        current = self._head
        result = None
        for level in reversed(range(height)):
            node = current
            while node._next[level] != self._tail and node._next[level]._key < k:
                node = node._next[level]

            if node._next[level]._key == k:
                result = node._next[level]
            update[level] = node
        return result, update

    def print_tree(self):
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^')
        node = self._head
        while node != None:
            print('#', end='\t')
            for i in range(self._height):
                lnk = node._next[i] if i < len(node._next) else None

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
                # print(f'h: {h}, node: {node._next}')
                node = node._next[h]
            print()
        print('vvvvvvvvvvvvvvvvvvvvvvvvvv')

'''
if __name__ == '__main__':
    sl = SkipList()
    for i in range(10):
        sl[i] = chr(65 + i)
        print(f'sl[{i}] = {sl[i]}')
    sl.print_tree()
    for i in range(0, 10, 3):
        print(i)
        del sl[i]
    sl.print_tree()
    for i in range(10):
        try:
            print(sl[i])
        except KeyError as e:
            print(e)
'''