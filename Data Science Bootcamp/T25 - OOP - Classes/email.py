#An Email Simulation
''' 
Create Email Class
    create the 4 veriables - spam, read, address, content
    initialise the Email class
    initialise has_been_read and is_spam to false
    create functions:
        mark_as_read
        mark_as_spam
    create list called inbox
        add all Email objects to inbox
Create functions:
    add_email
        create inputs for email address, and email content
        append to inbox
    get_count
        simply get len(inbox)
    get_email
        using for loop and while loop
            ask for index number
                if its<index length
                    print the email
    get_unread_emails
        using for loop and while loop
            check if has_been_read == false
                print all unread emails
    get_spam_emails
        using for loop and while loop
            check if is_spam == True
                print all spam emails
    delete
        using for loop and while loop
            ask for index number to specify which email to delete
                ask final confirmation
                    if y delete email
                    if n return to menu
'''
class Email():
    inbox = [] # class list for all emails

    def __init__(self, address, content, read=False, spam=False):
        self.from_address = address
        self.is_spam = spam 
        self.has_been_read = read 
        self.email_contents = content
        
        Email.inbox.append(self) # watched some OOP for begginer videos and I like how it works
    
    def __repr__(self): # watched some YT videos and found this method
        return f"""
--------------------------------------------------
Email: {self.from_address}
--------------------------------------------------
Spam: {self.is_spam}, Read: {self.has_been_read}
--------------------------------------------------
Content: 
--------------------------------------------------
{self.email_contents}
"""

    def mark_as_read(self): # marks as true - using Email Object 
        self.has_been_read = True
        
    def mark_as_spam(self): # marks as true - using Email Object 
        self.is_spam = True
    
    
def add_email():
    while True: # infinite loop
        address = input("Enter email address: \n")
        if "@" not in address: # checks for @
            print("@ is missing, try again.")
        elif "." not in address: # checks for .
            print(". is missing, try again")
        else:
            break    
    contents = input("Type your message: \n")
    email = Email(address, contents, False, False) #changed to Email(...), originally it was f"string....." - ran into errors doing that
    print("Email has been sent.")

def get_count():
    count = len(Email.inbox) # uses len() instead of for loop
    print(f"There are {count} messages in the inbox.\n")

def get_email():
    while True: #infinite loop
        i = int(input("Enter an index to view the message:\n")) 
        if i<len(Email.inbox): # if input is valid
            print(f"from : {Email.inbox[i].from_address}\nMessage:\n{Email.inbox[i].email_contents}\n")
            Email.inbox[i].mark_as_read() # marks the email as read
            break
        else: # if input is not valid
            print("Incorrect input, please try again.")

def get_unread_emails(): # prints all unread emails
    for i, unread in enumerate(Email.inbox): #for loop using enumerate
        if Email.inbox[i].has_been_read == False: # if False prints all unread emails
            print(f"Email {i}", unread)

def get_spam_emails(): # prints all unread emails
    for i, spam in enumerate(Email.inbox): #for loop using enumerate
        if Email.inbox[i].is_spam == True: # if True prints all unread emails
            print(f"Email {i}", spam)

def mark_as_spam():
    while True:
        i = int(input("Enter an index to view the message:\n")) 
        if i<len(Email.inbox):
            print(Email.inbox[i])
            choice = input("Would you like to mark this message as spam? (y/n)\n")
            if choice == "y":
                Email.inbox[i].mark_as_spam()
                break
            elif choice == "n":
                break   
        else:
            print("Index does not exist, please try again.")
            
def delete():
    while True: # infinite loop
        i = int(input("Enter an index to delete the email:\n"))
        if i<len(Email.inbox): # if input is correct
            print(f'Email {i}: {Email.inbox[i]}') # prints the specific email
            confirm = input("Are you sure you want to delete this email? (y/n):\n").lower()
            if confirm == 'y':
                Email.inbox.pop(i) # deletes from list
                print("This email has been deleted successfully")
                break
            else: # returns to menu
                print("You have chosen not to delete this email")
                break
        else: # error checking
            print("Incorrect index, please try again.")

# list of Email objects with different True and False for spam and read
mail1 = Email('klimbu@gmail.com', 'Wassup Bro', False, False)    
mail2 = Email('george@gmail.com', 'What is happening', True, False)   
mail3 = Email('george@gmail.com', 'What is happening', False, True) 

user_choice = ''
while user_choice != "quit": # simple output using indentation
    user_choice = input('''What would you like to do: 
- send          - mark spam
- read          - get count
- get unread    - get spam 
- delete        - quit?
: ''')
    if user_choice == "read":
        get_email()
    elif user_choice == "get count":
        get_count()
    elif user_choice == "get unread":
        get_unread_emails()
        # ran into issues where after sending an email and trying to check this - ran into error 'str' object has no attribute 'has_been_read'
    elif user_choice == "delete":
        delete()
    elif user_choice == "mark spam":
        mark_as_spam()
    elif user_choice == "get spam":
        get_spam_emails()
    elif user_choice == "send":
        add_email()
    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")
