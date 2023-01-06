'''
ask user input for age
if they are 18 or older
	display "Congrats, you are old enough."
else 
	display "Try again when you are 18."
'''

age = int(input("Enter your age: "))

if age >= 18:
	print("Congrats, you are old enough.")
else:
    print("Try again when you are 18.")