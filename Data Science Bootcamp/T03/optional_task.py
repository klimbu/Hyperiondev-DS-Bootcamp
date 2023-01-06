'''
Optional Bonus Task - pseudo code
	ask user for input on his favorite restaurant
	store it in variable called "fav_res"
	ask user for input on his favorite number
	store it in variable called "int_fav"
	print out "fav_res" and "int_fav" separately
	cast "fav_res" to an integer in a variable called "transform"
	explain the result using comments
'''
fav_res = input("What is your favorite restaurant? ")
int_fav = input("What is your favorite number? ")
print(fav_res)
print(int_fav)
transform = int(len(fav_res))

'''
result = ValueError: invalid literal for int() with base 10

Experiment using plain numbers for fav_res input was successful.
Experiment using len(fav_res) was also successful.
Experiment using combinations of numbers and letters was unsuccessful.
Therefore, int() only works with numbers as it is not logically possible to covert letters into numbers unless 
each letters had a corresponding number equivalent in which case it might work.  
'''