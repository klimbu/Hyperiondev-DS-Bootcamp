'''
create following variables:
	countdown = 20
while countdown != 0
	countdown -= 1
	print (countdown)
for i in range(1, 20)
	if i%2==0:
		print (i)
create variable:
	star = "*"
for i in range(0,5)
	star.add("*")
	print (star)
ask input for the two positive integers
	add math module
	use math.gcd(num1, num2)
'''
import math

countdown = 20

while countdown != 0:
	print(countdown) # countdown from 20 to 0
	countdown -= 1
	if countdown == 0: # without if statement countdown only goes up to 0
		print("0")
print ("")

for i in range(1, 20):  #all even numbers between 1 and 20 (not including 20)
	if i%2==0:
         print(i)
print("")
        
star = "*"
for i in range(0,5):
    print (star)
    star = star + ("*") # adds * to string every iteration
print ("")    

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"The GCD or HCF of {num1} and {num2} is {math.gcd(num1, num2)}")    
# math.gcd function finds the GCD or HCF through math module