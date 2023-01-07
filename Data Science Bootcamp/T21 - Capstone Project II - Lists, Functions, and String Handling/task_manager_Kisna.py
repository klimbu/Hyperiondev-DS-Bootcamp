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
    while True:
        new_username = input("\nEnter username : ")
        if len(new_username)<=2:
            print("\nInput length less than 3 characters, Please enter a longer name.")
        elif new_username in usernames:
            print("\nThis username already exists in the database. Try a different username.")
        else:
            usernames.append(new_username)
            break
    while True:
        new_password = input("\nEnter password : ")
        confirm_password = input("Confirm password : ")
        if confirm_password == new_password:
            file = open('user.txt', 'a')
            file.write(f"\n{new_username};{new_password}")
            print("New user added!")
            file.close()
            break
        else:
            print("\n Passwords do not match. Try Again.")
#==============================================================================================================================================

def add_task():
    print("\n Adding a task: ")
    while True:
        assigned_user = input("Enter assigned user : ")
        if assigned_user not in usernames:
            print("User does not exist, enter a valid username.")
        elif len(assigned_user)<3:
            print("\nInput length less than 3 characters, enter a valid input.")
        else:
            break
    while True:
        title = input("Enter task title : ")
        if len(title)<3:
            print("\nInput length less than 3 characters, enter a valid input.")
        else:
            break
    while True:
        desc = input("Enter description : ")
        if len(desc)<3:
            print("\nInput length less than 3 characters, enter a valid input.")
        else:
            break
    start_date = date.today()
    print(f"Starting date of the task : {start_date}")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")
    completed = 'No'
    
    new_task = {
        "username": assigned_user,
        "title": title,
        "description": desc,
        "due_date": due_date,
        "assigned_date": start_date,
        "completed": completed
    }
    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")
    
#==============================================================================================================================================

def view_all():
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

def view_mine():
	
    print(f"\n Viewing Tasks for {user_name}")
    for num, t in enumerate(task_list):
        if user_name == t['username']:
            disp_str = f"Task {num}: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Complete? \t {t['completed']}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)
    
    while True:
        t_num = int(input("Enter the task number you would like to edit or -1 to return to the main menu\n:"))
        if t_num <= len(task_data)-1:
            view = task_data[t_num].split(';')
            if t_num == -1:
                return
            elif user_name == view[0]:
                select = input("Enter 'm' to mark the task as complete or 'ed' to edit the task\n:").lower()
                if select == 'm':
                    view[5] = "Yes"
                    task_list[t_num]['completed'] = True
                    change = ';'.join(view)
                    task_data[t_num] = change
                    file = open("tasks.txt", 'w')
                    for i in task_data:
                        file.write(i+"\n")
                    file.close()
                    break
                elif select == 'ed':
                    while True:
                        assign_user = input("Enter the user you would like to assign this task to: \n")
                        if assign_user not in usernames:
                            print("User does not exist, enter a valid username.")
                        else:
                            break
                    while True:
                        try:
                            task_due_date = input("Due date of task (YYYY-MM-DD): ")
                            due_date = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                            break
                        except ValueError:
                            print("Invalid datetime format. Please use the format specified")
                    view[0] = assign_user
                    task_list[t_num]['username'] = assign_user
                    view[3] = task_due_date
                    task_list[t_num]['due_date'] = task_due_date
                    
                    change = ';'.join(view)
                    task_data[t_num] = change
                    file = open("tasks.txt", 'w')
                    for i in task_data:
                        file.write(i+"\n")
                    file.close()
                    break
        else:
            print("Incorrect input. Please use the format specified or choose the task assigned to you.")
#==============================================================================================================================================

def percentage(figure, total):
    if figure==0 or total==0:
        return f'0%'
    else:
        return f'{round((figure / total * 100), 2)}%'

#==============================================================================================================================================

def t_dt():
    with open("tasks.txt", 'r') as task_file:
        task_dt = task_file.read().split("\n")
        task_dt = [t for t in task_dt if t != ""]
        task_file.close()
    return task_dt

#==============================================================================================================================================

def today_date():
    toda = str(date.today())
    t_date = datetime.strptime(toda, DATETIME_STRING_FORMAT)
    return t_date

#==============================================================================================================================================

def generate_task_overview():    
    total_tasks = len(t_dt())
    task_completed = 0
    task_overdue = 0
    for t in range(len(t_dt())):
        view = t_dt()[t].split(';')
        due_date = datetime.strptime(view[3], DATETIME_STRING_FORMAT)
        if view[5] == 'Yes':
            task_completed += 1
        elif today_date()>due_date:
            task_overdue += 1
    task_incomplete = total_tasks - task_completed
    
    with open('task_overview.txt', 'w') as test:
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
        test.write(to_write_overview)
        test.close()

#==============================================================================================================================================

def each_user(name, list):
    no_of_tasks = 0
    tasks_complete = 0
    tasks_incomplete = 0
    tasks_overdue = 0    
    for i in range (len(list)):
        name_in_list = list[i].split(';')
        due_date = datetime.strptime(name_in_list[3], DATETIME_STRING_FORMAT)
        if name in name_in_list[0]:
            no_of_tasks += 1
            if name_in_list[5] == 'Yes':
                tasks_complete += 1
            else:
                if today_date()>due_date:
                    tasks_overdue += 1
    tasks_incomplete = no_of_tasks - tasks_complete
    return f"""\nUser: {name}
Total numbers of tasks assigned:        {no_of_tasks}
% share of the total tasks assigned:    {percentage(no_of_tasks, len(list))}
% of tasks completed:                   {percentage(tasks_complete,no_of_tasks)}
% of tasks not complete:                {percentage(tasks_incomplete,no_of_tasks)}
% of tasks not complete and overdue:    {percentage(tasks_overdue,no_of_tasks)}
-----------------------------------------------------------------------------------------------------"""

#==============================================================================================================================================

def generate_report():
    generate_task_overview()
    num_user = open("user.txt", "r")
    n_users = num_user.read().split('\n')
    num_users = len(n_users)
    num_tasks = len(task_list)
    
    with open ('user_overview.txt', 'w') as test:
        test.write(f"""
User Overview Report
Date: {date.today()}
-----------------------------------------------------------------------------------------------------
Total Number of users: \t\t {num_users}
Total Number of tasks: \t\t {num_tasks}
-----------------------------------------------------------------------------------------------------""")
        for i in range(len(usernames)):
            test.write(each_user(usernames[i], t_dt())) 
        test.close() 

#============================================================================================================================================== 
        
def display_statistics():
    if not os.path.exists("task_overview.txt"):
        with open("task_overview.txt", "w") as default_file:
            pass
    if not os.path.exists("user_overview.txt"):
        with open("user_overview.txt", "w") as default_file:
            pass
    
    generate_report()
    
    t_overview = open('task_overview.txt', 'r')
    print(t_overview.read())
    file.close()
    u_overview = open('user_overview.txt', 'r')
    print(u_overview.read())
    file.close()
    
#======================================================== TASK LIST ======================================================================================

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

usernames = []
passwords = []

file = open('user.txt', 'r')

for lines in file:
    temp = lines.strip()
    temp = temp.split(';')
    
    usernames.append(temp[0])
    passwords.append(temp[1])

file.close()

logged_in = False

while not logged_in:
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
if user_name == "admin":
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
else:
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
        elif menu == 'ds' and user_name == 'admin':
            display_statistics()
        elif menu == 'e':
            print('Goodbye!!!')
            exit()
        else:
            print("You have made a wrong choice, Please Try again")