from collections import defaultdict


def find_most_least_names(names):
    """Find the most and least common names by years"""
    girls_names = defaultdict()
    boys_names = defaultdict()

    for year in names['girls']:
        top_name = list(names['girls'][year].keys())[0]
        top_name_qty = list(names['girls'][year].values())[0]
        bottom_name = list(names['girls'][year].keys())[-1]
        bottom_name_qty = list(names['girls'][year].values())[-1]
        year = int(year)
        girls_names[year] = ((top_name, top_name_qty), (bottom_name, bottom_name_qty))

    for year in names['boys']:
        top_name = list(names['boys'][year].keys())[0]
        top_name_qty = list(names['boys'][year].values())[0]
        bottom_name = list(names['boys'][year].keys())[-1]
        bottom_name_qty = list(names['boys'][year].values())[-1]
        year = int(year)
        boys_names[year] = ((top_name, top_name_qty), (bottom_name, bottom_name_qty))

    return boys_names, girls_names


def find_most_least_names_in_range(names: dict[int: tuple[tuple[str, int]], tuple[tuple[str, int]]],
                                   start: int, stop: int):
    """Find the most and least common names by years range"""
    range_names = {}
    start = min(start, stop)
    stop = max(start, stop)
    for year, name in names.items():
        if start <= year <= stop:
            range_names[year] = name
    return range_names
