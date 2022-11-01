# def add_spec_char():
#     global name
#     name += '!'
#     return name + '!'


def add_spec_char():
    global name
    name = 'James' + '!'

    # def add_letter():
    #     nonlocal name
    #     name += '_'


name = 'bob'
print(name)
add_spec_char()
print(name)

# {
#     'name': 'bob',
#     'add_spec_char': {
#         'name': 'James' + '!'
#     }
# }
