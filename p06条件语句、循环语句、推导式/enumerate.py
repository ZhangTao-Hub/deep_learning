seasons = ['a', 'b', 'c', 'd']
obj = enumerate(seasons)
print(obj)
print(list(obj))

obj = enumerate(seasons, start=1)
print(list(obj))

