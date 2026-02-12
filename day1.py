#day-1
# datatypes

#################numeric
#int
num=12
print(type(num))

#float
num_float=12.5
print(type(num_float))

#complex
cmp=2+3j
print(type(cmp))

##################Text

#string
st="this is vishwa!"
print(st)
print(type(st))
print(st[0]) #index start from 0
#st[0]="B" #str object does not support item assignement. , immutable nature 

#slicing
print(st[0:-1]) #exclude last character
print(st[:-1]) #last character
print(st[-1:])



#################Sequence
#list
lst=["apple","banana","cherry","watermelon"]
print(lst[-1])
print(lst[0:-1])# -1 is excluded
print(lst[-4:])
lst[1:2]=["strawberry","papaya"]

lst.insert(5,"guava")
lst.pop(5)
print(lst)

#list comprehension
lst2=[x for x in lst if "s" in x]
print(lst2)


#Tuples
#same as lists but cannot change the content and delete items from it
fruits=("apple","banana","cherry","watermelon")
apple,banana,*cherry=fruits
print(fruits)
print(apple)
print(len(fruits))



#sets
#unordered
#unchangeable
#since unordered cannot be accessed through a index
set1={"apple","banana","cherry","watermelon"}

for i in set1:
    print(i)
set1.add("guava")
set1.remove("guava") #if item to remove does not exists it will generate error
set1.discard("guava") # this method will not raise error
print(set1)


frzset=frozenset({"1","2","3"}) #unlike set items cannot be removed or added
print(frzset)



#dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict["brand"])
print(thisdict.get("model"))
thisdict.update({"color":"red"}) #for adding and updating dictionary
print(thisdict)



##################conditional statements
#shorthand if
#syntax
# var= value_if_true if condition else value_if_false

a = 140
b = 122
c=130
max=  a if (a>b and a>c) else( b if b>c else c)
print(max)



####################functions

#function positional arguments
def hello_1(name,lname):
    print("hello "+name+" "+lname)
hello_1("vishwa","dhola") # here the arguments must be in same order as parameters in function definition


#function keyword aruguments
def hello(name,lname):
    print("hello "+ name+" "+lname)
hello(lname="dhola",name="vishwa")

#positional only arguments using '/' 
def hello_2(name,/):
     print("hello "+ name)
hello_2("vishwa") #j name='vishwa' will give error

#keyword only arguments using *
def hello_3(*,name):
    print("hello "+ name)
hello_3(name='vishwa') # 'vishwa' will generate error

def hello_4(name,lname,/,*,place,time):  # parameters before / are positional and parameters after * are keyword only
    print("hello "+name+" "+lname+" at "+place+" on "+time)
hello_4("vishwa","dhola",place="unikwork",time="10:30")


#arbitary positional arguments
def hello_5(*args):  # if you dont know how many postional arguments passed use this , it will be received as tuple of arguments
     print("hello "+args[0]+" "+args[1])
hello_5("vishwa","dhola")


def calculate(*nums):
    ans = 0
    for n in nums:
        ans+=n
    return ans
sum_cal=calculate(10,20,40) 
print(sum_cal)

#arbitary keyword arguments. 
def hello_6(**kwargs):
    print("hello "+kwargs["name"]+" "+kwargs["lname"])
hello_6(name="vishwa",lname="dhola")  


#python functino scope
#LEGB rule

x="Global"

def outer():
    x='Enclosed'
    def inner():
        x="Inner"
        print(x)
    inner()
    print(x)
outer()
print(x)


#decorators
#it lets you add extra behavior to the function without changing the code of the function
#takes another function as input and returns a new function

import functools
def upper_deco(func):
    @functools.wraps(func)
    def myinner(*args,**kwargs):
        return func(*args,**kwargs).upper()
    return myinner

def greet_deco(func):
    @functools.wraps(func)
    def myinner(*args,**kwargs):
        return "Hello "+ func(*args,**kwargs)+"!"
    return myinner


@greet_deco
@upper_deco
def myfunc(name,lname):
    return name+ " " +lname
print(myfunc("vishwa","dhola"))
print(myfunc.__name__)

#lambda function
#can take any number of arguments but have only one expression
#syntax
# lambda arguments: expression

def doubler(n):
    return lambda a:a*n
mydb=doubler(3)
print(mydb(11))

#lambda with map function
#map function syntax
#map(function,iterable)
numbers=[5,4,2,3,1]
db_list=list(map(lambda x:x*2,numbers))
print(db_list)

#labmda with filter function
#filter function syntax
#filter(function,iterable)

fil_list=list(filter(lambda x:x%2!=0,numbers))
print(fil_list)

#lambda with sorted function
#sorted function syntax
#sorted(iterable,key)
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sor_list=list(sorted(students,key=lambda x:x[1]))
print(sor_list)



#classes 

#inheritance
class Person:
    def __init__(self,name,lname):
        self.name=name
        self.lname=lname
    def print_info(self):
        print(self.name+" "+self.lname)

class Student(Person):
    def __init__(self,name,lname):
        super().__init__(self,name,lname) 

X=Person("vishwa","dhola")

X.print_info()


#Polymorphism
# it is in methods where multiple classes have same method names
class Vehicle:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def move(self):
        print("Move!")
class Car(Vehicle):
    pass
class Yatch(Vehicle):
    def move(self):
        print('sail!')
class Plane(Vehicle):
    def move(self):
        print("fly")

c1=Car("ford","black")
c1.move()
y1=Yatch("xyz","white")
y1.move()
p1=Plane("boeing","red")
p1.move()

#Encapsulation
#Protecting data inside a class using private and protected operators
#python only enforces private , protected is only a convention not a rule


class Account:
    def __init__(self,uname,password,amount):
        self.uname=uname
        self.__password=password
        self.balance=amount
        self.hide="*"*int(len(str(password)))
    def get_pass(self,uname):
        if uname==self.uname:
            return self.__password
        else:
            return "Invalid username"
    def get_info(self):
        print(self.uname)
        print(self.hide)
    def __showBalance(self):
        print(f"balance is {self.balance}")
        
    def get_balance(self,uname,password):
        if self.uname==uname and self.__password==password:
            self.__showBalance()
        else:
            print("Invalid username or passwod!!")
            

a1=Account("vishwa",1234,10000)
a1.get_info()
a1.get_balance("vishwa",1234)
print(a1.get_pass('vishwa'))

#python name mangling 
#using this we can access private properties of the class but not recommended
print(a1._Account__password)


#Inner and outer class
class outer:
    def __init__(self,name):
        self.name=name
    
    class inner:
        def __init__(self,outer):
            self.outer=outer
        def display(self):
            print(f"Hello from {self.outer.name}")
            
o=outer("vishwa")
i=o.inner(o)
i.display()


#generators
#functions that can pause and resume their execution
#returns a generator object , it executes when you iterate over it , until then it is compiled
#allows you to iterate over data without storing entire data in memory

def count_gen(n):
    for i in range(n):
        yield i
gen=count_gen(100)
print(gen)

print(next(gen))

#list comprehension vs generator comprehension
list_comp=[x*x for x in range(5)]
gen_comp=( x*x for x in range(5))
print(list_comp)
print(gen_comp)
print(next(gen_comp))

#methods
#send
def gen_meth():
    while True:
        received=yield
        print(received)

gen=gen_meth()
next(gen) # this is called priming the generator if we dont write this it will give error cant send value to a just started generator
gen.send("Hello")
gen.send("World!")
gen.close()
# gen.send("is it closed?") # it will give stop iteration error since generator is closed




###################file handling
