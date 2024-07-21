#!/usr/bin/env python3
""" Tuple Helper Function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Calculates start index and an end index corresponding to the range """
    
    return (page * page_size - page_size), (page * page_size)
