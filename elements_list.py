#Find the number of elements in a list.
my_list = [1,2,3,4,5]
my_list=['apple','call','suri','length','size','roja']
size=0
for i in my_list:
    size+=1
print(size)
i=0
while i < len(my_list):
    size+=1
    i+=1
print(size)


#functions with parameters and without return.
my_list=[1,2,3,4,5,6,7,8]
def length(my_list):
    size=0
    for i in my_list:
        if isinstance(i,list):
            size+=length(i)
        else:
            size+=1
    print(size)
lst3=length(my_list)


# functions with parameters and with return.
def length(my_list):
    size=0
    for i in my_list:
        if isinstance(i,list):
            size+=length(i)
        else:
            size+=1
    return size
my_list=[1,2,3,4,5,8,9,0,4]
print(length(my_list))
my_list=['apple','call','suri','length','size','roja']
print(length(my_list))

# function without parameters and with return 
def length():
    my_list=[1,8,6,0,3,2]
    size=0
    for i in my_list:
        if isinstance(i,list):
            size+=length(i)
        else:
            size+=1
    return size
length_lst=length()
print(length_lst)


#functions without parameters and without return
def length():
    my_list=['p','r','a','n','a','y']
    size=0
    for i in my_list:
        if isinstance(i,list):
            size+=length(i)
        else:
            size+=1
    print(size)
length_lst=length()


# anonymous function lambda
my_list=[1,2,3,4,5,6,7]
length=len(list(filter(lambda x: x-1,my_list)))
print(length)

my_list=['p','r','a','n','a','y']
length=len(list(filter(lambda x: x,my_list)))
print(length)
