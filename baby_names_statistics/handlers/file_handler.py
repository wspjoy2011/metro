"""Get data from files folder"""
import os

from baby_names_statistics.handlers.error_handler import check_file_exist, check_file_type_txt
from baby_names_statistics.handlers.normalize_handler import parse_names_qty_from_lines, parse_year_group


def get_list_of_files(folder: str):
    """Get lists of files in folder"""
    files = os.listdir(folder)
    return files


def read_data_from_file(path_to_file: str):
    """Read statistics from file"""
    if not check_file_exist(path_to_file):
        return False
    if not check_file_type_txt(path_to_file):
        return False
    names = {}
    with open(path_to_file) as file_names:
        for line in file_names:
            line = parse_names_qty_from_lines(line)
            if line:
                name = line[0]
                name_qty = line[1]
                names[name] = name_qty
    return names

