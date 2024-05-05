#!/usr/bin/env python3
"""Task 0"""


def index_range(page, page_size):
    """
    The function return a tuple of size two
    containing a start index and an end index
    corresponding to the range of indexes to return
    in a list for those particular pagination parameters.
    """
    start = page * page_size - page_size
    finish = page * page_size
    return (start, finish)
