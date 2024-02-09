#Flatten a shallow list
lst=[['pranay','hemanth','run out'],['vijay','chinna'],['friends']]
res_lst=[]
for char in lst:
    for i in char:
        res_lst.append(i)
print(res_lst)

index_out=0
while index_out<len(lst):
    index_in=0
    while index_in<len(lst[index_out]):
        res_lst.append(lst[index_out][index_in])
        index_in+=1
    index_out+=1
print(res_lst)

# function with parameters and without return
lst=[['pranay','raja','run out'],['vijay','chinna'],['friends']]
def shallow_list(lst):
    flatten_list=[]
    for char in lst:
        for i in char:
            flatten_list.append(i)
    print(flatten_list)
out_lst=shallow_list(lst)


# function with parameters and with return
lst=[['pranay','raja','run out'],['vijay','chinna'],['friends']]
def shallow_list(lst):
    flatten_list=[]
    for char in lst:
        for i in char:
            flatten_list.append(i)
    return flatten_list
out_lst=shallow_list(lst)
print(out_lst)


# function without parameters and with return
def shallow_list():
    lst=[['pranay','raja','run out'],['vijay','chinna'],['friends']]
    flatten_list=[]
    for char in lst:
        for i in char:
            flatten_list.append(i)
    return flatten_list
out_lst=shallow_list()
print(out_lst)




# function without parameters and without return
def shallow_list():
    lst=[['pranay','raja','run out'],['vijay','chinna'],['friends']]
    flatten_list=[]
    for char in lst:
        for i in char:
            flatten_list.append(i)
    print(flatten_list)
out_lst=shallow_list()


#anonymous functions lambda
lst=[['pranay','raja','run out'],['vijay','chinna'],['friends']]
flatten=list(filter(lambda x: x is not None,[ item for sublist in lst for item in  sublist]))
print(flatten)