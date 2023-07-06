#!/usr/bin/env python3
"""
Type-annotated function to_kv
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Accepts a string and a integer or float
    as argumetns and returns a tuple.
    First element of tuple is k.
    Second element is square of int/float v
    with is annotated as a float.
    """
    return (k, v ** 2)
