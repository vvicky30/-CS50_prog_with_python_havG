# here we're going to implement the global.ipynb code in object-oriented programming 
# one of the advantages of using OPP is that we don't really have to acess and define some variables globally
# as here attributes/variables defined in the class can be accessed by any function (within or outside the class) without any difficulty ,
# except for the honoury __var(private attributes of variables defined in the class).

class Account:
    def __init__(self):
        self.balance = 0 # initialized here pvt attribute with zero value
    
    @property  #getter for balance 
    def balance(self):
        return self._balance
    
    def __str__(self):
        return f"Your Balance: {self.balance}"
    
    @balance.setter   # setter   
    def balance(self,balance):
        if not isinstance(balance, int):
            raise ValueError("balance must be in int value")
        self._balance = balance
    
    # now implemeting deposit and withdraw fns 
    def deposit(self, n=0):
        self.balance += n
    
    def withdraw(self, n=0):
        self.balance -= n

def main():
    #creating class object of Account here 
    bal =Account()
    print("Initial balance:")
    print(bal)
    #or we can use getter fn as well to acess this balance attribute 
    print("from getter of balance",bal.balance)
    # deposit 150
    bal.deposit(150)
    print("balance after depositing amount of 150")
    print(bal)
    
    print("from getter of balance:",bal.balance)
    # withdraw 50
    bal.withdraw(50)
    print("balance after withdrawing amount of 50")
    print(bal)
    #or we can use getter fn as well to acess this balance attribute
    print("from getter of balance",bal.balance)
    
if __name__ == "__main__":
    main()
             
'''
[o/p]:
Initial balance:
Your Balance: 0
from getter of balance 0
balance after depositing amount of 150
Your Balance: 150
from getter of balance: 150
balance after withdrawing amount of 50
Your Balance: 100
from getter of balance 100
'''