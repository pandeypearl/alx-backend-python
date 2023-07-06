#!/usr/bin/env python3
"""
Type-annonated sum_list function
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Accepts list of floats as agrument and returns
    their sum as a float.
    """
    return sum(input_list)
