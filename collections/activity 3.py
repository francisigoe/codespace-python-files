# made 29/8/24
# by francis igoe
# finds the highest and lowest values in an array
array = [25, 14, 56, 15, 36, 56, 77, 18, 29, 49]
high = array[1]
low = array[1]

# replaces highest or lowest value if the current value is higher or lower than it
for x in array: 
    if x > high:
        high = x
    elif x < low:
        low = x    
    
print(high)
print(low)