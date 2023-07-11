#!/usr/bin/env python3
""" coroutine async_generator """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine will loop 10 times.
    Each time async wait 1 second.
    Then yield random number between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
