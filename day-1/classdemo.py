

class User:
    name='super-admin'

    

# constructor
    def __init__(self,age,city):
        self.age=age
        self.city=city
    def __str__(self):
        return f"user details {self.age} {self.city}"

    def printUser(self):
        
        print(f"user details {self.age} {self.city}")

user= User(31,'mumbai')
print(user)
#user.printUser()

#user.printUser()


