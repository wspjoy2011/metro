from collections import Counter


def check_frequency_analysis_letters(text):
    text = ''.join(text)
    qty_letters = Counter(text)
    return qty_letters
