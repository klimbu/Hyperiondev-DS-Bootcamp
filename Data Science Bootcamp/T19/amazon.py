''' 
read file input.txt
use split(), and slicing to separate the string and integers

create functions for min, max, avg

write to file output.txt
'''
def minim(minimum): #calculate minimum
    minim = min(minimum)
    return minim

def maxim(maximum): #calculates maximum
    maxim = max(maximum)
    return maxim

def average(value): #calculates average
    total = 0
    avg = 0
    for i in value:
        total = total + i
    avg = total/len(value)
    return avg

def intlist(oldlist, newlist): #converts string list with numbers to integer list
    old = oldlist.split(',')
    for i in range (len(old)):
        if old[i] not in newlist:
            newlist.append(int(old[i]))
    return newlist

with open ('input.txt', 'r', encoding='utf-8-sig') as file: #encoding gets rid of the symbols at the start of the file reading
    line = file.read() #reads whole file
file.close()

lines = line.split('\n') #separates by new line
new = [] #stores strings
num = [] #stores numbers

for i in range (len(lines)):
	newlines = lines[i].split(':') #to separate string and integers
	for i in range(len(newlines)):
		if i%2==0: #separates strings and numbers to separate lists
			new.append(newlines[i]) #stores string min, max, avg
		else:
			num.append(newlines[i]) #stores the numbers
minl = []
maxl = []
avgl = []

intlist(num[0], minl) #using my function made to deal with the nested lists
intlist(num[1], maxl) #handles any length of input numbers 
intlist(num[2], avgl)
# not sure if this is probably the way to go in terms of the criteria - handling any combination of operations

with open ('output.txt', 'w', encoding='utf-8-sig') as file: #writing to output.txt
    file.write(f'''The min of {minl} is {minim(minl)}. 
The max of {maxl} is {maxim(maxl)}. 
The avg of {avgl} is {average(avgl)}.''')
file.close()

