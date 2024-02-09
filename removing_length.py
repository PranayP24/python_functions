#Find the list of words that are longer than n from a given list of words
lst= ['hello', 'world', 'name', 'python', 'programming']
lst2=[]
n=4
for i in range(len(lst)):
    temp=lst[i]
    if len(temp)>n:
       lst2.append(lst[i])
print(lst2)

# function with parameters ,without return
lst= ['hello', 'world', 'name', 'python', 'programming']
def removing_length(lst):
    lst1=[]
    num=int(input('enter the number :'))
    for i in lst:
        if len(i)>num:
            lst1.append(i)
    print(lst1)
removing_lst=removing_length(lst)

# function with parameters and with return
lst= ['hello', 'world', 'name', 'python', 'programming']
def removing_length(lst):
    lst1=[]
    num=int(input('enter the number :'))
    for i in lst:
        if len(i)>num:
            lst1.append(i)
    return lst1
removing_lst=removing_length(lst)
print(removing_lst)


# function without parameters and with return
def removing_length():
    lst= ['hello', 'world', 'name', 'python', 'programming']
    lst1=[]
    num=int(input('enter the number :'))
    for i in lst:
        if len(i)>num:
            lst1.append(i)
    return lst1
removing_lst=removing_length()
print(removing_lst)

# function without parameters and without return
def removing_length():
    lst= ['hello', 'world', 'name', 'python', 'programming']
    lst1=[]
    num=int(input('enter the number :'))
    for i in lst:
        if len(i)>num:
            lst1.append(i)
    print(lst1)
removing_lst=removing_length()




#anonymous functions lambda
lst= ['hello', 'world', 'name', 'python', 'programming']
result_lst=list(filter( lambda each:len(each)>4,lst))
print(result_lst)

result=list(map( lambda each:len(each)>4,lst))
print(result)

