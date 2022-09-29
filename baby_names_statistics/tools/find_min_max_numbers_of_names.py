"""Find minimum and maximum of names numbers"""


def find_min_max_names(names):
    """Find minimum and maximum of names numbers"""
    most = []
    least = []
    for yaer, name in names.items():
        most.append((name[0][1], name[0][0], yaer))
        least.append((name[1][1], name[1][0], yaer))
    most.sort()
    least.sort()
    return least[0], most[-1]
