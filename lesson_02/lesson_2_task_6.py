# Фильтрация списка
lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

# Вариант 1.
for i in lst:
    if (i <= 30) and (i % 3 == 0):
        print(i)

# Вариант 2.
res = [i1 for i1 in lst if i1 <= 30 and i1 % 3 == 0]
print(res)
