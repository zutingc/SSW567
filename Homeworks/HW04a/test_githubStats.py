#Homework 04a - Develop with the Perspective of the Tester in mind

from datetime import date
import requests
import unittest
import re
from githubStats import getStats

def my_brand():
    print("\n=*=*=*= Zuting Chen s=*=*=*=\n")
    print("=*=*=*= Course 2023S-SSW567-WS =*=*=*= \n")
    print("=*=*=*= Homework 04a - Develop with the Perspective of the Tester in mind =*=*=*=\n")
    print("=*=*=*= ", date.today() ," =*=*=*= \n")
    
class TestTriangles(unittest.TestCase):
    def test_invalid_input(self):
        userId = "###Invalid_GitHub_Username###"
        output = getStats(userId)
        self.assertEquals(output, "Error in retrieving repos")
        
    def test_amnt_repos(self):
        userId = "zutingc"
        numberRepos = len(requests.get("https://api.github.com/users/" + userId + "/repos").json())
        output = getStats(userId).count("\n")
        self.assertEquals(output, numberRepos)
        
    def test_output_format(self):
        userId = "zutingc"
        match = re.findall( r"Repo: \w+ Number of commits: \d+", getStats(userId))
        self.assertTrue(match, "Output is not in the correct format")

my_brand()
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
my_brand()