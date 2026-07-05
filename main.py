
import os
from datetime import datetime
from colorama import Fore, Style, init
init(autoreset=True)

tasks = []

# Load Tasks from File

def load_tasks():

    global tasks

    if os.path.exists("tasks.txt"):

        file = open("tasks.txt", "r")

        for line in file:

            line = line.strip()

            if line != "":

                data = line.split("|")

                task = {
                    "name": data[0],
                    "category": data[1],
                    "important": data[2],
                    "note": data[3],
                    "date": data[4],
                    "reminder": data[5],
                    "status": data[6]
                }

                tasks.append(task)

        file.close()


# Save Tasks

def save_tasks():

    file = open("tasks.txt", "w")

    for task in tasks:

        file.write(
            task["name"] + "|" +
            task["category"]+"|"+
            task["important"] + "|" +
            task["note"] + "|" +
            task["date"] + "|" +
            task["reminder"] + "|" +
            task["status"] + "\n"
        )

    file.close()


# Welcome Screen

def welcome():

    print(Fore.LIGHTMAGENTA_EX+"=" * 45)
    print(Fore.WHITE+"        SMART TO-DO LIST")
    print(Fore.LIGHTMAGENTA_EX+"=" * 45)

    print(Fore.WHITE+"\nHello! 👋")

    print(Fore.WHITE+"\nWelcome to Smart To-Do List.")

    print(Fore.WHITE+"\nThis application helps you to:")

    print(Fore.LIGHTMAGENTA_EX+"- Organize your daily tasks")
    print(Fore.LIGHTMAGENTA_EX+"- Set completion dates")
    print(Fore.LIGHTMAGENTA_EX+"- Add reminders")
    print(Fore.LIGHTMAGENTA_EX+"- Track completed tasks")
    print(Fore.LIGHTMAGENTA_EX+"- Stay productive")

    input(Fore.WHITE+"\nPress Enter to Continue...")



# Dashboard

def dashboard():

    total = len(tasks)

    completed = 0
    pending = 0

    for task in tasks:

        if task["status"] == "Completed":
            completed += 1
        else:
            pending += 1

    print(Fore.LIGHTMAGENTA_EX+"\n" + "=" * 45)
    print(Fore.WHITE+"             DASHBOARD")
    print(Fore.LIGHTMAGENTA_EX+"=" * 45)

    print(Fore.WHITE+"Total Tasks      :", total)
    print(Fore.WHITE+"Pending Tasks    :", pending)
    print(Fore.WHITE+"Completed Tasks  :", completed)

    print(Fore.LIGHTMAGENTA_EX+"=" * 50)



# Menu

def menu():

    if len(tasks) == 0:

        print(Fore.WHITE+"\nMENU")
        print(Fore.WHITE+"1. Add Task")
        print(Fore.WHITE+"2. Exit")

    else:

        dashboard()

        print(Fore.LIGHTMAGENTA_EX+"\nMENU")
        print(Fore.WHITE+"1. Add More Tasks")
        print(Fore.WHITE+"2. View Tasks")
        print(Fore.WHITE+"3. Mark Task as Completed")
        print(Fore.WHITE+"4. Delete Task")
        print(Fore.WHITE+"5. Exit")

