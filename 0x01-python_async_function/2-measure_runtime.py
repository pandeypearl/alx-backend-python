#!/usr/bin/env python3
""" async routine measure_time """

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Takes two arguments measuring total execution
    time for wait_n and returns total_time
    """
    t = time.time()
    asyncio.run(wait_n(n, max_delay))
    return ((time.time() - t) / n)
