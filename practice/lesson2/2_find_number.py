from random import randint, choice


def find_number(numbers, value):
    for index, number in enumerate(numbers):
        if number == value:
            return index
    return -1


numbers = []

for _ in range(20):
    numbers.append(randint(1, 100))

random_number = choice(numbers)

print(numbers, random_number)
print(len(numbers))
print(find_number(numbers, random_number))
print(find_number(numbers, 101))
