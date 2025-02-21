square = [x ** 2 for x in range(10)]
print(square)

res = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(res)

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

res = [[row[i] for row in matrix] for i in range(3)]
print(res)
