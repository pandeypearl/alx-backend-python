#!/usr/bin/env python3
"""
Type-annotated zoom_array function
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Using mypy to validate code and apply necessary changes.
    """
    zoomed_in: List = [
            item for item in lst
            for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom2x = zoom_array(tuple(array))

zoom3x = zoom_array(tuple(array), int(3.0))
