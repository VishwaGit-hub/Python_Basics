#python built-in functions
mylist=[False,True,True]
print(all(mylist)) #returns true if all items in an iterable are true
print(any(mylist)) #returns true if any item in an iterable is true
print(bin(2)) #reutns any number in binary with prefix 0b
print(chr(97)) #returns a character for given ascii code


#enumerate
mylist_1=["apple","banana","cherry"]
y=enumerate(mylist_1)
print(list(y))
for index,item in enumerate(mylist_1,1):
    print(index,item)
    

#eval
eval_res=eval("1+3-5") #it evaluates string expression
print(eval_res)

#filter
#filters given iterable using function
mylist_2=[12,22,14,25,60]
def check(age):
    if age>18:
        return True
    else:
        return False
fil_res=filter(check,mylist_2)
print(list(fil_res))
print(list(filter(lambda x:x>18,mylist_2)))

#isinstance. 
#checks if given value is of type 
print(isinstance(3,int))


#iter
#turns into iterable object
iter_res=iter(mylist_1)
print(next(iter_res))
print(next(iter_res))
print(next(iter_res))


#map
#returns iterable applying function to each item
map_res=map(lambda x:x**2,mylist_2)
print(list(map_res))


#ord
#converts given character/number/symbol into ascii number
print(ord("a"))


#zip
#joins two iterables and returns new one

mylist_3=[1,2,3,4,5]
for i,j in zip(mylist_2,mylist_3):
    print(i," ",j)
    


#recursion
#sum of natural numbers
def rec_sum(n):
    if n==1:
        return 1
    else:
        return n+rec_sum(n-1)

rec_sum_ans=rec_sum(5)
print(rec_sum_ans)

#factorial number

def rec_fac(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return n*rec_fac(n-1)

rec_fac_ans=rec_fac(5)
print(rec_fac_ans)

#fibonacci
#0,1,1,2,3,5,8...
def rec_fib(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    else:
        return rec_fib(n-1)+rec_fib(n-2)

for i in range(0,4):
    print(rec_fib(i),end=" ")
print()
#range sum
def rec_range(start,end):
    if  end==0:
        return 0
    else:
        return end+rec_range(start,end-1)
rec_range_res=rec_range(3,6)
print(rec_range_res)
        
    

#regular expression
import re
st="this is spain, THIS IS SPAIN"
ans_st=re.findall("[A-M,a-m]",st) # gives list of all chracters between a-m and A-M
print(ans_st)

st_1="hello planet"
ans_st_1=re.findall("planet$",st_1) #returns true if string ends with planet
ans_st_2=re.findall("\Ahello",st_1) #returns true if string starts with hello
if ans_st_1 and ans_st_2:
    print("yes")
else:
    print("no")
    
ans_st_3=re.findall("he..o",st_1) # finds all words with he followed by any 2 chracters and followed by o
ans_st_4=re.findall("he.*o",st_1) # same as above but * indicates that 0 or more characters (any) , + indicates one or more characters , ? indicates 0 or 1 character
ans_st_4=re.findall("he.{2}o",st_1) # {} number specified in this indicates exact no of characters that appear
print(ans_st_4)

#split
ans_st_5=re.split("\s",st_1) #splits string from space
ans_st_6=re.split("\s",st,1) #splits first occurence only from space rest is not
print(ans_st_5)
print(ans_st_6)


#sub
ans_st_7=re.sub('\s',',',st)
print(ans_st_7)


