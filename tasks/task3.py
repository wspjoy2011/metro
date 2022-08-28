# =======================================================================================
# Задание №3
#
# Условие:
#
# Написать функцию, которая проверяет, являются ли две строки анаграммами?
# На вход идут две строки, состоящие из символов английского алфавита.
#
# Примеры:
#
# is_anagram('car', 'tar') -> False
# is_anagram('car', 'cart') -> False
# is_anagram('anagram', 'nagaram') -> True
# is_anagram('beluga', 'begula') -> True

from collections import namedtuple


def validate_data_type(data: tuple) -> bool:
    """
        Check data type of words. Must be (str, str)
    :param data:
    :return bool:
    """
    return isinstance(data[0], str) and isinstance(data[1], str)


def is_anagram(word1: str, word2: str) -> bool:
    """
        Check is words are anagram
    :param word1:
    :param word2:
    :return bool:
    """

    if not validate_data_type((word1, word2)):
        return False

    return sorted(word1) == sorted(word2)


if __name__ == '__main__':
    Words = namedtuple('Words', ['first', 'second'])

    words1 = Words('car', 'tar')
    words1_answer = False

    words2 = Words('car', 'cart')
    words2_answer = False

    words3 = Words('anagram', 'nagaram')
    words3_answer = True

    words4 = Words('beluga', 'begula')
    words4_answer = True

    empty_string = Words('', '')
    empty_string_answer = True

    wrong_data_type = Words(None, list)
    wrong_data_type_answer = False

    # Tests

    assert is_anagram(words1.first, words1.second) == words1_answer
    print('#' * 25)
    print(f'Test Anagram 1 {words1} == {words1_answer}')

    assert is_anagram(words2.first, words2.second) == words2_answer
    print('#' * 25)
    print(f'Test Anagram 2 {words2} == {words2_answer}')

    assert is_anagram(words3.first, words3.second) == words3_answer
    print('#' * 25)
    print(f'Test Anagram 3 {words3} == {words3_answer}')

    assert is_anagram(words4.first, words4.second) == words4_answer
    print('#' * 25)
    print(f'Test Anagram 4 {words4} == {words4_answer}')

    assert is_anagram(empty_string.first, empty_string.second) == empty_string_answer
    print('#' * 25)
    print(f'Test Anagram empty string {empty_string} == {empty_string_answer}')

    assert is_anagram(empty_string.first, empty_string.second) == empty_string_answer
    print('#' * 25)
    print(f'Test Anagram wrong data type {wrong_data_type} == {wrong_data_type_answer}')

    print('#' * 25)
    print('All tests passed')
