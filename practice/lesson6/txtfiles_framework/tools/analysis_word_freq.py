from collections import Counter


def check_frequency_analysis_words(text: list[str]) -> dict[str: int]:
    qty_words = Counter(text)
    qty_words_sort = dict(sorted(qty_words.items(), key=lambda item: item[1], reverse=True))
    return qty_words_sort
