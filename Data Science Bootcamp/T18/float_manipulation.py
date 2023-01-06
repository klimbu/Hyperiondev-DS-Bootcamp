''' 
import statistics
ask user input for 10 floats
	store in list
find total of the list
	use loop for this
find the index minimum of the list
	use min 
find the index maximum of the list
	use max
find the average of the list rounded to 2 decimal places
	divide total by len()
find the median of the list
	use statistics module for this
print all results
'''
import statistics
user_float = [] #storage for all floats
total = 0 #storage for total calculations
i = 1
while i<=10: #while loop for asking user input
    ask_float = float(input(f"{i}: Enter a float: \n")) #storage & input variable
    user_float.append(float(ask_float)) #appends to list
    total = total + ask_float #calculates total as user input registers 
    i+=1 #increases i counter per input

average = total/len(user_float) #calculates average 

print(f"The total of all numbers is {total}")
print (f"The minimum of all numbers is {min(user_float)}") #using min function
print (f"The maximum of all numbers is {max(user_float)}") #using max function
print (f"The average of all numbers is {round(average,2)}") #using round to limit average to 2 dp
print(f"The median of all numbers is {statistics.median(user_float)}")
#statistics module used for calculating median
