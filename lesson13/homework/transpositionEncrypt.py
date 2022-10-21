import pyperclip


def encrypt_message(key, message):
    ciphertext = [''] * key
    for column in range(key):
        current_index = column

        while current_index < len(message):
            ciphertext[column] += message[current_index]
            current_index += key

    return ''.join(ciphertext)


def main(message: str, key: int):
    ciphertext = encrypt_message(my_key, my_message)
    pyperclip.copy(ciphertext)
    return ciphertext


if __name__ == '__main__':
    my_message = """Augusta Ada King-Noel, Countess of Lovelace (10 December 1815 - 27 November 1852) was an English mathematician and writer, chiefly known for her work on Charles Babbage's early mechanical general-purpose computer, the Analytical Engine. Her notes on the engine include what is recognised as the first algorithm intended to be carried out by a machine. As a result, she is often regarded as the first computer programmer."""
    my_key = 13
    print(main(my_message, my_key))