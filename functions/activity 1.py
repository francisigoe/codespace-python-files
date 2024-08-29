# made 29/8/24
# by francis igoe

list = [10, 2, 3, 4, 7]
# prints the contence of a list
def  show_list(list):
        print("The content of the list is:", list)

# finds the max value of the list and returns it
def find_max(list):
    Max = 0
    for x in list:
        if Max < x:
            Max = x 
    return Max 

# using the functions
Max = find_max(list) 
show_list(list)
print("The max value in the list: ", Max)