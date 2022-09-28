"""Delete comments like # """
import argparse
from argparse import Namespace
from datetime import datetime


def calc_time(func):
    """Calc execution time decorator"""
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func_result = func(*args, **kwargs)
        end = datetime.now()
        print(f'Executions time: {end - start}')
        return func_result
    return wrapper


def parse_args() -> Namespace:
    """
    Parse cli arguments with argparse
    :return instance of argparse:
    """
    parser = argparse.ArgumentParser(prog='Module helps clean code with comments',
                                     usage='%(prog)s delete_comments.py --input "<filename>" [--output "<filename> '
                                           'default clean_code_out.py"]',
                                     description='Show report about racing logs')
    parser.add_argument('--input',
                        type=str,
                        help='path to file with comments',
                        required=True)
    parser.add_argument('--output',
                        type=str,
                        help='path to new file, default clean_code_out.py',
                        required=False,
                        default='clean_code_out.py')

    args = parser.parse_args()
    return args


def check_exist_file_type(filename: str) -> str | bool:
    """Check for FileNotFoundError, UnicodeDecodeError exceptions"""
    try:
        open(filename).readline()
    except FileNotFoundError as error:
        return str(error)
    except UnicodeDecodeError:
        return 'File must be text format'
    return False


def normalize_code_lines(line: str) -> str:
    """Normalize code lines include CHAR_TO_DELETE"""
    if line.strip().startswith(CHAR_TO_DELETE):
        return ''

    if CHAR_TO_DELETE in line:
        char_index = line.index(CHAR_TO_DELETE)
        line = line[:char_index] + '\n'
    return line


def read_code_from_file(filename: str) -> list[str]:
    """Read code from file"""
    normalized_code = []
    with open(filename) as code_file:
        for line in code_file:
            normalized_line = normalize_code_lines(line)
            if normalized_line:
                normalized_code.append(normalized_line)
    return normalized_code


def write_code_to_file(filename: str, codes):
    """Write code from file"""
    with open(filename, 'w') as code_file:
        for line in codes:
            code_file.write(line)
    return True


@calc_time
def main(filename_input: str, filename_output: str) -> None:
    """Main controller"""
    check = check_exist_file_type(filename_input)
    if check:
        print(check)
        exit()
    code = read_code_from_file(filename_input)
    if write_code_to_file(filename_output, code):
        print(f'Normalized code from {filename_input} to {filename_output}')


CHAR_TO_DELETE = '#'

if __name__ == '__main__':
    # input_code = 'example_code.py'
    # output_code = 'example_code_out.py'
    # input_image = 'tables.png'

    cli_args = parse_args()
    input_code = cli_args.input
    output_code = cli_args.output

    main(input_code, output_code)
