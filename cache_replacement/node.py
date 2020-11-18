class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self._prev = None
        self._next = None

    def __str__(self):
        return f'{self.key}: {self.value}'

    def __repr__(self):
        return f'{self.key}: {self.value}'

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev_node):
        if prev_node:
            if not isinstance(prev_node, Node):
                raise ValueError('prev must be a Node')

        self._prev = prev_node

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_node):
        if next_node:
            if not isinstance(next_node, Node):
                raise ValueError('next must be a Node')

        self._next = next_node
