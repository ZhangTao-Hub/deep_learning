"""replace"""
s = "Line1, Line2, Line4"
rs = s.replace("Li", "b")
print(rs)

rs = s.replace("Li", "b", 2)
print(rs)

"""strip"""
str1 = " \thello, world h \n"
print(str1.strip())

str2 = "oohello, world"
print(str2.strip('o'))

str3 = "www.example.com"
print(str3.strip("mecow."))

"""center"""
str4 = "hello "
print(str4.center(11, 'F'))
print(str4.center(3, 'F'))

"""ljust rjust"""
str5 = "hello"
print(str5.ljust(11, 'F'))
print(str5.ljust(3, 'F'))

print(str5.rjust(11, 'F'))
print(str5.rjust(3, 'F'))

"""partition"""
str6 = "hello, world"
print(str6.partition('l'))
print(str6.partition("ll"))
print(str6.partition("hd"))

print(str6.rpartition('l'))
print(str6.rpartition("ll"))
print(str6.rpartition("hd"))

"""startswith, endswith"""
str7 = "hello world"
print(str7.startswith('h'))
print(str7.startswith("he"))
print(str7.startswith(" w"))
print(str7.startswith(" w", 5, 8))
print(str7.startswith((" w", "h")))

print(str7.endswith("d"))
print(str7.endswith("ld"))
print(str7.endswith("lo"))
print(str7.endswith('lo', 1, 5))
print(str7.endswith(("h", "ld")))

"""isalnum isalpha isdigit isspace"""
str8 = "abc牛123"
print(str8.isalnum())
print(str8.isalpha())
print(str8.isdigit())

str9 = "abc"
print(str9.isalpha())
print(str9.isdigit())

str10 = "123"
print(str10.isdigit())

print(str8.isspace())
str11 = " \t\n"
print(str11.isspace())

"""split"""
s = " Line1-abcdef \nLine2-abc \nLine4-abcd"
a = s.split()
print(a)

a = s.split(" ")
print(a)

a = s.split("Li", 2)
print(a)

a = s.rsplit("Li", 2)
print(a)

"""join"""
a = "\\"

s1 = "hello world"
print(a.join(s1))

s2 = ["1", "2", "3", "4"]
print(a.join(s2))

s3 = ("1", "2", "3", "4", "5")
print(a.join(s3))

s4 = {"身高": 175, "体重": 65}
print(a.join(s4))

s5 = {"1", "2", "3", "1"}
print(a.join(s5))

"""count"""
a = "hello world"
rs = a.count('l')
rs1 = a.count('l', 0, 3)
print(rs, rs1)

"""find index"""
s = "hello world"
print(s.find('l'))
print(s.rfind('l'))

print(s.find('l', 4))
print(s.rfind('l', 4))

"""capitalize title upper lower swapcase"""
s = "hello world"
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.swapcase())


