'''
ask input for the year
	input_year = int (input(''))
ask input for the number of years 
	year_range = int (input(''))
for i in range(0, year_range):
	if (year+year_range)%4==0:
		print (input_year+i) is a leap year
	else:
        print (input_year+i) is not a leap year
'''

input_year = int (input('Enter a year to check for leap years:\n'))
year_range = int (input('How many years do you want to check?\n'))
print("") # for cleaner output

for i in range(0, year_range):
    if (input_year+i)%4==0:
        print(f"{input_year+i} is a leap year.") # for leap years
    else:
        print (f"{input_year+i} is not a leap year") # for non-leap years