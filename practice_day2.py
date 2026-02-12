import json

all_list={}


all_id=1
name=input("Enter name of the list...")

num_tasks=int(input('Enter no of tasks you want to add...'))

all_list['id']=all_id
all_list['name']=name
all_list['num_tasks']=num_tasks
iid=0
tasks=[]
for i in range(num_tasks):
    
    id=i+1
    task=input(f"Enter task {i+1}: ")
    st=input("enter status of task (completed/pending/in progress): ")
    des=input("enter small description of task: ")
    tasks.append([id,task,st,des])

all_list.update({"tasks":tasks})

list_json=json.dumps(all_list,indent=4)
print(type(list_json))
print(list_json)

with open("to_do.txt","a",encoding='utf-8') as f:
    json.dump(list_json,f,ensure_ascii=False,indent=4)
    

with open("to_do.txt",'r') as f:
    final=json.loads(f)
    print(final)