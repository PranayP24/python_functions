#Get the difference between two lists
lst1=[1, 2, 3, 4]
lst2=[1,2]
lst3=[]
for elements in lst1:
    if elements not in lst2:
        lst3.append(elements)
print(lst3)



#functions with parameters and without return
lst1=[1, 2, 3, 4]
lst2=[1,2]
def difference_BW_two_list(lst1,lst2):
    lst3=[]
    for elements in lst1:
        if elements not in lst2:
            lst3.append(elements)
    print(lst3)
dif_list=difference_BW_two_list(lst1,lst2)

#functions with parameters and with return 
def difference_BW_two_list(list1,list2):
    dif_list=[]
    print('combined two list :',list1+list2)
    for elements in list1:
        if elements not in list2:
            dif_list.append(elements)
    print('before return the difference:',dif_list)
    return dif_list
list1=[1,2,3,4]
list2=[1,2]
dif_list=difference_BW_two_list(list1,list2)
print('after return difference:',dif_list)

# funstions without parameters and with return
def difference_BW_two_list():
    lst1=[1,2,3,4]
    lst2=[1,2]
    lst3=[]
    for elements in lst1:
        if elements not in lst2:
            lst3.append(elements)
    return lst3
dif_lst=difference_BW_two_list()
print(dif_lst)


# functions without parameters and without return
def difference_BW_two_list():
    lst1=[1,2,3,4]
    lst2=[1,2]
    lst3=[]
    for elements in lst1:
        if elements not in lst2:
            lst3.append(elements)
    print(lst3)
difference_BW_two_list()


#anonymous functions lambda
lst1=[1,2,3,4]
lst2=[1,2]
dif_lst=list(filter(lambda a : a not in lst2,lst1 ))
print(dif_lst)
dif_lst=list(filter( lambda x: x is not None,[item for item in lst1 if item not in lst2]))
print(dif_lst)