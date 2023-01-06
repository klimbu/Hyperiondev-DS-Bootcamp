'''
ask user input for a number 
	input_num = int(input(""))

if input_num>10
	for i in range(0, input_num)
		print(input_num)
else
	print("Sorry, too small")
'''

input_num = int(input("Enter a number: \n"))

print("") #makes counting to double check easier

if input_num>10: #if input_num>10 prints it that many times.
	for i in range(0, input_num):
         print(input_num)
else:
    print("Sorry, too small")