# Логическое И (AND). Обязательно выполнение всех условий
user_login = "vika"
user_password = "123zxc"

login = input("Введи Логин: ") # запрос инф-ции через input
password = input("Введи Пароль: ")

if login == user_login and password == user_password:
    print("Добро пожаловать")
else:
    print("Проверьте правильность ввода")

# Логическое ИЛИ (OR). Должно выполниться хотя бы одно условие

color1 = "red"
color2 = "green"

c1 = input("Первый цвет: ")
c2 = input("Второй цвет: ")

if c1 == color1 or c2 == color2:
    print("Отличный выбор")
else:
    print("Выбери другой цвет")

