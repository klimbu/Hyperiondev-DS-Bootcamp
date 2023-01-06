'''
Compulsory Task 2 - Psuedocode
	ask input from the user for the following information:
		name, age, house number, street name
	store the results in the corresponding variables:
		name, age, house number, street name
	print out the details of the user in a friendly sentence.

'''
name = input("What is your name? ")
old = str(input("How old are you? "))
house_number = str(input("What is your house number? "))
street_name = input("What is your street name? " )
friendly_sentence = f"Hello {name}. So you are {old} years old. And your address is {house_number} {street_name}."
print(friendly_sentence)