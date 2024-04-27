#!/usr/bin/env python3
"""Task 2"""
from time import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> [float]:
    """ measure the total runtime and return it """
    start_t = time()
    tasks = [async_comprehension() for _ in range(5)]
    await asyncio.gather(*tasks)
    end_t = time()
    elapsed = end_t - start_t
    return elapsed
