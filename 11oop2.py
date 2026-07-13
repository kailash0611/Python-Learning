# Types of method
# - Intance Method
#   -- 1st param is self
#   -- Can access the class & instance attributes
#   -- can be called using object name only
    
# - Class Method
#   --1st param is cls
#   --Can access only class attribute
#   --We you a decorator '@classmethod' it is a like a meta data for the method that tells that it is a class method
#   -- Can be called using class name and object name both

# - Static Method
#   --No compulsory param req for class param
#   --No 'cls' and 'self' param needed for static method, it has its own param
#   --Cannot access instance and class attributes
#   --'@staticmethod' decorator converts normal method into static 

class Laptop:
    storage_type = "ssd"

    def __init__(self,RAM, Storage):
        self.RAM = RAM
        self.storage = Storage

    # instance method
    def get_info(self):
        print(f"Laptop has {self.RAM} RAM  & {self.storage} {self.storage_type}")

    #class method
    def get_storage_type(cls):
        print(f"Storage type = {cls.storage_type}")
        
    @staticmethod
    def get_discount(price,discount):
        discounted_price = price - (discount*price/100)
        discount_amt = price -discounted_price
        print(f"Dicounted Price = {discounted_price}")
        print(f"Discount Amount = {discount_amt}")

l1 = Laptop(8,126)
        
l1.get_info()

# Laptop.get_info() this will give error coz instance method cant be accessed using class name

l1.get_storage_type()
Laptop.get_storage_type(Laptop)
# Class methods can be called using class name and method name 
# if using class name then pass class name as a parameter

l1.get_discount(44340,10)
