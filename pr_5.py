#create a program that asks tha user for a number and then prints out a list of all the divisio of that number.
list=()
num=input("enter the number:")
for i in range(1,num+1):
    if num%i==0:
        list.append(i)
    print(list)
    