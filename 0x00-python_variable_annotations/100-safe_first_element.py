#!/usr/bin/env python3
"""
Type-annotated safe_first_element function
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Augmenting code with correct duck-typed annotations.
    """
    if lst:
        return lst[0]
    else:
        return None