#add task
def add_task():

    try:
        number = int(input(Fore.WHITE+"\nHow many tasks do you want to add? "))

    except ValueError:
        print(Fore.LIGHTMAGENTA_EX+"Invalid Number")
        return

    for i in range(number):

        print(Fore.LIGHTMAGENTA_EX+"\nTask", i + 1)

       
        name = input(Fore.WHITE+"Enter Task Name : ")

        
        print(Fore.LIGHTMAGENTA_EX+"\nChoose Category")
        print(Fore.WHITE+"1. Study")
        print(Fore.WHITE+"2. Personal")
        print(Fore.WHITE+"3. Work")
        print(Fore.WHITE+"4. Health")
        print(Fore.WHITE+"5. Add Your Own Category")

        category_choice = input(Fore.LIGHTMAGENTA_EX+"Enter your choice: ")

        if category_choice == "1":
            category = "Study"

        elif category_choice == "2":
            category = "Personal"

        elif category_choice == "3":
            category = "Work"

        elif category_choice == "4":
            category = "Health"

        elif category_choice == "5":
            category = input("Enter your category: ")

        else:
            print(Fore.LIGHTMAGENTA_EX+"Invalid choice! Default category set to Personal.")
            category = "Personal"

      
        important = input(Fore.WHITE+"Is it Important? (Yes/No): ")

        note = ""

        if important.lower() == "yes":
            note = input(Fore.LIGHTMAGENTA_EX+"Enter Note: ")

       
        while True:

            date = input(Fore.LIGHTMAGENTA_EX+"Enter Completion Date (dd/mm/yyyy): ")

            try:

                due_date = datetime.strptime(date, "%d/%m/%Y").date()

                today = datetime.today().date()

                if due_date < today:

                    print(Fore.WHITE+"❌ Due date cannot be in the past.")
                    print(Fore.LIGHTMAGENTA_EX+"Please enter today's date or a future date.")

                else:
                    break

            except ValueError:

                print(Fore.WHITE+"❌ Invalid date format.")
                print(Fore.LIGHTMAGENTA_EX+"Please enter the date in dd/mm/yyyy format.")
      
        reminder = input(Fore.WHITE+"Reminder (Yes/No): ")

        
        task = {
            "name": name,
            "category": category,
            "important": important,
            "note": note,
            "date": date,
            "reminder": reminder,
            "status": "Pending"
        }

        tasks.append(task)

    save_tasks()

    print(Fore.LIGHTMAGENTA_EX+"\nTasks Added Successfully!")
   
# View Tasks

def view_tasks():
    

    if len(tasks) == 0:
        print(Fore.WHITE+"\nYou haven't added any tasks yet.")
        return

    print("\n" + "=" * 50)
    print("               ALL TASKS")
    print(Fore.LIGHTMAGENTA_EX+"=" * 50)

    for i, task in enumerate(tasks):

        print(Fore.WHITE+f"\nTask Number : {i + 1}")
        print(Fore.WHITE+"Task        :", task["name"])
        print(Fore.WHITE+"Category    :",task["category"])
        print(Fore.WHITE+"Important   :", task["important"])

        if task["important"].lower() == "yes":
            print(Fore.WHITE+"Note        :", task["note"])

        print(Fore.WHITE+"Due Date    :", task["date"])
        print(Fore.WHITE+"Reminder    :", task["reminder"])
        print(Fore.WHITE+"Status      :", task["status"])

        print(Fore.LIGHTMAGENTA_EX+"-" * 50)

# Complete Task

def complete_task():

    if len(tasks) == 0:
        print("\nNo tasks available.")
        return

    view_tasks()

    try:
        number = int(input(Fore.LIGHTMAGENTA_EX+"\nEnter Task Number to Complete: "))

        if number < 1 or number > len(tasks):
            print(Fore.LIGHTMAGENTA_EX+"Invalid Task Number")
            return

        tasks[number - 1]["status"] = "Completed"

        save_tasks()

        print(Fore.LIGHTMAGENTA_EX+"\nTask marked as Completed! ✅")

    except ValueError:
        print(Fore.LIGHTMAGENTA_EX+"Please enter a valid number.")

# Delete Task

def delete_task():

    if len(tasks) == 0:
        print(Fore.LIGHTMAGENTA_EX+"\nNo tasks available.")
        return

    view_tasks()

    try:

        number = int(input(Fore.LIGHTMAGENTA_EX+"\nEnter Task Number to Delete: "))

        if number < 1 or number > len(tasks):
            print(Fore.LIGHTMAGENTA_EX+"Invalid Task Number")
            return

        deleted = tasks.pop(number - 1)

        save_tasks()

        print(Fore.LIGHTMAGENTA_EX+f"\n'{deleted['name']}' deleted successfully!")

    except ValueError:
        print(Fore.LIGHTMAGENTA_EX+"Please enter a valid number.")

  
# Main Program


load_tasks()
welcome()

while True:
   

    menu()
    choice = input(Fore.LIGHTMAGENTA_EX+"\nEnter your choice: ")

  

    
    if len(tasks) == 0:

        
        if choice == "1":
            add_task()

        elif choice == "2":
            print(Fore.LIGHTMAGENTA_EX+"\nThank you for using Smart To-Do List!")
            break

        else:
            print(Fore.LIGHTMAGENTA_EX+"Invalid choice!")

    else:

        
        if choice == "1":
            add_task()

        elif choice == "2":
           
            view_tasks()

        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        
        elif choice == "5":
            print(Fore.LIGHTMAGENTA_EX+"\nThank you for using Smart To-Do List!")
            break


        else:
            print(Fore.LIGHTMAGENTA_EX+"Invalid choice!")
