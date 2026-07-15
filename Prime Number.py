number=int(input("Enter A Number:  "))
number2=int(number**0.5)+1
prime=True
if number<=1:
    prime=False
else:
    for i in range(2,number2):
        if number%i==0:
            prime=False
            break
if prime:
    print("Prime")
else:
    print("Not Prime")