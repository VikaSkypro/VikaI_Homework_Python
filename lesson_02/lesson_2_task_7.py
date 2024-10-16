# Range. Создайте список lst1 = [ 18, 14, 10, 6, 2 ]

# Вариант 1.
for i in range(18, 2 + -4, -4):
    print(i, end=' ')

# Вариант 2.
res = [i1 for i1 in range(18, 0, -4)]
print(res)
