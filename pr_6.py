#take to list a=[1,1,2,3,5,8,13,21,34,55,89] b=[1,2,3,4,5,6,7,8,9,10,11,12,13]and write a program that return alist that contains on;y the elements that are common between the list
# a=[1,1,2,3,5,8,13,21,34,55,89]
# print(a)
# b=[1,2,3,4,5,6,7,8,9,10,11,12,13,]
# print(b)
# c=[]
# for i in range(len(a)):
#     if a[i] in range (len(a)):
#         if a[i] in b:
#             c.append(a[i]) 
#             c=set(c)
#             print(c)
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_elements = [x for x in a if x in b]
