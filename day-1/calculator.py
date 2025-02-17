


from abc import ABC,abstractmethod
import math_operations
#from math_operations import add,dicide,multi,sub
class Calculator(ABC):
    @abstractmethod
    def add(self,a,b):
        pass
  
class BasicCalc(Calculator):
 
    def add(self,a,b):
        return math_operations.add(a,b)