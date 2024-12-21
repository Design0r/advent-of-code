from functools import wraps
from time import perf_counter
from typing import Any, Callable


def benchmark(f: Callable[..., Any]) -> Callable[..., None]:
    @wraps(f)
    def wrapper(*args: Any, **kwargs: Any) -> None:
        start_time = perf_counter()
        res = f(*args, **kwargs)
        stop_time = perf_counter()
        print(f"{f.__name__}: executed in {(stop_time - start_time) * 100:.2f}ms")
        return res

    return wrapper
