import re
from functools import lru_cache


@lru_cache(maxsize=100)
def exclude_words(word: str) -> bool:
    """Check if word in ban list"""
    ban_list = {'and', 'the', 'whom', 'this', 'for', 'with', 'from'}
    return word not in ban_list


@lru_cache(maxsize=100)
def normalize_rows(line: str):
    """Normalize rows from user txt file"""
    match = re.findall(r'\w{3,}', line)
    match_lower = map(str.lower, match)
    match_nums_filter = filter(str.isalpha, match_lower)
    match_words_filter = filter(exclude_words, match_nums_filter)
    return list(match_words_filter)


def read_data_from_file(filename: str) -> list[str]:
    """Read data from txt files"""
    result = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                normalize_line = normalize_rows(line)
                result.extend(normalize_line)
    return result
