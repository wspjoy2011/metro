def receive_all(*args, **kwargs):
    print('Position arguments')
    for arg in args:
        print(arg)

    print('Named arguments')
    for arg_name, arg_value in kwargs.items():
        print(f'{arg_name}: {arg_value}')


# print(receive_all(1))
# print(receive_all(1, 2, 3))
# print(receive_all(a=1, b=2, c=3))
print(receive_all(1, 2, 3, a=1, b=2, c=3))
print([1, 2, 3])
print(*[1, 2, 3])
