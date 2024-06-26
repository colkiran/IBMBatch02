
class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, val):
        if val < 0:
            raise ValueError("Price cannot be less than zero")
        else:
            self.__price = val

    def del_price(self):
        self.__price = 0

import sys

try:
    coke = Product(50)
    print(coke.get_price())
    coke.set_price(120)
    print(coke.get_price())
    coke.del_price()
    print(coke.get_price())
except:
    print("Exception Occured......")
    print(sys.exc_info()[0], "Occured")
    print(sys.exc_info()[1])
