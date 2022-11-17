

class Customer :
    lst =[]
    def __init__(self, name, credit):
        self.name = name
        self.credit = credit
        self.my_cart = []

    def add_to_cart(self, product):
        self.my_cart.append(product)
        self.lst.append(product)
        self.flag = "add to cart used "


    def my_cart_show(self):
        for i in self.my_cart:
            print(i)

    def all_list(self):
        for i in self.lst:
            print(i)


cus_one = Customer("dew", 1200)
cus_two = Customer("olid", 2000)
cus_three = Customer("Ziss", 1200)

cus_three.add_to_cart("iphone")
cus_two.add_to_cart("xiomi")
cus_one.add_to_cart("Poco")

cus_three.my_cart_show()
print(cus_two.__doc__)
