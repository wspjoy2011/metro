# =======================================================================================
# Задание №2
#
# Условие:
#
# Написать функцию, которая сортирует список с оценками на основе английской системы.
# Всего 5 символов, в порядке убывания: A, B, C, D, F.
#
# Примеры:
#
# sort_grades(['A', 'B', 'C', 'C', 'F', 'A']) -> ['F', 'C', 'C', 'B', 'A', 'A']
# sort_grades(['b', 'c', 'C', 'f', 'A']) -> ['F', 'C', 'C', 'B', 'A']
# sort_grades([]) -> []


def validate_grades_type(data: list[str]) -> bool:
    """
        Validate data type, data must be list
    :param data:
    :return bool:
    """
    if not isinstance(data, list):
        return False
    return True


def validate_grades(data: list[str]) -> bool:
    """
        Validate grades must be "F D C B A"
    :param data:
    :return bool:
    """
    grades = 'FDCBA'
    result = [grade for grade in data if grade.upper() not in grades]
    if result:
        return False
    return True


def normalize_grades(data: list[str]) -> list[str]:
    """
        Normalize grades to upper case
    :param data:
    :return list[str]:
    """
    return [grade.upper() for grade in data]


def sort_grades(grades: list[str]) -> list[str] | str:
    """
        Sort grades in USA style
    :param grades:
    :return result:
    """
    if not validate_grades_type(grades):
        return 'Data type must be list'

    if not validate_grades(grades):
        return 'Data into list must be only "F D C B A"'

    grades = normalize_grades(grades)
    result = []
    grades_qty = {
        'F': 0,
        'D': 0,
        'C': 0,
        'B': 0,
        'A': 0
    }

    for grade in grades:
        grades_qty[grade] += 1

    for grade, qty in grades_qty.items():
        result += [grade for _ in range(qty)]

    return result


if __name__ == '__main__':

    grades1 = ['A', 'B', 'C', 'C', 'F', 'A']
    grades1_answer = ['F', 'C', 'C', 'B', 'A', 'A']

    grades_different_case = ['b', 'c', 'C', 'f', 'A']
    grades_different_case_answer = ['F', 'C', 'C', 'B', 'A']

    empty_grades = []
    empty_grades_answer = []

    wrong_data_type = None
    wrong_data_type_answer = 'Data type must be list'

    wrong_grades = ['F', 'D', 'Z']
    wrong_grades_answer = 'Data into list must be only "F D C B A"'

    # Tests

    assert sort_grades(grades1) == grades1_answer
    print('#' * 25)
    print(f'Test Grades {str(grades1)} == {grades1_answer}')

    assert sort_grades(grades_different_case) == grades_different_case_answer
    print('#' * 25)
    print(f'Test Grades different cases {str(grades_different_case)} == {grades_different_case_answer}')

    assert sort_grades(empty_grades) == empty_grades_answer
    print('#' * 25)
    print(f'Test Empty list {str(empty_grades)} == {empty_grades_answer}')

    assert sort_grades(wrong_data_type) == wrong_data_type_answer
    print('#' * 25)
    print(f'Test Wrong type of data {str(wrong_data_type)} == {wrong_data_type_answer}')

    assert sort_grades(wrong_grades) == wrong_grades_answer
    print('#' * 25)
    print(f'Test Wrong grades {str(wrong_grades)} == {wrong_grades_answer}')

    print('#' * 25)
    print('All tests passed')