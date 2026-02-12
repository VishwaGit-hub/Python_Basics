import json
tasks={}


def add_task(num_tasks):
    global tasks
    for i in range(num_tasks):
        task=input(f"Enter task {i+1}...")
        tasks.update({task:"pending"})
   
    
    
       

def show_tasks():
    global tasks
    for key,val in tasks.items():
        print(key,val)

def add_to_file():
    global tasks
    tasks_json=json.dumps(tasks)
    with open("to_do.txt","a",encoding='utf-8')as file:
        json.dump(tasks_json,file,ensure_ascii=False,indent=4)

# def read_from_file():
#     with open("to_do.txt",'r') as file:
        
        
    

while True:
    print("1.add task")
    print("2.show all tasks")
    print("3.add task to file")
    print("4.delete a list")
    print("5.Exit")
    
    ch=int(input("what do you want to do?..."))
    
    match ch:
        case 1:
            num_tasks=int(input("how many tasks do you want to enter?"))
            add_task(num_tasks)
        case 2:
            show_tasks()
        case 3:
            add_to_file()
        case 4:
            pass
        case 5:
            break