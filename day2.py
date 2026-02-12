with open("demo.txt",'w') as f: #opening a file in write mode
    f.write("this data is written in the file!\n")

with open("demo.txt",'a') as a: #opening a file in append mode
    a.write("this content is appended in the file!") 
    

with open("demo.txt") as f: #opening a file in read mode
    # print(f.read()) #.read() reads entire data of file
    # print(f.readline()) #readline() only reads first line!
    lines=f.readlines() #readlines reads file line by line and returns a list of lines
# print(lines)
    


import json
# person={
#     "id":1,
#     "name":"vishwa",
#     "country":"india",
#     "city":"surat",
#     "skills":["python","c","c++"]
# }

# person_json=json.dumps(person,indent=4)
# print(person_json)

# with open("demo.txt",'w',encoding='utf-8') as f:
#     json.dump(person,f,ensure_ascii=False,indent=8)


# with open("demo.txt",'r')as f:
#     person=json.load(f)


##################modules and packages
import modexample as md
# from modexample import *


pr=md.person
pr['name']="xyz"
print(pr)



#######################python standard library
#os
import os

print(os.name) #name of operating system
print(os.getcwd()) # get current directory name

parend_dir=os.getcwd()
demo_path=os.path.join(parend_dir,"demo") #joins path of folders 
# os.mkdir(demo_path) # creates a directory at path specified
# os.rmdir(demo_path). #removes directory at path specified
print(demo_path)
print(os.listdir()) #lists all the files 



#sys
import sys
print(sys.version) #current system version
print(sys.path)  # paths that python use when searching for modules 
print(sys.modules) #lists all available modules 
print(sys.getrecursionlimit()) #gives max recursion limit
print(sys.maxsize)
print(sys.getdefaultencoding()) #gives default encoing method used 'utf-8'

n=len(sys.argv)

print("total arguments passed..",n)
print("name of script...",sys.argv[0])
for i in range(1,n):
    print(sys.argv[i],end=" ")
    


#math
import math
print(math.e)
print(math.pi)
print(math.tau)
print(math.inf)


#random
import random
random.seed(10) # random number generator, random number generator requires a number to start with , by default it uses current system time
print(random.randrange(3,9)) #generates a random number between given range

rnd_list=[3,6,8,9,2,1]
print(random.choices(rnd_list,k=2)) # selects a random number from given list,if choices given returns list of randomly selected numbers, k will decide number of items to return
print(random.random()) #returns a random floating point number between 0 and 1


#datetime module
import datetime 
from datetime import date
import time
print(datetime.datetime.now()) #module class method
x=datetime.datetime(2026,9,17)
print(x.strftime("%A")) #day of week 
print(x.strftime("%j")) #day number of the year
print(x.strftime("%U")) #week number as sunday first day of week

print(date.max) #displays max date
print(date.min) #displays min date
# time.sleep(10)
# print("after 10 seconds")
print(time.time())


#Garbage collection and memory management
import gc
x=[1,2,3]
y=[4,5,6]
x.append(y)
y.append(x)
print(sys.getrefcount(x)) #gives no of refernces for an object
print(sys.getrefcount(y))
print(gc.get_threshold()) #returns threshold tuple for generation 0,1,2

a = [1, 2, 3]
b = {"a": 1, "b": 2}
c = "Hello, world!"




