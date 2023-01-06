'''
ask empty variable for student names
	student_names = ''
create a int variable to store total number of names/students
	total_students = 0
print "Please enter the names of all pupils in your class. Enter Stop when you have finished."
while student_names != "Stop":
	total_students += 1
	student_names = input()

'''

student_name = '' # stores for input
total_students = 0 # stores total number of students

print("Please enter the name of the students in your class. Enter Stop when you have finished")
while student_name != "Stop": #stops when input is Stop
    student_name = input().capitalize() #ensures input is capitalized
    
    if student_name != "Stop": #prevents Stop from being counted as a student 
        total_students += 1
print("Total students: " + str(total_students))