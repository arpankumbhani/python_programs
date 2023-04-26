#devlop a python program to make a simple calculator using a condition loop.
print("calculator")
print("1.addition")
print("2.subtraction")
print("3.mutiplication")
print("4.divition")
ch=int(input("enter the choice(1-4):"))
if ch==1:
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    c=a+b
    print("sum=",c)
elif ch==2:
    a=int(input("enter a:"))   
    b=int(input("enter b:"))
    c=a-b
    print("sub=",c)
elif ch==3:
    a=int(input("enter a:"))   
    b=int(input("enter b:"))
    c=a*b
    print("multiply=",c)
elif ch==4:
    a=int(input("enter a:"))   
    b=int(input("enter b:"))
    c=a/b
    print("division=",c)
else:
    print("invalid choice")

