

# define a function that takes an array as input and return the sum of its elements

def sumofarray(*arr):
    total=0
    for num in arr:
        total +=num
    return total

#numbers=[]
result=sumofarray(12,13,14,15)
print(f" the sum is  {result}")
