
class Student:
    def __init__(self,rollno,name,subject,marks):
        self.name=name
        self.rollno=rollno
        self.subject=subject
        self.marks=marks
    def displayData(self):
        print (f"Student Data is here: {self.name} {self.rollno} {self.subject} {self.marks}")
stu=Student("199","stu1","phy",30)
stu.displayData()