
import requests
import json


new_tasks=[]

#load existing tasks
try:
    with open("tasks.json", "r") as file:
        created_tasks = json.load(file)
    print("\nExisting tasks:")

    for task in created_tasks:
        print(task)

except FileNotFoundError:
    created_tasks = []
    print("No existing tasks file found")

#checking user's input (amount of tasks)
def task_amount_check():

    while True:
        task_amount=input("How many tasks you want to create? ")
        try: 
            number=int(task_amount)
            if number <=0:
                print("Value must be more than zero")
            else: return number
        
        
        except ValueError:
            print("You have to type numerical value")



#checking user's input (title)
def title_check(i):
    while True:
        title=input(f"Task {i} title : ")
        title = title.strip()
        if title == "":
            print("Title cannot be empty")
        else: return title



#checking user's input (completed status)
def completion_status_check(i):

    while True:
        status=input(f"Completion status for task {i}: ")

        if status.lower() == "true":
            return True
        elif status.lower() == "false":
            return False
        else: print("Wrong status type, enter True or False")


#post function
def do_post(title, status):
    new_task={"title": title, "completed": status}
    response=requests.post("https://jsonplaceholder.typicode.com/todos", json=new_task)

    if response.status_code == 201:

        created_task=response.json()

        created_tasks.append(created_task)
        new_tasks.append(created_task)

        print("Successfully created task: ", created_task)
    else:
        print("Failed to create task")
        print(response.status_code)

def main(): 

    #getting checked value
    tasks_amount_input=task_amount_check()  

    #asking user a title and completion status for each new task
    for i in range(1, tasks_amount_input+1):
        user_title=title_check(i)
        user_status=completion_status_check(i)

        do_post(user_title, user_status)

    completed = 0

    #summary 
    for task in new_tasks:
        if task["completed"]:
            completed +=1
        
    not_completed=len(new_tasks)-completed

    print("Summary: ")
    print("Tasks created: ", len(new_tasks))
    print("Completed: ", completed)
    print("Not completed: ",  not_completed)



    with open("tasks.json", "w") as file:
        json.dump(created_tasks, file, indent=4)

    print("Tasks saved to tasks.json")



if __name__ == "__main__":

    main()