def get_string(string):
    if len(string) > 10:
        return string[:10]


large_value = 'Len some string'
small_value = 'Hello'

result_large = get_string(large_value)
print(result_large)

result_small = get_string(small_value)
print(result_small)

if result_small is None:
    print('small')

if result_small is not None:
    print('small')

none = None
empty = False
