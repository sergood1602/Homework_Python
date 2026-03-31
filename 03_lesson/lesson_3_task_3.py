from address import Address
from mailing import Mailing


from_address = Address(190000, "Санкт-Петербург", "Невский проспект", 70, 10)
to_address = Address(188800, "Выборг", "Крепостная", 20, 5)
cost = 1000
track = "45005145009749"

mailing = Mailing(to_address, from_address, cost, track)

print(mailing)
