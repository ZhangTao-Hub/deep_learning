# while
a = 1
while a < 4:
    print(a)
    a += 1

#
a = 1
while True:
    print('hello')
    a += 1
    if a == 4:
        break

#
count = 0
while count < 5:
    print(count, "小于5")
    count += 1
    if count >= 5:
        break
else:
    print(count, "大于等于5")

#
right = 1
while right <= 9:
    left = 1
    while left <= right:
        print(f"{left}*{right}={left * right}", end='\t')
        left += 1
    print()
    right += 1
