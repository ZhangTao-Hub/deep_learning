a = {"name": "zhangsan", "age": 18}
print(a)

a = dict()
a['name'] = 'zhangsan'
a['age'] = 18
print(a)

a = dict(name='zhangsan', age=18)
print(a)

a = dict([("name", "zhangsan"), ("age", 18)])
print(a)

a = dict(zip(["name", "age"], ["zhangsan", 18]))
print(a)

dic1 = dict.fromkeys(("name", "age", "sex"))
print(dic1)

print(dict(one=1, two=2, three=3))
print(dict(zip(["one", "two", "three"], [1, 2, 3])))
print(dict([("one", 1), ("two", 2), ("three", 3)]))

res = zip("abcd", "efgh")
print(list(res))

res = zip("abcd", "efg")
print(list(res))

res = zip()
print(list(res))

res = zip("abcd")
print(list(res))

dic = {"name": "zhangsan", "age": 18}
print(dic['name'])
print(dic['age'])

dic['name'] = 'lisi'
dic['sex'] = 'male'
print(dic)