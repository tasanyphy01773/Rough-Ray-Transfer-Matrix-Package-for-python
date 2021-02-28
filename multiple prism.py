from numpy import *
from math import *

n = int(input("Enter number of prism=", ))
M = 1 

for i in range(n):
    k = float(input("Enter the beam expansion factor, k=", ))
    M = k*M
print("The value of M=", M)

B = float(input("Enter the total optical propagation distance of the multiple prism expander, B=", ))

def mulpri(M, B):
    return arr08
arr08 = array([
                [M, B],
                [0, 1/M]
                            ], float)
print("The ray transfer matrix for a multiple prism is: ")
print(arr08)
