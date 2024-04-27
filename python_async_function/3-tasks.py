#!/usr/bin/env python3
"""Task 3 """
import asyncio
from typing import List
import time

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ returns a asyncio.Task """
    return asyncio.create_task(wait_random(max_delay))
