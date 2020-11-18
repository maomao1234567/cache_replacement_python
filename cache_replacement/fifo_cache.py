from cache_replacement.node import Node
from cache_replacement.double_linked_list import DoubleLinkedList


class FIFOCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.cache_map = {}
        self.cache_list = DoubleLinkedList(capacity)

    def get(self, key):
        if key not in self.cache_map:
            return -1
        else:
            return self.cache_map.get(key)

    def put(self, key, value):
        if key in self.cache_map:
            old_node = Node(key, self.cache_map[key])
            self.cache_list.remove(old_node)
            new_node = Node(key, value)
            self.cache_list.append(new_node)
            self.cache_map[key] = value
        else:

            if self.size == self.capacity:
                replace_node = self.cache_list.pop()
                self.cache_list.append(Node(key, value))
                self.cache_map.pop(replace_node.key)
                self.cache_map[key] = value
            else:
                self.cache_list.append(Node(key, value))
                self.cache_map[key] = value
                self.size += 1
