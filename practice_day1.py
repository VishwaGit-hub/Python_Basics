#factorial number
def fact(n):
    ans = 1
    for i in range(1,n+1):
        ans *=i
    return ans
#print(fact(5))

#palindrom number
def palindrom(n):
    temp=n
    rev=0
    while temp>0:
        last=temp%10
        rev=rev*10+last
        temp=temp//10
    print(n,rev)
    if n==rev:
        return True
    else:
        return False

# print(palindrom(121))

#palidrom string
st1="racecar"
# print("True" if st1==st1[::-1]else "False")


#max number in a single number
def max_num(n):
    temp=n
    li=[]
    max=0
    sum_digits=0
    while temp>0:
        last=temp%10
        li.append(last)
        temp=temp//10
    print(li)
    for i in li:
        sum_digits+=i
        if i>max:
            max=i
    print(max)
    print(sum_digits)
# max_num(123)


#linear seach
list_search=[5,6,8,4,1,2]
target=5
def lin_search(target):
    flag=False
    ind=0
    for i in range(len(list_search)):
        if list_search[i]==target:
            flag=True
            ind=i
            break
    if flag==True:
        print(f"element found at index {ind}")
    else:
        print("element not found in the list")
        
        
# lin_search(target)


#remove duplicates from list
li=[1,1,2,3,4,5]
def remove_dup(li):
    low = 0
    high = len(li)-1
    mid=(len(li)//2)-1
    for i in range(low,mid):
        for j in range(high,mid,-1):
            if li[i]!=li[j]:
                print(i,j)
                high-=1
            elif li[i]==li[j]:
                temp=li[high]
                print("temp",temp)
                li.remove(temp)
                low+=1
            else:
                break
    print(li)            
remove_dup(li)



