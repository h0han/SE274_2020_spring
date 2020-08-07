import random
from heap_priority_queue import HeapPriorityQueue
class HeapPriorityQueue_A6_6(HeapPriorityQueue):
    def heappushpop(self, e):
        self.add(e[0], e[1])
        return self.remove_min()

    def heapreplace(self, e):
        pop = self.remove_min()
        self.add(e[0], e[1])
        return pop


Q = HeapPriorityQueue_A6_6()
random.seed(5)
names = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima",
         "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey",
         "X-ray", "Yankee", "Zulu"]
for name in random.sample(names, 5):
    key = random.randint(0, 100)
    Q.add(key, name)
print(Q._data)
print()
print(Q.heappushpop((21, 'jungwoo')))
print(Q._data)
print()
print(Q.heappushpop((19, 'Sunjun')))
print(Q._data)
print('----------------------------------------------------------------------')
H = HeapPriorityQueue_A6_6()
random.seed(5)
for name in random.sample(names, 5):
    key = random.randint(0, 100)
    H.add(key, name)
print(H._data)
print()
print(H.heapreplace((21, 'jungwoo')))
print(H._data)
print()
print(H.heapreplace((19, 'Sunjun')))
print(H._data)