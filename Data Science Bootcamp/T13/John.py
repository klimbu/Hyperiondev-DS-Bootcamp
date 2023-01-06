'''
correct = "john"

incorrect = []

Ask user input for name:
while incorrect!=correct:
	incorrect = input().lower()
	if not incorrect==correct:
		incorrect.capitalize()
print(incorrect)
'''

correct = "john" #lowercase to match input
user_input = '' # variable to register user input
incorrect = [] # list to sore user input

while user_input!=correct:
    user_input = (input("Enter you name: ").lower()) #lower() to match user_input and correct variables
    if incorrect!=correct:
         incorrect.append((user_input.capitalize())) #adds to list and capitalizes the name

if "John" in user_input: #if user_input contains John - remove it from the list
    user_input.remove("John")
print(f"Incorrect names: {incorrect}") #prints incorrect names