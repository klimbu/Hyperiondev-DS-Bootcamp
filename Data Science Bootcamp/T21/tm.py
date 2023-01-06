''' 
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
import os
from datetime import datetime, date
DATETIME_STRING_FORMAT = "%Y-%m-%d"

#==============================================================================================================================================

def reg_user():
    while True:
        new_username = input("\nEnter username : ")
        if new_username in usernames:
            print("\nThis username already exists in the database. Try a different username.")
        else:
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
    assigned_user = input("Enter assigned user : ")
    if assigned_user not in usernames:
        print("User does not exist, enter a valid username.")
    title = input("Enter task title : ")
    desc = input("Enter description : ")
    start_date = date.date.today()
    print(f"Starting date of the task : {start_date}")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")
    completed = 'No'
    
    print(f'''This is the task : {title}
User : {assigned_user}
Title : {title}
Description : {desc}
Start Date : {start_date}
Due Date : {due_date}
Completed Status: {completed}
''')
    file = open("tasks.txt", 'a')
    file.write(f"\n{assigned_user};{title};{desc};{start_date};{due_date};{completed}")
    print("New task added")
    file.close()
    
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
        t_num = int(input("Enter the task number you would like to edit or -1 to return to the main menu"))
        view = task_data[t_num].split(';')
        if t_num == -1:
            return
        elif user_name == view[0]:
            select = input("Enter 'm' to mark the task as complete or 'ed' to edit the task").lower()
            if select == 'm':
                view[5] = "No"
                change = ';'.join(view)
                task_data[t_num] = change
                file = open("test.txt", 'w')
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
                view[3] = task_due_date
                change = ';'.join(view)
                task_data[t_num] = change
                file = open("test.txt", 'w')
                for i in task_data:
                    file.write(i+"\n")
                file.close()
                break
        else:
            print("Incorrect input. Please use the format specified.")
#==============================================================================================================================================

# def generate_report():
    

#==============================================================================================================================================
def display_statistics():
    num_users = len(usernames)
    num_tasks = len(task_list)

    print("-----------------------------------")
    print(f"Number of users: \t\t {num_users}")
    print(f"Number of tasks: \t\t {num_tasks}")
    print("-----------------------------------")    
    
#======================================================== TASK LIST ======================================================================================
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

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
    user_name = input("Username : ")
    pass_word = input("Password : ")
    
    if user_name not in usernames:
        print("Incorrect username...Try again")
    elif pass_word not in passwords:
        print("Incorrect password...Try again")
    else:
        print(f"\n Welcome {user_name}, please make a selection from the menu.")
        logged_in = True
if user_name == "admin":
    while logged_in:
        menu = input('''
    Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    gr - Generate reports
    ds - Display statistics
    e - Exit
    : ''').lower()
        
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
else:
    while logged_in:
        menu = input('''
    Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    e - Exit
    : ''').lower()
        
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