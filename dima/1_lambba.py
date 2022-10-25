def make_pow(number):
    return number ** 2


persons = {
    'one': 3,
    'two': 2,
    'three': 1
}
persons_sort = dict(sorted(persons.items(), key=lambda person: person[1]))

numbers = [number for number in range(1, 11)]
# numbers_square = list(map(str, numbers))
# numbers_square = list(map(lambda number: number ** 2, numbers))
numbers_square = list(map(make_pow, numbers))
print(numbers_square)
