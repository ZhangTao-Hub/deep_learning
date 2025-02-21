var1 = 999
print(type(var1))

var2 = "999"
print(type(var2))

var = 256
print(id(256))
print(id(var))

var = 258
print(id(257))
print(id(var))

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(id(a))
print(id(b))
print(id(c))

a.append(4)
print(a)
print(b)
print(c)