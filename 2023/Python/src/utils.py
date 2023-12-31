from time import perf_counter
from typing import Callable, Any

Vec2 = tuple[int, int]
StrGrid2D = list[list[str]]
IntGrid2D = list[list[int]]


def timeit(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        stop = perf_counter()
        print(f"finished {func.__qualname__} in {stop-start:.3f}s")

    return wrapper
