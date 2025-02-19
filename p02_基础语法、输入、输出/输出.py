# print("hello, python")
#
# with open("abc.txt", mode='w') as f:
#     print("12345", file=f)

import time

print(1, 2, 3, sep='-', end='\n\n')
print("Loading", end='')

for i in range(10):
    print('.', end='', flush=True)
    time.sleep(0.3)
