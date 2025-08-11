
class Bank:

    def __init__(self,acc,balance):
        self.acc = acc
        self.__balance = balance

    def get_balance(self):
        print(self.__balance)

    def set_balance(self,amount):
        self.__balance +=amount

kotak = Bank("saving",1000)
kotak.set_balance(2000)
kotak.get_balance()