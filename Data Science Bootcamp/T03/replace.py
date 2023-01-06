'''
Compulsory Task 2 - Pseudocode
	create a string variable named "messy" with the value “The!quick!brown!fox!jumps!over!the!lazy!dog!.”
	create a new variable named "neater" 
		use the replace function to replace the "!" with a black space " "
	print out "neater" and the output should be "The quick brown fox jumps over the lazy dog."
	create a new variable named "capital"
		use the upper function to capitalize the whole sentence
	print out "capital" and the output should be "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG."
	using the index [-1] print out "neater" in reverse order
'''

messy = "The!quick!brown!fox!jumps!over!the!lazy!dog!."
neater = messy.replace("!", " ")
# it prints out "The quick brown fox jumps over the lazy dog ." so I want to remove that space before the full stop
# experimentation using strip function and creating a new string variable and adding the full stop -> result = fail
# experimentation 2 using indexing to replace the blank space with the full stop -> result = success
neater2 = neater[0:len(neater)-2]
neater3 = neater2 + "."
print(neater3)

capital = neater3.upper()
print(capital)
print(neater3[len(neater3)::-1])
# experimented using index to output complete reverse sentence as I was having trouble with outputting the "T" 