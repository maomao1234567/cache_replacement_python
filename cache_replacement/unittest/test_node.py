import pytest

from cache_replacement.node import Node


def test_create_node():
    node = Node('name', 'yangmao')

    assert node.key == 'name'
    assert node.value == 'yangmao'


def test_str_node():
    node = Node('name', 'yangmao')

    assert str(node) == 'name: yangmao'
    assert repr(node) == 'name: yangmao'


def test_prev_node():
    node = Node('name', 'yangmao')
    prev_node = Node('name', 'weixiaochun')

    node.prev = prev_node
    assert str(node.prev) == 'name: weixiaochun'

    with pytest.raises(ValueError):
        prev_node.prev = 'ali'


def test_next_node():
    node = Node('name', 'yangmao')
    next_node = Node('name', 'weixiaochun')

    node.next = next_node
    assert str(node.next) == 'name: weixiaochun'

    with pytest.raises(ValueError):
        next_node.next = 'hello'
