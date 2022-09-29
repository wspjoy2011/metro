# =======================================================================================
# Задание №1
#
# Условие:
# Написать функцию, которая находит самые повторяющиеся слова в строке.
#
# Пример:
#
# simple_text('Am I want write code? Yeah! I like it') → I
# simple_text('Hi! How are you? Hi! I am okay') → Hi
# simple_text('test text test and test that again') → test


# Я так понимаю что мы ищем слова с учётом регистра?
# А если у слов одинаковое число вхождений? Я буду возвращать строку если у одного слова наибольшее число вхождений
# и список если у слов равное число вхождений и отсортированных лексикографически.


import re, os


def find_most_popular_words(text: str) -> list | str:
    """
        Find most popular words
    :param text:
    :return result:
    """

    if not isinstance(text, str):
        return 'Data type must be string'

    words = re.findall(r'\w+', text)

    if not words:
        return 'Empty string'

    unique_words = set(words)
    words_qty = {value: words.count(value) for value in unique_words}
    max_qty = max(words_qty.values())
    result = [word for word, qty in words_qty.items() if qty == max_qty]

    if len(result) == 1:
        return result.pop()

    return sorted(result)


if __name__ == '__main__':

    text1 = 'Am I want write code? Yeah! I like it'
    text1_answer = 'I'

    text2 = 'Hi! How are you? Hi! I am okay'
    text2_answer = 'Hi'

    text3 = 'test text test and test that again'
    text3_answer = 'test'

    text_with_multiple_matches = 'a a b b c'
    text_with_multiple_matches_answer = ['a', 'b']

    empty_string = ''
    empty_string_answer = 'Empty string'

    wrong_type = [1, None, 'test']
    wrong_type_answer = 'Data type must be string'

    # Tests

    assert find_most_popular_words(text1) == text1_answer
    print('#' * 25)
    print(f'Test 1 {text1} == {text1_answer}')

    assert find_most_popular_words(text2) == text2_answer
    print('#' * 25)
    print(f'Test 2 {text2} == {text2_answer}')

    assert find_most_popular_words(text3) == text3_answer
    print('#' * 25)
    print(f'Test 3 {text3} == {text3_answer}')

    assert find_most_popular_words(empty_string) == empty_string_answer
    print('#' * 25)
    print(f'Test on empty string \'\' == {empty_string_answer}')

    assert find_most_popular_words(wrong_type) == wrong_type_answer
    print('#' * 25)
    print(f'Test on wrong data type {str(wrong_type)} == {wrong_type_answer}')

    assert find_most_popular_words(text_with_multiple_matches) == text_with_multiple_matches_answer
    print('#' * 25)
    print(f'Test on text with multiple matches {text_with_multiple_matches} == {str(text_with_multiple_matches_answer)}')

    print('#' * 25)
    print('All tests passed')

