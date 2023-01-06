'''
open files numbers1.txt and numbers2.txt separately 
	read the files and store it into corresponding list indexes
open file all_numbers.txt 
	add numbers1 and number2 to all_numbers index
	use sort to sort numbers from smallest to largest
	write the file to all_numbers.txt
close file

'''
# just using file name wasnt working until I turned on execute in file dir

all_numbers = [] #variables to store information
numbers1 = []
numbers2 = []

with open('number1.txt', 'r') as f: #reads file number1
    lines = f.read()
    lines = lines.split(',') #gets rid of all the ','
    for i in range(len(lines)): #for all index in lines appends to index number1
    	numbers1.append(lines[i].replace(' ', '')) #gets rid of all the random spaces 
f.close()

with open('numbers2.txt') as f: #reads file number1
    lines = f.read()
    lines = lines.split(',')
    for i in range(len(lines)): #for all index in lines appends to index number1
    	numbers2.append(lines[i].replace(' ', ''))
f.close()

# Was having massive issues with using sort() and sorted()
# list looked like this ['2', '3', '4', '5'...]
# The sorted list looked like this ['10', '11', '2', '20', '3', '35', '5' etc...]
# I knew the issue was the '' but I didn't realize that I had to cast it into int until 3-4 hours of struggling



with open('all_numbers.txt', 'w') as f:
    all_numbers = []
    for i in range(len(numbers1)): #for i in index numbers1
        num = int(numbers1[i]) #cast to int and append to list numbers1
#The solution was so simple and I felt like I tried it before but it initially didnt work for some reason
#I simply ruled out casting to int because of that but it was the ultimate solution at the end 
        all_numbers.append(num) 
    
    for i in range(len(numbers2)): 	#for i in index numbers2
        num = int(numbers2[i]) #cast to int and append to list numbers2
        all_numbers.append(num)
          
    sorted_num = sorted(all_numbers) #sorted in order small to large
    
    for i in range(len(sorted_num)): #for i in index sorted_num
        str_con = (f"{str(sorted_num[i])}, ") #cast to string 
        f.write(str_con) #write to file
f.close()
    