from abc import ABC,abstractmethod
class Employee(ABC):

    def __init__(self,name,empid,position):
        self.name=name
        self.empid=empid
        self.position=position
    @abstractmethod
    def calculateSalary(self):
        pass

class FullTimeEmployee(Employee):
     def __init__(self,name,empid,position,salary):
        super().__init__(name,empid,position)
        self.salary=salary
     def calculateSalary(self):
         return self.salary
        

class PartTimeEmployee(Employee):
     def __init__(self,name,empid,position,hourlyRates,hoursOfWork):
        super().__init__(name,empid,position)
        self.hourlyRates=hourlyRates
        self.hoursOfWork=hoursOfWork
     def calculateSalary(self):
         return self.hourlyRates*self.hoursOfWork
     

fte= FullTimeEmployee("Alice",101,"SE",5000)
pte= PartTimeEmployee("Bob",102,"QA",25,20)

print(f"{fte.name}'s Salary ${fte.calculateSalary()}")
print(f"{pte.name}'s Salary ${pte.calculateSalary()}")



        