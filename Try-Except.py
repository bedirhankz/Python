List=["1","2","5a","10b","abc","10","50"]
Numbers=[]
for i in List:
    try:
        Try=int(i)
        if Try/1==Try:
            Numbers.append(i)
    except ValueError:
        pass
print(Numbers)
while True:
    Loop=input("Something:  ")
    if Loop=="q" or Loop=="Q":
        break
    try:
        check=int(Loop)
        print("Number")
    except ValueError:
        print("Wrong Value")
Password=input("Enter Your Password:  ")
turkish="ıöşğüçIÖÇÜĞ"
try:
    for check1 in Password:
        if check1 in turkish:
            raise Exception(" Turkish Character Cannot be Used")
    print(f"Your New Password:{Password}")
except Exception as Error:
    print(f"Error{Error}")
import math
try:
    UserNumber=int(input("Enter Your Number:  "))
    Print=math.factorial(UserNumber)
    print(f"Result:{Print}")
except ValueError:
    print("Wrong Number")

