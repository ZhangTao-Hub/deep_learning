import datetime

print("name: %s, age: %s, sleep: %s" % ("zhangsan", 18, 8))
print("name: %s, hobby: %s" % ("zhangsan", "bark"))
print("name: %r, hobby: %r" % ("zhangsan", "bark"))

d = datetime.date.today()
print("%s" % d)
print("%r" % d)

print("%c, %c, %c, %c" % (65, 90, 97, 122))
print("%c, %c, %c, %c" % ('A', 'Z', 'a', 'z'))

print("%o" % 20)
print("%x, %X" % (28, 28))

print("%e" % 123)
print("%E" % 123)

print("%g" % 1.23456789)
print("%g" % 123456.789)
print("%g" % 1234567.89)
print("%G" % 123456789)

name = "wangcai"
age = 2
print(f"名字是：{name}, 年龄是：{age}, 宝宝今年：{age}月")