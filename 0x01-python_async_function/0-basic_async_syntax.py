#!/usr/bin/env pytho3
""" Asynchronous coroutine wait_random """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Accepts integer as argument and waits for random delay
    between 0 and max_delay seconds and eventually and
    returns it.
    """
    n = random.uniform(0, max_delay)
    await asyncio.sleep(n)
    return n
