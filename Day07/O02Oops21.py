

from abc import ABC, abstractmethod

class Account(ABC):

    def Deposit(self):
        pass

    @abstractmethod
    def CheckBalance(self):
        pass


class Savings(Account):

    def CheckBalance(self):
        print("The balance in the account ending **** is  ######.##")

    def Withdraw(self):
        print("Amount ##### debited successfully from the account.....")


save1 = Savings()
save1.Withdraw()

class Current(Account):

    def CheckBalance(self):
        pass

curr1 = Current()
