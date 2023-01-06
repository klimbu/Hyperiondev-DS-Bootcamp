'''
Compulsory Task 3 - Pseudo code
	ask user for input
 	store it in a variable called "str_manip" 
	use len on "str_manip"
 	store it in a variable called "len_str"
	print out "len_str"
 
	use "len_str" to find last letter in str_manip
	store in a variable called "last" 
	use replace on "str_manip" to replace all of the same letters as "last" with "@"
	store it in a variable called "replacing"
	print out "replacing"
 
	use index on "str_manip" to find last 3 letters in str_manip
	store in a variable called "last3"
	print out "last3"
 
	use index on "str_manip" to find first 3 letters in str_manip and the last 2 characters in str_manip
	store in a variable called "new_word"
    print out "new_word"
    
    test sentence "like dislike like dislike like dislike"
 '''
 
str_manip = input("Enter a sentence to your liking: ")
len_str = len(str_manip) 
print(len_str)

last = str_manip[len_str-1:len_str]
# using -1 on len_str allows us to find the last letter in str_manip 
replacing = str_manip.replace(last, "@")
# replacing every instance of "last" in str_manip with "@"
print(replacing)

last3 = str_manip[len_str-3:len_str]
# using -3 on len_str allows us to find the last 3 letters in str_manip 
print(last3)

new_word = str_manip[0:3] + str_manip[len_str-2:len_str]
# using index to find first 3 and last 2 letters of str_manip
print(new_word)

