balance= 0.0
income=0.0
try:
    income=float(input("Enter Your Income:  "))
except ValueError:
    print("Write A Number")

def money_add (income) :
    global balance
    if income < 0:
        print ("Wrong Number")
    else:
        global balance
        balance= balance+income
        return balance
money_add (income)
while True:
    try:
        spend3 =int(input("Do you want to spend more press 1 for yes press 0 for no: "))
        if spend3 == 1:
            spend_amount = float(input("Enter Your Spend: "))
            balance = balance-spend_amount
            print("Balance:", balance)
            if 0>balance:
                balance=balance+spend_amount
                print("There isn't enough money.")
        elif spend3 == 0:
            print("Balance:", balance)
            break
        else:
            print("Press 1 or 0")
    except ValueError:
        print("Press 1 or 0")