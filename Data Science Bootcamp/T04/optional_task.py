import math
'''
Optional Bonus Task - pseudo code
	keeping in mind that the formula for "area" is √(s(s-a)*(s-b)*(s-c))
	and the formula for s = (side1 + side2 + side3)/2 


	ask user for the lengths of three sides of a triangle
	store it in the following variables
		a, b, c
	
 	create variable called "s" which calculates the total of a,b,c divided by 2
	
	the formula for "area" is √(s(s-a)*(s-b)*(s-c))
	create the following variables:
		a1, a2, area
	in a1 calculate s(s-a)*(s-b)*(s-c)
	in area calculate the sqrt of a1
 
	print out "The area of the triangle is {area} m^2"
'''

a = int(input("What are the three lengths of the triangle? \na = "))
b = int(input("b = "))
c = int(input("c = "))

s = (a+b+c) / 2
# calculates s integral for calculating the area of the triangle

a1 = s*((s-a)*(s-b)*(s-c))

# previously I had another part a2 which multiplied s by a1 which separately calculated ((s-a)*(s-b)*(s-c))
# this resulted in a vastly lower area of the triangle which gave the incorrect result as I found out after doing some calculations on online triangle area calculators 

area = round(math.sqrt(a1), 2)
# rounding to 2 decimal places prevents calculation from looking messy 

print(f"The area of the triangle is {area}m\u00b2")
