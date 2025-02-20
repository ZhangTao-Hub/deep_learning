tup = ()
print(type(tup))

lst = []
print(type(lst))

tup = (1,)
print(tup)
print(type(tup))

num = (1)
print(num)
print(type(num))

lst = [1, ]
print(lst)
print(type(lst))

lst = [1]
print(lst)
print(type(lst))

tup1 = ("china", 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"
print(tup3)

# tuple是不可变的，tuple中的列表是可以变的
tup4 = (1, 2, [3, 4, 5])
tup4[2][2] = 6
print(tup4)

# tuple([iterable])
print(tuple())
print(tuple("china"))
print(tuple([1, 2, 3]))
print(tuple({1: 1, 2: 3}))
print(tuple({1, 2, 3}))

