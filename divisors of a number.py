def Divisor():
    list=[]
    Number=int(input("Enter Your Number:  "))
    for number in range(1,Number):
        if Number%number==0:
            list.append(number)
    print("Divisors of the number",list)
Divisor()

