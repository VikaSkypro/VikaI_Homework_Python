# Месяц — сезон
def month_to_season(n_month):
    if 1 <= n_month <= 2:
        return "Зима"
    elif 3 <= n_month <= 5:
        return "Весна"
    elif 6 <= n_month <= 8:
        return "Лето"
    elif 9 <= n_month <= 11:
        return "Осень"
    elif 12 <= n_month <= 12:
        return "Зима"
    else:
        return "Неверный номер месяца"


try:
    n_month = int(input("Введите номер месяца (1-12): "))
    print(month_to_season(n_month))
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12.")
