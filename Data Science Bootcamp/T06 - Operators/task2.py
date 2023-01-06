'''
Ask user input for the shape of the building
Based on the input ask user input for length, width or radius etc
	if input is square
		ask input for length
		calculate area of square = length^2
		display area of square
	elif input is rectangle
		ask input for length and width
		calculate area of rectangle = length x width
		display area of rectangle
	elif input is circle
        ask input for radius
		calculate area of circle = pi*radius^2
		display area of circle
	else
        display error
'''
# import math for math.pow() and math.pi for calculations
import math 

building_shape = input("What is the shape of the building (square, rectangle, round)? \n").lower()

if building_shape == 'square':
    length = int(input("What is the length of the building? "))
    area = math.pow(length, 2)
    # calculating length**2 
    print("The area of the building is {} m\u00b2".format(round(area, 2))) #\u00b2 useful for formatting the text
    # using round to show answer to nearest 2 decimal places

# using elif and the same format for the next two shapes 
    
elif building_shape == 'rectangle':
    length = int(input("What is the length of the building? "))
    width = int(input("What is the width of the building? "))
    area = length*width
    print("The area of the building is {} m\u00b2".format(round(area, 2)))

elif building_shape == 'round':
    radius = int(input("What is the radius of the building? "))
    area = math.pi*(math.pow(radius, 2))
    print("The area of the building is {} m\u00b2".format(round(area, 2)))

else:
    print("Incorrect input. Please try again.")
    # in case user input is not within the range of the conditional statements above