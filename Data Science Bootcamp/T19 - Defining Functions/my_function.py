''' 
function 1 - prints out all days of the week
	- create function that simply prints out all days of the week
function 2 - replaces every 2nd word in a sentence with hello
	- use loop, .split(), index and %
'''

def days(): #just playing with spacing in this function
    print(''' 
				Monday
				Tuesday
				Wednesday
				Thursday
				Friday
				Saturday
				Sunday
          ''')

days()

test = "create function that simply prints out all days of the week"
def replace(string):
    line = string.split()
    for i in range(len(line)):
        if i%2==1:
            line[i] = "Hello"
    print(line)

replace(test)