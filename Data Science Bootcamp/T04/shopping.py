import math
'''
Compulsory Task 2 - pseudo code
	ask user input for the names of three products 
	store it in the following variables:
		name_product1, name_product2, name_product3
	ask user input for the prices of each products in the format:
		"what is the price of {variables}? "
	store it in the following variables:
		price_product1, price_product2, price_product3
	create variable called "total_price" which calculates the total of all three products
	create variable called "average" which calculate the average price of all three products and use round to the nearest 2 decimal places 
	print out "The total of name_product1, name_product2, name_product3 is total_price"
	print out "The average price of name_product1, name_product2, name_product3 is average_price"
'''
name_product1 = input("What are the name of three products in your shopping list? \n1: ")
name_product2 = input("2: ")
name_product3 = input("3: ")

price_product1 = float(input(f"What is the price of {name_product1}? "))
price_product2 = float(input(f"And {name_product2}? "))
price_product3 = float(input(f"And {name_product3}? "))
# using float instead of int in case of prices with decimal points

total_price = price_product1 + price_product2 + price_product3
average = total_price/3 
print(f"The total price of {name_product1}, {name_product2}, {name_product3} is ${round(total_price, 2)}.")
print(f"The average price of {name_product1}, {name_product2}, {name_product3} is ${round(average, 2)}.")

# using round to make the calculation look neat by limiting the decimal point to 2.