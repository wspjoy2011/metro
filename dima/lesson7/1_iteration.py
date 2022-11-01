persons = [
    {
        'name':        'John',
        'age':         25,
        'department': 'Web dev'
    },
    {
        'name':        'Bob',
        'age':         27,
        'department': 'Sales'
    },
]

for person in iter(persons):
    name = f"{person['name']} Smith"
    print(persons)

persons.__iter__()

persons_iter = iter(persons)
persons_iter.__iter__()
persons_iter.__next__()

print(next(persons_iter))


persons_iter = iter(persons)
cursor = 0

while cursor < len(persons):
    print(next(persons_iter))
    cursor += 1
