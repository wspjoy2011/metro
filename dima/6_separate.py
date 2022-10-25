MORSE = {
    'A': '.-',
    'B': '-...'
}

string = 'AbbA'
result_decode = ''

for letter in string:
    if letter in MORSE:
        result_decode += MORSE[letter] + '|'


print(result_decode)
print(result_decode.split('|')[:-1])
