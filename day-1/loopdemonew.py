
# initialize empty array
user_nubers=[]
# ask the user to share the data

n=int(input("Home many numbers yo wana add....! :"))
# take this into an array

for i in range(n):
    num=int(input(f"Enter numbers {i+1}"))
    user_nubers.append(num)

#loop through the array

for num in user_nubers:
    if num% 2==0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an ODD number")