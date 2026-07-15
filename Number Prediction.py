import random
number=random.randint(0, 100)
print(number)
rights=int(input("Enter your Rights:  "))
health=rights
point=100
point1=0
while rights>0:
    guess=int(input("Enter Your Number:  "))
    if number==guess:
        print("Your Score:  ",point1)
        break
    elif number>guess:
        print("Wrong Number More Upper")
        rights=rights-1
        point1 = (100 / health) * rights
        point=point-point1
    elif number<guess:
        rights=rights-1
        point1 = (100 / health) * rights
        point=point-point1
        print("Wrong Number More Lower")
if rights==0:
    print("Game Over True Number Was: ",number)
        