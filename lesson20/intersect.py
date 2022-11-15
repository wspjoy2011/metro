import itertools
from typing import Iterable, Any, Hashable


class UnhashableType(Exception):
    pass


def intersect_list_comprehension(iterable_one: Iterable[Any], iterable_second: Iterable[Any]):
    return [item for item in iterable_one if item in iterable_second]


def check_hashable_items(iterable: Iterable[Any]):
    iterable_flat = itertools.chain.from_iterable(iterable)
    try:
        [hash(item) for item in iterable_flat]
    except TypeError as error:
        raise UnhashableType(error)


def intersect_sets(iterable_one: Iterable[Hashable], iterable_second: Iterable[Hashable]):
    """Works only with hashable type"""
    check_hashable_items([item for item in (iterable_one, iterable_second)])
    return set(iterable_one) & set(iterable_second)


if __name__ == '__main__':
    items_one = [None, 1, 'bob']
    items_second = [range, 1, 100.0, TypeError]

    print(*intersect_list_comprehension(items_one, items_second))
    print(*intersect_sets(items_one, items_second))
