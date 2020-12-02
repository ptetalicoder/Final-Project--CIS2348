#Pranav Tetali
#ID 1541822
#Homework 3 11.18

num_values = input()
# I converted the values to integers.
list_values = [int(num) for num in num_values.split()
if int(num) >= 0]
# The values should be in ascending order.
list_values.sort()
# The display should be sorted with a list of positive integers
for value in list_values:
    print(value, end = ' ')
