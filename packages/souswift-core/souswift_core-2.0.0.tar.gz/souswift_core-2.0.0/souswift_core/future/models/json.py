from typing import Any

import orjson

from souswift_core.future.models import serializer

loads = orjson.loads


def dumps(v: Any, *, default=None):
    return orjson.dumps(v, default=default or serializer.serializer)
