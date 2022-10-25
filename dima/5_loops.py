large_value = 'Len some string'

# for index in range(len(large_value)):
#     print(f'{index + 1}: {large_value[index]}')


# for index, letter in enumerate(large_value, 1):
#     if not letter.strip():
#         break
#     if letter.isupper():
#         continue
#     print(f'{index}: {letter}')
words = large_value.split()

new_words = []
for word in words:
    for letter in word:
        if not letter.isupper():
            new_words.append(letter)

letters = [letter for word in words for letter in word if not letter.isupper()]
print(letters)

if 'e' in large_value:
    pass

person = {
    'name': 'bob',
    'lastname': 'locksmith'
}

if 'name' not in person:
    print(person['name'])

if 'bob' in person.values():
    print('Bob found')


print(person.items())
print(person.keys())
print(person.values())
