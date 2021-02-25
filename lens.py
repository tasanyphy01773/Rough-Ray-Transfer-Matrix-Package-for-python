from numpy import *
from math import *
#this is the user defined function for thin lens, must be convex and f should be positive 
def thinlens(f):
    arr02 = array([
                    [1, 0],
                    [-1/f, 1]                    
                            ])
    print("The ray transfer matrix for your thin lens of focal lenth f is", )
    print(arr02)
thinlens(float(input("Enter focal length, f=", )))