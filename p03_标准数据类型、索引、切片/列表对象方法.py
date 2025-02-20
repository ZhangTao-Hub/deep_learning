# append
lst = [1, 2]
lst.append(1)
lst.append('1')
lst.append([1, 2])
lst.append((3, 4))
lst.append({'a': 1, "b": 2})
lst.append({1, "2"})
print(lst)

# extend
li = [1, 2]
li.extend('1')
li.extend([1, 2])
li.extend((3, 4))
li.extend({"a": 1, "b": 2})
li.extend({5, 6})
print(li)

# insert
l1 = [1, 2, 3, 4, True, False]
a = [5, 6, 7]
l1.insert(4, a)
print(l1)

# sort
num_lst = [1, -2, 5, -3]
num_lst.sort()
print(num_lst)

num_lst.sort(reverse=True)
print(num_lst)

num_lst.sort(key=abs)
print(num_lst)

# sorted
num_tup = (1, -2, 5, -3)
res = sorted(num_tup, reverse=False)
print(res)

res = sorted(num_tup, reverse=True)
print(res)

res = sorted(num_tup, key=abs)
print(res)

# reverse
li = [1, 2, 3, 4]
li.reverse()
print(li)

# reversed
seq = "hello world"
res = reversed(seq)
print(list(res))

# count
a = [1, 23, 2, 3, 23, '23']
print(a.count(23))

# index
a = [1, 2, 3, 4, 3, 2, 3]
print(a.index(3))
print(a.index(3, 3, 5))

# pop
li = [1, 2.3, 2+3j, '4', True, False]
print(li.pop())
print(li)

li.pop(2)
print(li)

# remove
li = [1, 2, 4, 2, 3, 3]
li.remove(2)
li.remove(3)
print(li)
# li.remove(5)

# copy [:]
li = [1, 2, 3]
li2 = li.copy()
print(li2)

# clear del
li.clear()
print(li)