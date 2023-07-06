#!/usr/bin/env python3
"""
Type-annotated safely_get_value function
"""
from typing import Any, Mapping, TypeVar, Union


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[TypeVar('T'), None])\
                     -> Union[Any, TypeVar('T')]:
    """
    Adding type annonations to the function
    considering the parametrs and return values.
    """
    if key in dct:
        return dct[key]
    else:
        return default
