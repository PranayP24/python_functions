# Clone or copy a list
list=[10,20,40,]
copied_list=[]
for elements in list :
    copied_list.append(elements)
print('copied list :',copied_list)

#function with parameters,without return
def copied_list(lst):
    print(lst)
    lst2=lst.copy()
    lst2.append(50)
    print(lst2)
lst=[10,20,30,40]
copy_lst=copied_list(lst)
#function with parameters,with return
def copied_list(lst):
    print(lst)
    lst2=lst.copy()
    lst2.append(50)
    return lst2
lst=[10,20,30,40]
copy_lst=copied_list(lst)
print(copy_lst)
#functions without parameters,with return
def copied_list():
    lst=[10,20,30,40]
    lst2=lst.copy()
    lst2.append(50)
    return lst2
copy_lst=copied_list()
print(copy_lst)
# functions without parameters,without return
def copied_list():
    lst=[10,20,30,40]
    lst2=lst.copy()
    lst2.append(90)
    print(lst2)
copied_list()

#anonymous functions lambda
lst=[10,20,40,]
copied_list=list(filter(lambda num: num is not None ,lst ))
print(copied_list)




