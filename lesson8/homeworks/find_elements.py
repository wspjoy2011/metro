"""Find chemical elements"""
import re
from collections import namedtuple
from prettytable import PrettyTable


def check_type_exist(filename: str):
    """Check if file exist and has text type"""
    try:
        open(filename).readline()
    except FileNotFoundError as error:
        return str(error)
    except UnicodeDecodeError:
        return 'File must be text format'
    return False


def check_element_format(element: str):
    """Check element format like '91,Pa,Protactinium' """
    match = re.match(r'[0-9]+,([A-Z]|[A-Z][a-z]+),[A-Z][a-z]+', element)
    return True if match else False


def read_elements_from_file(filename: str):
    """Read data from text file"""
    elements = []
    with open(filename) as elements_file:
        for element in elements_file:
            element = element.strip()
            if check_element_format(element):
                proton, abbr, name = element.split(',')
                Element = namedtuple('Element', 'proton abbr name')
                element = Element(proton, abbr, name)
                elements.append(element)
    return elements


def find_element(elements: list, user_search: str):
    """Find chemical element"""
    result_element = [element for element in elements if user_search.capitalize() in element]
    return result_element if result_element else False


def print_result_table(element):
    """Print chemical element"""
    element = element.pop()
    element_table = PrettyTable()
    element_table.field_names = ['№', 'Abbr', 'Name']
    element_table.add_row([element.proton, element.abbr, element.name])
    print(element_table)


def main(filename: str, user_search):
    """Main controller"""
    check = check_type_exist(filename)
    if check:
        print(check)
        exit()

    elements = read_elements_from_file(filename)
    find_result = find_element(elements, user_search)
    if find_result:
        print_result_table(find_result)
    else:
        print(f'Element {user_search} not found')


if __name__ == '__main__':
    file = 'elements.txt'
    # user_search = '100'
    while True:
        user_search = input('Enter any element: ')
        if not user_search:
            print('Bye')
            exit()
        main(file, user_search)

