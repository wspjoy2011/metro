def add_spec_char(element):
    return element + '!'


names = ['Zack Aron', 'April Fox', 'James Brown']
names_length = map(len, names)
print(list(names_length))


strings = ['1', '2', '3']
numbers = map(int, strings)
numbers = list(numbers)

names_add = map(add_spec_char, names)
print(list(names_add))

numbers_square = map(lambda number: number ** 2, numbers)
print(list(numbers_square))

scores = [1, 3, 5, 10, 7]
scores_over_five = filter(lambda score: score > 5, scores)
print(list(scores_over_five))
