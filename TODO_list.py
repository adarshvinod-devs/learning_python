from datetime import datetime , date
import json

task_list = {}

def create_task():
    task_name = input("Enter task name: ")
    task_discription = input("Enter task discription: ")
    date_str = input("Enter due date(DD-MM-YYYY): ")
    #due_date = datetime.strptime(date_str,"%d-%m-%Y").date()
    created_date = date.today()
    task_list[task_name] = {"Discription":task_discription,"Due Date":date_str,"Task added on":str(created_date)}
    with open("TODO.json","w") as file:
        json.dump(task_list,file)


create_task()

