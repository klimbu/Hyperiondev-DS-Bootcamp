'''
create following variables:
input_number = ''
valid_number = 0 

use while loops and nested if and elif statements

ask user input in variable input_number

while input_number>100
	if input_number>100
		print "Try again with a number less than or equal to 100"
		ask user input in variable input_number
	elif input_number <=100
		if input_number%2=0
			in valid_number multiply input_number by 2
			print (valid_number)
		else
			in valid_number multiply input_number by 3
        print (valid_number)
'''

input_number = ''
valid_number = 0

input_number = int(input("Enter a number less than or equal to 100: \n"))
while input_number>100:
    input_number = int(input("Try again with a number less than or equal to 100: \n"))
    # different from original pseudocode as I found that I didn't need the first if statement
    if input_number<=100: #if number is less than or equal to 100
        if input_number%2==0: # if number is even
            valid_number = input_number * 2
            print (f"The number is {valid_number}")
            exit() #exits after statement is executed
        else: # if number is odd
            valid_number = input_number * 3
            print (f"The number is {valid_number}")
            exit() #exits after statement is executed