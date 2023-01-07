''' PSEUDO CODE
make functions for each user option
	- register
	- adding new task
	- view all
	- view mine
	- display stats
	- generate reports 

create menu for user to follow
	- defensive programming to make sure they do not enter incorrect menu options
	- display separate menus for if admin is logged in or another is logged in
 
 creating register user functions
	- request user to enter new username
 	- request user to enter new password
	 	- if username already exists within out db, request they try again
	- save username and password combination to user.txt
	- return to menu
 
creating add task function
	- request details of the task from user
	- make sure that the start date and due date of the task are in the correct format
		- the datetime module python provides is very useful in this regard
	- once the data has been collected, save to tasks.txt
	- return to menu

creating view all functions
	- open tasks.txt
	- iterate through the lines and then using formatting / styling to display each 
 		task in a neat and easy to read manner
	- print out tasks to the user
	- once complete ask user if they would like to return to menu

creating view mine function
    - iterate through the lines and then using formatting / styling to display each 
 		task in a neat and easy to read manner
	- print out tasks to the user - each task having its own number
    - ask user if they would like to edit task based on task number
        - ask if they want task to be completed 
            - mark task as completed and write/change it
        - or if they want to edit the task
            - edit the task and replace it with the edited task (task number)
        - provide -1 option to return to choice selection

creating generate reports functions
    - generate two text files
        - task_overview.txt
        - user_overview.txt
    - task_overview should contain
        - total number of tasks generated and tracked using tm.py
        - total number of tasks completed
        - total number of tasks not completed and overdue
        - % of tasks incomplete
        - % of tasks overdue
    - user_overview should contain
        - total number of users registered with tm.py
        - total number of tasks generated and tracked using tm.py
        - for each user 
            - total number of tasks assigned to that user
            - % of total number of tasks that have been assigned to that user
            - % of tasks assigned to that user that have been completed
            - % of tasks assigned to that user that must still be completed
            - % of tasks assigned to that user that have not been completed and overdue

creating display stats functions
    - display generated reports from task_overview.txt and user_overview.txt
    - if the files don't exist then call the code to generate the text files

'''
#==============================================================================================================================================

import os
from datetime import datetime, date
DATETIME_STRING_FORMAT = "%Y-%m-%d"

#==============================================================================================================================================

def reg_user(): 
    while True: #keeps repeating until correct input
        new_username = input("\nEnter username : ")
        if len(new_username)<=2:
            print("\nInput length less than 3 characters, Please enter a longer name.")
        elif new_username in usernames:
            print("\nThis username already exists in the database. Try a different username.")
        else:
            usernames.append(new_username)
            break
    while True: #keeps repeating until correct input
        new_password = input("\nEnter password : ")
        confirm_password = input("Confirm password : ")
        if confirm_password == new_password: # keeps repeating until both passwords are same
            file = open('user.txt', 'a') # opens file for append operation
            file.write(f"\n{new_username};{new_password}") # adds username and password to the database
            print("New user added!")
            file.close()
            break
        else:
            print("\n Passwords do not match. Try Again.") # loops back until both passwords match
#==============================================================================================================================================

def add_task():
    print("\n Adding a task: ")
    while True: #keeps repeating until correct input
        assigned_user = input("Enter assigned user : ")
        if assigned_user not in usernames: # if invalid input detected loops back to input
            print("User does not exist, enter a valid username.")
        elif len(assigned_user)<3:
            print("\nInput length less than 3 characters, enter a valid input.")
        else:
            break
    while True: #keeps repeating until correct input
        title = input("Enter task title : ")
        if len(title)<3: # if invalid input detected loops back to input
            print("\nInput length less than 3 characters, enter a valid input.")
        else:
            break
    while True: #keeps repeating until correct input
        desc = input("Enter description : ")
        if len(desc)<3: # if invalid input detected loops back to input
            print("\nInput length less than 3 characters, enter a valid input.")
        else:
            break
    start_date = date.today()
    print(f"Starting date of the task : {start_date}")
    while True: #keeps repeating until correct input
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")
    completed = 'No'
    # mostly original base code 
    new_task = { # to add to task_file
        "username": assigned_user,
        "title": title,
        "description": desc,
        "due_date": due_date,
        "assigned_date": start_date,
        "completed": completed
    }
    task_list.append(new_task) # updates task_list with the new task
    
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [ # changes formats - joining only values together for writing to file
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs)) # joins using ';'
        task_file.write("\n".join(task_list_to_write)) # writes to file
    print("Task successfully added.")
    
#==============================================================================================================================================

def view_all(): # prints out all of task_file and enumerates them
    print("\n Viewing all tasks:")
    for num, t in enumerate(task_list):
        disp_str = f"Task {num}: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Complete? \t {t['completed']}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)
        
