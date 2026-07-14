
numbers=[1,3,5,7,9,12,19,21]
b="num"
while b=="num":
    print(numbers)
    b="num1"
number1=int(input("Enter your start:  "))
number2=int(input("Enter your finish:  "))
while number1<=number2:
    print(number1)
    number1=number1+1
test=1
test2=100
while test2>test:
    test2=test2-1
    print(test2)
number3=int(input("Enter number:  "))
number4=int(input("Enter number:  "))
number5=int(input("Enter number:  "))
number6=int(input("Enter number:  "))
number7=int(input("Enter number:  "))
c="numt"
while c=="numt":
    placement=(number3,number4,number5,number6,number7)
    placement1=sorted(placement)
    print(placement1)
    c="numtt"

total_products=int(input("Number of Products:  "))
d=0
total=""
while total_products>d:
    product_name=input("Enter A Name:  ")
    price=int(input("Enter a price:  "))
    d=d+1
    total=total+"Product: "+product_name+" Price: "+str(price) + "\n"
print(total)