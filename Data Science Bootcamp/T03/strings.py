'''
Compulsory Task 1 - Pseudocode
	create variable named "hero" that contains the value "$$$Superman$$$"
	create a new variable named "superhero" 
 	in "superhero" use the strip string method to remove the $'s from "hero"  
	print out "superhero" and the output should be "Superman"
'''

hero = "$$$Superman$$$"
superhero = hero.strip("$")
print(superhero)