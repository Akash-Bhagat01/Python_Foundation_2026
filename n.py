class Bank:
    def __init__(self, balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def update_balance(self,new_bal):
        self.__balance=new_bal
# b = Bank(10000)
# print("Old Balance:",b.get_balance())
# b.update_balance(999999)
# print("New Balance :",b.get_balance())

