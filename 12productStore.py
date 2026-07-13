class Product:
    count = 0

    def __init__(self,name,price):
        self.name = name
        self.price = price
        Product.count += 1
    
    def get_info(self):
        print(f"price of {self.name} is Rs. {self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total {cls.count} products are created")
    

    @staticmethod
    def calc_discount(price, percentage):
        discount = percentage*price/100
        print(f"the price of discount is {discount}")

p1 = Product("laptop", 30000)
p2 = Product("mobile", 25000)
p3 = Product("pen",30)
p4 = Product("bag",1000)

p1.get_count()

p2.calc_discount(p4.price, 12)