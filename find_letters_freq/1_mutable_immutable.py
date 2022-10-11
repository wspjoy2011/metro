text = 'Hello, world'
print(id(text))
text += text + '!'
print(id(text))

number = 1
print(id(number))
number += 1
print(id(number))

names = ['bob', 'mike', 'rich']
print(id(names))
names.append('new_name')
print(id(names))

names_new = names
names_new.append('wrong')
print(names)
