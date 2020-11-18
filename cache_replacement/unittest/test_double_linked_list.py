import pytest

from cache_replacement.node import Node
from cache_replacement.double_linked_list import DoubleLinkedList


def test_create_double_linked_list():
    double_linked_list = DoubleLinkedList(capacity=5)

    assert double_linked_list.capacity == 5
    assert double_linked_list.size == 0


def test_append_head_node():
    double_linked_list = DoubleLinkedList(capacity=5)

    assert double_linked_list.capacity == 5
    assert double_linked_list.size == 0

    with pytest.raises(ValueError):
        double_linked_list.append_front('hello')

    node1 = Node('name', 'yangmao')
    double_linked_list.append_front(node1)
    assert double_linked_list.size == 1
    assert double_linked_list.head == node1

    node2 = Node('name', 'weixiaochun')
    double_linked_list.append_front(node2)
    assert double_linked_list.size == 2
    assert double_linked_list.head == node2
    assert double_linked_list.head.next == node1
    assert double_linked_list.head.prev is None


def test_append_node():
    double_linked_list = DoubleLinkedList(capacity=5)

    assert double_linked_list.capacity == 5
    assert double_linked_list.size == 0

    node1 = Node('name', 'yangmao')
    double_linked_list.append(node1)
    assert double_linked_list.size == 1
    assert double_linked_list.head == node1
    assert double_linked_list.tail == node1

    node2 = Node('name', 'weixiaochun')
    double_linked_list.append(node2)
    assert double_linked_list.size == 2
    assert double_linked_list.head == node1
    assert double_linked_list.tail == node2


def test_pop_node():
    double_linked_list = DoubleLinkedList(capacity=5)

    assert double_linked_list.size == 0
    assert double_linked_list.pop() is None

    node1 = Node('name', 'yangmao')
    node2 = Node('name', 'weixiaochun')

    double_linked_list.append(node1)
    assert double_linked_list.size == 1

    assert double_linked_list.pop() == node1
    assert double_linked_list.size == 0

    double_linked_list.append(node2)
    double_linked_list.append(node1)
    assert double_linked_list.pop() == node2
    assert double_linked_list.size == 1


def test_remove_node():
    double_linked_list = DoubleLinkedList(capacity=5)

    assert double_linked_list.size == 0

    assert double_linked_list.remove(node=None) is None

    node1 = Node('name', 'yangmao')
    double_linked_list.append_front(node1)
    assert double_linked_list.size == 1

    assert double_linked_list.remove(node1) == node1
    assert double_linked_list.size == 0

    node2 = Node('name', 'weixiaochun')
    node3 = Node('name', 'daiqiu')
    double_linked_list.append(node1)
    double_linked_list.append(node2)

    assert double_linked_list.remove(node=None) == node2
    assert double_linked_list.size == 1

    double_linked_list.append(node2)
    double_linked_list.append(node3)
    assert double_linked_list.size == 3

    assert double_linked_list.remove(node2) == node2
    assert double_linked_list.size == 2
    assert double_linked_list.tail == node3

    double_linked_list.print()

