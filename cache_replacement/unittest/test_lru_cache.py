from cache_replacement.lru_cache import LRUCache


def test_create_lru_cache():
    lru_cache = LRUCache(capacity=2)
    assert lru_cache.size == 0


def test_get_cache():
    lru_cache = LRUCache(capacity=2)
    assert lru_cache.size == 0
    assert lru_cache.get(1) == -1


def test_put_cache():
    lru_cache = LRUCache(capacity=3)
    assert lru_cache.size == 0

    lru_cache.put(1, 1)
    assert lru_cache.size == 1
    assert lru_cache.get(1) == 1

    lru_cache.put(2, 2)
    assert lru_cache.size == 2
    assert lru_cache.get(2) == 2

    lru_cache.put(3, 3)
    assert lru_cache.size == 3
    assert lru_cache.get(3) == 3

    lru_cache.put(4, 4)
    assert lru_cache.size == 3
    assert lru_cache.get(4) == 4
    assert lru_cache.get(1) == -1
