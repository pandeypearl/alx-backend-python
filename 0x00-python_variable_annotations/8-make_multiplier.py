#!/usr/bin/env python3
"""
Type-annotated make_multiplier function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    accepts float multiplier argument and returns
    function that multiplies a float by muliplier.
    """
    def f(x):
        return x * multiplier
    return f
