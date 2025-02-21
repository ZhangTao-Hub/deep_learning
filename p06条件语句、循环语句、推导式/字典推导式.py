dic = {x: x ** 2 for x in range(4)}
print(dic)

dic = {x: x ** 2 for x in range(6) if x % 2 == 0}
print(dic)

dic = {k: v for k, v in zip((1, 2, 3), (6, 7, 8))}
print(dic)