class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def next_node(self):
        return self._next

    @next_node.setter
    def next_node(self, next_node):
        self._next = next_node


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index
        is invalid, return -1.
        """
        if self.head is None:
            return -1

        real_index = 0
        tmp = self.head

        while True:
            if real_index == index:
                break

            tmp = tmp.next_node
            if tmp is not None:
                real_index += 1
            else:
                break
        if tmp:
            return tmp.value
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the
        linked list.
        """
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            node.next_node = self.head
            self.head = node

        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)

        tail_node = self.head
        while tail_node.next_node is not None:
            tail_node = tail_node.next_node

        tail_node.next_node = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be
        appended to the end of linked list. If index is greater than the
        length, the node will not be inserted.
        """
        node = Node(val)

        if index == 0:
            self.addAtHead(val)
        elif index == self.size - 1:
            self.addAtTail(val)
        else:

            real_index = 0
            tmp = self.head
            while tmp:
                if real_index == index - 1:
                    break

                tmp = tmp.next_node
                real_index += 1

            if tmp:
                node.next_node = tmp.next_node
                tmp.next_node = node

            self.size += 1

    def deleteHead(self):
        if self.head:
            self.head = self.head.next
            self.size = self.size - 1

    def deleteTail(self):
        tail_node = self.head
        while tail_node.next_node.next_node is not None:
            tail_node = tail_node.next_node

        tail_node.next_node = None
        self.size = self.size - 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        real_index = 0
        tmp = self.head
        if index == 0:
            self.deleteHead()
        elif index == self.size - 1:
            self.deleteTail()
        else:

            while tmp:
                if real_index == index - 1:
                    break
                tmp = tmp.next_node
                real_index += 1

            if tmp:
                delete_node = tmp.next_node
                tmp.next_node = delete_node.next_node
                self.size = self.size - 1


if __name__ == '__main__':
    myLinkedList = MyLinkedList()
