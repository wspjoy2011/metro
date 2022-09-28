from random import choice, shuffle, randint


def generate_password_from_file(text):
    letters = list(choice(text) + choice(text))
    shuffle(letters)
    letters_diff_case = ''.join(map(lambda x: x.upper() if choice((0, 1)) else x, letters))
    password = {letters_diff_case: len(letters_diff_case)}
    return password
