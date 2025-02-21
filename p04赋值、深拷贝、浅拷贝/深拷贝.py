import copy

tup1 = (9, '99', [])
tup2 = copy.deepcopy(tup1)
print(id(tup1))
print(id(tup2))

tup1[2].append(5)
print(tup1)
print(tup2)

lst = [99, '99', [1, 2]]
lst2 = copy.deepcopy(lst)
print(lst)
print(lst2)
print(id(lst))
print(id(lst2))

lst[2][0] = 999
print(lst)
print(lst2)


