#!/usr/bin/env python3
"""
Type-annotated element_length function
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotating parameters and return values
    with appropriate types
    """
    return [(i, len(i)) for i in lst]
