### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email:

    # Declare the class variable, with default value, for emails. 
    has_been_read = False

    # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True

# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox_list = []

# --- Functions --- #
# The required functions for your program.
def populate_inbox():
    # Create 3 sample emails and add it to the Inbox list.
    inbox_list.append(Email('noreply@hyperiondev.com', 'Welcome to HyperionDev!', 
    'You should apply for a jot to complete the Hyperion Bootcamp'''))
    inbox_list.append(Email('teacher@hyperiondev.com', 'Great work on the bootcamp!', 
    'You are doing a great job! We hope you continue this way'))
    inbox_list.append(Email('score@hyperiondev.com', 'Your excellent marks!', 
    'Your answers were amazing. You will finish in a good position'))

def list_emails(only_unread = False):
    # Function which prints the email’s subject_line, along with a corresponding number.
    title = "{:5}|{:40s}|{:8s}|".format("Id", "Subject", "Read?")
    print(title)
    for i, value in enumerate(inbox_list):
        line = "{:5}|{:40s}|{:8s}|".format(i, value.subject_line, str(value.has_been_read))
        if (only_unread == False):
            print(line)
        elif (value.has_been_read == False):
            print(line)

def read_email(index):
    # Function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    email = inbox_list[index]
    line  = f"e-mail address: \t {email.email_address}\n"
    line += f"subject: \t\t {email.subject_line}\n"
    line += f"content: \t\t {email.email_content}"
    print("-" * 80)
    print(line)
    print(f"\nEmail from {email.email_address} marked as read.")
    email.mark_as_read()

# --- Email Program --- #
import os

# Call the function to populate the Inbox for further use in your program.
populate_inbox()
 
while True:
    os.system('cls||clear')
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
    os.system('cls||clear')

    if user_choice == 1:
        # add logic here to read an email
        list_emails()
        mail_choice = input("Please choice a mail to read: ")
        if mail_choice.isnumeric():
            if (int(mail_choice) >= 0 and int(mail_choice) < len(inbox_list)):
                read_email(int(mail_choice))
                input("Press any key to continue...")
            else:
                input("Invalid option. Press any key to continue...")
        else:
            input("Invalid option. Press any key to continue...")

    elif user_choice == 2:
        # add logic here to view unread emails
        print("Showing unread e-mails:")
        list_emails(True)
        input("Press any key to continue...")

    elif user_choice == 3:
        # add logic here to quit appplication
        print('Goodbye!!!')
        exit()

    else:
        print("Oops - incorrect input.")

