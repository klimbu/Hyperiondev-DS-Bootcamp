'''
create empty variable
	request_number = ''
create a int variable to store total amount of inputs 
	total_input = 0
create another int variable to store and add all inputs together
	total = 0
print "Enter a number. Enter -1 to Stop."
while total_input!= -1
	request_number = int(input())
	if request_number != -1:
		total += request_number
        total_input += 1
print f"The average of the numbers entered = {total/total_input}"
        
'''

request_number = ''
total_input = 0
total = 0
print("Enter a number. Enter -1 to Stop.")

while total_input!= -1:
    request_number = int(input()) #inputs have to be integers
    if request_number != -1:
        total += request_number # totals input numbers
        total_input += 1 # counting total amount of inputs
    elif  request_number == -1:
        print(f"The average of the numbers entered = {total/total_input}")
        exit() # Exit the program after calculating the average
    else:
        print("Incorrect input. Program terminated.")
        exit() # in case a string or character was entered
