""""""
from prettytable import PrettyTable
from random import randint


def throws(number_of_shots: int = 1000):
    """"""
    throw_result = []
    for number_shots in range(0, number_of_shots):
        cube1 = randint(1, 6)
        cube2 = randint(1, 6)
        throw_result.append(cube1 + cube2)
    return throw_result


def throw_statics(throw_result: list[int]):
    statistics = {}
    for number_cube in range(2, 13):
        interest = throw_result.count(number_cube) / len(throw_result) * 100
        static = {number_cube: interest}
        statistics.update(static)
    return statistics


def print_table(data):
    static = [0, 0, 2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]
    table = PrettyTable()
    table.field_names = ['faces of Cuba', 'result', 'Expect a result', 'difference']
    for key, qty in data.items():
        table.add_row([key, round(qty, 2), static[key], round(abs(qty - static[key]), 2)])
    print(table)


def main():
    """Main controller"""
    throw = throws()
    statics = throw_statics(throw)
    print_table(statics)


if __name__ == '__main__':
    main()
