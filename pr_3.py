#ask the user for number.dependding on whether the number is even or odd,print out an appropriate message to the user,if the number is a multiple of 4,print out a different message
n=int(input("enter the number:"))
if(n%2==0):
    print("the given number is even")
if(n%4==0):
    print("the given number is multiple of 4")
else:
    print("the given number is odd")