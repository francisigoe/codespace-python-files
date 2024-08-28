# date 28/08/24
# by francis igoe  
# uses a while loop to calculate davinchi seqence two didgets at a time stoping when over a diget is over 50
val1 = 0
val2 = 1
while val1 <= 50:
    print(val1)
    print(val2)
    val1 = (val1 + val2)
    val2 = (val1 + val2)

