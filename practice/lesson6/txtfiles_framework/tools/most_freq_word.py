from collections import Counter


def get_most_freq_words(words: list[str]) -> dict[str: int]:
    """Returns most frequent words in collection"""
    words_counter = Counter(words)
    max_qty = max(words_counter.values())
    most_freq_words = sorted([word for word, qty in words_counter.items() if qty == max_qty])
    qty_words = {word: max_qty for word in most_freq_words}
    return qty_words


