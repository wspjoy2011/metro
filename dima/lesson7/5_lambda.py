def return_last_element(person):
    return person.split(' ')[-1]


names = ['Zack Aron', 'April Fox', 'James Brown']
names.sort()
print(names)
names.sort(key=lambda person: person.split(' ')[-1])
print(names)
names.sort(key=return_last_element)
print(names)
