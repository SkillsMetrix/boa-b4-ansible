
from abc import ABC,abstractmethod


class RBI(ABC):
    @abstractmethod
    def deposit(self):
         pass
    @abstractmethod
    def withdraw(self):
         pass
    @abstractmethod
    def checkBalance(self):
          pass
    def openFD(self):
          print('optional service...!')


class ICICI(RBI):
     def deposit(self):
          return "Deposited"
     def withdraw(self):
          return "Withdrawen"
     def checkBalance(self):
          return "balance checked"

bank= ICICI()
print(bank.deposit())
   
     


 