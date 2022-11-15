# class SmartKey:
#     def __init__(self, obj):
#         self.obj = obj
#
#     def __lt__(self, other):
#         return (other.obj + self.obj) < (self.obj + other.obj)
#
#
# def join_to_biggest(items: list[int]):
#     return int(
#             ''.join(sorted(
#                 map(str, items),
#                 key=SmartKey
#             )))
#
#
# print(join_to_biggest([501, 2, 1, 80, 9]))

from itertools import permutations

stuff = [1, 2, 3]

comb = permutations([1, 2, 3], len(stuff))

for i in comb:
    print(i)
