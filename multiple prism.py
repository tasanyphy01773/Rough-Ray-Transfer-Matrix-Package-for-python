from numpy import *
from math import *
"""

Code is incomplete



"""
#multiple prism is as mulpri
a = radians(float(input("Enter the angle of refraction(in degree)=", )))
b = radians(float(input("Enter the angle of incidence(in degree)=", )))
k = cos(a)/cos(b)
print("k=", k)
d = float(input("Prism path length,d=", ))
n = float(input("Refractive index of the prism material,n=", ))
#This matrix applies for orthogonal beam exit

def mulpri(k, d, n):
    return arr08
arr08 = array([
                [k, d/(n*k)],
                [0, 1/k]
                            ], float)
print("The ray transfer matrix for a single prism is: ")
print(arr08)

