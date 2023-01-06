import math
'''
Compulsory Task 1 - pseudo code
	ask user input for 3 different integers and store them on the following variables:
		num1, num2, num3
	create the following variables:
	  	maths1, maths2, maths3, maths4
	in maths1 sum all three numbers 
	in maths2 calculate num1-num2
	in maths3 calculate num3*num1
	in maths4 calculate sum of all three numbers/num3
	print out maths1, maths2, maths3, maths4 in seperate lines
'''

# casting int() prevents python from mistaking the variables as strings
num1= int(input("Enter an integer: "))
num2= int(input("Enter a different integer: "))
num3= int(input("Enter a different 2integer: "))
maths1 = num1+ num2+ num3
maths2 = num1 - num3
maths3 = num3 * num1
maths4 = maths1 / num3
print(f"{maths1} \n{maths2} \n{maths3} \n{maths4}") # using f"" saves space