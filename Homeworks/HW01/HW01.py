#HW 01 - Testing triangle classification

from datetime import date
import unittest

def my_brand(): 
    print("\n=*=*=*= Zuting Chen s=*=*=*=\n")
    print("=*=*=*= Course 2023S-SSW567-WS =*=*=*= \n")
    print("=*=*=*= HW 01 - Testing triangle classification =*=*=*=\n") 
    print("=*=*=*= ", date.today() ," =*=*=*= \n")

def classify_triangle(a, b, c):
    if a == b and b == c:
        return "Equilateral"
    if a == b or a == c: # bug: missing "or b == c"
        return "Isosceles"
    if pow(a,2) + pow(b,2) == pow(c,2):
        return "Right"
    if a != b and b != c and a != c:
        return "Scalene"
    return "Invalid" # catch bug case

class test_triangles(unittest.TestCase):
    def test1(self):
        self.assertEqual(classify_triangle(3,4,5),"Right")

    def test2(self):
        self.assertEqual(classify_triangle(1,1,1),'Equilateral')
        self.assertNotEqual(classify_triangle(10,10,10),'Isoceles')
        self.assertEqual(classify_triangle(10,15,30),'Scalene')

    # def test3(self):
        # self.assertEqual(classify_triangle(1,2,2), 'Scalene') # Invalid because bug


my_brand() ## START

# classify_triangle(1, 2, 2)

if __name__ == '__main__':
    classify_triangle(1,2,3)
    classify_triangle(1,1,1)
    
    unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line

my_brand() ## END
