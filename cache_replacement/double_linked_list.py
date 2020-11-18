from cache_replacement.node import Node


class DoubleLinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None

    def __add_head(self, node):
        if self.head is None:
            node.next = None
            node.prev = None
            self.head = self.tail = node
        else:
            node.next = self.head
            node.prev = None
            self.head.prev = node
            self.head = node

        self.size += 1

    def __add_tail(self, node):
        if self.tail is None:
            node.next = None
            node.prev = None
            self.head = self.tail = node
        else:
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node

        self.size += 1

    def __del_head(self):
        if self.head is None:
            return None

        node = self.head
        next_node = self.head.next

        if not next_node:
            self.head = self.tail = None
        else:
            next_node.prev = None
            self.head = next_node

        self.size -= 1

        return node

    def __del_tail(self):
        if self.tail is None:
            return None

        node = self.tail
        prev_node = self.tail.prev

        if not prev_node:
            self.head = self.tail = None
        else:
            prev_node.next = None
            self.tail = prev_node

        self.size -= 1

        return node

    # 从头部添加节点
    def append_front(self, node):
        if not isinstance(node, Node):
            raise ValueError('node must be a Node')

        self.__add_head(node)

    # 从尾部添加节点
    def append(self, node):
        if not isinstance(node, Node):
            raise ValueError('node must be a Node')

        self.__add_tail(node)

    #  从头部删除节点
    def pop(self):
        return self.__del_head()

    # 删除任意节点
    def remove(self, node):
        if node is None:
            node = self.tail

        if node == self.head:
            return self.__del_head()
        elif node == self.tail:
            return self.__del_tail()
        else:
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            self.size -= 1

            return node

    def print(self):
        head = self.head

        s = ''
        while head:
            s += f'{str(head)}'
            head = head.next
            if head:
                s += ' => '

        print(s)
