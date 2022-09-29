"""Handle file errors"""
import os


def check_folder_exist(folder: str):
    """Check if folder exist"""
    if not os.path.isdir(folder):
        return False
    return True


def check_file_exist(filename: str):
    """Check if file exist"""
    if not os.path.isfile(filename):
        return False
    return True


def check_file_type_txt(filename: str):
    """Check if file txt format"""
    try:
        open(filename).readline()
    except UnicodeDecodeError:
        return False
    return True
