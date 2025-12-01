from __future__ import annotations

from functools import wraps
from time import perf_counter
from typing import Any, Callable, NamedTuple


class Vec2(NamedTuple):
    x: int
    y: int

    def __add__(self, other: tuple[int, int] | Vec2 | int) -> Vec2:  # type: ignore
        if isinstance(other, Vec2):
            return Vec2(self.x + other.x, self.y + other.y)
        if isinstance(other, tuple):
            return Vec2(self.x + other[0], self.y + other[1])

        return Vec2(self.x + other, self.y + other)

    def __mul__(self, other: tuple[int, int] | Vec2 | int) -> Vec2:  # type: ignore
        if isinstance(other, Vec2):
            return Vec2(self.x * other.x, self.y * other.y)
        if isinstance(other, tuple):
            return Vec2(self.x * other[0], self.y * other[1])

        return Vec2(self.x * other, self.y * other)

    def __sub__(self, other: tuple[int, int] | Vec2 | int) -> Vec2:
        if isinstance(other, Vec2):
            return Vec2(self.x - other.x, self.y - other.y)
        if isinstance(other, tuple):
            return Vec2(self.x - other[0], self.y - other[1])

        return Vec2(self.x - other, self.y - other)

    def __eq__(self, other: tuple[int, int] | Vec2) -> bool:  # type: ignore
        if isinstance(other, Vec2):
            return self.x == other.x and self.y == other.y

        return self.x == other[0] and self.y == other[1]

    def invert(self) -> Vec2:
        return self * -1

    def __hash__(self) -> int:
        return hash((self.x, self.y))


def benchmark(f: Callable[..., Any]) -> Callable[..., None]:
    @wraps(f)
    def wrapper(*args: Any, **kwargs: Any) -> None:
        start_time = perf_counter()
        res = f(*args, **kwargs)
        stop_time = perf_counter()
        print(f"{f.__name__}: executed in {(stop_time - start_time) * 100:.2f}ms")
        return res

    return wrapper
