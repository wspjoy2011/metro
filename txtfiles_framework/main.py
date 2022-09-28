import os

from tools.most_freq_word import get_most_freq_words as freq_words
from tools.most_len_word import get_most_len_words as len_words
from tools.analysis_letter_freq import check_frequency_analysis_letters
from tools.analysis_word_freq import check_frequency_analysis_words
from tools.pass_gen import generate_password_from_file
from tools.show_table import make_pretty_table

from handler.file_handler import read_data_from_file
from handler.error_handler import check_errors


def print_logo():
    """Print logo"""
    logo = """
#######                                                                      
#       # #      ######      ##   #    #   ##   #      #  ####  #   #  ####  
#       # #      #          #  #  ##   #  #  #  #      # #       # #  #      
#####   # #      #####     #    # # #  # #    # #      #  ####    #    ####  
#       # #      #         ###### #  # # ###### #      #      #   #        # 
#       # #      #         #    # #   ## #    # #      # #    #   #   #    # 
#       # ###### ######    #    # #    # #    # ###### #  ####    #    ####  
    """
    print(logo + '\n')


def main(filename: str, func):
    """Main controller"""
    if check_errors(filename):
        return check_errors(filename)
    data = read_data_from_file(filename)
    qty_words = func(data)
    result_table = make_pretty_table(qty_words, func.__name__)
    return result_table


def menu():
    """User menu"""
    print_logo()
    while True:
        filename = input('Enter path to file: ')
        try:
            open(filename, 'r')
            break
        except (FileNotFoundError, UnicodeDecodeError) as error:
            print(error)

    while True:
        print("Choose a menu item: ")
        print("""
        1 - 'longest'
        2 - 'frequent'
        3 - 'analysis_letters'
        4 - 'analysis_words'
        5 - 'password': generate_password_from_file,
        0 - exit
        """)

        while True:
            func_name_id = input('Enter number of menu item: ')
            try:
                func_name_id = int(func_name_id)
                break
            except ValueError:
                print('Use only digits')

        if not func_name_id:
            print('Exiting for application')
            exit()

        if not 0 < func_name_id <= len(funcs_map.keys()):
            print('Incorrect menu item')
            continue

        func_keys = list(funcs_map.keys())
        func_name = func_keys[func_name_id - 1]
        func = funcs_map[func_name]
        print(f'Find the {func_name} words in {filename}')
        print(main(filename, func))
        input('Press enter to continue...')


funcs_map = {
    'longest': len_words,
    'frequent': freq_words,
    'analysis_letters': check_frequency_analysis_letters,
    'analysis_words': check_frequency_analysis_words,
    'password': generate_password_from_file,
}

if __name__ == '__main__':
    # examples\\example.txt
    menu()
