'''
ask user input and store the result
	user_input
create int variable to store len value of user_input divided by 2
	int_palin = len(user_input)/2
create following variables:
	palin1 = user_input[0:int_palin]
	palin2 = user_input[-1:int_palin]
if palin1 == palin2:
	print "Your word is a palindrome"
else
	print "Your word is not a palindrome"

'''

user_input = input("Enter a string: \n").lower()
int_input = len(user_input) #for guidance on input length
int_palin = int(len(user_input)/2) #for guidance to mirror line/ middle point
palin1 = '' #empty variables to be used in conditional statements
palin2 = ''

# when doing psuedocode - didn't account for odd of even len() 
 
if int_input%2==0: #if input len is even use this statement
    palin1 = user_input[0:int_palin]
    palin2 = user_input[int_palin:int_input] 
    palin2 = palin2[::-1] #reversing palin2 to check for palindrome 
    if palin1 == palin2: #if the letters are same then its a palindrome
	    print("Your word is a palindrome.")
    else:
        print("Your word is not a palindrome")

# running into random indentation errors with pylance extension in vscode- disabling/uninstalling it makes it works
# its becoming very annoying getting errors that make no sense 
        
elif int_input%2==1: #if input len is odd use this statement
    palin1 = user_input[0:int_palin]
    palin2 = user_input[int_palin+1:int_input] #ignores the middle letter (odd one out) as the other letters are used to check for palindrome
    palin2 = palin2[::-1]
    if palin1 == palin2: #if the letters are same then its a palindrome
	    print("Your word is a palindrome.")
    else:
        print("Your word is not a palindrome")