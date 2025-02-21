#
for i in [1, 2, 3, 4]:
    print(i)

for i in [1, 2, 3, 4]:
    print(i)
    if i > 2:
        break
else:
    print(5)

#
for right in range(1, 10):
    for left in range(1, right+1):
        print(f"{left}*{right}={left * right}", end='\t')
    print()

#
for i in range(3):
    for j in range(3):
        print('hello')
        break

#
for i in range(3):
    for j in range(3):
        if j == '0':
            continue
        print('hello')

# 
