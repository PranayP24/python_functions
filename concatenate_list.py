# #Concatenate two lists
# list1 = [1,2,3,4]
# list2 =[5,6,7,8]
# print('list1 before concatenation:',list1)
# for i in list2:
#     list1+=list2
#     break
# print('list1 after concatenation:',list1)


# #functions with parameters and without return
# def concatenation_lists(list1,list2):
#         list=list1+list2
#         print(list)
# list1=[1,2,3,4]
# list2=[5,8,9,0,3]
# output=concatenation_lists(list1,list2)


# # functions with parameters and with return
# def concatenation_lists(list1,list2):
#             return list1+list2
# list1=[1,2,3,4]
# list2=[5,8,9,0,3]
# output=concatenation_lists(list1,list2)
# print('number:',output)
# list1=['p','r','a','n','a','y']
# list2=['t','e','j','a']
# output=concatenation_lists(list1,list2)
# print('name:',output)



# #functions without parameters and with return
# def concatenation_lists():
#     list1=[1,2,3,4]
#     list2=[5,6,8,9,2,0]
#     list=list1+list2
#     return list
# output_lst=concatenation_lists()
# print(output_lst)



# #functions without parameters and without return
# def concatenation_lists():
#     list1=[1,2,3,4]
#     list2=[5,6,7,8,9,0,2]
#     list=list1+list2
#     print(list)
# output_list=concatenation_lists()


#anonymuos function lambda
list1=[1,2,3,4]
list2=[5,6,7,8,9,0,2]
concatenation_lists=[x for x in list1+list2 ] 
print(concatenation_lists)
