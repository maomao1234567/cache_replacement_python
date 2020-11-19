from cache_replacement.double_linked_list import DoubleLinkedList
from cache_replacement.node import Node


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.cache_map = {}
        self.cache_list = DoubleLinkedList(capacity=capacity)

    def get(self, key):
        if key not in self.cache_map:
            return -1
        else:
            value = self.cache_map.get(key)
            node = Node(key, value)
            self.cache_list.remove(node)
            self.cache_list.append_front(node)
            return value

    def put(self, key, value):
        if key in self.cache_map:
            old_node = Node(key, self.cache_map.get(key))
            self.cache_list.remove(old_node)
            new_node = Node(key, value)
            self.cache_list.append(new_node)
            self.cache_map[key] = value
        else:

            if self.size == self.capacity:
                old_node = self.cache_list.remove()
                self.cache_map.pop(old_node.key)
            else:
                self.size += 1

            new_node = Node(key, value)
            self.cache_list.append_front(new_node)
            self.cache_map[key] = value
