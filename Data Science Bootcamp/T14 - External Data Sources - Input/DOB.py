'''
Open and read File DOB.txt
File.Read and split all the text into its own index in a list
As names use 2 index spaces and DOB uses 3 index spaces 
	The plan is to create a loop that will separate the names and DOB into separate indexes

Separate each sentence into its own list (e.g. 'Full names DOB', ...)
Create a while/for loop for that list 
	create a nested loop for each sentence in the list that will:
		Separate the first 2 index items as Names
		Separate the last 3 index items as DOB
The idea is to use loops to do this for every sentence in the list 
Display results.
'''
# Had some trouble opening the file using just 'DOB.txt' and had to experiment with file path to open it up
with open('Data Science Bootcamp\T14\DOB.txt', 'r') as file:
    lines = file.read()
    
    temp = lines.split(',') #Splits everything into a sentence using ','
    temp_split = [] #list variables to be used as storage
    full_names= []
    dob = []
    
    '''EXPERIMENTED CODES: Test coding for before loop to check how and if it works
    
    temp_split = temp[0].split()
    print(temp_split)
    full_names = temp_split[0] + " " + temp_split[1]
    dob = temp_split[2] + " " + temp_split[3] +" " + temp_split[4]
    print(full_names)
    print(dob)
    '''
    
    for i in range (len(temp)): #for every i in the list temp 
        temp_split = temp[i].split() #splits every word into its own index like this ['Orville', 'Wright', '12', 'July', '1998']
        temp_name = " ".join(temp_split[0:2]) #takes the name (0) and surname (1) and joins them using space like this ['Orville Wright']
        full_names.append(temp_name) #adds to the list full_names
        temp_dob = " ".join(temp_split[2:]) #joins the dates (index 2,3,4) e.g. ['12 July 1998']
        dob.append(temp_dob) #adds to the list dob
        
        '''EXPERIMENTED CODES: tried doing a nested for loop - didn't really work
        
        for i in range (len(temp_split)):
            full_names = list(temp_split[0] + " " + temp_split[1])
            dob = list(temp_split[2] + " " + temp_split[3] +" " + temp_split[4])
		'''
    print('Name:')
    for i in range(len(full_names)): #for every i in full_name
        print(full_names[i]) #prints all names out
    
    print('Birthdate:') 
    for i in range(len(dob)): #for every i in dob
        print(dob[i]) #prints all dob out        
    file.close()