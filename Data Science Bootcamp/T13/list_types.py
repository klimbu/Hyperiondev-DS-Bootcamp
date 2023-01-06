'''
create a list variable with 3 full names
friends_names = ['Cam Ron', 'Zac Styles', 'Wright Byron']

print 1st friends full name
print last friends full name
print len(friends_names)

create a list variable with ages of friends in corresponding order
friends_ages = ['24', '25', '23']
	for i in range(len(friends_names)):
		print(f"{i}: This is {friends_names[i]} and they are {friends_ages[i]} years old.")
'''

friends_names = ['Cam Ron', 'Zac Styles', 'Wright Byron'] #3 full names

print(friends_names[0])
print(friends_names[2])
print(len(friends_names))

friends_ages = ['24', '25', '23'] #corresponding ages

#task doesn't really tell what to do with the 2nd list so I put it to use in the below for loop

for i in range(len(friends_names)): #for every i in the list print name and age of each person
    print(f"{i}: This is {friends_names[i]} and they are {friends_ages[i]} years old.")