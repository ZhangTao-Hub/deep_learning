dic = {"name": "zhangsan"}
# for key in dic:
#     dic.pop(key)
# print(dic)

# for key in dic:
#     dic.update({'age': 18})
# print(dic)

dic2 = dic.copy()
for key in dic2.keys():
    dic.pop(key)
print(dic)

# s = {1, 2, 3, 'aa'}
# for item in s:
#     s.remove(item)
# print(s)

# s = {1, 2, 3, 'aa'}
# for item in s:
#     s.add('bb')
# print(s)

s = {1, 2, 3, 'aa'}
s1 = s.copy()
for item in s1:
    s.remove(item)
print(s)