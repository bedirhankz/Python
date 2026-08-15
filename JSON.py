import json
import os
import time
if not os.path.exists("users.json"):
    with open("users.json", "w", encoding="utf-8") as f:
        json.dump([], f)
with open("users.json", "r", encoding="utf-8") as f:
    users = json.load(f)
def register():
    username= input("Enter username: ")
    if any(user["username"]==username for user in users):
        print("Username already exists.")
        return
    password= input("Enter password: ")
    if len(password) < 6:
        print("Password must be at least 6 characters long.")
        return
    global users
    users.append({"username": username, "password": password})
    print("Registration successful")
    time.sleep(2)
    with open("users.json", "w",encoding="utf-8") as f:
        json.dump(users, f,indent=4)
def login():
    username=input("Enter username: ")
    password=input("Enter password: ")
    for user in users:
        if user["username"]==username and user["password"]==password:
            time.sleep(2)
            print("Login successful!")
            return True
    print("Invalid username or password.")
    return False

while True:
    print("1(Register)\n2(Login)\n3(Exit)\n")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            register()
        elif choice == 2:
            login()
        elif choice == 3:
            break
        elif choice not in [1, 2, 3]:
            print("Invalid choice.")
    except ValueError:
        print("Enter 1 2 or 3 only")
        continue