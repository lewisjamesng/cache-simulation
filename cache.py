from linked_list import LinkedList
from random import uniform
import math

## uses inverted form of  U = 1 - e^(-rT)
## swapped 1-U for U as is symmetrical
def time_sample(rate):
    return (-1/(rate)) * math.log(uniform(0, 1))


class Cache:

    def __init__(self, m, is_fifo):
        self.m = m

        self.cache = LinkedList([])
        self.map = {}
        self.is_fifo = is_fifo

    def getResource(self, n):

        # types of cache only differing by eviction management
            if n in self.map:
                if not self.is_fifo:
                    list_node = self.map.get(n)

                    self.cache.remove(list_node)
                    self.map.update({n: self.cache.addFront(list_node.val)})
                return 1
            else:
                if self.m == len(self.map.keys()):
                    
                    evict = self.cache.popBack()
                    self.map.pop(evict.val)

                self.map.update({n: self.cache.addFront(n)})
                
                return 0
            


