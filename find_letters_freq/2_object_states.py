name = 'bob'

name = name.capitalize()

print(help(str))

print(name.__add__('!'))
num = 1

sum = num + 1
sum = num.__add__(1)

names = [1, 2, 3]  # On ** 2


names = {1: '1', 2: '2'}  # O1

# print(id(names[1]))

print(type(True))
print(1 + True)

isinstance(1, int)
isinstance(True, bool)

print(hash('sum'))
print(hash('mus'))


nums = []
for _ in range(2 ** 1000):
    nums.append(1)
