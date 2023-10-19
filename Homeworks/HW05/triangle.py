""" HW 02a - Testing a legacy program and reporting on testing results
"""

from datetime import date

def my_brand():
    """ Header function
    """
    print("\n=*=*=*= Zuting Chen s=*=*=*=\n=*=*=*= Course 2023S-SSW567-WS =*=*=*= \n")
    print("=*=*=*= HW 02a - Testing a legacy program and reporting on testing results =*=*=*=\n")
    print("=*=*=*= ", date.today() ," =*=*=*= \n")

def classify_triangle(a,b,c):
    """ Returns the type of triangle it is

    Args:
        a (_type_): side 1
        b (_type_): side 2
        c (_type_): side 3

    Returns:
        _type_: string
    """
    # require that the input values be >= 0 and <= 200
    invalid_a = not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int))
    invalid_b = a > 200 or b > 200 or c > 200
    invalid_c = a <= 0 or b <= 0 or c <= 0

    if invalid_a or invalid_b or invalid_c:
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    case_a = (pow(a,2) + pow(b,2) == pow(c,2))
    case_b = (pow(b,2) + pow(c,2) == pow(a,2))
    case_c = (pow(a,2) + pow(c,2) == pow(b,2))

    if a == b and b == a:
        return 'Equilateral'
    if case_a or case_b or case_c:
        return 'Right'
    if (a != b) and  (b != c) and (a != c):
        return 'Scalene'
    return 'Isoceles'

my_brand()
