#This is a program for calculation that removes the fees 
# import lib for rounding up function
import math
def calculate(fee, amount):

    calculatedfee = 10 - (fee / 10)
    
    return math.ceil(amount * 10 / calculatedfee)




