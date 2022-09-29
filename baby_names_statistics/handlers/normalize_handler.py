"""Normalize file lists name in directory"""
import re


def filter_files_names(files: list[str]) -> list[str]:
    """Filter file names use template year_BoysNames.txt or year_GirlsNames.txt"""
    filtered_files = []
    for file in files:
        match = re.match(r'^[1-2][0-9][0-9][0-9]_(BoysNames|GirlsNames)\.txt$', file)
        if match:
            filtered_files.append(file)
    return filtered_files


def parse_names_qty_from_lines(line) -> tuple[str, int] | bool:
    """Parse name and number of names"""
    line = line.strip()
    match_line = re.match(r'[A-Z][a-z]+\s[0-9]+', line)
    if match_line:
        name, qty = match_line.group(0).split(' ')
        return name, int(qty)
    return False


def parse_year_group(filename: str):
    """Parse name and number of names"""
    year = int(re.match(r'^[1-2][0-9][0-9][0-9]', filename).group(0))
    gender = re.search(r'Girls|Boys', filename).group(0).lower()
    return year, gender
