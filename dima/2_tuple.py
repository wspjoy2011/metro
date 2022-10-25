def return_multiple_values():
    return 'first', 'second'


values = return_multiple_values()
print(type(values))

value1, value2 = return_multiple_values()
print(value1)

value1, value2 = value2, value1

print(value1, value2)
