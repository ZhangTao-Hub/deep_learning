# dict.keys()
d1 = {"name": "zhangsan", "age": 18, "height": 175}
a = d1.keys()
print(a)
print(list(a))


# dict.values()
d2 = {"name": "zhangsan", "age": 18, "height": 175}
a = d2.values()
print(a)
print(list(a))


# items()
print(list(d2.items()))

# get()
v = d2.get("name")
print(v)

v = d2['name']
print(v)

v = d2.get("xxx")
print(v)

# update
d1 = {'name': 'zhangsan'}
d2 = {"sex": 'male'}
d3 = {"height": 1.75, 'name': 'lisi'}

d1.update(d2)
d1.update(d3)
print(d1)

d1.update(dict([("address", "else")]))
print(d1)

d1.update(weight=105)
print(d1)

# pop()
d1.pop('weight')
print(d1)

# error
# d1.pop('xxx')
# print(d1)

# popitem()
res = d1.popitem()
print(res)

# copy()
d_copy = d1.copy()
print(d_copy)

# clear()
d_copy.clear()
print(d_copy)

