# made 29/8/24
# by francis igoe
# adds all numbers in an array together and divides by the arrays length
total = 0
array = [20, 30, 25, 35, -16, 60, -100]
for x in array: 
    total = total + x
print(total / len(array))