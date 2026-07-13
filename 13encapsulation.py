# Encapsulation - wrapping data and methods together 

# Access modifiers
# - Public
#   -- Can access inside and outside class
#   -- By defefault its public
# - Protected
#   -- Can accces in class and subclass
#   -- add one '_' before attribute name to make it protected

# - Private
#   -- Can access in class only
#   -- add two '_' before attribute name to make it private


class BankAccount:
    def __init__(self,name,balance):
        self.name = name    #public
        self.__balance = balance    #private

    def get_balance(self):  #getter
        return self.__balance
    
    def set_balance(self,newBalance):   #setter
        self.__balance = newBalance

acc1 = BankAccount("Kailash",40000)

acc1.set_balance(34000)     #accesssing private variable through getter and setter
print(acc1.get_balance())
