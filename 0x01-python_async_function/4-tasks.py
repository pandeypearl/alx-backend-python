#!/usr/bin/env python3
""" Async routine task_wait_n """

import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Accepts two int arguments. Will spawn wait_random
    n times with specified max_delay.
    """
    functs = [
        task_wait_random(max_delay) for i in range(n)
    ]
    results = []
    for x in asyncio.as_completed(functs):
        result = await x
        results.append(result)
    return results
