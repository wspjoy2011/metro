import sys

a = 1
b = 1


print(sys.getrefcount(a))
print(id(a), id(b))
