#!/usr/bin/env python3
""" Task 9 """
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Duck type the behaviour of the function"""
    return [(i, len(i)) for i in lst]
