'''
ask input for the price of package they would like to purchase
ask input for total distance of the delivery in kms
ask input for air or freight as delivery preference
	if preference is air
		calculate distance x R0.36 per km
		add to cost of delivery
	else if preference is freight
		calculate distance x R0.25 per km
		add to cost of delivery
ask input for preference on full or limited insurance
	if preference is full insurance
		add R50.00 to cost of delivery
	else if preference is limited insurance
		add R25.00 to cost of delivery
ask input to check whether the delivery is a gift or not
	if delivery is a gift 
		add R15.00 to cost of delivery
	else
        add R0.00 to cost of delivery
ask input for preference on priority or standard delivery
	if preference is priority delivery
        add R100.00 to cost of delivery
	else preference is standard delivery
        add R20.00 to cost of delivery
calculate the total cost of the package based on all selection
'''

package_price = int(input("Please enter the price of the package you would like to purchase: R"))
# experimenting with using (or) in the if statements made the program not work properly  

delivery_distance = int(input("Please enter the total distance of the delivery(km): "))

delivery_preference = input("Would you like the 'air' or 'freight' delivery? ").lower()
# lower makes the input match whether lower or uppercase letters   
if delivery_preference == 'air':
# using '' to guide correct input 
    package_price = package_price + (delivery_distance*0.36)
elif delivery_preference == 'freight':
    package_price = package_price + (delivery_distance*0.25)
else:
	print("You have not specified the listed delivery preference. Please try again.") 
	exit()
# terminates program due to invalid input

insurance = input("Would you like 'full' insurance or 'limited' insurance for the package? ").lower()
if insurance == 'full':
    package_price = package_price + 50.00
elif insurance == 'limited':
    package_price = package_price + 25.00
else:
    print("You must enter either 'full insurance' or 'limited insurance'. Please try again.")
    exit()

gifting = input("Is this a gift ('Yes'/'No')? ").lower()
# guiding input
if gifting == 'yes':
    package_price = package_price + 15
elif gifting == 'no':
    package_price
    # do nothing
else:
	print("You must enter either 'yes' or 'no'. Please try again.")
	exit()

priority_delivery = input("Would you like the 'priority' or 'standard' delivery service? ").lower()
if priority_delivery == 'priority':
    package_price = package_price + 100
elif priority_delivery == 'standard':
    package_price = package_price + 20
else:
    print("You must enter either 'priority' or 'standard'. Please try again.")
    exit()
print(f"The total cost of the package is R{round(package_price, 2)}")
# using f"" and rounding for simple and concise programming 