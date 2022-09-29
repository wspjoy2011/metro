"""Show statistics about baby names"""
import os
import configparser
from pathlib import Path

import baby_names_statistics

from baby_names_statistics.handlers.error_handler import check_folder_exist
from baby_names_statistics.handlers.file_handler import get_list_of_files, read_data_from_file
from baby_names_statistics.handlers.normalize_handler import filter_files_names, parse_year_group
from baby_names_statistics.tools.most_least_common import find_most_least_names, find_most_least_names_in_range
from baby_names_statistics.tools.print_statistics import print_table
from baby_names_statistics.tools.write_to_json import write_to_json


def make_names_table(filtered_files: list[str], folder: str):
    """Make dict format [gender][year][name][number_of_names]"""
    names_table = {
        'girls': {},
        'boys': {}
    }
    for file in filtered_files:
        path = os.path.join(folder, file)
        names = read_data_from_file(path)
        year, gender = parse_year_group(file)
        names_table[gender][year] = names
    return names_table


def main(folder: str) -> None:
    """Main controller"""
    if not check_folder_exist(folder):
        print('Incorrect folder')
        exit()

    files = get_list_of_files(folder)
    filtered_files = filter_files_names(files)
    names_table = make_names_table(filtered_files, folder)
    boys_names, girls_names = find_most_least_names(names_table)

    json_format = {
        'boys': boys_names,
        'girls': girls_names
    }
    package_dir = Path(baby_names_statistics.__file__).parent
    path_to_config = os.path.join(package_dir, 'config.ini')
    config = configparser.ConfigParser()
    config.read(path_to_config)
    ban_names = config['ban-names']['name'].split(', ')
    print(ban_names)
    # range_names_boys = find_most_least_names_in_range(boys_names, 1900, 2000)
    # print_table(range_names_boys, 'boys')
    # write_to_json(json_format)
    print_table(boys_names, 'boys', ban_names)
    # print_table(girls_names, 'girls')


if __name__ == '__main__':
    current_dir = os.getcwd()
    folder_path = os.path.join('baby_names_statistics', 'baby_names')
    main(folder_path)
