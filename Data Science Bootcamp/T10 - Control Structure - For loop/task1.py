'''
ask user input for a number 
input_number = input('')
create a for loop for a multiplication table counting to 12 x (number)
for i in range(1, 13):
	print {input_number} x {i} = {input_number*i}
'''

input_number = int(input("Enter a number you would like to see the times table of: \n"))

# creates multiplication table for input_number from 1-12 multiples
for i in range(1, 13):
    print (f"{input_number} x {i} = {input_number*i}")