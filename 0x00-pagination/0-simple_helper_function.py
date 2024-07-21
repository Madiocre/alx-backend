#!/usr/bin/env python3
""" Tuple Helper Function """


def index_range(page: int, page_size: int) -> tuple[int, int]:
    return ((page - 1) * page_size), ((page - 1) * page_size + page_size)
