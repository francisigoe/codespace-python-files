# made 29/8/24
# by francis igoe
# returns wether a number is prime as a boolean using a for loop
def prime(val):
    for i in range(2,val):
        prime = val % i
        if not prime:
            break
    return prime

# executes function and sais weather its prime or not
prime = prime(77232917)
if prime:
    print("the number is prime")
else:
    print("the number is not prime")