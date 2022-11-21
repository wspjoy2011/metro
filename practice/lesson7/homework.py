import os


def longest_words(filename):
    all_words = []
    with open(filename) as file:
        counter = 1
        for line in file:
            line = line.strip()
            if line:
                all_words.append(f'{counter}: {line}\n')
                counter += 1
    longest_words = []
    max_len_word = 0
    for word in all_words:
        if len(word) > max_len_word:
            max_len_word = len(word)
    for word in all_words:
        if len(word) == max_len_word:
            all_words.append(word)
    print(max_len_word, longest_words)


print(__name__)
if __name__ == '__main__':
    current_dir = os.getcwd()
    path_to_file = os.path.join(current_dir, 'example.txt')
    longest_words(path_to_file)
