# made 29/8/24
# by francis igoe
# function that finds the factorial of a number
def factorial(val):
    count = 1
    n = 1
    while count <= val:
        n *= count
        count += 1
    print(n)
    
factorial(6)
