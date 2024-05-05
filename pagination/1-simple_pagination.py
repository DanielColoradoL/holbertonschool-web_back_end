#!/usr/bin/env python3
""" task 1 """
import csv
from typing import List


def index_range(page, page_size):
    """
    Return a tuple of size two
    containing a start index and an end index
    """
    start = page * page_size - page_size
    finish = page * page_size
    return (start, finish)


class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return small dataset out of dataset
        based on page and page size
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        list_index = index_range(page, page_size)
        return self.__dataset[list_index[0]: list_index[1]]
