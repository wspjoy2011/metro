"""Chessboard module"""

import string
from typing import Any


def make_chessboard(size: int) -> dict[str, int]:
    """Make chessboard structure data"""
    letters = string.ascii_lowercase[:size]
    digits = range(1, size + 1)
    chessboard = {}
    color = 0
    line_start_color = 0

    for letter in letters:
        for digit in digits:
            cell = letter + str(digit)
            color = 1 if line_start_color % 2 == 0 else 0
            chessboard[cell] = color
            line_start_color += 1
        line_start_color = 0 if color else 1

    return chessboard


def check_data_type(data: Any) -> None:
    """Check data type, raise TypeError if data not str"""
    if not isinstance(data, str):
        raise TypeError(f'Invalid data type: {type(data)}')


def check_chessboard_size(size: int) -> None:
    """Check size of chessboard max value 26,
    if size more than 25 raise ValueError"""
    if size >= len(string.ascii_lowercase):
        raise ValueError(f"Max size must be less the {len(string.ascii_lowercase)}")


def check_cell(data: dict[str, int], cell) -> None:
    """Check cell of chessboard, if cell not exist raise ValueError"""
    if cell not in data:
        raise ValueError(f'Cell not found in chessboard {cell}')


def find_cell_color(data: dict[str, int], cell: str) -> str:
    """Find cell color in chessboard
    :return 'black' if cell contains 1 else white:
    """
    return 'black' if data[cell] else 'white'


def main(cell='a1', size: int = 8) -> str:
    """Main controller of module chessboard"""
    check_data_type(cell)
    check_chessboard_size(size)

    chessboard = make_chessboard(size)

    check_cell(chessboard, cell)

    cell_color = find_cell_color(chessboard, cell)
    return cell_color


if __name__ == '__main__':
    user_cell = 'e5'

    try:
        print(main(cell=user_cell, size=8))
    except (ValueError, TypeError) as error:
        print(error)
