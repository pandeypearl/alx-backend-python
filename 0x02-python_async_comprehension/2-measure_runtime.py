#!/usr/bin/env python3
""" Measure runtime """

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine will execute async_comprehension 4 times
    in parallel using asyncio.gather.
    mesure runtime should measure total runtime and return
    the float.
    """
    t = time.time()
    functs = [async_comprehension() for i in range(4)]
    await asyncio.gather(*functs)

    return time.time() - t
