# Transposition Cipher Encryption
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import pyperclip


def main():
    my_message = """Augusta Ada King-Noel, Countess of Lovelace (10 December 1815 - 27 November 1852) was an English mathematician and writer, chiefly known for her work on Charles Babbage's early mechanical general-purpose computer, the Analytical Engine. Her notes on the engine include what is recognised as the first algorithm intended to be carried out by a machine. As a result, she is often regarded as the first computer programmer."""
    myKey = 13
    my_message = my_message
    ciphertext = encrypt_message(myKey, my_message)

    # Print the encrypted string in ciphertext to the screen, with
    # a | ("pipe" character) after it in case there are spaces at
    # the end of the encrypted message.
    print(ciphertext + '|')

    # Copy the encrypted string in ciphertext to the clipboard.
    pyperclip.copy(ciphertext)


def encrypt_message(key, message):
    # Each string in ciphertext represents a column in the grid.
    ciphertext = [''] * key

    # Loop through each column in ciphertext.
    for column in range(key):
        current_index = column

        # Keep looping until current_index goes past the message length.
        while current_index < len(message):
            # Place the character at current_index in message at the
            # end of the current column in the ciphertext list.
            ciphertext[column] += message[current_index]

            # move current_index over
            current_index += key

    # Convert the ciphertext list into a single string value and return it.
    return ''.join(ciphertext)


# If transpositionEncrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()