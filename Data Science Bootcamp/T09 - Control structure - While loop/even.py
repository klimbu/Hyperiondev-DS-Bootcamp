'''
ask user input for a number
store it in variable input_num
create a new variable 
	even = 2

while even < input_num
	even += 2
'''

input_num = int(input("Please enter a number: "))
even = 0 # used comparison and to store even numbers

while even < input_num:
    even += 2 # increment of 2 for even numbers
    
    if even <= input_num: # prints all even numbers up to input_num if its even
    	print(even)
     
# realised I had to use a nested if statement to avoid a higher number than
# input_num being printed