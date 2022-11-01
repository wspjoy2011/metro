def wrapper(number: int):
    def add_num(second_number: int):
        return number + second_number
    return add_num


wrap = wrapper(100)(10)
print(wrap)
# print(wrap(10))
