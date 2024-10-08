#!/usr/bin/env python3
"""
Class to print values from given csv file
"""
import csv
import math
from typing import List
from typing import Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    initialized index_range func
    """
    starting = (page - 1) * page_size
    ending = starting + page_size
    res = (starting, ending)
    return res


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        method 2 fetch page data
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset_len = len(self.dataset())
        starting, ending = index_range(page, page_size)

        if starting >= dataset_len:
            return []

        return self.dataset()[starting:ending]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Method 2 fetch more data per request
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.get_page(page, page_size)
        totalpages = len(data) / page_size
        totalpages = math.ceil(totalpages)
        hyper_data = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < totalpages else None,
            "prev_page": page + 1 if page > 1 else None,
            "total_pages": totalpages
        }
        return hyper_data
