from cache_replacement.fifo_cache import FIFOCache


def test_create_fifo_cache():
    fifo_cache = FIFOCache(capacity=2)
    assert fifo_cache.capacity == 2
    assert fifo_cache.size == 0


def test_get_cache():
    fifo_cache = FIFOCache(capacity=2)
    assert fifo_cache.size == 0

    assert fifo_cache.get(1) == -1


def test_put_cache():
    fifo_cache = FIFOCache(capacity=2)
    assert fifo_cache.size == 0

    fifo_cache.put(1, 1)
    assert fifo_cache.size == 1

    assert fifo_cache.get(1) == 1
    fifo_cache.put(2, 2)
    assert fifo_cache.size == 2

    fifo_cache.put(3, 3)
    assert fifo_cache.size == 2
    assert fifo_cache.get(3) == 3
    assert fifo_cache.get(1) == -1
