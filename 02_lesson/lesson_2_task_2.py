# Високосный год
def is_year_leap(yyyy):
    return "True" if yyyy % 4 == 0 else "False"


num_yyyy = int(input("Введите число: "))
res = is_year_leap(num_yyyy)
print(f"год {num_yyyy}: {res}")
