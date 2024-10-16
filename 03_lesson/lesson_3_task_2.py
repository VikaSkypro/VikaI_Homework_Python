from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 14", "+79015249966"),
    Smartphone("Samsung", "Galaxy S21", "+79616855555"),
    Smartphone("Samsung", "Galaxy A52", "+79040042020"),
    Smartphone("Google", "Pixel 6", "+79155648779"),
    Smartphone("Xiaomi", "Redmi Note 10", "+79656565656")
]

for i in catalog:
    print(f"{i.brand} - {i.model}. {i.number}")
