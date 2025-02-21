"""
可变元素：修改后会影响到原始对象和浅拷贝对象，因为它们引用的是同一个对象。
不可变元素：修改后不会影响原始对象和浅拷贝对象，因为不可变对象无法修改，修改会导致创建新的对象。
"""
import copy

tup1 = (999, "111")
tup2 = copy.copy(tup1)
print(tup1)
print(tup2)
print(id(tup1))
print(id(tup2))

tup3 = (1, '11', [])
tup4 = copy.copy(tup3)
print(tup3)
print(tup4)
print(id(tup3))
print(id(tup4))

tup3[2].append(5)
print(tup3)
print(tup4)

lst = [99, '9', (1, 2), [3, 4]]
lst2 = copy.copy(lst)
print(id(lst))
print(id(lst2))

lst[3][0] = 33
print(lst)
print(lst2)

