# --- Properties --
# Property = object that sits in front of an attribute and allows to set and get the value of it
class Product:
    def __init__(self, price, color):
        self.__price = price
        self.__color = color

    @property
    def price(self):
        return self.__price

    # @price.setter  # we can remove the setter if we don't want access
    # def price(self, value):
    #     if value < 0:
    #         raise ValueError("Price cannot be negative.")
    #     self.__price = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value


product = Product(10, "red")
print(product.price)
