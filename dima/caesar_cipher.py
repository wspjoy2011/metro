from string import ascii_lowercase, ascii_uppercase


def encode_message(message: str, shift: int):
    """Encode message Caesar cipher"""
    result = ''
    for letter in message:
        if letter in ascii_uppercase:
            index = ascii_uppercase.index(letter) + shift - len(ascii_uppercase)
            result += ascii_uppercase[index]
        else:
            result += letter
    return result


def main(message: str, shift: int, encode: bool = True):
    """Main controller"""
    if shift > len(ascii_uppercase):
        shift = shift % len(ascii_uppercase) + 1
    return encode_message(message, shift)


if __name__ == '__main__':
    test_to_encode = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'
    test_encode = 'QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD'
    print(main(test_to_encode, 230))
