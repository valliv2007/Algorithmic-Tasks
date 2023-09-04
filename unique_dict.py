from collections import defaultdict
from typing import List


def del_dublicate(list_dicts: List) -> List:
    dict_dicts = defaultdict(int)
    result = []
    for item in list_dicts:
        dict_dicts[frozenset(item.keys())] += 1
        if dict_dicts[frozenset(item.keys())] == 1:
            result.append(item)
    return result
