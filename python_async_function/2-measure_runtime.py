#!/usr/bin/env python3
"""Task 1 """
import asyncio
from typing import List
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ returns total_time / n """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    elapsed = end_time - start_time
    return elapsed / n
