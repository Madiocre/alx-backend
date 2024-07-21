#!/usr/bin/env python3
""" Tuple Helper Function """


def index_range(page: int, page_size: int) -> tuple[int, int]:
    return (page * page_size - page_size), page * page_size
