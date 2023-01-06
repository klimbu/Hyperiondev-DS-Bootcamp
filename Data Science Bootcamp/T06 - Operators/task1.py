'''
craate the following variables
	num1, num2, num3
assign a number value to each variable
1 - compare num1 and num2
	if num1>num2
		print num1
	else
        print num2
2 - determine if num1 is odd or even
	if num1%2 == 0
		print "{num1} is even"
	else
        print "{num1} is odd"
3 - using conditional statement sort out the three numbers from largest to smallest
	if num3>num1 and num3>num2
    	if num2>num1
			print "{num3} + {num2} + {num1}
		else
			print "{num3} + {num1} + {num2}
	repeat this for num1 and num2
 
'''
import random #wanted to make the code work regardless of the numbers in each variables

num1 = random.randint(0, 99)
num2 = random.randint(0, 99)
num3 = random.randint(0, 99)

# ensures each num variables are random numbers on every test - makes it interesting
print(f'''
      Number 1 = {num1}
      Number 2 = {num2}
      Number 3 = {num3}
      ''')
# just to show the value of each variables


if num1>num2:
	print(num1)
else:
    print(num2)

if num1%2 == 0: #if remainder is 0 the number is even 
    print(f"Number 1 ({num1}) is even")
else:
    print(f"Number 1 ({num1}) is odd")

if num3>num1 and num3>num2:
    if num1>num2:
        print(f"{num3} + {num1} + {num2}")
    else:
        print(f"{num3} + {num2} + {num1}")

# original plan was to use sort but realised it wasn't what I was asked to do so I thought to use nested conditional statements and it worked         

if num2>num1 and num2>num3:
    if num1>num3:
        print(f"{num2} + {num1} + {num3}")
    else:
        print(f"{num2} + {num3} + {num1}")
# doing this for each num variables ensures that the program displays numbers from largest to smallest        
if num1>num2 and num1>num3:
    if num2>num3:
        print(f"{num1} + {num2} + {num3}")
    else:
        print(f"{num1} + {num3} + {num2}")