'''
Open and Read File 'input.txt'

lines = file.read().

Count number of characters, words, lines in the file.
	characters - use len()
	words - use split() and then len()
	lines - user split('.') and then len()
Count total number of vowels (a, e, i, o, u)
	Create a for loop (characters)
		create variables:
			total, a, e, i, o, u
		Use if statements to count every instance of the vowels
		total will add all instances of the vowels
Display results.

'''

with open('Data Science Bootcamp\T14\input.txt', 'r') as file:
    lines = file.read()
    
    characters = lines #stores all of lines
    words = lines.split() #separates into words
    lines = lines.split('.') #separates into lines
file.close()

print(f''' 
Total number of characters = {len(characters)}. 
Total number of words = {len(words)}.
Total number of lines = {len(lines)}.
		''')	
# Assuming characters include spaces.

total = 0 #total number of vowels
a = 0 #for each instance of each vowels
e = 0
i = 0 #realized i was using for i and I had to change it to ind to get a proper number
o = 0
u = 0

for ind in range(len(characters)): #for every index check for vowels and add to count if its a vowel
    if characters[ind] == 'a':
        a += 1
    elif characters[ind] == 'e':
        e += 1
    elif characters[ind] == 'i':
        i += 1
    elif characters[ind] == 'o':
        o += 1
    elif characters[ind] == 'u':
        u += 1

# sum of all vowels and displaying results
total = a + e + i + o + u 
print(f'''
Total instances of vowels = {total}.
Total a = {a}.
Total e = {e}.
Total i = {i}.
Total o = {o}.
Total u = {u}.
'''
)