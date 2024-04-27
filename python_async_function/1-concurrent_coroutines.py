#!/usr/bin/env python3
"""Task 1 """
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """ waits for a random delay and return it """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delay = await asyncio.gather(*tasks)
    return sorted(delay)
