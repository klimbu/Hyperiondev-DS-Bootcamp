'''
create a string variable with a sentence
	alternative_char = "create a string variable with a sentence"
use for loop
for i in range(0, len(alternative_char))
	i = 1
	alternative_char[i].upper()
	i +=2
print(alternative_char)

create another string variable with a sentence
	alternative_words = "create a string variable with a sentence"
	alternative_words = alternative_words.split(" ")
for i in range(0, len(alternative_words))
	i=1
	alternative_words[i].upper()
    i+=2
print(" ".join(alternative_words))
'''
empty = ''
alternative_char = "create a string variable with a sentence"
for i in range(len(alternative_char)):
    if not i%2==0: #for every odd index number in variable alternative_char
        empty = empty + alternative_char[i].upper() #capitalise it
    else: 
        empty = empty + alternative_char[i].lower() #lower case it for every even index number
        
        #Struggled with this one as I tried to do it according to my psuedo code (refer to pseudocode)
        #Ended up using https://www.geeksforgeeks.org/python-alternate-cases-in-string/ 
        #Would have probably gotten to the same solution sooner or later
print(str(empty))

alternative_words = "create a string variable with a sentence"
alternative_words = alternative_words.split()
empty_words = '' #empty string to store the altered sentence
print('') #adding empty line 

for i in range(len(alternative_words)):
    if not i%2==0: #for every odd index in range
        empty_words = empty_words + alternative_words[i].upper() + " " #capitalise and add space
    else: #else every even index in range
        empty_words = empty_words + alternative_words[i].lower() + " " #lower case it and add space
print(str("".join(empty_words)))

# played around with the coding to get the solution this time
# was having issues with using the " ".join as it wasn't printing the space
# output looked like this: createAstringVARIABLEwithAsentence
# finally found the solution which was to add " " at the end of the variables instead of using " ".join