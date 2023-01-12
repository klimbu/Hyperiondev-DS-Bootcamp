''' 
ask user for input and maths operation to perform simple calculation
display answer 
write to file all the equations 
	handle exceptions try...catch or raise
ask user input to either continue calculations or read all equations
	if choice is to read all equations
		try...catch or raise
			open file 
			read all equations
			display all equations
'''
import os

def view_everything(file): 
    """_summary_
    Takes the parameter as file name and if the file doesn't exist it creates a new file
    Also opens file for writing and write every line in list equations 
    
    Args:
        file: generated from user input
    """    
    if not os.path.exists(file):
        with open(file, "w") as default_file:
            pass
    file_write = open(file, "w")    
    for line in equations:
        file_write.write(line+"\n")
    file_write.close()

num1 = 0
num2 = 0
equations = []
while True: # loops until user exits
    while True: # for num1 - try catches until correct input 
        try:
            num1 = int(input("Please enter two numbers and the operation you would like to perform\n1: "))
            break
        except ValueError:
            print("Please enter a valid input")
    while True:	# for num2 - try catches until correct input	
        try:    
            num2 = int(input("2: "))
            break
        except ValueError:
            print("Please enter a valid input")    
    while True: # for operation - try catches until correct input
        operation = input("Select the operation you would like to perform (+,-,x,/,%)\n : ")
        if operation == '+': # if user selects +
            add = num1 + num2 #calculation
            add_string = (f"{num1} + {num2} = {add}") # for appending to list
            print(add_string) #displays results
            equations.append(add_string) # appends to list = equations
            break
        elif operation == '-': # if user selects 
            subtract = num1 - num2 #calculation
            subtract_string = (f"{num1} - {num2} = {subtract}") # for appending to list
            print(subtract_string) #displays results
            equations.append(subtract_string) # appends to list = equations
            break
        elif operation == 'x': # if user selects 
            multiply = num1 * num2 #calculation
            multiply_string = (f"{num1} x {num2} = {multiply}") # for appending to list
            print(multiply_string) #displays results
            equations.append(multiply_string) # appends to list = equations
            break
        elif operation == '/': # if user selects 
            divide = num1 / num2 #calculation
            divide_string = (f"{num1} / {num2} = {divide}") # for appending to list
            print(divide_string) #displays results
            equations.append(divide_string) # appends to list = equations
            break
        elif operation == '%': # if user selects 
            modulus = num1 % num2 #calculation
            modulus_string = (f"{num1} % {num2} = {modulus}") # for appending to list
            print(modulus_string) #displays results
            equations.append(modulus_string) # appends to list = equations
            break
        else: # returns to operation input until correct input
            print("Choose the correct operation.")
    while True: # loops until correct input for choice 
        choice = input("Enter c to continue, va to view all equations in an new txt file or e to exit\n: ")
        if choice == 'c': # returns to num1
            break 
        elif choice == 'va': # asks user input for file name
            file_name = input("Choose a name for the txt file\n: ")+".txt"
            view_everything(file_name) # uses function to create new file if it doesn't exist and write to file 
            for line in equations: # prints everything stored in equations list
                print(line)
        elif choice == 'e': # exits the program
            exit()
        else: # loops until correct input for choice
            print("Incorrect input. Please enter c or va")
            
            
            
    
        