'''
sample = 'google.com'
dictionary = {}

Store each letter in the dictionary including the number of occurences in the sample string
Using Loops: 
	Count the occurences of each character in sample
	Store it in the format "g": 'count' of occurences for each character
	Remove duplicates if any 
	Store it in dictionary format
Print the results

'''

sample = 'google.com'
diction = {} #final storage variable
list_dict = [] #stores all characters in sample in format 'g','o','o'...
count_dict = [] #stores occurences of each character in format '2','3','3'....

for i in sample: #for every character in sample stores characters and their count/occurences in seperate lists 
    list_dict.append(i) #outputs: ['g', 'o', 'o', 'g', 'l', 'e', '.', 'c', 'o', 'm']
    count_dict.append(sample.count(i)) #outputs: [2, 3, 3, 2, 1, 1, 1, 1, 3, 1]

for i in range(len(list_dict)): #for every index in list_dict 
    diction[list_dict[i]] = count_dict[i] #stores in dictionary in the format {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
print(diction)
# I thought the program would have duplicates but it seems that this method doesn't make duplicates.