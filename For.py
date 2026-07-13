numbers=[1,3,5,7,9,12,19,21]
for num in numbers:
    if num % 3 == 0:
        print(f"{num} is multiple of 3")
    else:
        print(f"{num} is not a multiple of 3")
numberstotal= sum(numbers)
print(f"The total sum of the numbers is: {numberstotal}")
for num1 in numbers:
    if num1 %2 == 1:
        print(num1**2)
citys=["Kocaeli","Istanbul","Ankara","Izmir","Rize"]
for citys5 in citys:
    if len(citys5) > 5:
        print(f"{citys5} has more than 5 letters")
    else:
        print(f"{citys5} has 5 or fewer letters")
products=[ 
{"name":"Samsung S6","price":3000},
{"name":"Samsung S7","price":4000},
{"name":"Samsung S8","price":5000},
{"name":"Samsung S9","price":6000},
{"name":"Samsung S10","price":7000}
]
for product in products:
    print(product["name"], product["price"])
total = sum(product["price"] for product in products)
print("Total Price:", total)
for product in products:
    if product["price"] <= 5000:
        print(product["name"], product["price"])
