#HW 02a - Testing a legacy program and reporting on testing results

from datetime import date

def my_brand(): 
    print("\n=*=*=*= Zuting Chen s=*=*=*=\n")
    print("=*=*=*= Course 2023S-SSW567-WS =*=*=*= \n")
    print("=*=*=*= HW 02a - Testing a legacy program and reporting on testing results =*=*=*=\n") 
    print("=*=*=*= ", date.today() ," =*=*=*= \n")

def classifyTriangle(a,b,c):
    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput';
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == a:
        return 'Equilateral'
    elif (pow(a,2) + pow(b,2) == pow(c,2)) or (pow(b,2) + pow(c,2) == pow(a,2)) or (pow(a,2) + pow(c,2) == pow(b,2)):
        return 'Right'
    elif (a != b) and  (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isoceles'

my_brand()
