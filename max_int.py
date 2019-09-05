# Design an algorithm that finds the maximum positive integer input by a user. 
#  The user repeatedly inputs numbers until a negative value is entered.
# First we need to initialize the number and the max number

num_int = 0
max_int = 0

# Using while loop we let the user input a number until he inputs a negative number
while num_int >= 0:
    num_int = int(input("Input a number: "))    # Do not change this line
    
    # We need to keep track of the max number
    if num_int > max_int:
        max_int = num_int

print("The maximum is", max_int)    # Do not change this line
