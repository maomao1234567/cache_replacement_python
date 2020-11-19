from cache_replacement.lfu_cache import LFUCache


def test_create_cache():
    lfu_cache = LFUCache(capacity=5)
    assert lfu_cache.size == 0


def test_get_cache():
    lfu_cache = LFUCache(capacity=4)
    assert lfu_cache.size == 0

    assert lfu_cache.get(1) == -1


def test_put_cache():
    lfu_cache = LFUCache(capacity=4)
    assert lfu_cache.size == 0

    lfu_cache.put(1, 1)
    lfu_cache.put(2, 2)
    lfu_cache.put(3, 3)

    assert lfu_cache.size == 3
    assert lfu_cache.get(2) == 2

    lfu_cache.put(4, 4)
    assert lfu_cache.size == 4

    assert lfu_cache.get(3) == 3
    lfu_cache.put(5, 5)

    assert lfu_cache.get(1) == -1

    assert lfu_cache.get(4) == 4
    lfu_cache.put(6, 6)
    assert lfu_cache.get(5) == -1
    assert lfu_cache.size == 4
