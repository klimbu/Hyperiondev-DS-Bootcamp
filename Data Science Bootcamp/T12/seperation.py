'''
create a variable called sentence
	sentence = "Writing a program that will take a sentence and display each word in separate lines."
use .split function to turn the variable into an index
use a for loop to get the output
for i in range(len(sentence)):
	print(sentence[i])
'''

sentence = "Writing a program that will take a sentence and display each word in separate lines."
sentence = sentence.split()

for i in range(len(sentence)): #for every i in the index sentence - prints each words in separate lines
    print(sentence[i])