# =======================================================================================
# Задание №5
#
# Условие:
#
# Написать функцию которая, будет переводить римские символы в привычную нам десятичную систему.
#
# Пример:
#
# roman_to_int('XXI') -> 21
# roman_to_int('IV') -> 4
# roman_to_int('I') -> 1

ROMAN_MAP = (
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1)
)


def check_int_data_type(data) -> bool:
    """
    Check datatype Integer
    :param data:
    :return bool:
    """
    if not isinstance(data, int):
        return False
    return True


def check_str_data_type(data) -> bool:
    """
    Check datatype String
    :param data:
    :return bool:
    """
    if not isinstance(data, str):
        return False
    return True


def check_roman_numbers(data: str) -> bool:
    """
    Check roman numbers in string
    :param data:
    :return:
    """
    roman_nums = 'IVXCDM'
    check = [char for char in data if char not in roman_nums]
    return False if check else True


def convert_int_to_roman(n: int) -> str:
    """
        Convert integer numbers into roman
    :param n:
    :return result:
    """
    if not check_int_data_type(n):
        return 'Data type must be integer'

    result = ""
    for numeral, integer in ROMAN_MAP:
        while n >= integer:
            result += numeral
            n -= integer
    return result


def convert_roman_to_int(s: str) -> int | str:
    """
        Convert roman to integer
    :param s:
    :return:
    """
    if not check_str_data_type(s):
        return 'Data type must be string'

    if not check_roman_numbers(s):
        return 'String must contains only IVXCDM'

    result = 0
    index = 0
    for numeral, integer in ROMAN_MAP:
        while s[index:index + len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result


if __name__ == '__main__':
    roman1 = 'I'
    integer1 = 1

    roman4 = 'IV'
    integer4 = 4

    roman21 = 'XXI'
    integer21 = 21

    wrong_data_type = None

    wrong_data_type_int_answer = 'Data type must be integer'
    wrong_data_type_roman_answer = 'Data type must be string'

    wrong_roman_number = 'IVXCDMR'
    wrong_roman_number_answer = 'String must contains only IVXCDM'

    test1_roman = convert_int_to_roman(integer1)
    assert test1_roman == roman1
    print('#' * 25)
    print(f'Test 1 convert integer {integer1} to roman {test1_roman}')

    test1_integer = convert_roman_to_int(roman1)
    assert test1_integer == integer1
    print('#' * 25)
    print(f'Test 2 convert roman {roman1} to roman {test1_integer}')

    test4_roman = convert_int_to_roman(integer4)
    assert test4_roman == roman4
    print('#' * 25)
    print(f'Test 3 convert integer {integer4} to roman {test4_roman}')

    test4_integer = convert_roman_to_int(roman4)
    assert test4_integer == integer4
    print('#' * 25)
    print(f'Test 4 convert roman {roman4} to roman {test4_integer}')

    test21_roman = convert_int_to_roman(integer21)
    assert test21_roman == roman21
    print('#' * 25)
    print(f'Test 5 convert integer {integer21} to roman {test21_roman}')

    test21_integer = convert_roman_to_int(roman21)
    assert test21_integer == integer21
    print('#' * 25)
    print(f'Test 6 convert roman {roman21} to roman {test21_integer}')

    assert convert_int_to_roman(wrong_data_type) == wrong_data_type_int_answer
    print('#' * 25)
    print(f'Test 7 wrong data type for convert_int_to_roman {wrong_data_type} == {wrong_data_type_int_answer}')

    assert convert_roman_to_int(wrong_data_type) == wrong_data_type_roman_answer
    print('#' * 25)
    print(f'Test 8 wrong data type for convert_roman_to_integer {wrong_data_type} == {wrong_data_type_roman_answer}')

    assert convert_roman_to_int(wrong_roman_number) == wrong_roman_number_answer
    print('#' * 25)
    print(f'Test 9 wrong roman number {wrong_roman_number} == {wrong_roman_number}')

    print('#' * 25)
    print('All tests passed')
