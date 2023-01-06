'''
ask user input for a number of their choice
store it in variable called "choice_number"

create conditional statements and use nested if statements 
if "choice_number"%2==0 and "choice_number%5==0
	print "{choice_number} is divisible by both 2 and 5"
elif "choice_number"%2==0 or "choice_number%5==0
	if "choice_number"%5==0
		print "{choice_number} is divisible by 5"
	else
		print "{choice_number} is divisible by 2"

elif "choice_number"%2!=0 or "choice_number%5!=0
	if "choice_number"%5!=0
		print "{choice_number} is not divisible by 5"
	else
        print "{choice_number} is not divisible by 2"
 
'''

choice_number = int(input("Please enter a number of your choice: \n"))

if choice_number%2==0 and choice_number%5==0: #checking if %==0 for both using AND
    print (f"1: {choice_number} is divisible by both 2 and 5.") 
else: # if not then this should be printed
    print (f"1: {choice_number} is not divisible by both 2 and 5.")


if choice_number%2==0 or choice_number%5==0: # using OR and nested if statements for this section
    if choice_number%5==0:
         print (f"2: {choice_number} is divisible by 5")
    else:
         print (f"2: {choice_number} is divisible by 2")
else:
    print (f"2: {choice_number} is not divisible by either 2 or 5")
    exit() # using exit to stop the program here as it won't be required for the next step as it already does it


if choice_number%2!=0 or choice_number%5!=0: 
#using != and OR and nested if statements for this section assuming program is not terminated by exit()
    if choice_number%5!=0:
        print(f"3: {choice_number} is not divisible 5.")
    elif choice_number%2!=0:
        print(f"3: {choice_number} is not divisible 2.")