'''
open file 'reg_form' for writing 
ask user input for the number of students 
	student_no = input
use a loop to store the input for the number of students
	for i in range(student_no):
		stu_id = input()
  		f.write (stu_id)
'''
# just using file name wasnt working until I turned on execute in file dir
# opens file 'reg_form' for writing
with open('reg_form.txt', 'w') as file:
    student_no = int(input("How many students do you want to register? \n"))
    #asks input for number of students
    
    for i in range(student_no): #runs program for x no. of students 
        stu_id = input("Enter ID no.: \n") #takes input
        file.write(stu_id + "\n") #writes input to file with \n for readability

file.close() #close file 