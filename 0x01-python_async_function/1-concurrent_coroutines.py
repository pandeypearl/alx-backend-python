#!/usr/bin/env python3
""" Async routine wait_n """

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Accepts two int arguments: max_delay, n.
    Will spawn wait_random n times with specified max_delay.
    """
    functs = [
            wait_random(max_delay) for i in range(n)
    ]
    results = []
    for x in asyncio.as_completed(functs):
        result = await x
        results.append(result)
    return results
