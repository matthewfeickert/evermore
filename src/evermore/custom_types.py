from collections.abc import Callable
from typing import Any

import jaxtyping

AddOrMul = Callable[[jaxtyping.ArrayLike, jaxtyping.ArrayLike], jaxtyping.Array]


class Sentinel:
    __slots__ = ("repr",)

    def __init__(self, repr: str) -> None:
        self.repr = repr

    def __repr__(self) -> str:
        return self.repr

    __str__ = __repr__


_NoValue: Any = Sentinel("<NoValue>")
