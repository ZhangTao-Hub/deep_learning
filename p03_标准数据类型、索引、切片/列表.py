list0 = []
list1 = ["china", 1997, True]
list2 = ['a', 'b', 'c']

# 列表修改
list1 = ['h', 'e', 'l', 'l', '0']
list1[4] = '-'
print(list1)

list1[:4] = ['H', 'E', 'L', 'L']
print(list1)

# list([iterale])
print(list())
print(list("china"))
print(list(('a', 'b', 'c', 'd')))
print(list({'a': 1, 'b': 2}))
print(list({1, 2, 3}))

