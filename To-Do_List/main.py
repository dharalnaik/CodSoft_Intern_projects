import mysql.connector as mc
from task_manager import TaskManager
task_manager = TaskManager()

mydb = mc.connect(
  host="localhost",
  user="root",
  password="dpnaik@2010",
  database="todolist",
)
cursor = mydb.cursor()

def signup(name, username, password):
    cursor.execute("SELECT user_id FROM login WHERE username=%s and password=%s", (username,password,))
    result = cursor.fetchone()
    if not result:
        signup_list=[]
        signup_list.append(username)
        signup_list.append(password)
        sql = "INSERT INTO login (username, password) VALUES (%s, %s)"
        val = (signup_list[0], signup_list[1])
        cursor.execute(sql, val)
        mydb.commit()
        print(name, "welcome to To-do List. Please login.\n")
        login(name)
    else:
        print("\nUser already exists. Please login.\n")
        login(name)

# Function to login a user
def login(name):
    flag=0
    username = str(input("Enter your username: "))
    password = str(input("Enter your password: "))
    cursor.execute("SELECT password FROM login WHERE username = %s", (username, ))
    result = cursor.fetchone()
    if result:
        if password == result[0]:
            print("\n",name, "welcome to To-do List Management System:-")
            flag=1
        else:
            flag=0
            print("Your entered username and password are wrong.")
            login(name)
    else: 
        print("User not found. Try again.")
        login(name)
    
    while (flag==1):
            print("\n-:Task Management System:-")
            print("1. Add a New Task.")
            print("2. Display all Tasks.")
            print("3. Mark a Task as Completed.")
            print("4. Delete a Task.")
            print("5. Save Tasks.")
            print("6. Signup a New User or Login other User.")
            print("7. Exit.")
            choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")

            if choice == "1":
                name = input("\nEnter task name: ")
                description = input("Enter task description: ")
                task_manager.add_task(name, description, username)
            elif choice == "2":
                task_manager.display_tasks(username)
            elif choice == "3":
                task_manager.display_tasks(username)
                task_id = int(input("Enter task id of the task to be marked as completed: "))
                task_manager.mark_completed(username, task_id)
            elif choice == "4":
                task_manager.display_tasks(username)
                task_id = int(input("\nEnter task id of the task to be deleted: "))
                task_manager.delete_task(username, task_id)
            elif choice == "5":
                task_manager.save_tasks()
                print("\nTasks saved.")
            elif choice == "6":
                print("\nTo sign up or log in.")
                main()
            elif choice == "7":
                print("\nDo you want to save the changes you made to Task Manager and then Exit?")
                answer = input("Yes/No: ")
                if ((answer == "Yes") or (answer == "yes")):
                    task_manager.save_tasks()
                    print("Tasks saved.\nExiting...")
                    break
                else:
                    print("Exiting...")
                    break
            else:
                print("\nInvalid choice. Try again.")

def main():
    print("\n-:What do you want do?:-")
    print("1. Sign Up a New User.")
    print("2. Log in.")
    print("3. Delete a User.")
    print("4. Exit.")
    choice = input("Enter your choice (1/2/3/4): ")
    if choice == "1":
        name = str(input("\nEnter your name: "))
        username = str(input("Enter your username: "))
        password = str(input("Enter your password: "))
        signup(name, username, password)
    elif choice == "2":
        name = str(input("\nEnter your name: "))
        login(name)
    elif choice == "3":
        username = str(input("\nEnter username of user to be deleted: "))
        password = str(input("Enter your password: "))
        task_manager.delete_user(username, password)
    elif choice == "4":
        print("Exiting...")
    else:
        print("\nInvalid choice. Try again.")

if __name__ == "__main__":
    main()