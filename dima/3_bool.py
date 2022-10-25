some_string = 'some string'
empty_string = ''

if len(some_string) != 0:
    print('Len some string')

if some_string:
    print('Not empty')

if empty_string:
    print('Empty string')

print(int(False) + 1)

array = [1, 2]  # False

if not array:
    print('Array')

if not array and some_string:
    pass

if some_string > empty_string:
    pass

first_str = 'first'
second_str = 'firpt'

print(first_str > second_str)
# print(ord('S'), ord('s'))

for index, letter in enumerate(first_str):
    print(ord(letter), ord(second_str[index]))
