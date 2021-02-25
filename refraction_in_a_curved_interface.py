from numpy import *
from math import *

#refraction in a curved interface as refracurve
n1 = float(input("Enter initial refractive index, n\N{SUBSCRIPT ONE}= ", ))
n2 = float(input("Enter final refractive index, n\N{SUBSCRIPT TWO}= ", ))
R = float(input("Enter radius of curvature, R= ", ))

def refracurve(n1, n2, R):
    return arr04
arr04 = array([
                [1, 0],
                [(n1-n2)/(R*n2), n1/n2]
                            ], float)
print("The ray transfer matrix for refraction at a curved interface is ")
print(arr04)