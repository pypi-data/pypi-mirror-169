#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-06-18 09:37:54
# @Author  : Chenghao Mou (mouchenghao@gmail.com)
from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List
from typing import Tuple

from redis import Redis

from text_dedup.utils.storage.base import StorageDict


class RedisDict(StorageDict):
    """
    A dictionary-like object backed by Redis.

    Parameters
    ----------
    storage_config : Dict[str, Any]
        Storage configuration.

    Examples
    --------
    >>> import redis
    >>> from text_dedup.utils.storage.redis_dict import RedisDict
    >>> def test_func():
    ...     try:
    ...         d = RedisDict(
    ...             storage_config={
    ...                 "type": "redis",
    ...                 "prefix": "temp",
    ...                 "redis": {"host": "localhost", "port": 6379, "decode_responses": True},
    ...             },
    ...         )
    ...         d.clear()
    ...         d.add((123, 234), (0, 213123124))
    ...         d.add((123, 234), (1, 213123124))
    ...     except redis.exceptions.ConnectionError as e:
    ...         d = {(123, 234): [(0, 213123124), (1, 213123124)]}
    ...     return sorted(d[(123, 234)])
    >>> test_func()
    [(0, 213123124), (1, 213123124)]
    """

    def __init__(self, storage_config: Dict[str, Any]):
        if storage_config.get("type", "redis") != "redis":
            raise ValueError("Only redis is supported")

        self.basename = storage_config.pop("basename", "redis_dict")

        if "decode_responses" not in storage_config["redis"] or not storage_config["redis"]["decode_responses"]:
            storage_config["redis"]["decode_responses"] = True

        self.redis = Redis(**storage_config["redis"])

    def add(self, key: str | Tuple[int, int], value: str | Tuple[int, int]):
        if isinstance(key, tuple):
            key = "#".join(map(str, key))
        key = f"{self.basename}:{key}"
        if isinstance(value, tuple):
            value = "#".join(map(str, value))
        self.redis.sadd(key, value)

    def __len__(self):
        return sum(1 for _ in self.redis.scan_iter(f"{self.basename}:*"))

    def __iter__(self):
        for key in self.redis.scan_iter(f"{self.basename}:*"):
            yield key.split(":", 1)[-1]

    def __getitem__(self, key: str | Tuple[int, int]) -> List[Tuple[int, ...]]:
        if isinstance(key, tuple):
            key = "#".join(map(str, key))
        key = f"{self.basename}:{key}"

        results: List[Tuple[int, ...]] = []
        for record in self.redis.smembers(key):
            results.append(tuple(map(int, record.split("#"))))

        return results

    def clear(self):
        for k in self:
            self.redis.delete(f"{self.basename}:{k}")
