import re
import os
from prettytable import PrettyTable
from pathlib import Path
from collections import Counter

import examples


def check_type_exist(filename: str):
    """Check if file exist and has text type"""
    try:
        open(filename).readline()
    except FileNotFoundError as error:
        return str(error)
    except UnicodeDecodeError:
        return 'File must be text type'
    return False


def read_text_from_file(filename: str):
    """Read data from txt file"""
    words = []
    letters = []
    with open(filename) as txt_file:
        for line in txt_file:
            line = line.strip()
            if line:
                temp = re.findall(r'\w+', line)
                temp = [word.lower() for word in temp]
                words += temp
                letters += [letter for letter in ''.join(temp)]
    return words, letters


def count_sort_collection_elements(data: list[str], reverse=True):
    """Count collection elements"""
    counter = Counter(data)
    counter_order = dict(sorted(counter.items(), key=lambda words_qty: words_qty[1], reverse=reverse))
    return counter_order


def print_result_table(data: dict[str, int], title: str):
    """Print most length words"""
    result_table = PrettyTable()
    result_table.field_names = [title.title(), 'Frequency']
    for key, qty in data.items():
        result_table.add_row([key, qty])
    print(result_table)


def main(filename: str):
    check = check_type_exist(filename)
    if check:
        print(check)
        exit()
    words, letters = read_text_from_file(filename)
    words_qty = count_sort_collection_elements(words, False)
    letters_qty = count_sort_collection_elements(letters)
    print_result_table(words_qty, 'words')
    print_result_table(letters_qty, 'letters')


def get_path():
    """Get emails path"""
    folder = str(Path(examples.__file__).parent.absolute())
    file = 'test.txt'
    path = os.path.join(folder, file)
    return path


if __name__ == '__main__':
    main(get_path())
    print(abs(-1))
