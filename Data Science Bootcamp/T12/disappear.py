'''
ask user to input a sentence
	input_sentence = input("")
ask user input for characters they would like removed
create a empty list and store input in that list
	disappear_char = []
disappear_char = input("What characters do you want to remove from this sentence? (Type X to Stop)\n")
while disappear_char != "X":
	disappear_char = input()
	if disappear_char == "X":
        break
use a for loop to loop through the disappear_char list and use strip to remove the characters
for i in range(0, len(disappear_char)):
	input_sentence = input_sentence.strip("disappear_char[i]")

print(input_sentence)	
'''
# I used basic framework of the code but had to implement many little different changes to it 
# the direction was right but had many logical errors which made it difficult for me 

input_sentence = input("Enter a sentence: \n")
input_sentence = input_sentence.lower() #lowercases the input 

disappear_char = '' #input variable 
remove_char = '' 
print("What characters do you want to remove from this sentence? (Type stop to terminate.)")
while disappear_char != "stop":
    disappear_char = input().lower()
    if disappear_char == "stop": # prevents characters in the word 'stop' from being excluded in remove_char
        break
    # tried a nested for loop, nested while loop etc. which didn't work/ output correctly   
    else: # this was not in the pseudocode - spent a lot of time figuring this part out as I experimented with lots of different codes
        remove_char = remove_char + disappear_char #stores all inputs not including 'stop'

for i in range(0, len(remove_char)): #repeats for every index in variable remove_char
    input_sentence = input_sentence.replace(remove_char[i], '')
    # removes every instance of the characters represented by remove_char[i]
    # struggled a lot as I initially thought .strip() would work but it didn't and I spent a lot of time thinking about the current solution
    
print(input_sentence)

# input sentence testing for uppercase, lowercase
# test sentence = What words has X or x in it? 
# disappear_char input = w, x, s, i, r