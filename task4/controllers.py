from typing import Optional, Any


def operation(a: int, b: int) -> Optional[Any]:
    if (a is None) or (b is None):
        return None
    return a + b