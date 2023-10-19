#Homework 04a - Develop with the Perspective of the Tester in mind

from datetime import date
import requests

def my_brand():
    print("\n=*=*=*= Zuting Chen s=*=*=*=\n")
    print("=*=*=*= Course 2023S-SSW567-WS =*=*=*= \n")
    print("=*=*=*= Homework 04a - Develop with the Perspective of the Tester in mind =*=*=*=\n")
    print("=*=*=*= ", date.today() ," =*=*=*= \n")

# In order to be able to send more requests, I'm using session which requires my GitHub token that's in a config file
# If file is not provided, then we use requests instead of sessions
try:
    import config
    username = "zutingc"
    token = config.TOKEN
    session = requests.Session()
    session.auth = (username, token)
except:
    session = requests

def getStats(userId):
    output = ""
    repos = session.get("https://api.github.com/users/" + userId + "/repos")

    if repos.status_code == 200:
        for repo in repos.json():
            output += "Repo: " + repo['name'] + " "
            eachRepo = session.get(f"https://api.github.com/repos/" + userId + "/" + repo['name'] + "/commits")
            if eachRepo.status_code == 200:
                output += "Number of commits: " + str(len(eachRepo.json())) + "\n"
            else:
                return("Error in retrieving repo " + repo)
    else:
        return("Error in retrieving repos")
    
    return output

my_brand()
userInput = input("GitHub Username: ")
print(getStats(userInput))
my_brand()
