from cache_replacement.node import Node
from cache_replacement.double_linked_list import DoubleLinkedList


class LFUNode(Node):
    def __init__(self, key, value):
        self._freq = 0
        super(LFUNode, self).__init__(key, value)

    @property
    def freq(self):
        return self._freq

    def update_freq(self, freq):
        self._freq = freq


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.cache_map = {}
        self.freq_caches = {}

    def _update_node_freq(self, node):
        old_freq = node.freq
        if old_freq in self.freq_caches:
            self.freq_caches[old_freq].remove(node)
            if self.freq_caches[old_freq].size == 0:
                self.freq_caches.pop(old_freq)

        new_freq = old_freq + 1
        node.update_freq(new_freq)
        if new_freq in self.freq_caches:
            self.freq_caches[new_freq].append(node)
        else:
            nodes_list = DoubleLinkedList(capacity=self.capacity)
            nodes_list.append(node)
            self.freq_caches[new_freq] = nodes_list

    def get(self, key):
        if key not in self.cache_map:
            return -1
        else:
            node = self.cache_map[key]
            self._update_node_freq(node)
            return node.value

    def put(self, key, value):
        if key in self.cache_map:
            old_node = self.cache_map[key]
            old_node.value = value
            self._update_node_freq(old_node)
        else:
            node = LFUNode(key, value)
            self._update_node_freq(node)
            self.cache_map[key] = node

            if self.size == self.capacity:
                min_freq = min(self.freq_caches)
                del_node = self.freq_caches[min_freq].pop()
                self.cache_map.pop(del_node.key)
            else:
                self.size += 1