#==============================================================================================================================================

def view_mine(): # prints out the whole of task_file so its important to update task_file as well as the txt files
	
    print(f"\n Viewing Tasks for {user_name}")
    for num, t in enumerate(task_list): # {num} used for finding tasks for editing 
        if user_name == t['username']:
            disp_str = f"Task {num}: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Complete? \t {t['completed']}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)
    
    while True: #keeps repeating until correct input
        t_num = int(input("Enter the task number you would like to edit or -1 to return to the main menu\n:"))
        if t_num <= len(task_data)-1:
            view = task_data[t_num].split(';') # selects the line for editing and splits 
            if t_num == -1: #returns to menu
                return 
            elif user_name == view[0]: # if the user name matches the selected task username - proceed 
                select = input("Enter 'm' to mark the task as complete or 'ed' to edit the task\n:").lower()
                if select == 'm':
                    view[5] = "Yes" # changes the No to a Yes
                    task_list[t_num]['completed'] = True #updates task_file for view all/ view mine
                    
                    change = ';'.join(view) 
                    task_data[t_num] = change # changes No/False to True/Yes
                    file = open("tasks.txt", 'w') # open file for writing and updates to file using loop
                    for i in task_data:
                        file.write(i+"\n")
                    file.close()
                    break
                elif select == 'ed':
                    while True: #keeps repeating until correct input
                        assign_user = input("Enter the user you would like to assign this task to: \n")
                        if assign_user not in usernames:
                            print("User does not exist, enter a valid username.")
                        else:
                            break
                    while True: #keeps repeating until correct input
                        try:
                            task_due_date = input("Due date of task (YYYY-MM-DD): ")
                            due_date = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                            break
                        except ValueError:
                            print("Invalid datetime format. Please use the format specified")
                    view[0] = assign_user # changes user to the input if its in the database
                    task_list[t_num]['username'] = assign_user # updates the list with nested dictionary
                    view[3] = task_due_date # changes due date in the database
                    task_list[t_num]['due_date'] = task_due_date # updates task_list 
                    
                    change = ';'.join(view) # joins to the standard format
                    task_data[t_num] = change #changed the list with the edited version
                    file = open("tasks.txt", 'w') # opens file for writing
                    for i in task_data: # loop writes code 
                        file.write(i+"\n") # all lines written to file and edited line is updated in the file
                    file.close()
                    break
        else: # repeats until correct input
            print("Incorrect input. Please use the format specified or choose the task assigned to you.")
#==============================================================================================================================================

def percentage(figure, total): #gets the % in proper format
    if figure==0 or total==0: # gets rid of division by zero error issue by returning 0%
        return f'0%'
    else:
        return f'{round((figure / total * 100), 2)}%'

#==============================================================================================================================================

def t_dt(): # for detecting changes in task.txt and used only in generating reports
    with open("tasks.txt", 'r') as task_file:
        task_dt = task_file.read().split("\n")
        task_dt = [t for t in task_dt if t != ""]
        task_file.close()
    return task_dt

#==============================================================================================================================================

def today_date(): # used to calculate date comparisons in ds and gr
    toda = str(date.today())
    t_date = datetime.strptime(toda, DATETIME_STRING_FORMAT)
    return t_date

#==============================================================================================================================================

def generate_task_overview():    # using loop to generate task overview and write to file
    total_tasks = len(t_dt())
    task_completed = 0
    task_overdue = 0
    
    for t in range(len(t_dt())): #using t_dt function to ensure ds updates every time task is edited or marked complete or new user added
        view = t_dt()[t].split(';')
        due_date = datetime.strptime(view[3], DATETIME_STRING_FORMAT)
        if view[5] == 'Yes': # if task is completed 
            task_completed += 1
        elif today_date()>due_date: # if today is past the due date 
            task_overdue += 1
    
    task_incomplete = total_tasks - task_completed
    
    with open('task_overview.txt', 'w') as test: #open file for writing
        to_write_overview = (f'''Tasks Overview: 
Date accessed: {date.today()}
-----------------------------------------------------------------------------------------------------
    Total tasks:                                    | {total_tasks} 
    Total number of tasks completed:                | {task_completed} 
    Total number of tasks not completed:            | {task_incomplete} 
    Total number of tasks overdue and not complete: | {task_overdue} 
    % of tasks not completed:                       | {percentage(task_incomplete, total_tasks)} 
    % of tasks overdue:                             | {percentage(task_overdue, total_tasks)} 
-----------------------------------------------------------------------------------------------------''')
        test.write(to_write_overview) # write the above string to file
        test.close()

#==============================================================================================================================================

