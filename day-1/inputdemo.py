  
age=input('Enter Your Age:')

userAge=(int(age))

if(userAge <0):
    print('Enter valid Age')
elif(userAge <18):
    print('Your are no allowed to vote')
elif(userAge >=18 and userAge <70):
    print('Your are allowed to vote')
else:
    print('Your are senior citizen')

 

 