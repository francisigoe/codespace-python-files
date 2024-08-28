# made 28/8/24
# by francis igoe
# takes 3 inputs and determines whether none some or all are equal
x = input("enter a number")
y = input("enter a number")
z = input("enter a number")
if x == y and y == z and x == z:
    print("All numbers are equal")
elif x != y and x != z and y != z:
    print("All numbers are different")
else:
    print("Neither all are equal or different")