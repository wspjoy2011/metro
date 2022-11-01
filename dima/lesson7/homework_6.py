MORSE_UPPER = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.'
}


def encode(string: str):
    """decode string"""
    result_encode = ''
    for badge in string:
        if badge in MORSE_UPPER:
            result_encode += MORSE_UPPER[badge] + '|'
    return result_encode[:-1]


def decode(string: str):
    """encode string"""
    revers_morse = {badge_morse: signs for signs, badge_morse in MORSE_UPPER.items()}
    result_encode = ''
    for badge in string.split('|'):
        if badge in revers_morse:
            result_encode += revers_morse[badge]
    return result_encode


def main(string: str, mode: str):
    """Main controller"""
    if mode == 'encode':
        return encode(string, )
    elif mode == 'decode':
        return decode(string)
    return False


if __name__ == '__main__':
    string_test = 'HELLO'
    string_encode = main(string_test, mode='encode')
    print(string_encode)
    print(main(string_encode, mode='decode'))
