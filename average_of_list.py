#Calculate the average of numbers in a list
list=[6,8,9,3,8]
list=[41,18,9,3,85]
sum=0
avg=1
for i in list:
    sum=sum+i
    avg=sum/len(list)
print('average of numbers in a list :',avg)



#Function with parameters and without return
def average(list):
    sum=0
    avg=1
    for i in list:
        sum=sum+i
        avg=sum/len(list)
    print('average of numbers in a list:',avg)
list=[6,8,9,3,8]
output=average(list)
list=[41,18,9,3,85]
output=average(list)
list=[1,2,3,4,5]
output=average(list)



#Function with parameters and with return
def average(list):
    sum=0
    avg=1
    for i in list:
        sum=sum+i
        avg=sum/len(list)
    return avg
list=[6,8,9,3,8]
output=average(list)
print('average of numbers in a list:',output)
list=[41,18,9,3,85]
output=average(list)
print('average of numbers in a list:',output)
list=[1,2,3,4,5]
output=average(list)
print('average of numbers in a list:',output)


#functions without parameters and with return
def average():
    list=[6,8,9,3,8]
    sum=0
    avg=1
    for i in list:
        sum=sum+i
        avg=sum/len(list)
    return avg
output=average()
print('average of numbers in a list:',output)



#functions without parameters and without return
def average():
    list=[6,8,9,3,8]
    sum=0
    avg=1
    for i in list:
        sum=sum+i
        avg=sum/len(list)
    print('average of numbers in a list:',avg)
output=average()






 #anonymous functions lambda
from functools import reduce as re
list=[6,8,9,3,8]
average=lambda x:re(lambda a,b: a+b,x)/len(x)
avg=average(list)
print('average of numbers in a list:',avg)
