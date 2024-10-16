from address import Address
from mailing import Mailing

to_address = Address(568568, "Москва", "Ленина", "5A", 5)
from_address = Address(568555, "Москва", "Пушкина", "10Б", 10)
mailing = Mailing(to_address, from_address, 200, "665a")

print(mailing)
