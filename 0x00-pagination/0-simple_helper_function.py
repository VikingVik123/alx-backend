#!/usr/bin/env python3
"""
Write a function named index_range
takes two integer arguments page and page_size.
The function should return a tuple of size two
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    initialized index_range func
    """
    starting = (page - 1) * page_size
    ending = starting + page_size
    res = (starting, ending)
    return res
