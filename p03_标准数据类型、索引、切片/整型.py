a = int()
print(a)

a = int(3.99)
print(a)

a = int("12")
print(a)

# error
# a = int("12.1")
# print(a)

a = int("101010", base=2)
print(a)

a = int("0b101010", base=2)
print(a)

a = int("11", base=8)
print(a)

a = int("0o11", base=8)
print(a)

a = int("17", base=16)
print(a)

a = int("0x17", base=16)
print(a)

# error
# a = int(17, base=16)
# print(a)
