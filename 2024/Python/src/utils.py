from functools import wraps
from time import perf_counter
from typing import Any, Callable


def benchmark(label: str) -> Callable[[Callable[..., Any]], Callable[..., None]]:
    def func_wrapper(f: Callable[..., Any]) -> Callable[..., None]:
        @wraps(f)
        def wrapper(*args: Any, **kwargs: Any) -> None:
            start_time = perf_counter()
            f(*args, **kwargs)
            stop_time = perf_counter()
            print(label, f"{(stop_time - start_time) * 100:.2f}ms")

        return wrapper

    return func_wrapper
