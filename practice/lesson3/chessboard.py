import string


def make_chessboard(size=8):
    """Make chessboard structure data"""
    if size >= len(string.ascii_lowercase):
        raise ValueError(f"Max size must be less the {len(string.ascii_lowercase)}")

    letters = string.ascii_lowercase[:size]
    chessboard = {}
    color = 0
    counter = 0

    for letter in letters:
        for number in range(1, size + 1):
            cell = letter + str(number)
            color = 1 if counter % 2 == 0 else 0
            chessboard[cell] = color
            counter += 1
        counter = 0 if color else 1

    return chessboard


def check_data_type(data):
    if not isinstance(data, str):
        raise TypeError(f'Invalid data type: {type(data)}')
    return


def check_cell(data, cell):
    if cell not in data:
        raise ValueError(f'Cell not found in chessboard {cell}')


def find_cell_color(data, cell):
    if data[cell]:
        return 'black'
    return 'white'


def main(cell='a1'):
    chessboard = make_chessboard()

    check_data_type(cell)
    check_cell(chessboard, cell)

    cell_color = find_cell_color(chessboard, cell)
    return cell_color


if __name__ == '__main__':
    user_cell = 'b100'

    try:
        print(main(cell=user_cell))
    except (ValueError, TypeError) as error:
        print(error)
