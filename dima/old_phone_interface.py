"""Encode, decode old phone message """


def make_phone_map_keys(phone_interface: dict[str, tuple[str]]):
    """Make phone map keys"""
    phone_map_keys = {}
    for key, chars in phone_interface.items():
        temp = {char: key * index for index, char in enumerate(chars, 1)}
        phone_map_keys.update(temp)
    return phone_map_keys


def check_message(phone_map_keys: dict[str, str], char: str):
    """Check code, char in PHONE_INTERFACE"""
    if char not in phone_map_keys:
        raise KeyError(f'{char} not in {phone_map_keys}')


def encode_message(phone_map_keys: dict[str, str], message: str):
    """Encode phone message"""
    encode_line = ''
    for char in message:
        char = char.upper()
        check_message(phone_map_keys, message)
        encode_line += phone_map_keys[char] + '|'
    return encode_line[:-1]


def decode_message(phone_map_keys: dict[str, str], message: str):
    """Decode phone message"""
    decode_line = ''
    message = message.split('|')
    inv_phone_map_keys = {code: char for char, code in phone_map_keys.items()}
    for code in message:
        check_message(inv_phone_map_keys, code)
        decode_line += inv_phone_map_keys[code]
    return decode_line


def main(phone_interface: dict[str, tuple[str]], message: str, encode: bool = True):
    """Main controller"""
    phone_map_keys = make_phone_map_keys(phone_interface)
    if encode:
        result = encode_message(phone_map_keys, message)
    else:
        result = decode_message(phone_map_keys, message)
    return result


PHONE_INTERFACE = {
    '1': ('.', ',', '?', '!', ':'),
    '2': ('A', 'B', 'C'),
    '3': ('D', 'E', 'F'),
    '4': ('G', 'H', 'I'),
    '5': ('J', 'K', 'L'),
    '6': ('M', 'N', 'O'),
    '7': ('P', 'Q', 'R', 'S'),
    '8': ('T', 'U', 'V'),
    '9': ('W', 'X', 'Y', 'Z'),
    '0': (' ',)
}


if __name__ == '__main__':
    test_message = 'Hello, world!'
    print(main(PHONE_INTERFACE, test_message))

    test_code = '44|33|555|555|666|11|0|9|666|777|555|3|1111'
    print(main(PHONE_INTERFACE, test_code, False))
