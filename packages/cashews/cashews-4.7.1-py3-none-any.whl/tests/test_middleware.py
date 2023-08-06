from unittest.mock import Mock

import pytest

from cashews import Cache
from cashews.backends.memory import Memory
from cashews.disable_control import ControlMixin
from cashews.helpers import add_prefix, all_keys_lower, memory_limit

pytestmark = pytest.mark.asyncio


@pytest.fixture(name="target")
def _target() -> Mock:
    class MemCache(ControlMixin, Memory):
        pass

    return Mock(wraps=MemCache())


@pytest.fixture(name="cache")
def __cache(target):
    _cache = Cache()
    _cache._add_backend(Memory)
    _cache._backends[""] = (target, _cache._backends[""][1])
    return _cache


async def test_all_keys_lower(cache: Cache, target):
    cache._backends[""] = cache._backends[""][0], (all_keys_lower(),)
    await cache.get(key="KEY")
    target.get.assert_called_once_with(key="key", default=None)

    await cache.set(key="KEY", value="value")
    target.set.assert_called_once_with(
        key="key",
        value="value",
        exist=None,
        expire=None,
    )
    await cache.ping()
    target.ping.assert_called_once_with(message=b"PING")


async def test_memory_limit(cache: Cache, target):
    cache._backends[""] = cache._backends[""][0], (memory_limit(min_bytes=52, max_bytes=75),)

    await cache.set(key="key", value="v")
    target.set.assert_not_called()

    await cache.set(key="key", value="v" * 31)
    target.set.assert_not_called()

    await cache.set(key="key", value="v" * 15)
    target.set.assert_called_once_with(
        key="key",
        value="v" * 15,
        exist=None,
        expire=None,
    )

    await cache.ping()
    target.ping.assert_called_once_with(message=b"PING")


async def test_add_prefix(cache: Cache, target):
    cache._backends[""] = cache._backends[""][0], (add_prefix("prefix!"),)

    await cache.get(key="key")
    target.get.assert_called_once_with(key="prefix!key", default=None)

    await cache.set(key="key", value="value")
    target.set.assert_called_once_with(
        key="prefix!key",
        value="value",
        exist=None,
        expire=None,
    )
    await cache.ping()
    target.ping.assert_called_once_with(message=b"PING")


async def test_add_prefix_get_many(cache: Cache, target):
    cache._backends[""] = cache._backends[""][0], (add_prefix("prefix!"),)
    await cache.get_many("key")
    target.get_many.assert_called_once_with("prefix!key")


async def test_add_prefix_delete_match(cache: Cache, target):
    cache._backends[""] = cache._backends[""][0], (add_prefix("prefix!"),)
    await cache.delete_match("key")
    target.delete_match.assert_called_once_with(pattern="prefix!key")
