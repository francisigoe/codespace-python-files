# made 28/8/24 
# by francis igoe  
# takes 3 inputs and returns wheather they are assending, desending or neither
x = input("enter a number")
y = input("enter a number")
z = input("enter a number")
if x < y:
    if y < z:
        print("Increasing order")
    else:    
elif x > y:
    if y > z:
        print("Decreasing order")
    else:
print("Neither increasing or decreasing order")