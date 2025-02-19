print("执行第一行")
print(2 / 0)
print("执行到第三行")
a = 123


def add(left, right):
    print("执行到第8行")
    print("执行到第9行", left + right)


print("执行到第12行啦")
add(3, 4)
a = 124
print("执行到第15行啦")
