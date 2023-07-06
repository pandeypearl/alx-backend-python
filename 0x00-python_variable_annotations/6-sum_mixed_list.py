#!/usr/bin/env python3
"""
Type-annotated sum_mixed_list function
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Accepts a list of integers and floats as argument and returns
    their sum as a float.
    """
    return sum(mxd_list)
