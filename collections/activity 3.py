# made 28/8/24
# by francis igoe
#
array = [25, 14, 56, 15, 36, 56, 77, 18, 29, 49]
high = array[1]
low = array[1]
for x in array: 
    if x > high:
        high = x
    elif x < low:
        low = x    
    
print(high)
print(low)