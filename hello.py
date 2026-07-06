class BankAccount:
    def __init__(self,balance):
        self.__balance=balance



    def get_balance(self):
        print(f"your balance is {self.__balance}")


    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount


    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance -= amount
            

acc=BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
acc.get_balance()