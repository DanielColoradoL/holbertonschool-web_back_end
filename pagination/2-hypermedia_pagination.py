#!/usr/bin/env python3
""" task 1 """
import csv
from typing import List, Dict


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
        self.dataset()
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        list_index = index_range(page, page_size)
        return self.__dataset[list_index[0]: list_index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        returns a dictionary containing the following key-value pairs:
        page_size, page, data, next_page, prev_page, total_pages
        """
        self.dataset()

        output = {}
        output["page_size"] = page_size
        output["page"] = page

        no_pages = round(len(self.__dataset) / page_size)
        next_page = page + 1 if page <= no_pages else None
        prev_page = page - 1 if page > 0 else None

        output["total_pages"] = no_pages
        output["next_page"] = next_page
        output["prev_page"] = prev_page

        list_index = index_range(page, page_size)
        output["data"] = self.__dataset[list_index[0]: list_index[1]]

        return output
