import requests
import time
class Github:
    def __init__(self):
        self.url="https://api.github.com"
    def userinfo(self,username):
        response=requests.get(f"{self.url}/users/{username}")
        return response.json()
    def repoinfo(self,username,reponame):
        response=requests.get(f"{self.url}/repos/{username}/{reponame}")
        return response.json()

github = Github()

while True:
    Userinput=input("1.Get user info\n2.Get repo info\n3.Exit\nEnter your choice:")
    if Userinput not in ["1","2","3"]:
        print("Invalid input please try again")
        continue
    if Userinput=="3":
        print("Exiting")
        break
    elif Userinput=="1":
        try:
            username=input("Enter the username:")
            userinfo=github.userinfo(username)
            print(f"Username: {userinfo['login']}\nName: {userinfo.get('name')}\nPublic Repos: {userinfo['public_repos']}\nFollowers: {userinfo['followers']}\nFollowing: {userinfo['following']}")
            time.sleep(1)
        except KeyError:
            print("User not found")
        except Exception:
            print("Something went wrong please try again")
    elif Userinput=="2":
        try:
            username=input("Enter Username:")
            reponame=input("Enter Repo Name:")
            repoinfo=github.repoinfo(username,reponame)
            print(f"Repo Name: {repoinfo['name']}\nDescription: {repoinfo.get('description')}\nStars: {repoinfo['stargazers_count']}\nForks: {repoinfo['forks_count']}")
            time.sleep(1)
        except KeyError:
            print("Repo not found")
        except Exception:
            print("Something went wrong please try again")
    else:
        print("Something went wrong please try again")