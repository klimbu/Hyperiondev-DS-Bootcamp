'''
ask user input for their full name
use len() to get the number of characters/letters entered
if len is less than 1 characters
	display "You haven't entered anything. Please enter your full name."
elif len is less than 4 characters
	display "You have entered less than 4 characters. Please make sure you have entered your name and surname."
elif len is greater than 25 characters
	display "You have entered more than 25 characters. Please make sure you have only entered your full name and surname."
else
	display "Thank you for entering your name."
'''

name_input = input("Please enter your full name: ").strip(" ")
full_name = len(name_input)
# using len on the variable = only 1 variable needed so its simple and clean
# discovered that program counts blank spaces as characters so i thought to use the strip() to resolve this
# works smoothly and makes logical sense 

if full_name < 1: 
    print("You haven't entered anything. Please enter your full name.")

elif full_name < 4:
    print("You have entered less than 4 characters. Please make sure you have entered your name and surname.")

elif full_name > 25:
    print("You have entered more than 25 characters. Please make sure you have only entered your full name.")

else:
    print("Thank you for entering your name.")