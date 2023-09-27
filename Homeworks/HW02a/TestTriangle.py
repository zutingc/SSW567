#HW 02a - Testing a legacy program and reporting on testing results

from datetime import date

def my_brand(): 
    print("\n=*=*=*= Zuting Chen s=*=*=*=\n")
    print("=*=*=*= Course 2023S-SSW567-WS =*=*=*= \n")
    print("=*=*=*= HW 02a - Testing a legacy program and reporting on testing results =*=*=*=\n") 
    print("=*=*=*= ", date.today() ," =*=*=*= \n")

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(4,5,3),'Right','4,5,3 is a Right triangle')

    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsoceles(self): 
        self.assertEqual(classifyTriangle(2,3,2),'Isoceles','2,3,2 is a Isoceles triangle')

    def testScalene(self): 
        self.assertEqual(classifyTriangle(3,7,6),'Scalene','1,0,1 is a Scalene triangle')

    def testInvalidInput(self): 
        self.assertEqual(classifyTriangle(1,0,1),'InvalidInput','1,0,1 is not a valid input')

    def testInvalidInput2(self): 
        self.assertEqual(classifyTriangle(1,201,1),'InvalidInput','1,201,1 is not a valid input')

    def testInvalidInput3(self): 
        self.assertEqual(classifyTriangle(201,1,1),'InvalidInput','201,1,1 is not a valid input')

    def testNotATriangle(self): 
        self.assertEqual(classifyTriangle(1,100,1),'NotATriangle','1,100,1 should not be a triangle')


my_brand() ## START

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

my_brand() ## END
