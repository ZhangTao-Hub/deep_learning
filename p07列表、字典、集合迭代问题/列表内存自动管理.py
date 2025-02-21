import copy

lst = [1, 2, 3]
for item in lst:
    lst.remove(item)
print(lst)

lst = [1, 2, 3]
lst2 = [1, 2, 3]
for item in lst2:
    lst.remove(item)
print(lst)

lst = [1, 2, 3]
for item in lst[:]:
    lst.remove(item)
print(lst)

lst = [1, 2, 3]
lst2 = lst.copy()
for item in lst2:
    lst.remove(item)
print(lst)

lst = [1, 2, 3]
lst2 = copy.copy(lst)
for item in lst2:
    lst.remove(item)
print(lst)

lst = [1, 2, 3]
lst2 = copy.deepcopy(lst)
for item in lst2:
    lst.remove(item)
print(lst)

