from numpy import *
from math import *

#single prism
a = radians(float(input("Enter the angle of refraction(in degree)=", )))
b = radians(float(input("Enter the angle of incidence(in degree)=", )))
k = cos(a)/cos(b)
print("k=", k)
d = float(input("Prism path length,d=", ))
n = float(input("Refractive index of the prism material,n=", ))
#This matrix applies for orthogonal beam exit

def sinpri(k, d, n):
    return arr07
arr07 = array([
                [k, d/(n*k)],
                [0, 1/k]
                            ], float)
print("The ray transfer matrix for a single prism is: ")
print(arr07)

