# =======================================================================================
# Задание №4
#
# Условие:
#
# Написать функцию, которая сортирует список, но все четные числа должны остаться на своем месте.
#
# Примеры:
#
# sort_array([3, 1]) -> [1, 3]
# sort_array([3, 2, -1, 4]) -> [-1, 2, 3, 4]
# sort_array([5, 3, 2, 8, 1, 4]) -> [1, 3, 2, 8, 5, 4]

def validate_data_type(data: list[int]) -> bool:
    """
        Data type must be list[int]
    :param data:
    :return:
    """
    if not isinstance(data, list):
        return False

    len_numbers = len([number for number in data if isinstance(number, int)])
    return len_numbers == len(data)


def sort_only_odd_numbers(numbers: list[int]) -> list[int] | str:
    """
        Sort only odd numbers
    :param numbers:
    :return numbers:
    """
    if not validate_data_type(numbers):
        return f'Data type must be list[int], not {numbers}'

    odd_sorted = sorted([number for number in numbers if number % 2 != 0])
    pointer = 0

    for i, number in enumerate(numbers):
        if number % 2 != 0:
            numbers[i] = odd_sorted[pointer]
            pointer += 1

    return numbers


if __name__ == '__main__':

    arr1 = [3, 1]
    arr1_answer = [1, 3]

    arr2 = [3, 2, -1, 4]
    arr2_answer = [-1, 2, 3, 4]

    arr3 = [5, 3, 2, 8, 1, 4]
    arr3_answer = [1, 3, 2, 8, 5, 4]

    wrong_numbers = [1, 3, 2, 8, None, 5, 4]
    wrong_numbers_answer = 'Data type must be list[int], not [1, 3, 2, 8, None, 5, 4]'

    wrong_data_type = None
    wrong_data_type_answer = 'Data type must be list[int], not None'

    # Tests

    assert sort_only_odd_numbers(arr1) == arr1_answer
    print('#' * 25)
    print(f'Test Sort 1 {arr1} == {arr1_answer}')

    assert sort_only_odd_numbers(arr2) == arr2_answer
    print('#' * 25)
    print(f'Test Sort 2 {arr2} == {arr2_answer}')

    assert sort_only_odd_numbers(arr3) == arr3_answer
    print('#' * 25)
    print(f'Test Sort 3 {arr3} == {arr3_answer}')

    assert sort_only_odd_numbers(wrong_numbers) == wrong_numbers_answer
    print('#' * 25)
    print(f'Test Sort wrong numbers {wrong_numbers} == {wrong_numbers_answer}')

    assert sort_only_odd_numbers(wrong_data_type) == wrong_data_type_answer
    print('#' * 25)
    print(f'Test Sort wrong data type {wrong_data_type} == {wrong_data_type_answer}')

    print('#' * 25)
    print('All tests passed')
