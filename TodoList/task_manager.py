import mysql.connector as mc

mydb = mc.connect(
  host="localhost",
  user="root",
  password="dpnaik@2010",
  database="todolist",
)
cursor = mydb.cursor()

class TaskManager:
    
    
    def add_task(self, name, description, username):
        task = []
        task.append(name)
        task.append(description)
        cursor.execute("SELECT user_id FROM login WHERE username=%s", (username,))
        result = cursor.fetchone()
        sql = "INSERT INTO tasks (task_name, task_desc, user_id) VALUES (%s, %s, %s)"
        val = (task[0], task[1], result[0])
        cursor.execute(sql, val)
        mydb.commit()
        
    def display_tasks(self, username):
        cursor.execute("SELECT user_id FROM login WHERE username=%s", (username,))
        result = cursor.fetchone()
        cursor.execute("SELECT task_id, task_name, task_desc, task_status FROM tasks, login where tasks.user_id=%s and tasks.user_id=login.user_id", (result[0],))
        results = cursor.fetchall()
        if not results:
            print("\nNo tasks found.")
        else:
            print("\nCurrent Tasks:")
            for x in results:
                print(x)
      
    def mark_completed(self, username, task_id):
        cursor.execute("SELECT user_id FROM login WHERE username=%s", (username,))
        result1 = cursor.fetchone()
        cursor.execute("SELECT * FROM tasks WHERE task_id=%s and user_id=%s", (task_id, result1[0]))
        result2 = cursor.fetchone()
        if not result2:
            print("Invalid task id.")
        else:
            cursor.execute("UPDATE tasks SET task_status='Completed' WHERE task_id=%s and user_id=%s", (task_id, result1[0]))
            mydb.commit()
            print("Task marked as completed.")

    def delete_task(self, username, task_id):
        cursor.execute("SELECT user_id FROM login WHERE username=%s", (username,))
        result1 = cursor.fetchone()
        cursor.execute("SELECT * FROM tasks WHERE task_id=%s and user_id=%s", (task_id, result1[0]))
        result2 = cursor.fetchone()
        if not result2:
            print("Invalid task id.")
        else:
            cursor.execute("DELETE FROM tasks WHERE task_id=%s and user_id=%s", (task_id, result1[0]))
            mydb.commit()
            print("Task deleted.")

    def save_tasks(self):
        mydb.commit()

    def delete_user(self, username, password):
        cursor.execute("SELECT * FROM login WHERE username=%s", (username,))
        result1 = cursor.fetchone()
        if not result1:
            print("User not found.")
        else:
            cursor.execute("SELECT password FROM login WHERE username = %s", (username, ))
            result2 = cursor.fetchone()
            if result2:
                if password == result2[0]:
                    cursor.execute("DELETE FROM login WHERE username=%s", (username,))
                    mydb.commit()
                    print("User deleted.")
                else:
                    print("Your entered username and password are wrong.")
            else:
                print("User not found.")