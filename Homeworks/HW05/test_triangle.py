""" HW 02a - Testing a legacy program and reporting on testing results
"""

from datetime import date
import unittest
from triangle import classify_triangle

def my_brand():
    """ _Header function_
    """
    print("\n=*=*=*= Zuting Chen s=*=*=*=\n")
    print("=*=*=*= Course 2023S-SSW567-WS =*=*=*= \n")
    print("=*=*=*= HW 02a - Testing a legacy program and reporting on testing results =*=*=*=\n")
    print("=*=*=*= ", date.today() ," =*=*=*= \n")

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangle(unittest.TestCase):
    """
    Unit tests for Triangle.py
    """

    def test_right_a(self):
        """
        Test right triangle 1
        """
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def test_right_b(self):
        """ Test right triangle 2
        """
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def test_right_c(self):
        """ Test right triangle 3
        """
        self.assertEqual(classify_triangle(4,5,3),'Right','4,5,3 is a Right triangle')

    def test_equi_a(self):
        """ Test equilateral triangle 1
        """
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def test_iso_a(self):
        """ Test isoceles triangle 1
        """
        self.assertEqual(classify_triangle(2,3,2),'Isoceles','2,3,2 is a Isoceles triangle')

    def test_scal_a(self):
        """ Test scalene triangle 1
        """
        self.assertEqual(classify_triangle(3,7,6),'Scalene','1,0,1 is a Scalene triangle')

    def test_invalid_a(self):
        """ Test invalid input 1
        """
        self.assertEqual(classify_triangle(1,0,1),'InvalidInput','1,0,1 is not a valid input')

    def test_invalid_b(self):
        """ Test invalid input 2
        """
        self.assertEqual(classify_triangle(1,201,1),'InvalidInput','1,201,1 is not a valid input')

    def test_invalid_c(self):
        """ Test invalid input 3
        """
        self.assertEqual(classify_triangle(201,1,1),'InvalidInput','201,1,1 is not a valid input')

    def test_not_tri_a(self):
        """ Test not a triangle 1
        """
        self.assertEqual(classify_triangle(1,100,1),'NotATriangle','1,100,1 is not a triangle')


my_brand() ## START

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

my_brand() ## END