def each_user(name, list): #function to iterate over all users and write reports for each user
    no_of_tasks = 0
    tasks_complete = 0
    tasks_incomplete = 0
    tasks_overdue = 0    
    
    for i in range (len(list)): # loop used for counting the above variables
        name_in_list = list[i].split(';')
        due_date = datetime.strptime(name_in_list[3], DATETIME_STRING_FORMAT) # for date comparisons 
        if name in name_in_list[0]: # for name in every task (new line)
            no_of_tasks += 1
            if name_in_list[5] == 'Yes': #for counting completed tasks
                tasks_complete += 1
            else:
                if today_date()>due_date: # using today_date function to enable date comparison
                    tasks_overdue += 1
    
    tasks_incomplete = no_of_tasks - tasks_complete
    # using percentage function for calculating %
    return f"""\nUser: {name}
Total numbers of tasks assigned:        {no_of_tasks}
% share of the total tasks assigned:    {percentage(no_of_tasks, len(list))}
% of tasks completed:                   {percentage(tasks_complete,no_of_tasks)}
% of tasks not complete:                {percentage(tasks_incomplete,no_of_tasks)}
% of tasks not complete and overdue:    {percentage(tasks_overdue,no_of_tasks)}
-----------------------------------------------------------------------------------------------------"""

#==============================================================================================================================================

def generate_report():#generates report using each_user ang generate_task_overview
    
    generate_task_overview() #generates task overview
    
    num_user = open("user.txt", "r") #opens file for reading and updates every time new user is added
    n_users = num_user.read().split('\n')
    num_users = len(n_users)  # using file to get the number of users
    
    num_tasks = len(task_list) #using task_list to get number of tasks
    
    with open ('user_overview.txt', 'w') as test: #opens file for writing
        test.write(f"""
User Overview Report
Date: {date.today()}
-----------------------------------------------------------------------------------------------------
Total Number of users: \t\t {num_users}
Total Number of tasks: \t\t {num_tasks}
-----------------------------------------------------------------------------------------------------""")
        for i in range(len(usernames)): #using each_user to write the user report
            test.write(each_user(usernames[i], t_dt())) 
        test.close() 

#============================================================================================================================================== 
        
def display_statistics():# if files do not exist, create them and generate statistics
    if not os.path.exists("task_overview.txt"):
        with open("task_overview.txt", "w") as default_file:
            pass
    if not os.path.exists("user_overview.txt"):
        with open("user_overview.txt", "w") as default_file:
            pass
    
    generate_report() #uses the function to generate the report
    
    t_overview = open('task_overview.txt', 'r') #simple read and output
    print(t_overview.read())
    file.close()
    u_overview = open('user_overview.txt', 'r') #read and output
    print(u_overview.read())
    file.close()
    
#======================================================== TASK LIST ======================================================================================

#Original snippet of code used
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass
with open("tasks.txt", 'r') as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]
        task_file.close()
        
task_list = []
for t_str in task_data:
    curr_t = {}
    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)

#======================================================= LOGIN SECTION=======================================================================================

usernames = [] #stores usernames
passwords = [] #stores passwords

file = open('user.txt', 'r')

for lines in file:
    temp = lines.strip()
    temp = temp.split(';')
    
    usernames.append(temp[0])
    passwords.append(temp[1])

file.close()

logged_in = False

while not logged_in: #keeps repeating until correct input
    print("LOGIN")
    user_name = input("Username : ")
    pass_word = input("Password : ")
    
    if user_name not in usernames:
        print("Incorrect username...Try again")
    elif pass_word not in passwords:
        print("Incorrect password...Try again")
    else:
        print(f"\nWelcome {user_name}, please make a selection from the menu.")
        logged_in = True

if user_name == "admin": #admin menu selection
    while logged_in: 
        menu = input("""
Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: """).lower()
        
        if menu == 'r':
            reg_user()
        elif menu == 'a':
            add_task()
        elif menu == 'va':
            view_all()
        elif menu == 'vm':
            view_mine()
        elif menu == 'gr' and user_name == 'admin':
            generate_report()
        elif menu == 'ds' and user_name == 'admin':
            display_statistics()
        elif menu == 'e':
            print('Goodbye!!!')
            exit()
        else:
            print("You have made a wrong choice, Please Try again")
else: # non-admin menu
    while logged_in:
        menu = input("""
Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
e - Exit
: """).lower()
        
        if menu == 'r':
            reg_user()
        elif menu == 'a':
            add_task()
        elif menu == 'va':
            view_all()
        elif menu == 'vm':
            view_mine()
        elif menu == 'e':
            print('Goodbye!!!')
            exit()
        else:
            print("You have made a wrong choice, Please Try again")